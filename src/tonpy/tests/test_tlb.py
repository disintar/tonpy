from tonpy.tlb_gen.py import add_tlb
from bitstring import BitArray
from tonpy.types import TLB, CellBuilder
from itertools import product


def test_tag_multi_bits():
    # language=tl-b
    add_tlb("""
    a$00 = AMultiTagBits;
    b$10 = AMultiTagBits;
    c$01 = AMultiTagBits;
    """, globals())

    a_instance = CellBuilder().store_bitstring("00").begin_parse()
    b_instance = CellBuilder().store_bitstring("10").begin_parse()
    c_instance = CellBuilder().store_bitstring("01").begin_parse()

    A_record = AMultiTagBits()  # noqa
    assert A_record.get_tag(a_instance) == A_record.Tag.a
    assert A_record.get_tag(b_instance) == A_record.Tag.b
    assert A_record.get_tag(c_instance) == A_record.Tag.c


def test_tag_multi_int():
    # language=tl-b
    add_tlb("""
    a#32 = AMultiTagInt;
    b#1111 = AMultiTagInt;
    c#5FE = AMultiTagInt;
    """, globals())

    a_instance = CellBuilder().store_uint(0x32, 8).begin_parse()
    b_instance = CellBuilder().store_uint(0x1111, 16).begin_parse()
    c_instance = CellBuilder().store_uint(0x5fe, 12).begin_parse()

    A_record = AMultiTagInt()  # noqa
    assert A_record.get_tag(a_instance) == A_record.Tag.a
    assert A_record.get_tag(b_instance) == A_record.Tag.b
    assert A_record.get_tag(c_instance) == A_record.Tag.c


def test_tag_multi_int_large():
    tlb_text = ""

    for i in range(64):
        tag = hex(i)[2:].zfill(2)
        tlb_text += f"a{i}#{tag} = ALargeIntTags;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeIntTags()  # noqa

    for i in range(64):
        instance = CellBuilder().store_uint(i, 8).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{i}", globals(), locals())


def test_tag_multi_bits_large():
    tags = [''.join(tag) for tag in list(product('10', repeat=6))]

    tlb_text = ""

    for tag in tags:
        tag_name = int(tag, 2)
        tlb_text += f"a{tag_name}${tag} = ALargeBitTags;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeBitTags()  # noqa

    for tag in tags:
        instance = CellBuilder().store_bitstring(tag).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{int(tag, 2)}", globals(), locals())


def test_tag_multi_bits_large_zfilled():
    tags = [''.join(tag) for tag in list(product('10', repeat=6))]

    tlb_text = ""

    for tag in tags:
        tag_name = int(tag, 2)
        tlb_text += f"a{tag_name}${tag.zfill(62)} = ALargeBitTagsZfilled;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeBitTagsZfilled()  # noqa

    for tag in tags:
        instance = CellBuilder().store_bitstring(tag.zfill(62)).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{int(tag, 2)}", globals(), locals())


def test_tag_multi_int_large_zfilled():
    tlb_text = ""

    for i in range(64):
        tag = hex(i)[2:].zfill(8)
        tlb_text += f"a{i}#{tag} = ALargeIntTagsFilled;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeIntTagsFilled()  # noqa

    for i in range(64):
        instance = CellBuilder().store_uint(i, 32).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{i}", globals(), locals())


