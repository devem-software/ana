import setuptools
import io

REQUIREMENTS = [
    i.strip()
    for i in io.open("requirements.txt", mode="r", encoding="utf-8").readlines()
]

print(REQUIREMENTS)

with io.open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ana",
    version="0.0.1",
    author="Edwin Marroquin",
    author_email="devem.software@gmail.com",
    description="análisis estructural mediante el método matricial en python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devem-software/ana.git",
    packages=setuptools.find_packages(include=["ana", "ana.*"]),
    package_dir={
        "ana": "ana",
        "ana.core.Bars": "Bars",
        "ana.core.Displacements": "Displacements",
        "ana.core.Loads": "Loads",
        "ana.core.Materials": "Materials",
        "ana.core.Nodes": "Nodes",
        "ana.core.Restrictions": "Restrictions",
        "ana.core.Sections": "Sections",
        "ana.parse.Parse": "Parse",
        "ana.utils.Area": "Area",
        "ana.utils.Centroid": "Centroid",
        "ana.utils.Error": "Error",
        "ana.utils.I18n": "I18n",
        "ana.utils.Inertia": "Inertia",
        "ana.utils.json2Py": "json2Py",
        "ana.utils.Validate": "Validate",
    },
    package_data={"ana": ["*html", "*.css", "*devem-logo.png"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={},
    include_package_data=True,
    python_requires=">=3.10",
)
