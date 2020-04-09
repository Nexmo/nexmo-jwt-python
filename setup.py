import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nexmo-jwt",
    version="1.0.0",
    author="Diana Rodriguez",
    author_email="diana.rodriguezmanrique@vonage.com",
    description="JWT Generator for Nexmo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nexmo/nexmo-jwt-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
    install_requires=["pyjwt>=1.0.1"],
)
