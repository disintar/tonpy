[![Based on dTON fork][ton-svg]][dtonfork]
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://badge.fury.io/py/tonpy.svg)](https://pypi.org/project/tonpy/)


[![Chat][chat-badge]][chat-url]
[![About us][about-badge]][about-url]
[![Docs][docs-badge]][docs-url]
[![Keys and rates][keys-badge]][keys-url]
[![X (Twitter)][x-badge]][x-url]

[chat-badge]: https://img.shields.io/badge/chat-@dtontech-2CA5E0?logo=telegram&logoColor=white&style=flat
[chat-url]: https://t.me/dtontech
[about-badge]: https://img.shields.io/badge/About%20us-tech.dton.%D1%81o-blue
[about-url]: https://tech.dton.io/
[docs-badge]: https://img.shields.io/badge/Docs-docs.dton.%D1%81o-blue
[docs-url]: https://docs.dton.io/
[keys-badge]: https://img.shields.io/badge/Keys%20and%20rates-@dtontech__bot-2CA5E0?logo=telegram&logoColor=white&style=flat
[keys-url]: https://t.me/dtontech_bot
[x-badge]: https://img.shields.io/badge/follow-@dton__io-black?logo=x&logoColor=white&style=flat
[x-url]: https://x.com/dton_io
[telegram-tondev-url]: https://t.me/tondev_eng
[ton-svg]: https://img.shields.io/badge/Based%20on-dTON%20fork-blue
[telegram-tondev-badge]: https://img.shields.io/badge/chat-TONDev-2CA5E0?logo=telegram&logoColor=white&style=flat
[dtonfork]: https://github.com/disintar/ton

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

## Documentation

Documentation can be found on [tonpy.dton.io](https://tonpy.dton.io)

### Supported systems / architectures / Python

| System | Architecture | Python versions | CI status              |
|:--|:--|:----------------|:-----------------------|
| 🐧 Linux | `x86_64` | 3.10 – 3.13      | ✅ |
| 🐧 Linux | `aarch64` | 3.10 – 3.13      | ✅  |
| 🍎 macOS | `x86_64` (Intel) | 3.10 – 3.13      | ✅  |
| 🍎 macOS | `aarch64` (Apple Silicon) | 3.10 – 3.13      | ✅ |
| 🪟 Windows | `x86_64` | 3.10 – 3.13      | ✅  |
| 🪟 Windows | `aarch64` | —               | ⛔                      |


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


## Donation

If you want to support our work, send any coins to:

`dton.ton`

## License 

Copyright (c) 2023 Disintar LLP Licensed under the Apache License

