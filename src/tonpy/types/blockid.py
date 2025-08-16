# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from typing import Union
from tonpy.libs.python_ton import BlockId as ton_BlockId, \
    BlockIdExt as ton_BlockIdExt


class BlockId:
    __slots__ = ['workchain', 'shard', 'seqno', 'blockid']

    workchain: int
    shard: int
    seqno: int
    blockid: ton_BlockId

    def __init__(self, workchain: int = None, shard: Union[str, int] = None, seqno: int = None,
                 blockid: ton_BlockId = None):

        if blockid is None:
            if isinstance(shard, str):
                shard = int(shard, 16)

            self.blockid = ton_BlockId(workchain, shard, seqno)
            self.seqno = seqno
            self.shard = shard
            self.workchain = workchain
        else:
            self.blockid = blockid
            self.workchain = self.blockid.workchain
            self.shard = self.blockid.shard
            self.seqno = self.blockid.seqno

    def __getstate__(self):
        return {
            'workchain': self.workchain,
            'shard': self.shard,
            'seqno': self.seqno
        }

    def __setstate__(self, data):
        self.workchain = data['workchain']
        self.shard = data['shard']
        self.seqno = data['seqno']
        self.blockid = ton_BlockId(self.workchain, self.shard, self.seqno)

    def __hash__(self):
        return hash(":".join(map(str, [self.workchain, self.shard, self.seqno])))

    def __str__(self):
        return str(self.blockid)

    def __repr__(self):
        return f"<BlockId: {str(self.blockid)}>"

    def __eq__(self, other):
        return self.workchain == other.workchain and self.shard == other.shard and self.seqno == other.seqno


class BlockIdExt:
    __slots__ = ['id', 'file_hash', 'root_hash', 'blockidext']
    id: BlockId
    file_hash: str  # hex
    root_hash: str  # hex
    blockidext: ton_BlockIdExt

    def __init__(self, id_: BlockId = None, file_hash: Union[str, int] = None, root_hash: Union[str, int] = None,
                 blockidext: ton_BlockIdExt = None):
        if blockidext is None:
            if isinstance(file_hash, str):
                file_hash = int(file_hash, 16)

            if isinstance(root_hash, str):
                root_hash = int(root_hash, 16)

            self.id = id_
            self.blockidext = ton_BlockIdExt(id_.blockid, str(root_hash), str(file_hash))
            self.file_hash = hex(file_hash).upper()[2:]
            self.root_hash = hex(root_hash).upper()[2:]
        else:
            self.blockidext = blockidext
            self.id = BlockId(blockid=self.blockidext.id) if isinstance(self.blockidext.id,
                                                                        ton_BlockId) else self.blockidext.id
            self.file_hash = self.blockidext.file_hash
            self.root_hash = self.blockidext.root_hash

    def __str__(self):
        return str(self.blockidext)

    def __repr__(self):
        return f"<BlockIdExt: {str(self.blockidext)}>"

    def __getstate__(self):
        return {
            'id': {
                'workchain': self.id.workchain,
                'shard': self.id.shard,
                'seqno': self.id.seqno
            },
            'root_hash': self.root_hash,
            'file_hash': self.file_hash
        }

    def __setstate__(self, data):
        self.id = BlockId(data['id']['workchain'], data['id']['shard'], data['id']['seqno'])
        self.file_hash = data['file_hash']
        self.root_hash = data['root_hash']
        self.blockidext = ton_BlockIdExt(self.id.blockid, str(int(self.root_hash, 16)), str(int(self.file_hash, 16)))

    def __hash__(self):
        return hash(hash(self.id) + hash(self.root_hash + self.file_hash))

    def __eq__(self, other: "BlockIdExt"):
        return self.id == other.id and self.root_hash == other.root_hash and self.file_hash == other.file_hash

    def to_data(self):
        """This needed for C7 pass"""
        return [self.id.workchain, self.id.shard, self.id.seqno, int(self.root_hash, 16), int(self.file_hash, 16)]