def test_tag_with_aug():
    # language=tl-b
    tlb_text = """
    test$001 {x:#} a:(## x) = A x;
    test1$000 a:# = A 1;
    test2$010 a:# = A 2;
    test3$110 a:# = A 3;
    test4$111 a:# = A 4;
    test5$100 a:# = A 5;
    
    test$001 {x:#} {y:#} a:(## x) b:(## y) = B x y;
    test1$000 {y:#} a:# b:(## y) = B 1 y;
    test2$010 {x:#} a:# b:(## x) = B x 2;
    test3$110 a:# = B 1 1;
    test4$111 a:# = B 2 2;
    test5$100 a:# = B 3 3;
    
    test$001 {x:#} {y:#} {z:#} a:(## x) b:(## y) c:(## z) = C x y z;
    test1$000 {y:#} {z:#} a:# b:(## y) c:(## z) = C 1 y z;
    test2$010 {x:#} {z:#} a:# b:(## x) c:(## z)= C x 2 z;
    test3$110 {z:#} a:# b:# c:(## z) = C 1 1 z;
    test4$111 a:# = C 2 2 2;
    test5$100 a:# = C 3 3 3;
    
    
    test$001 {x:#} {y:#} {z:#} {h:#} a:(## x) b:(## y) c:(## z) d:(## h) = D x y z h;
    test$001 {x:#} {y:#} {z:#} {h:#} {i:#} a:(## x) b:(## y) c:(## z) d:(## h) e:(## i) = E x y z h i;
    
    
    test$001 {x:#} a:(## x) = F ~a x;
    test1$011 a:(## 32) = F ~a 0;
    """
    add_tlb(tlb_text, globals())

    A_record = A(0)  # noqa
    B_record = B(0, 0)  # noqa
    C_record = C(0, 0, 0)  # noqa
    D_record = D(0, 0, 0, 0)  # noqa
    E_record = E(0, 0, 0, 0, 0)  # noqa
    F_record = F(0)  # noqa

    assert A_record.get_tag(CellBuilder().store_bitstring("001").begin_parse()) == A_record.Tag.test
    assert A_record.get_tag(CellBuilder().store_bitstring("000").begin_parse()) == A_record.Tag.test1
    assert A_record.get_tag(CellBuilder().store_bitstring("010").begin_parse()) == A_record.Tag.test2
    assert A_record.get_tag(CellBuilder().store_bitstring("110").begin_parse()) == A_record.Tag.test3
    assert A_record.get_tag(CellBuilder().store_bitstring("111").begin_parse()) == A_record.Tag.test4
    assert A_record.get_tag(CellBuilder().store_bitstring("100").begin_parse()) == A_record.Tag.test5

    assert B_record.get_tag(CellBuilder().store_bitstring("001").begin_parse()) == B_record.Tag.test
    assert B_record.get_tag(CellBuilder().store_bitstring("000").begin_parse()) == B_record.Tag.test1
    assert B_record.get_tag(CellBuilder().store_bitstring("010").begin_parse()) == B_record.Tag.test2
    assert B_record.get_tag(CellBuilder().store_bitstring("110").begin_parse()) == B_record.Tag.test3
    assert B_record.get_tag(CellBuilder().store_bitstring("111").begin_parse()) == B_record.Tag.test4
    assert B_record.get_tag(CellBuilder().store_bitstring("100").begin_parse()) == B_record.Tag.test5

    assert C_record.get_tag(CellBuilder().store_bitstring("001").begin_parse()) == C_record.Tag.test
    assert C_record.get_tag(CellBuilder().store_bitstring("000").begin_parse()) == C_record.Tag.test1
    assert C_record.get_tag(CellBuilder().store_bitstring("010").begin_parse()) == C_record.Tag.test2
    assert C_record.get_tag(CellBuilder().store_bitstring("110").begin_parse()) == C_record.Tag.test3
    assert C_record.get_tag(CellBuilder().store_bitstring("111").begin_parse()) == C_record.Tag.test4
    assert C_record.get_tag(CellBuilder().store_bitstring("100").begin_parse()) == C_record.Tag.test5

    assert D_record.get_tag(CellBuilder().store_bitstring("001").begin_parse()) == D_record.Tag.test
    assert E_record.get_tag(CellBuilder().store_bitstring("001").begin_parse()) == E_record.Tag.test

    assert F_record.get_tag(CellBuilder().store_bitstring("001").begin_parse()) == F_record.Tag.test
    assert F_record.get_tag(CellBuilder().store_bitstring("011").begin_parse()) == F_record.Tag.test1


