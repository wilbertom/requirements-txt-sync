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


def verify_requirements(requirements_1, requirements_2, file_name):
    warnings = []

    for requirement, version in requirements_2.items():
        if requirement not in requirements_1.keys():
            warnings.append(
                f"{file_name}: {requirement} should be uninstalled or added to root."
            )
        elif requirements_2[requirement] != requirements_1[requirement]:
            if version != None:
                warnings.append(
                    f"{file_name}: {requirement}={version} needs to be {requirement}=={requirements_1[requirement]}"
                )
            else:
                warnings.append(
                    f"{file_name}: {requirement} needs to be {requirement}=={requirements_1[requirement]}"
                )

    return warnings


def replace_requirements(requirements_1, requirements_2):
    replaced_requirements = []
    for requirement, version in requirements_2.items():
        if requirement in requirements_1.keys():
            if requirements_1[requirement] == requirements_2[requirement]:
                if requirements_1[requirement] is None:
                    replaced_requirements.append(f"{requirement}")
                else:
                    replaced_requirements.append(
                        f"{requirement}=={requirements_1[requirement]}"
                    )

            elif requirements_1[requirement] != requirements_2[requirement]:
                if requirements_1[requirement] is None:
                    replaced_requirements.append(f"{requirement}")
                else:
                    replaced_requirements.append(
                        f"{requirement}=={requirements_1[requirement]}"
                    )

    return replaced_requirements
