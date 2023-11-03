from tonpy.utils.token import parse_token_data
from tonpy.types import CellSlice


def test_simple():
    cs = CellSlice(
        "te6ccuECFQEAAfYAAAoAFAAeACgAcAB6AMgBEAFYAZQCGAIiAiwCdAK8AuwC/gNGA44D2gPsAQMAwAECASACAwIBbgQFAgEgCwwBQb8EF1sx2r0ADJelNWIzlEb5b/btztDfcUeykORfXpD49gYCASAHCABKAG15LWN1c3RvbS1zdGFrZS1hZGRyZXNzLnRvbi9pY29uLmltZwFBvscuvbUU2cl8KDt/CuUXkCnithGcOUYnGeT0btj3QT5kCQFBvtpI/WcK4t8h751/8hc3JVWkKRUdqyAh7yMnRvKAwlLsCgA4AG15LWN1c3RvbS1zdGFrZS1hZGRyZXNzLnRvbgCAALCUJAt0OnSVx+/vox99sZteKgDObTFOXmlTRZL69I/R9FxztRuykJvdnItqDNE49VKfsPQWRZOMMaCP7ss2iQIBIA0OAgFIERIBQb9FRqb/4bec/dhrrT24dDE9zeL7BeanSqfzVS2WF8edEw8BQb9u1PlCp4SM4ssGa3ehEoxqH/jEP0OKLc4kYSup/6uLAxAALABXaXRoZHJhd2FsIFBheW91dCMxMDYADgDij7LvuI8BQb8kEb3o3rQ6nzuczVZhPpUKJgvizfI97zskfescafNEEhMBQb8M64GBDA20NHDvicgGsFe5Mc9qM23yPNGLOMIAmCVrAhQASABDb252ZXJ0cyBidXJuZWQgUG9vbCBKZXR0b25zIHRvIFRPTgAOAGhpZGRlbuPIESA=")

    data = parse_token_data(cs)
    assert data == {'type': 'onchain',
                    'value': {'name': {'type': 'snake', 'value': 'Withdrawal Payout#106'},
                              'symbol': {'type': 'snake', 'value': '⏲️'},
                              'description': {'type': 'snake', 'value': 'Converts burned Pool Jettons to TON'},
                              'render_type': {'type': 'snake', 'value': 'hidden'},
                              'image': {'type': 'snake', 'value': 'my-custom-stake-address.ton/icon.img'},
                              'uri': {'type': 'snake', 'value': 'my-custom-stake-address.ton'},
                              '7B491FACE15C5BE43DF3AFFE42E6E4AAB48522A3B564043DE464E8DE50184A5D': {'type': 'unknown',
                                                                                                   'value': ''}}}
