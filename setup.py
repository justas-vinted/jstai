import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jst.dbr",
    version="0.0.2",
    author="Justas Dambrauskas",
    author_email="jst.dbr@gmail.com",
    description="AI helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justas-vinted/jst_ai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)