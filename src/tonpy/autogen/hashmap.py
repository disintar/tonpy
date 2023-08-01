# !!!!!!# This is autogen file from tonpy.tlb# !!!!!!
from enum import Enum
import bitstring
from tonpy import *
from typing import Optional, Union, List
tlb_classes = []


# class for type `Unit`
class Unit(TLBComplex):
    class Tag(Enum):
        unit = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Unit.Tag.unit: Unit.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Unit.Tag"]:
        return Unit.Tag(0)


    def fetch_enum(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> int:
        return 0


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        return True


    class Record(RecordBase):
        def get_tag_enum(self):
            return Unit.Tag.unit

        def get_tag(self):
            return Unit.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Unit.cons_len_exact[self.get_tag_enum().value] if isinstance(Unit.cons_len_exact, list) else Unit.cons_len_exact

        def get_type_class(self):
            return Unit


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                return True                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Unit")


# class for type `Truet`
class Truet(TLBComplex):
    class Tag(Enum):
        true = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Truet.Tag.true: Truet.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Truet.Tag"]:
        return Truet.Tag(0)


    def fetch_enum(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> int:
        return 0


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        return True


    class Record(RecordBase):
        def get_tag_enum(self):
            return Truet.Tag.true

        def get_tag(self):
            return Truet.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Truet.cons_len_exact[self.get_tag_enum().value] if isinstance(Truet.cons_len_exact, list) else Truet.cons_len_exact

        def get_type_class(self):
            return Truet


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                return True                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Truet")


# class for type `Bool`
class Bool(TLBComplex):
    class Tag(Enum):
        bool_false = 0
        bool_true = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Bool.Tag.bool_false: Bool.Record_bool_false, Bool.Tag.bool_true: Bool.Record_bool_true}

    def get_tag(self, cs: CellSlice) -> Optional["Bool.Tag"]:
        return Bool.Tag(int(cs.preload_uint(1)))


    def fetch_enum(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> int:
        value = cs.load_uint(1)
        assert value in self.cons_tag, f'Unexpected value {value} for tag, expected one of: {self.cons_tag}'
        return value


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        assert value is not None, 'You must provide enum to store'
        cb.store_uint(value, 1)
        return True


    class Record_bool_false(RecordBase):
        def get_tag_enum(self):
            return Bool.Tag.bool_false

        def get_tag(self):
            return Bool.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Bool.cons_len_exact[self.get_tag_enum().value] if isinstance(Bool.cons_len_exact, list) else Bool.cons_len_exact

        def get_type_class(self):
            return Bool


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_bool_true(RecordBase):
        def get_tag_enum(self):
            return Bool.Tag.bool_true

        def get_tag(self):
            return Bool.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Bool.cons_len_exact[self.get_tag_enum().value] if isinstance(Bool.cons_len_exact, list) else Bool.cons_len_exact

        def get_type_class(self):
            return Bool


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Bool")


# class for type `BoolFalse`
class BoolFalse(TLBComplex):
    class Tag(Enum):
        bool_false = 0

    cons_len_exact = 1
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BoolFalse.Tag.bool_false: BoolFalse.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BoolFalse.Tag"]:
        return BoolFalse.Tag(0)


    def fetch_enum(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> int:
        value = cs.load_uint(1)
        assert value == 0, 'Not valid tag fetched'
        return value


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        cb.store_uint(0, 1)
        return True


    class Record(RecordBase):
        def get_tag_enum(self):
            return BoolFalse.Tag.bool_false

        def get_tag(self):
            return BoolFalse.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BoolFalse.cons_len_exact[self.get_tag_enum().value] if isinstance(BoolFalse.cons_len_exact, list) else BoolFalse.cons_len_exact

        def get_type_class(self):
            return BoolFalse


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BoolFalse")


# class for type `BoolTrue`
class BoolTrue(TLBComplex):
    class Tag(Enum):
        bool_true = 0

    cons_len_exact = 1
    cons_tag = [1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BoolTrue.Tag.bool_true: BoolTrue.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BoolTrue.Tag"]:
        return BoolTrue.Tag(0)


    def fetch_enum(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> int:
        value = cs.load_uint(1)
        assert value == 1, 'Not valid tag fetched'
        return value


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        cb.store_uint(1, 1)
        return True


    class Record(RecordBase):
        def get_tag_enum(self):
            return BoolTrue.Tag.bool_true

        def get_tag(self):
            return BoolTrue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BoolTrue.cons_len_exact[self.get_tag_enum().value] if isinstance(BoolTrue.cons_len_exact, list) else BoolTrue.cons_len_exact

        def get_type_class(self):
            return BoolTrue


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BoolTrue")


# class for type `Maybe`
class Maybe(TLBComplex):
    class Tag(Enum):
        nothing = 0
        just = 1

    cons_len_exact = 1
    cons_tag = [0, 1]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {Maybe.Tag.nothing: self.get_param_record("Record_nothing"), Maybe.Tag.just: self.get_param_record("Record_just")}

    def get_tag(self, cs: CellSlice) -> Optional["Maybe.Tag"]:
        return Maybe.Tag(int(cs.preload_uint(1)))


    class Record_nothing(RecordBase):
        def get_tag_enum(self):
            return Maybe.Tag.nothing

        def get_tag(self):
            return Maybe.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Maybe.cons_len_exact[self.get_tag_enum().value] if isinstance(Maybe.cons_len_exact, list) else Maybe.cons_len_exact

        def get_type_class(self):
            return Maybe


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_just(RecordBase):
        def get_tag_enum(self):
            return Maybe.Tag.just

        def get_tag(self):
            return Maybe.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Maybe.cons_len_exact[self.get_tag_enum().value] if isinstance(Maybe.cons_len_exact, list) else Maybe.cons_len_exact

        def get_type_class(self):
            return Maybe

        # value : X
        value: "CellSlice" = None

        def __init__(self, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.value = self.X_.fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Maybe")


# class for type `Either`
class Either(TLBComplex):
    class Tag(Enum):
        left = 0
        right = 1

    cons_len_exact = 1
    cons_tag = [0, 1]

    X_: TLB = None
    Y_: TLB = None

    def __init__(self, X_: TLB, Y_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")
        self.Y_ = Y_
        self.params_attrs.append("Y_")

        self.has_params = True

        self.tag_to_class = {Either.Tag.left: self.get_param_record("Record_left"), Either.Tag.right: self.get_param_record("Record_right")}

    def get_tag(self, cs: CellSlice) -> Optional["Either.Tag"]:
        return Either.Tag(int(cs.preload_uint(1)))


    class Record_left(RecordBase):
        def get_tag_enum(self):
            return Either.Tag.left

        def get_tag(self):
            return Either.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Either.cons_len_exact[self.get_tag_enum().value] if isinstance(Either.cons_len_exact, list) else Either.cons_len_exact

        def get_type_class(self):
            return Either

        # value : X
        value: "CellSlice" = None

        def __init__(self, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.value = self.X_.fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_right(RecordBase):
        def get_tag_enum(self):
            return Either.Tag.right

        def get_tag(self):
            return Either.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Either.cons_len_exact[self.get_tag_enum().value] if isinstance(Either.cons_len_exact, list) else Either.cons_len_exact

        def get_type_class(self):
            return Either

        # value : Y
        value: "CellSlice" = None

        def __init__(self, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.value = self.Y_.fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Either")


# class for type `Both`
class Both(TLBComplex):
    class Tag(Enum):
        pair = 0

    cons_len_exact = 0
    cons_tag = [0]

    X_: TLB = None
    Y_: TLB = None

    def __init__(self, X_: TLB, Y_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")
        self.Y_ = Y_
        self.params_attrs.append("Y_")

        self.has_params = True

        self.tag_to_class = {Both.Tag.pair: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["Both.Tag"]:
        return Both.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Both.Tag.pair

        def get_tag(self):
            return Both.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Both.cons_len_exact[self.get_tag_enum().value] if isinstance(Both.cons_len_exact, list) else Both.cons_len_exact

        def get_type_class(self):
            return Both

        # first : X
        first: "CellSlice" = None
        # second : Y
        second: "CellSlice" = None

        def __init__(self, first: "CellSlice" = None, second: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.first = first    
            self.field_names.append("first")
            self.second = second    
            self.field_names.append("second")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.first = self.X_.fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)
                self.second = self.Y_.fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Both")


# class for type `Bit`
class Bit(TLBComplex):
    class Tag(Enum):
        bit = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Bit.Tag.bit: Bit.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Bit.Tag"]:
        return Bit.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Bit.Tag.bit

        def get_tag(self):
            return Bit.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Bit.cons_len_exact[self.get_tag_enum().value] if isinstance(Bit.cons_len_exact, list) else Bit.cons_len_exact

        def get_type_class(self):
            return Bit

        # ## 1
        x: "bool" = None

        def __init__(self, x: "bool" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_bool()
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Bit")


# class for type `Hashmap`
class Hashmap(TLBComplex):
    class Tag(Enum):
        hm_edge = 0

    cons_len_exact = 0
    cons_tag = [0]

    m_: int = None
    X_: TLB = None

    def __init__(self, m_: int, X_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {Hashmap.Tag.hm_edge: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["Hashmap.Tag"]:
        return Hashmap.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Hashmap.Tag.hm_edge

        def get_tag(self):
            return Hashmap.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Hashmap.cons_len_exact[self.get_tag_enum().value] if isinstance(Hashmap.cons_len_exact, list) else Hashmap.cons_len_exact

        def get_type_class(self):
            return Hashmap

        # n : #
        n: "int" = None
        # l : #
        l: "int" = None
        # m : #
        m: "int" = None
        # label : HmLabel ~l n
        label: "CellSlice" = None
        # node : HashmapNode m X
        node: "CellSlice" = None

        def __init__(self, label: "CellSlice" = None, node: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.l = -1    
            self.field_names.append("l")
            self.m = -1    
            self.field_names.append("m")
            self.label = label    
            self.field_names.append("label")
            self.node = node    
            self.field_names.append("node")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.n = self.m_

                assert self.n >= 0, 'Field is leq than zero'

                self.label = HmLabel(self.m_).fetch_to(self, cs, ["l"], rec_unpack, strict)
                assert self.add_r1("m", self.l, self.m_), 'Add_r1 failed'

                self.node = HashmapNode(self.m, self.X_).fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Hashmap")


# class for type `HashmapNode`
class HashmapNode(TLBComplex):
    class Tag(Enum):
        hmn_leaf = 0
        hmn_fork = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None
    X_: TLB = None

    def __init__(self, m_: int, X_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {HashmapNode.Tag.hmn_leaf: self.get_param_record("Record_hmn_leaf"), HashmapNode.Tag.hmn_fork: self.get_param_record("Record_hmn_fork")}

    def get_tag(self, cs: CellSlice) -> Optional["HashmapNode.Tag"]:
        # distinguish by parameter `m_` using 1 2 2 2
        return HashmapNode.Tag.hmn_fork if self.m_ else HashmapNode.Tag.hmn_leaf




    class Record_hmn_leaf(RecordBase):
        def get_tag_enum(self):
            return HashmapNode.Tag.hmn_leaf

        def get_tag(self):
            return HashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapNode.cons_len_exact, list) else HashmapNode.cons_len_exact

        def get_type_class(self):
            return HashmapNode

        # value : X
        value: "CellSlice" = None

        def __init__(self, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0
                self.value = self.X_.fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_hmn_fork(RecordBase):
        def get_tag_enum(self):
            return HashmapNode.Tag.hmn_fork

        def get_tag(self):
            return HashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapNode.cons_len_exact, list) else HashmapNode.cons_len_exact

        def get_type_class(self):
            return HashmapNode

        # n : #
        n: "int" = None
        # left : ^(Hashmap n X)
        left: "Cell" = None
        # right : ^(Hashmap n X)
        right: "Cell" = None

        def __init__(self, left: "Cell" = None, right: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.left = left    
            self.field_names.append("left")
            self.right = right    
            self.field_names.append("right")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = RefT(Hashmap(self.n, self.X_)).fetch(self.left, True, strict) # at 1
                    if strict:
                        assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(Hashmap(self.n, self.X_)).fetch(self.right, True, strict) # at 1
                    if strict:
                        assert self.right is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HashmapNode")


# class for type `HmLabel`
class HmLabel(TLBComplex):
    class Tag(Enum):
        hml_short = 0
        hml_long = 1
        hml_same = 2

    cons_len = [1, 2, 2]
    cons_tag = [0, 2, 3]

    n_: int = None

    def __init__(self, n_: int):
        super().__init__()
        self.n_ = n_
        self.params_attrs.append("n_")

        self.has_params = True

        self.tag_to_class = {HmLabel.Tag.hml_short: self.get_param_record("Record_hml_short"), HmLabel.Tag.hml_long: self.get_param_record("Record_hml_long"), HmLabel.Tag.hml_same: self.get_param_record("Record_hml_same")}

    def get_tag(self, cs: CellSlice) -> Optional["HmLabel.Tag"]:
        return HmLabel.Tag(int(cs.bselect(2, 13)))


    class Record_hml_short(RecordBase):
        def get_tag_enum(self):
            return HmLabel.Tag.hml_short

        def get_tag(self):
            return HmLabel.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HmLabel.cons_len_exact[self.get_tag_enum().value] if isinstance(HmLabel.cons_len_exact, list) else HmLabel.cons_len_exact

        def get_type_class(self):
            return HmLabel

        # m : #
        m: "int" = None
        # n : #
        n: "int" = None
        # len : Unary ~n
        len: "CellSlice" = None
        # s : n * Bit
        s: "bitstring.BitArray" = None

        def __init__(self, len: "CellSlice" = None, s: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.m = -1    
            self.field_names.append("m")
            self.n = -1    
            self.field_names.append("n")
            self.len = len    
            self.field_names.append("len")
            self.s = s    
            self.field_names.append("s")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.m = self.n_

                assert self.m >= 0, 'Field is leq than zero'

                self.len = TLBComplex.constants["t_Unary"].fetch_to(self, cs, ["n"], rec_unpack, strict)
                assert self.n <= self.n_, 'Params not equal: n and n_'

                self.s = cs.load_bitstring(self.n)

                self.m_ = self.n
                self.negate_params.append("m_")
                assert self.n >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_hml_long(RecordBase):
        def get_tag_enum(self):
            return HmLabel.Tag.hml_long

        def get_tag(self):
            return HmLabel.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HmLabel.cons_len_exact[self.get_tag_enum().value] if isinstance(HmLabel.cons_len_exact, list) else HmLabel.cons_len_exact

        def get_type_class(self):
            return HmLabel

        # m : #
        m: "int" = None
        # n : #<= m
        n: "int" = None
        # s : n * Bit
        s: "bitstring.BitArray" = None

        def __init__(self, n: "int" = None, s: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.m = -1    
            self.field_names.append("m")
            self.n = n    
            self.field_names.append("n")
            self.s = s    
            self.field_names.append("s")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'

                self.m = self.n_

                assert self.m >= 0, 'Field is leq than zero'

                self.n = cs.load_uint_leq(self.n_)
                self.s = cs.load_bitstring(self.n)

                self.m_ = self.n
                self.negate_params.append("m_")
                assert self.n >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_hml_same(RecordBase):
        def get_tag_enum(self):
            return HmLabel.Tag.hml_same

        def get_tag(self):
            return HmLabel.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HmLabel.cons_len_exact[self.get_tag_enum().value] if isinstance(HmLabel.cons_len_exact, list) else HmLabel.cons_len_exact

        def get_type_class(self):
            return HmLabel

        # m : #
        m: "int" = None
        # v : Bit
        v: "bool" = None
        # n : #<= m
        n: "int" = None

        def __init__(self, v: "bool" = None, n: "int" = None):
            super().__init__()
            self.field_names = []
            self.m = -1    
            self.field_names.append("m")
            self.v = v    
            self.field_names.append("v")
            self.n = n    
            self.field_names.append("n")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'

                self.m = self.n_

                assert self.m >= 0, 'Field is leq than zero'

                self.v = cs.load_bool()
                self.n = cs.load_uint_leq(self.n_)
                self.m_ = self.n
                self.negate_params.append("m_")
                assert self.n >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HmLabel")


# class for type `Unary`
class Unary(TLBComplex):
    class Tag(Enum):
        unary_zero = 0
        unary_succ = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self, ):
        super().__init__()

        self.has_params = True

        self.tag_to_class = {Unary.Tag.unary_zero: self.get_param_record("Record_unary_zero"), Unary.Tag.unary_succ: self.get_param_record("Record_unary_succ")}

    def get_tag(self, cs: CellSlice) -> Optional["Unary.Tag"]:
        return Unary.Tag(int(cs.preload_uint(1)))


    class Record_unary_zero(RecordBase):
        def get_tag_enum(self):
            return Unary.Tag.unary_zero

        def get_tag(self):
            return Unary.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Unary.cons_len_exact[self.get_tag_enum().value] if isinstance(Unary.cons_len_exact, list) else Unary.cons_len_exact

        def get_type_class(self):
            return Unary


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.m_ = 0
                self.negate_params.append("m_")
                assert 0 >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_unary_succ(RecordBase):
        def get_tag_enum(self):
            return Unary.Tag.unary_succ

        def get_tag(self):
            return Unary.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Unary.cons_len_exact[self.get_tag_enum().value] if isinstance(Unary.cons_len_exact, list) else Unary.cons_len_exact

        def get_type_class(self):
            return Unary

        # n : #
        n: "int" = None
        # x : Unary ~n
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.x = TLBComplex.constants["t_Unary"].fetch_to(self, cs, ["n"], rec_unpack, strict)
                self.m_ = self.n + 1
                self.negate_params.append("m_")
                assert self.n + 1 >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Unary")


# class for type `HashmapE`
class HashmapE(TLBComplex):
    class Tag(Enum):
        hme_empty = 0
        hme_root = 1

    cons_len_exact = 1
    cons_tag = [0, 1]

    m_: int = None
    X_: TLB = None

    def __init__(self, m_: int, X_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {HashmapE.Tag.hme_empty: self.get_param_record("Record_hme_empty"), HashmapE.Tag.hme_root: self.get_param_record("Record_hme_root")}

    def get_tag(self, cs: CellSlice) -> Optional["HashmapE.Tag"]:
        return HashmapE.Tag(int(cs.preload_uint(1)))


    class Record_hme_empty(RecordBase):
        def get_tag_enum(self):
            return HashmapE.Tag.hme_empty

        def get_tag(self):
            return HashmapE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapE.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapE.cons_len_exact, list) else HashmapE.cons_len_exact

        def get_type_class(self):
            return HashmapE


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    class Record_hme_root(RecordBase):
        def get_tag_enum(self):
            return HashmapE.Tag.hme_root

        def get_tag(self):
            return HashmapE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapE.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapE.cons_len_exact, list) else HashmapE.cons_len_exact

        def get_type_class(self):
            return HashmapE

        # n : #
        n: "int" = None
        # root : ^(Hashmap n X)
        root: "Cell" = None

        def __init__(self, root: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.root = root    
            self.field_names.append("root")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.n = self.m_

                assert self.n >= 0, 'Field is leq than zero'

                self.root = cs.load_ref()
                
                if rec_unpack:
                    self.root = RefT(Hashmap(self.m_, self.X_)).fetch(self.root, True, strict) # at 1
                    if strict:
                        assert self.root is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HashmapE")


# class for type `BitstringSet`
class BitstringSet(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {BitstringSet.Tag.cons1: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["BitstringSet.Tag"]:
        return BitstringSet.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BitstringSet.Tag.cons1

        def get_tag(self):
            return BitstringSet.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BitstringSet.cons_len_exact[self.get_tag_enum().value] if isinstance(BitstringSet.cons_len_exact, list) else BitstringSet.cons_len_exact

        def get_type_class(self):
            return BitstringSet

        # n : #
        n: "int" = None
        # Hashmap n Truet
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.n = self.m_

                assert self.n >= 0, 'Field is leq than zero'

                self.x = Hashmap(self.m_, TLBComplex.constants["t_Truet"]).fetch(cs, rec_unpack=rec_unpack, strict=strict, load_ref=True)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (RuntimeError, KeyError, ValueError, AssertionError, IndexError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BitstringSet")

# definitions of constants
TLBComplex.constants["t_Unit"] = Unit()
TLBComplex.constants["t_Truet"] = Truet()
TLBComplex.constants["t_Bool"] = Bool()
TLBComplex.constants["t_BoolFalse"] = BoolFalse()
TLBComplex.constants["t_BoolTrue"] = BoolTrue()
TLBComplex.constants["t_Bit"] = Bit()
TLBComplex.constants["t_Unary"] = Unary()

TLBComplex.constants["t_natwidth_1"] = NatWidth(1)
