[telegram-tondev-url]: https://t.me/tondev_eng
[ton-svg]: https://img.shields.io/badge/Based%20on-TON-blue
[telegram-tondev-badge]: https://img.shields.io/badge/chat-TONDev-2CA5E0?logo=telegram&logoColor=white&style=flat
[ton]: https://ton.org


[![Based on TON][ton-svg]][ton]
![Python version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Supported OS](https://img.shields.io/badge/os-Linux%20%7C%20MacOS%20%7C%20Windows-green)
![Supported arch](https://img.shields.io/badge/arch-arm64%20%7C%20x86_64-purple)
[![Telegram Community Chat][telegram-tondev-badge]][telegram-tondev-url]
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://badge.fury.io/py/tonpy.svg)](https://pypi.org/project/tonpy/)

# tonpy: powerful Python TON toolkit

## What is it?

**tonpy** is a Python package that provides data structures and API to interact
with [TON blockchain](https://github.com/ton-blockchain/ton). Tonpy is separate for two
packages: [C++ bindings](https://github.com/disintar/ton/tree/master/tvm-python)
and [main package](https://github.com/disintar/tonpy)
that [takes](https://github.com/disintar/tonpy/tree/main/.github/workflows) pre-built binaries compiled
by [workflow](https://github.com/disintar/ton/tree/master/.github/workflows) and creates complete python package with
some python code on top of C++ bindings.


## Installation

One command: `pip install tonpy`

Complex installation for not supported systems and python versions are described in [documentation](https://tonpy.dton.io/installation.html#development-setup-compile-from-sources)

## Speed compare

`compare/pytoniq.py`

Cell load tests 

| module  | 100.000 Cells, 1 ref, 1024 bits | vs tonpy |
|---------|---------------------------------|----------|
| tonpy   | 0.02                            | 1        |
| pytoniq | 1.39                            | 69.5     |

`compare/tvm_run.py`

TVM Run

> Be careful, `enable_stack_dump=True` increase time of execution

| mode            | Secs   | TVM Instances Count |
|-----------------|--------|---------------------|
| sync            | 3.53   | 10                  |
| multiprocessing | 1.10   | 10                  |
| async           | 0.59   | 10                  |
|                 |        |                     |
| sync            | 36.36  | 100                 |
| multiprocessing | 5.36   | 100                 |
| async           | 5.15   | 100                 |


## Documentation

Documentation can be found on [tonpy.dton.io](https://tonpy.dton.io)

## Donation

If you want to support our work, send any coins to:

`EQDfmsDtWQP5D_YkXX-XlULvs4HivRaKY38ftT2hS5yAANRf`

## License 

Copyright (c) 2023 Disintar LLP Licensed under the Apache License

