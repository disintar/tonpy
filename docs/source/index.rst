tonpy: powerful Python TON toolkit
==================================

**tonpy** is a Python package that provides data structures and API to interact
with `TON blockchain`_. Tonpy is separate for two
packages: `C++ bindings`_
and `main package`_
that `takes`_ pre-built binaries compiled
by `workflow`_ and creates complete python package with
some python code on top of C++ bindings.

.. _TON blockchain: https://github.com/ton-blockchain/ton
.. _C++ bindings: https://github.com/disintar/ton/tree/master/tvm-python
.. _main package: https://github.com/disintar/tonpy
.. _takes: https://github.com/disintar/tonpy/tree/main/.github/workflows
.. _workflow: https://github.com/disintar/ton/tree/master/.github/workflows

What is supported?
------------------

|

- Basic types:
   - `Cell`_
   - `CellSlice`_
   - `CellBuilder`_
   - `VmDict`_

- TVM
   - Raw TVM
   - Transaction Emulator

- TLB
   - Python codegen


.. _Cell: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cell
.. _CellSlice: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellslice
.. _CellBuilder: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellbuilder
.. _VmDict: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.vmdict

|

.. _check tests examples out: https://github.com/disintar/tonpy/tree/main/src/tonpy/tests


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   tonpy


.. role:: raw-html(raw)
    :format: html

Tests
-----

We try to provide 100% test coverage on all functions, feel free to `check tests examples out`_
