## v2

- Smart-contract address class added
- Mnemonic / (ED25519) PublicKey / (ED25519) PrivateKey classes added
- Merge testnet on commit:
- Allow disassemble libs (root cell & PUSREF*)
- Allow large (>256 bits) keys in VmDict (lookup, set, etc.)
- Add LiteClient
- Add RoundRobin strategy for LiteClient
- Update C7 to "TVM Upgrade 2023.07", add BlockId & BlockIdExt
- Add set_prev_blocks_info with BlockIdExt's support to emulator
- Add shard_is_ancestor, shard_child to tonpy.utils.shard_account
- Add BlockId / BlockIdExt python native support in C++, add wrappers
- Allow VmDict initialization from PyDict
- Add `combine_with` in VmDict to fast combine dictionaries
- Critical change: TLB dump - forced `dump_bin_as_hex` to true. This means if bitsting is `x % 8 == 0` then it'll be
  dumped as hex (this is most of use-cases)
- Critical change: Run method in TVM will throw error on unsuccessful exit code
- Fix: emulator, account none several transaction emulation
- Fix: C7 helper
- Fix: Emulator set_libs
- Fix: parse_token_data rewritten to python
- Fix: TVM exit code will be always positive (~x)
- Fix: UTF-8 multichar load in C++ fetch_string in CellSlice
- Update build system to new ARC
- Add EmulatorExtern for checking new TON versions over external .so files (it's recommended to use native Emulator for
  other proposals)
