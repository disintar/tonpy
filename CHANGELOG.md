# Roadmap

- dABI update with events
- SmartContract class
  - Getters / liteserver API
  - Compile from source
  - Publish to liteserver
- Blockchain Emulator
  - With tests on SmartContracts and events
- TOLK compiler support
- Async support for LiteClient / BlockScanner(?)

# Changelog

## [0.1.3] - 2025-08-16

### Added
- Async/await support in TVM and Emulator for highly concurrent workflows (see tests: `test_tvm_async.py`, `test_emulator_async.py`).
- Smart contract `Address` class with first‑class parsing and formatting.
- Key management primitives: Mnemonic, ED25519 `PublicKey` and `PrivateKey`.
- LiteClient with a Round‑Robin connection strategy for resilient RPC access (`tonpy.types.liteclient` and helpers in `tonpy.types.lite_utils.*`).
- Block Scanner module for streaming and indexed processing of TON blocks (`tonpy.blockscanner.*`).
- dABI integration: https://github.com/disintar/dABI
- FunC support: strings and sources handling (`tonpy.func.func`).
- VmDict can be initialized directly from Python dicts.
- `combine_with` to efficiently merge VmDicts.
- `tonpy.utils.shard_account`: `shard_is_ancestor` and `shard_child` helpers.
- `EmulatorExtern` to validate new TON VM versions via external shared objects (`tonpy.tvm.not_native.emulator_extern`). Prefer native Emulator for general use.
- `BlockId` / `BlockIdExt` native support in C++ bindings plus Python wrappers.
- Lightweight job scheduler for sequential/background tasks (`tonpy.scheduler`).
- Wheels published for Linux/macOS/Windows on x86_64 and aarch64 where available. Supported Python versions: 3.8–3.13 (see README for the current matrix).

### Changed
- Heavy/slow operations no longer hold the Python GIL, enabling true multi‑threaded usage patterns.
- C7 updated to “TVM Upgrade 2023.07”; added `BlockId` & `BlockIdExt` types across the stack (`tonpy.tvm.c7`).
- TLB dump now forces `dump_bin_as_hex = true` when bitstring length is a multiple of 8; hex is emitted in these common cases for better readability and interoperability. BREAKING
- `tvm.run` now raises on unsuccessful exit codes by default. This converts silent failures into explicit exceptions. BREAKING
- Build system refreshed to the new ARC.

### Fixed
- Emulator: corrected multi‑transaction emulation when an account is `None`.
- C7 helper stability improvements.
- Emulator `set_libs` behavior aligned with expectations in complex disasm/lib scenarios (root cell & `PUSHREF*`).
- `parse_token_data` fully rewritten in Python for correctness and maintainability.
- TVM exit code normalization: values are now always positive (`~x`) as expected by tooling.
- UTF‑8 multi‑character loading fixed in C++ `CellSlice::fetch_string`.

### Performance
- GIL‑free critical sections substantially improve throughput in threaded workloads.

### Notes for Upgraders
- If you rely on raw binary dumps from the TLB dumper, audit your tooling for the new hex output rule on 8‑bit‑aligned bitstrings.
- If you previously depended on `tvm.run` returning error codes instead of raising, wrap calls with `try/except` and handle `TonpyTvmError` (or your app’s error type) accordingly.
- For maximum compatibility with wheels, see the support matrix in README; building from source is still available and documented.

---