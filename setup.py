from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", encoding="utf-8") as fh:
    install_requires = fh.read().split('\n')

setup(
    name="tonpy",
    version="0.0.1",
    author="Disintar LLP",
    author_email="andrey@head-labs.com",
    description="Types / API for TON blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/disintar/tonpy",
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/disintar/tonpy/issues",
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=install_requires,
    packages=['tonpy'],
    python_requires=">=3.9,<=3.11",
)
