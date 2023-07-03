import os
from setuptools import setup

with open(f"README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open(f"requirements.txt", encoding="utf-8") as fh:
    install_requires = fh.read().split('\n')

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

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
    setup_requires=install_requires,
    install_requires=install_requires,
    package_dir={'': 'tonpy'},
    python_requires=">=3.9,<=3.11",
    cmdclass={'bdist_wheel': bdist_wheel}
)
