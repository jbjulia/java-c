from setuptools import setup, find_packages

with open("../README.md") as readme:
    long_description = readme.read()

with open("../requirements.txt") as requirements:
    install_requires = [line.strip() for line in requirements]

setup(
    name="JavaC",
    version="1.0.0",
    license="MIT",
    url="https://github.com/jbjulia/JavaC",
    author="Joseph Julian",
    author_email="joseph.b.julian@gmail.com",
    description="A small Python utility that converts Java (.java) files into Java (.class) files. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ]
)
