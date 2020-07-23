import setuptools

# with open("README.md", "r") as fh:
    # long_description = fh.read()

setuptools.setup(
    name="diskan",
    version="0.0.1",
    author="theunderd0g",
    author_email="ahmedbonumstelio@gmail.com",
    description="An not so obslete way to analyize disks-space mangment",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/theunderd0g/diskan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts':['diskan=src.cli:main']
        }
)
