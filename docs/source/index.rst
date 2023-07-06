.. tonpy documentation master file, created by
   sphinx-quickstart on Mon Jul  3 13:48:41 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tonpy's documentation!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   tonpy


.. role:: raw-html(raw)
    :format: html

What is supported?
------------------
:raw-html:`<br />`

- Basic types:
   - `Cell`_
   - `CellSlice`_
   - `CellBuilder`_

- TVM
   - Raw TVM
   - Transaction Emulator

- TLB
   - Python codegen


.. _Cell: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cell
.. _CellSlice: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellslice
.. _CellBuilder: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellbuilder

:raw-html:`<br />`

Tests
-----

We try to provide 100% test coverage on all functions, feel free to `check tests examples out`_

.. _check tests examples out: https://github.com/disintar/tonpy/tree/main/src/tonpy/tests