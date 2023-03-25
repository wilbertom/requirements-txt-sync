import sys
from functions_for_program import (
    requirements_used,
    verify_requirements
)

# what if i make this is a whole for loop where it goes by file, instead of putting everything in one?
i = 2
for file_name in sys.argv[2:]:
    
    file_1 = open(sys.argv[1])
    file_2 = open(sys.argv[i])

    requirements_in_file_1 = requirements_used(file_1)
    requirements_in_file_2 = requirements_used(file_2)

    warnings = verify_requirements(
        requirements_in_file_1, requirements_in_file_2, file_name
    )

    for warning in warnings:
        print(warning)
    i += 1
