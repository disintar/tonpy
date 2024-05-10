from tonpy.types.keys import Mnemonic, get_bip39_words, PrivateKey, PublicKey


def test_bip39():
    assert len(get_bip39_words()) == 2048


def test_mnemo():
    m = Mnemonic(words_count=48)
    words = m.get_words()
    key = m.get_private_key_hex()

    assert len(words) == 48
    assert len(key) == 64


def test_mnemo_2():
    mnemo = ['market', 'record', 'talent', 'wear', 'caught', 'soup', 'crater',
             'alpha', 'cattle', 'exercise', 'eight', 'page', 'easy', 'rural', 'tired', 'chapter',
             'major', 'make', 'organ', 'pipe', 'position', 'else', 'common', 'crop']
    m = Mnemonic(words=mnemo)
    assert m.get_private_key_hex() == '8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271'
    k = m.get_private_key()

    assert k.to_hex() == '8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271'
    assert k.get_public_key().to_hex() == '5F0A08B035F60A0A13BC38D033EBE5B808FAD0DAF954E3305CE4438E7FBC9548'


def test_private_key():
    key = PrivateKey()
    assert len(key.to_hex()) == 64


def test_private_key_v2():
    key = PrivateKey('8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271')
    assert key.to_hex() == '8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271'


def test_public_key():
    key = PrivateKey('8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271')
    assert key.get_public_key().to_hex() == '5F0A08B035F60A0A13BC38D033EBE5B808FAD0DAF954E3305CE4438E7FBC9548'


def test_public_key_v2():
    key = PublicKey('5F0A08B035F60A0A13BC38D033EBE5B808FAD0DAF954E3305CE4438E7FBC9548')
    assert key.to_hex() == '5F0A08B035F60A0A13BC38D033EBE5B808FAD0DAF954E3305CE4438E7FBC9548'


def test_signature():
    key = PrivateKey('4B8A8882B9F0E542A47CA297F87447CCB69106917CF36B4505D5C6C3D3BDC0AF')
    key2 = PrivateKey('8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271')
    data = "lolkek".encode()

    pub = key.get_public_key()
    signature = key.sign(data)
    signature2 = key2.sign(data)

    assert pub.verify_signature(data, signature)
    assert not pub.verify_signature(data, signature2, False)


def test_signature_cell():
    from tonpy import CellBuilder

    key = PrivateKey('8A9184CC9D0A26F846BB85A1178425C0EB4BB5C489E8C8A9436960CCAF93C271')
    data = CellBuilder().store_uint(0, 32).end_cell().get_hash()

    pub = key.get_public_key()
    signature = key.sign(data)

    assert pub.verify_signature(data, signature)
