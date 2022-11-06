from setuptools import find_packages, setup

import versioneer

setup(
    name="bamboo",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages("src"),
    package_dir={"": "src"},
)
