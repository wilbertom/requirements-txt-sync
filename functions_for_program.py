# Don't make noise if everything is OK
# Handle multiple requirements file
import sys


def requirements_used(file):
    requirements = {}

    for line in file:
        name, version = _parse_requirement_line(line)
        requirements[name] = version

    return requirements


def _parse_requirement_line(line):
    line = line.strip("\n")
    line = line.split("==")

    if len(line) == 2:
        name = line[0]
        version = line[1]
    else:
        name = line[0]
        version = None

    return name, version


def verify_requirements(root, app_txt_file, file_name):
    warnings = []

    for requirement, version in app_txt_file.items():
        if requirement not in root.keys():
            warnings.append(
                f"{file_name}: {requirement} should be uninstalled or added to root."
            )
        elif app_txt_file[requirement] != root[requirement]:
            if version != None:
                warnings.append(
                    f"{file_name}: {requirement}={version} needs to be {requirement}=={root[requirement]}"
                )
            else:
                warnings.append(
                    f"{file_name}: {requirement} needs to be {requirement}=={root[requirement]}"
                )

    return warnings


def replace_requirements(root, app_txt_file):
    replaced_requirements = []
    for requirement in app_txt_file.keys():
        if requirement in root.keys():
            if root[requirement] == app_txt_file[requirement]:
                if root[requirement] is None:
                    replaced_requirements.append(f"{requirement}")
                else:
                    replaced_requirements.append(f"{requirement}=={root[requirement]}")

            elif root[requirement] != app_txt_file[requirement]:
                if root[requirement] is None:
                    replaced_requirements.append(f"{requirement}")
                else:
                    replaced_requirements.append(f"{requirement}=={root[requirement]}")

    return replaced_requirements


def write_requirements(f, requirements):
    lines = "\n".join(requirements)
    f.write(lines)
