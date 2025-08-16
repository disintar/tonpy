# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

import os
from setuptools import setup, find_packages
IS_DEV = os.environ.get('DEV_PYPI', False)

with open(f"README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open(f"requirements.txt", encoding="utf-8") as fh:
    install_requires = fh.read().split('\n')

with open(f"docs_requirements.txt", encoding="utf-8") as fh:
    docs_extras = fh.read().split('\n')

with open(f"built_requirements.txt", encoding="utf-8") as fh:
    built_extras = fh.read().split('\n')

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


    class bdist_wheel(_bdist_wheel):
        plat_name = 'manylinux2014_x86_64'

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setup(
    name="tonpy" if not IS_DEV else "tonpy-dev",
    version="0.0.0.1.3a0" if not IS_DEV else "0.0.0.5.9b1",
    author="Disintar LLP",
    author_email="andrey@head-labs.com",
    description="Types / API for TON blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/disintar/tonpy",
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
    setup_requires=install_requires,
    install_requires=install_requires,
    python_requires=">=3.8,<=3.13",
    packages=find_packages(
        where='src',  # '.' by default
    ),
    package_dir={
        "": "src",
    },
    extras_require={'docs': docs_extras, 'built': built_extras},
    cmdclass={'bdist_wheel': bdist_wheel},
    include_package_data=True
)

