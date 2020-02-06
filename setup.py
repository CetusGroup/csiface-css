import os
import os.path
from setuptools import find_packages, setup


project_dir = os.path.dirname(os.path.abspath(__file__))


def parse_requirements(file_path):
    requirements, dependencies = [], []

    with open(file_path) as f:
        for line in f:
            line = line.strip()

            if line.startswith("-e"):
                line = line.split(' ', 1)[1]
                dependencies.append(line)
                line = line.split("#egg=", 1)
                if len(line) == 2:
                    line = line[1]
                    requirements.append(line)
            elif line.startswith("-r"):
                name = line.split(' ', 1)[1]
                path = os.path.join(os.path.dirname(file_path), name)
                subrequirements, subdependencies = parse_requirements(path)
                requirements.extend(subrequirements)
                dependencies.extend(subdependencies)
            else:
                requirements.append(line)

    return requirements, dependencies


README = open(os.path.join(project_dir ,"README.rst")).read()
REQUIREMENTS, DEPENDENCIES = parse_requirements(os.path.join(project_dir ,"requirements.txt"))
EXCLUDE_FROM_PACKAGES = []

setup(
    name="csiface-css",
    version="0.0.1",
    description="",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCIES,
    package_data={  # Optional
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console"
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
