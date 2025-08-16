Module setup
===============

Setup from PyPi
---------------

``pip install tonpy``


Supported OS:

- MacOS
- Linux
- Windows

Supported Python versions:

- Python 3.9
- Python 3.10
- Python 3.11

Supported arch:

- aarch64 (include Mac M1)
- x86_64

For each ``OS`` / ``Python`` / ``arch`` it's separated ``.whl`` distribution in `pypi`_

.. _pypi: https://pypi.org/project/tonpy/#files

Also you can compile lib from sources for your os or for local development.

Development setup (pre-built)
-----------------------------

1. Find you ``OS`` / ``Python`` / ``arch`` in `releases`_
2. Download ``so`` or ``dll`` from release and put it into ``src/tonpy/libs/`` folder

.. _releases: https://github.com/disintar/ton/releases


Development setup (compile from sources)
----------------------------------------

If you want to setup ``tonpy`` package for local development (including C++ code) you need to:

1. Download Disintar TON monorepo fork:
    ``git clone --recurse-submodules -j8 https://github.com/disintar/ton``

2. Compile ``python_ton`` target with ``cmake``:
    .. code-block:: console

        cd ton && mkdir build && cd build

        cmake .. -DCMAKE_BUILD_TYPE=Debug -DTON_USE_PYTHON=1 \
         -DPYTHON_INCLUDE_DIRECTORIES=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")  \
          -DPYTHON_LIBRARY=$(python3 -c "import distutils.sysconfig as sysconfig; print(sysconfig.get_config_var('LIBDIR'))") \
         -DPYTHON_EXECUTABLE=$(which python3)

        cmake --build . -j 8 --target python_ton

    Optionally add path to openssl ``-DOPENSSL_ROOT_DIR=/opt/homebrew/opt/openssl@3``

    After compilation ``so`` / ``dll`` file will be in ``build/tvm_python`` folder. Example name: ``python_ton.cpython-39-darwin.so``

3. Link compiled shared object to ``src/tonpy/libs/`` of ``tonpy`` project:
    ``ln -s PATH_TO_LIB src/tonpy/libs/``

