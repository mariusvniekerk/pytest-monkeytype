from setuptools import find_packages, setup


package_name = "pytest-monkeytype"
version = "1.0.3"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=package_name,
    version="1.0.5",
    description="pytest-monkeytype: Generate Monkeytype annotations from your pytest tests.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mariusvniekerk/pytest-monkeytype",
    author="Marius van Niekerk",
    author_email="marius.v.niekerk@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["MonkeyType>=18.2.0", "pytest>=3.2.0"],
    entry_points={"pytest11": ["pytest_monkeytype = pytest_monkeytype.plugin",]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Framework :: Pytest",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Software Development :: Testing",
    ],
    keywords="pytest py.test types annotations MonkeyType monkeytype pep484",
    python_requires=">=3.6",
)
