## xxx

- Smart-contract address class added
- Mnemonic / (ED25519) PublicKey / (ED25519) PrivateKey classes added
- Critical change: Run method in TVM will throw error on unsuccessful exit code
- Merge testnet on commit:
- Allow disassemble libs (root cell & PUSREF*)
- Update C7 to "TVM Upgrade 2023.07", add BlockId
- Add set_prev_blocks_info with BlockId's to emulator
- Fix: emulator, account none several transaction emulation
- Fix: C7 helper
- Fix: Emulator set_libs
- Fix: parse_token_data rewritten to python
- Fix: TVM exit code will be always positive (~x)
- Fix: UTF-8 multichar load in C++ fetch_string in CellSlice
