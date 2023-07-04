from pathlib import Path
import sys

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.libs.python_ton import PyCell, PyCellSlice, PyCellBuilder, PyDict, PyEmulator, parseStringToCell


def test_load_boc():
    cell = parseStringToCell('te6ccuEBAQEACgAUABAAAAAAAAAAe4EqE1s=')
    cs = cell.begin_parse()
    assert cs.load_int(64) == '123'
