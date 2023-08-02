Main information
================



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
   - StackEntry
   - Stack

- TVM
   - Raw TVM
   - Transaction Emulator

- TLB
   - `TLB basic types`_
   - `Python codegen`_

- Autogen
   - `Block TLB types`_

- Tools
   - `Fift disassembler`_
   - Token metadata parser

- Fift
   - Fift (with support Stack / StackEntry)


.. _Cell: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cell
.. _CellSlice: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellslice
.. _CellBuilder: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellbuilder
.. _VmDict: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.vmdict
.. _TLB basic types: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.tlb
.. _Python codegen: https://tonpy.dton.io/tonpy.tlb_gen.html#module-tonpy.tlb_gen.py
.. _Fift disassembler:
.. _Block TLB types: https://github.com/disintar/tonpy/blob/main/src/tonpy/autogen/block.py
|

.. _check tests examples here: https://github.com/disintar/tonpy/tree/main/src/tonpy/tests


Test examples may show you how to work with library, `check tests examples here`_

Tests
-----

We try to provide 100% test coverage on all function.

