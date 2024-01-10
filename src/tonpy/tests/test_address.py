# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.types.address import Address
import pickle as pck
from tonpy.types.cellbuilder import CellBuilder


def helper(a: Address):
    assert a.serialize() == 'EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA'
    assert a.pack().get_hash() == '94804DD004BE8628522901CF117E4B03CF69E78FC0A9E92BC578BCCB1B3FD0D2'
    assert a.wc == 0
    a.wc = -1
    assert a.serialize() == 'Ef_rLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPZsI'
    assert a.pack().get_hash() == '4FD6BD06AA7BB5EBC5ACFBB694A7DF00AA3F8C6155E47F11620D9B32ED11B5D0'
    assert a.address == 'EB2EAF97EA32993470127208218748758A88374AD2BBD739FC75C9AB3A3F233D'
    assert a.bounceable is True
    a.bounceable = False
    assert a.serialize() == 'Uf_rLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPcbN'
    assert a.pack().get_hash() == '4FD6BD06AA7BB5EBC5ACFBB694A7DF00AA3F8C6155E47F11620D9B32ED11B5D0'
    assert a.testnet is False
    a.testnet = True
    # todo: double check
    assert a.serialize() == '0f_rLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPX1H'


def test_address_string():
    a = Address("EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA")
    helper(a)


def test_pickle_friendly():
    a = Address("EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA")
    assert pck.loads(pck.dumps(a)).serialize() == "EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA"


def test_address_string_fail():
    try:
        Address("LOLKEK")
    except RuntimeError:
        pass
