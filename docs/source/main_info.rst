Main information
================



**tonpy** is a Python package that provides data structures and API to interact
with `TON blockchain`_. Tonpy is separate for two
packages: `C++ bindings`_
and `main package`_
that `takes`_ pre-built binaries compiled
by `workflow`_ and creates complete python package with
some python code on top of C++ bindings.

We try to provide 100% test coverage on all structures and functions. Github workflow automatically run tests on all supported systems (Linux, Windows, MacOS) / (x86_64 / aarch64) / (py39, py310, py311) and publish package to pypi.


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
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_cell.py>`_
   - `CellSlice`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_cellslice.py>`_
   - `CellBuilder`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_cellbuilder.py>`_
   - `VmDict`_ (HashmapE, HashmapAugE)
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_vmdict.py>`_
   - `TypedVmDict`_ (same as VmDict but allow to unpack values / extra with TLB types)
      - `Augmented TypedVmDict usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_autogen_block.py#L138>`_
   - `StackEntry`_ (Tuple included)
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_fift.py#L13>`_
   - `Stack`_
      - `Fift usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_fift.py#L11>`_
      - `TVM usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tvm.py#L48>`_
   - `Continuation`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tvm.py#L85>`_
   - `Augmented data`_ (eval_leaf / skip_extra / eval_fork / eval_empty for HashmapAugE)
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_aug_vmdict.py#L21>`_

- TVM
   - `Raw TVM`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tvm.py>`_

   - `Detailed TVM step info`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tvm.py#L108>`_

   - `Transaction Emulator`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_aug_vmdict.py#L21>`_


- TLB
   - `TLB basic types`_
      - `Basic TLB examples <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tlb_redefine.py>`_
   - `Python codegen`_
      - `Unpack / pack examples <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tlb_unpack.py>`_
      - `Tag examples <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_tlb.py>`_


- Autogen
   - `Block TLB types`_
      - `Block parse example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_autogen_block.py>`_


- Tools
   - `Fift disassembler`_
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_disasm.py>`_

   - `Token metadata parser`_

- Fift
   - `Fift`_ (with support of Stack / StackEntry)
      - `Usage example <https://github.com/disintar/tonpy/blob/main/src/tonpy/tests/test_fift.py>`_



.. _Cell: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cell
.. _CellSlice: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellslice
.. _CellBuilder: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.cellbuilder
.. _VmDict: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.vmdict
.. _TLB basic types: https://tonpy.dton.io/tonpy.types.html#module-tonpy.types.tlb
.. _Python codegen: https://tonpy.dton.io/tonpy.tlb_gen.html#module-tonpy.tlb_gen.py
.. _Fift disassembler: https://tonpy.dton.io/tonpy.fift.html#tonpy.fift.disasm.disassembler
.. _Block TLB types: https://github.com/disintar/tonpy/blob/main/src/tonpy/autogen/block.py
.. _TypedVmDict: https://tonpy.dton.io/tonpy.types.html#tonpy.types.vmdict.TypedVmDict
.. _StackEntry: https://tonpy.dton.io/tonpy.types.html#tonpy.types.stack.StackEntry
.. _Continuation: https://tonpy.dton.io/tonpy.types.html#tonpy.types.stack.Continuation
.. _Stack: https://tonpy.dton.io/tonpy.types.html#tonpy.types.stack.Stack
.. _Augmented data: https://tonpy.dton.io/tonpy.types.html#tonpy.types.vmdict.AugmentedData
.. _Raw TVM: https://tonpy.dton.io/tonpy.tvm.html#tonpy.tvm.tvm.TVM
.. _Detailed TVM step info: https://tonpy.dton.io/tonpy.tvm.html#tonpy.tvm.tvm.StepInfo
.. _Transaction Emulator: https://tonpy.dton.io/tonpy.tvm.html#module-tonpy.tvm.emulator
.. _Token metadata parser: https://tonpy.dton.io/tonpy.utils.html#module-tonpy.utils.token
.. _Fift: https://tonpy.dton.io/tonpy.fift.html#module-tonpy.fift.fift
|

.. _check tests examples here: https://github.com/disintar/tonpy/tree/main/src/tonpy/tests


Test examples may show you how to work with library, `check tests examples here`_


