from tonpy.types.blockid import BlockId, BlockIdExt
import pickle


def test_dump():
    test = BlockIdExt(BlockId(0, 1, 2), 'a', 'b')
    test2 = pickle.loads(pickle.dumps(test))
    assert test == test2
