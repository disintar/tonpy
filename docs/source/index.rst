.. tonpy documentation master file, created by
sphinx-quickstart on Mon Jul  3 13:48:41 2023.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

tonpy: powerful Python TON toolkit
==================================

**tonpy** is a Python package that provides data structures and API to interact
with [TON blockchain](https://github.com/ton-blockchain/ton). Tonpy is separate for two
packages: [C++ bindings](https://github.com/disintar/ton/tree/master/tvm-python)
and [main package](https://github.com/disintar/tonpy)
that [takes](https://github.com/disintar/tonpy/tree/main/.github/workflows) pre-built binaries compiled
by [workflow](https://github.com/disintar/ton/tree/master/.github/workflows) and creates complete python package with
some python code on top of C++ bindings.


What is supported?
------------------
:raw-html:`<br />`

- Basic types:
   - `Cell`_
   - `CellSlice`_
   - `CellBuilder`_
   - VmDict

- TVM
   - Raw TVM
   - Transaction Emulator

- TLB
   - Python codegen


.. _Cell: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cell
.. _CellSlice: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellslice
.. _CellBuilder: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellbuilder

:raw-html:`<br />`

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
