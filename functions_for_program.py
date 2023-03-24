# Don't make noise if everything is OK
# Handle multiple requirements file
import sys


def requirements_used(file):
    requirements = {}

    for line in file:
        name, version = _parse_requirement_line(line)
        requirements[name] = version

    return requirements


def requirements_used_in_multiple_files(files):
    requirements = {}

    for file in files:
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


def verify_requirements(requirements_1, requirements_2, file_name):
    warnings = []

    for requirement, version in requirements_1.items():
        if requirement in requirements_2.keys():
            if requirements_1[requirement] != requirements_2[requirement]:
                if requirements_2[requirement] is None:
                    warnings.append(
                        f"{requirement} needs to be {version} in {file_name}"
                    )

                else:
                    warnings.append(
                        f"{requirement}=={version} needs to be {requirement}=={requirements_2[requirement]} in {file_name}"
                    )
        else:
            warnings.append(f"{requirement} is missing in {file_name}")

    for requirement, version in requirements_2.items():
        if requirement not in requirements_1.keys():
            warnings.append(
                f"{requirement} should be uninstalled or added to root in {file_name}"
            )

    return warnings
