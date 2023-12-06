# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PyLiteClient, ipv4_int_to_str, globalSetVerbosity

globalSetVerbosity(3)

from tonpy.types.keys import PublicKey
from base64 import b64decode
from tonpy.types.lite_utils.server_list import servers
from time import sleep


def base64_to_hex(b):
    return b64decode(b).hex()


class Bits256:
    def to_hex(self) -> str:
        pass


class BlockIdExt:
    workchain: int
    shard: int
    seqno: int
    file_hash: Bits256
    root_hash: Bits256


class MasterchainInfoExt:
    mode: int
    version: int
    capabilities: int
    last_utime: int
    now: int
    state_root_hash: Bits256
    last: BlockIdExt


class LiteClient:
    def __init__(self, host: str, port: int, pubkey: PublicKey):
        self.client = PyLiteClient(
            host=host,
            port=port,
            public_key=pubkey.key,
            timeout=1.0
        )

    def get_connected(self):
        return self.client.get_connected()

    def get_time(self):
        return self.client.get_time()

    def get_MasterchainInfoExt(self) -> MasterchainInfoExt:
        return self.client.get_MasterchainInfoExt()

    def send_message(self, cell):
        return self.client.send_message(cell.cell)


if __name__ == "__main__":
    from tonpy import Cell

    # for server in servers:
    server = {'started_at': 1701882334.870854,
              'id': {'@type': 'pub.ed25519',
                     'key': 'Fi6e++zdCQIYOoHze+i2ZzU8oKj6GbQIlya3GKVbLtQ='},
              'port': 30123,
              'ip': -957035708}
    print("Start: ", server)

    lc = LiteClient(host=ipv4_int_to_str(server['ip']), port=server['port'],
                    pubkey=PublicKey(base64_to_hex(server['id']['key'])))

    print(server, lc.send_message(Cell(
        "te6ccuECAwEAAQYAAPQBWwIMBOeIAH7hK4c4nJzGSMTE1XJQptlwjSiHswHqdg6PwzQ880ZCBfnYKEwemTqcIjvAdtSKAGgGjASr+lli1xGyYDhExZMDCkaNPZiKM0ATJdNjDxvd7+KKdWVCigfX77NiGLoS0AlNTRi7K4cJyAAAA7AACAgIDAEBAQEBYGIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQIArgAAAABkYXRhOmFwcGxpY2F0aW9uL2pzb24seyJwIjoidG9uLTIwIiwib3AiOiJtaW50IiwidGljayI6Im5hbm8iLCJhbXQiOiIxMDAwMDAwMDAwMDAifQgv2J4=")))
    # connected = False
    # while not connected:
    #     time = lc.get_MasterchainInfoExt()
    #     sleep(1)
    #     print("Got connected: ", time.last_utime, time.now,
    #           time.last.workchain, time.last.shard, time.last.seqno)