def test_enum():
    # TODO: fix
    # language=tl-b
    tlb_text = """
    test$_ = A; // simple Enum
    test$01 = B;

    a$0 = C;
    b$1 = C;

    a$0 = D;
    c$101 = D;
    b$11 = D;
    """
    add_tlb(tlb_text, globals())

    A_record = A()
    B_record = B()
    C_record = C()
    D_record = D()

    assert A_record.fetch_enum(CellBuilder().begin_parse()) == 0

    cb = CellBuilder()
    A_record.store_enum_from(cb)  # While enum is $_ it'll do nothing
    assert A_record.fetch_enum(cb.begin_parse()) == cb.bits == 0

    assert B_record.fetch_enum(CellBuilder().store_bitstring('01').begin_parse()) == int('01', 2)

    cb = CellBuilder()
    B_record.store_enum_from(cb)  # While enum is const it'll always save const
    assert B_record.fetch_enum(cb.begin_parse()) == int('01', 2)

    assert C_record.fetch_enum(CellBuilder().store_bitstring('0').begin_parse()) == int('0', 2)

    cb = CellBuilder()
    C_record.store_enum_from(cb, 0)
    assert C_record.fetch_enum(cb.begin_parse()) == int('0', 2)

    assert C_record.fetch_enum(CellBuilder().store_bitstring('1').begin_parse()) == int('1', 2)

    cb = CellBuilder()
    C_record.store_enum_from(cb, 1)
    assert C_record.fetch_enum(cb.begin_parse()) == int('1', 2)

    assert D_record.fetch_enum(CellBuilder().store_bitstring('0').begin_parse()) == int('0', 2)

    cb = CellBuilder()
    D_record.store_enum_from(cb, int('0', 2))
    assert D_record.fetch_enum(cb.begin_parse()) == D_record.cons_tag[0] == int('0', 2)

    assert D_record.fetch_enum(CellBuilder().store_bitstring('11').begin_parse()) == int('11', 2)

    cb = CellBuilder()
    D_record.store_enum_from(cb, int('11', 2))
    assert D_record.fetch_enum(cb.begin_parse()) == D_record.cons_tag[2] == int('11', 2)

    assert D_record.fetch_enum(CellBuilder().store_bitstring('101').begin_parse()) == int('101', 2)

    cb = CellBuilder()
    D_record.store_enum_from(cb, int('101', 2))
    assert D_record.fetch_enum(cb.begin_parse()) == D_record.cons_tag[1] == int('101', 2)


def test_special():
    # language=tl-b
    tlb_text = """
    !test$0 = A;
    test$0 = B;
    """

    add_tlb(tlb_text, globals())

    A_record = A()
    B_record = B()

    assert A_record.always_special() is True
    assert B_record.always_special() is False


def test_records():
    # language=tl-b
    tlb_text = """
    _ {x:Type} k:# = T x;
    a$0 {x:Type} a:# b:(## 32) c:bits512 e:^(T uint32) f:(T x) = A x;
    b$1 {x:Type} e:# d:(## 32) c:bits512 b:^(T uint32) a:(T x) = A x;
    """

    add_tlb(tlb_text, globals())

    A_record = A(TLB())
    T_record = T(TLB())
    test_record = T_record.Record(32)
    assert test_record.k == 32

    empty_cell = CellBuilder().store_uint(0, 32).end_cell()
    empty_cs = CellBuilder().store_uint(0, 32).begin_parse()

    # Can create Record_a from params
    test_record = A_record.Record_a(1, 2, BitArray("0b11"), empty_cell, empty_cs)
    assert test_record.a == 1
    assert test_record.b == 2
    assert test_record.c.bin == '11'
    assert test_record.e == empty_cell
    assert test_record.f == empty_cs
    assert test_record.cell_pack().get_hash() == '47277DEFA53A72F6C47E4A92498C24B69A11A9EACA915F8654A4724227F244AE'

    # Can create Record_b from params
    test_record = A_record.Record_b(3, 4, BitArray("0b01"), empty_cell, empty_cs)
    assert test_record.e == 3
    assert test_record.d == 4
    assert test_record.c.bin == '01'
    assert test_record.b == empty_cell
    assert test_record.a == empty_cs
    assert test_record.cell_pack().get_hash() == '9E31F51F54F392AB927D2124E8209C9E1ADF2C28FB0A677DC3C82FFC790150FE'

