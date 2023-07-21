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


    def fetch_enum(self, cs: CellSlice) -> int:
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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


    def fetch_enum(self, cs: CellSlice) -> int:
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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


    def fetch_enum(self, cs: CellSlice) -> int:
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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


    def fetch_enum(self, cs: CellSlice) -> int:
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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


    def fetch_enum(self, cs: CellSlice) -> int:
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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

                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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

                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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

                self.value = self.Y_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
                self.first = self.X_.fetch(cs) 
                self.second = self.Y_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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

                self.node = HashmapNode(self.m, self.X_).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(Hashmap(self.n, self.X_)).fetch(self.right, True, strict) # at 1
                    assert self.right is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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

                
                if rec_unpack and self.s is not None:
                    self.s = TLBComplex.constants["t_tuple_Bit"].fetch(self.s, True, strict) # at 3
                    assert self.s is not None

                self.m_ = self.n
                self.negate_params.append("m_")
                assert self.n >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (TabError):
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

                
                if rec_unpack and self.s is not None:
                    self.s = TLBComplex.constants["t_tuple_Bit"].fetch(self.s, True, strict) # at 3
                    assert self.s is not None

                self.m_ = self.n
                self.negate_params.append("m_")
                assert self.n >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (TabError):
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (TabError):
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (TabError):
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

                self.x = self.fetch_to(self, cs, ["n"], rec_unpack, strict)
                self.m_ = self.n + 1
                self.negate_params.append("m_")
                assert self.n + 1 >= 0, 'Constraint check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs, self.m_) and cs.empty_ext()

            except (TabError):
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
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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
                    assert self.root is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
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

                self.x = Hashmap(self.m_, t_Truet).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BitstringSet")


# class for type `HashmapAug`
class HashmapAug(TLBComplex):
    class Tag(Enum):
        ahm_edge = 0

    cons_len_exact = 0
    cons_tag = [0]

    m_: int = None
    X_: TLB = None
    Y_: TLB = None

    def __init__(self, m_: int, X_: TLB, Y_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")
        self.Y_ = Y_
        self.params_attrs.append("Y_")

        self.has_params = True

        self.tag_to_class = {HashmapAug.Tag.ahm_edge: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["HashmapAug.Tag"]:
        return HashmapAug.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return HashmapAug.Tag.ahm_edge

        def get_tag(self):
            return HashmapAug.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapAug.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapAug.cons_len_exact, list) else HashmapAug.cons_len_exact

        def get_type_class(self):
            return HashmapAug

        # n : #
        n: "int" = None
        # l : #
        l: "int" = None
        # m : #
        m: "int" = None
        # label : HmLabel ~l n
        label: "CellSlice" = None
        # node : HashmapAugNode m X Y
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

                self.node = HashmapAugNode(self.m, self.X_, self.Y_).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HashmapAug")


# class for type `HashmapAugNode`
class HashmapAugNode(TLBComplex):
    class Tag(Enum):
        ahmn_leaf = 0
        ahmn_fork = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None
    X_: TLB = None
    Y_: TLB = None

    def __init__(self, m_: int, X_: TLB, Y_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")
        self.Y_ = Y_
        self.params_attrs.append("Y_")

        self.has_params = True

        self.tag_to_class = {HashmapAugNode.Tag.ahmn_leaf: self.get_param_record("Record_ahmn_leaf"), HashmapAugNode.Tag.ahmn_fork: self.get_param_record("Record_ahmn_fork")}

    def get_tag(self, cs: CellSlice) -> Optional["HashmapAugNode.Tag"]:
        # distinguish by parameter `m_` using 1 2 2 2
        return HashmapAugNode.Tag.ahmn_fork if self.m_ else HashmapAugNode.Tag.ahmn_leaf




    class Record_ahmn_leaf(RecordBase):
        def get_tag_enum(self):
            return HashmapAugNode.Tag.ahmn_leaf

        def get_tag(self):
            return HashmapAugNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapAugNode.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapAugNode.cons_len_exact, list) else HashmapAugNode.cons_len_exact

        def get_type_class(self):
            return HashmapAugNode

        # extra : Y
        extra: "CellSlice" = None
        # value : X
        value: "CellSlice" = None

        def __init__(self, extra: "CellSlice" = None, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.extra = extra    
            self.field_names.append("extra")
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0
                self.extra = self.Y_.fetch(cs) 
                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_ahmn_fork(RecordBase):
        def get_tag_enum(self):
            return HashmapAugNode.Tag.ahmn_fork

        def get_tag(self):
            return HashmapAugNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapAugNode.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapAugNode.cons_len_exact, list) else HashmapAugNode.cons_len_exact

        def get_type_class(self):
            return HashmapAugNode

        # n : #
        n: "int" = None
        # left : ^(HashmapAug n X Y)
        left: "Cell" = None
        # right : ^(HashmapAug n X Y)
        right: "Cell" = None
        # extra : Y
        extra: "CellSlice" = None

        def __init__(self, left: "Cell" = None, right: "Cell" = None, extra: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.left = left    
            self.field_names.append("left")
            self.right = right    
            self.field_names.append("right")
            self.extra = extra    
            self.field_names.append("extra")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = RefT(HashmapAug(self.n, self.X_, self.Y_)).fetch(self.left, True, strict) # at 1
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(HashmapAug(self.n, self.X_, self.Y_)).fetch(self.right, True, strict) # at 1
                    assert self.right is not None

                self.extra = self.Y_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HashmapAugNode")


# class for type `HashmapAugE`
class HashmapAugE(TLBComplex):
    class Tag(Enum):
        ahme_empty = 0
        ahme_root = 1

    cons_len_exact = 1
    cons_tag = [0, 1]

    m_: int = None
    X_: TLB = None
    Y_: TLB = None

    def __init__(self, m_: int, X_: TLB, Y_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")
        self.Y_ = Y_
        self.params_attrs.append("Y_")

        self.has_params = True

        self.tag_to_class = {HashmapAugE.Tag.ahme_empty: self.get_param_record("Record_ahme_empty"), HashmapAugE.Tag.ahme_root: self.get_param_record("Record_ahme_root")}

    def get_tag(self, cs: CellSlice) -> Optional["HashmapAugE.Tag"]:
        return HashmapAugE.Tag(int(cs.preload_uint(1)))


    class Record_ahme_empty(RecordBase):
        def get_tag_enum(self):
            return HashmapAugE.Tag.ahme_empty

        def get_tag(self):
            return HashmapAugE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapAugE.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapAugE.cons_len_exact, list) else HashmapAugE.cons_len_exact

        def get_type_class(self):
            return HashmapAugE

        # extra : Y
        extra: "CellSlice" = None

        def __init__(self, extra: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.extra = extra    
            self.field_names.append("extra")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.extra = self.Y_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_ahme_root(RecordBase):
        def get_tag_enum(self):
            return HashmapAugE.Tag.ahme_root

        def get_tag(self):
            return HashmapAugE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HashmapAugE.cons_len_exact[self.get_tag_enum().value] if isinstance(HashmapAugE.cons_len_exact, list) else HashmapAugE.cons_len_exact

        def get_type_class(self):
            return HashmapAugE

        # n : #
        n: "int" = None
        # root : ^(HashmapAug n X Y)
        root: "Cell" = None
        # extra : Y
        extra: "CellSlice" = None

        def __init__(self, root: "Cell" = None, extra: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.root = root    
            self.field_names.append("root")
            self.extra = extra    
            self.field_names.append("extra")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.n = self.m_

                assert self.n >= 0, 'Field is leq than zero'

                self.root = cs.load_ref()
                
                if rec_unpack:
                    self.root = RefT(HashmapAug(self.m_, self.X_, self.Y_)).fetch(self.root, True, strict) # at 1
                    assert self.root is not None

                self.extra = self.Y_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HashmapAugE")


# class for type `VarHashmap`
class VarHashmap(TLBComplex):
    class Tag(Enum):
        vhm_edge = 0

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

        self.tag_to_class = {VarHashmap.Tag.vhm_edge: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["VarHashmap.Tag"]:
        return VarHashmap.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VarHashmap.Tag.vhm_edge

        def get_tag(self):
            return VarHashmap.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarHashmap.cons_len_exact[self.get_tag_enum().value] if isinstance(VarHashmap.cons_len_exact, list) else VarHashmap.cons_len_exact

        def get_type_class(self):
            return VarHashmap

        # n : #
        n: "int" = None
        # l : #
        l: "int" = None
        # m : #
        m: "int" = None
        # label : HmLabel ~l n
        label: "CellSlice" = None
        # node : VarHashmapNode m X
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

                self.node = VarHashmapNode(self.m, self.X_).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VarHashmap")


# class for type `VarHashmapNode`
class VarHashmapNode(TLBComplex):
    class Tag(Enum):
        vhmn_leaf = 0
        vhmn_fork = 1
        vhmn_cont = 2

    cons_len = [2, 2, 1]
    cons_tag = [0, 1, 1]

    m_: int = None
    X_: TLB = None

    def __init__(self, m_: int, X_: TLB):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {VarHashmapNode.Tag.vhmn_leaf: self.get_param_record("Record_vhmn_leaf"), VarHashmapNode.Tag.vhmn_fork: self.get_param_record("Record_vhmn_fork"), VarHashmapNode.Tag.vhmn_cont: self.get_param_record("Record_vhmn_cont")}

    def get_tag(self, cs: CellSlice) -> Optional["VarHashmapNode.Tag"]:
        return VarHashmapNode.Tag(int(cs.bselect(2, 7)))


    class Record_vhmn_leaf(RecordBase):
        def get_tag_enum(self):
            return VarHashmapNode.Tag.vhmn_leaf

        def get_tag(self):
            return VarHashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarHashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(VarHashmapNode.cons_len_exact, list) else VarHashmapNode.cons_len_exact

        def get_type_class(self):
            return VarHashmapNode

        # value : X
        value: "CellSlice" = None

        def __init__(self, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'

                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vhmn_fork(RecordBase):
        def get_tag_enum(self):
            return VarHashmapNode.Tag.vhmn_fork

        def get_tag(self):
            return VarHashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarHashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(VarHashmapNode.cons_len_exact, list) else VarHashmapNode.cons_len_exact

        def get_type_class(self):
            return VarHashmapNode

        # n : #
        n: "int" = None
        # left : ^(VarHashmap n X)
        left: "Cell" = None
        # right : ^(VarHashmap n X)
        right: "Cell" = None
        # value : Maybe X
        value: "CellSlice" = None

        def __init__(self, left: "Cell" = None, right: "Cell" = None, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.left = left    
            self.field_names.append("left")
            self.right = right    
            self.field_names.append("right")
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'

                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = RefT(VarHashmap(self.n, self.X_)).fetch(self.left, True, strict) # at 1
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(VarHashmap(self.n, self.X_)).fetch(self.right, True, strict) # at 1
                    assert self.right is not None

                self.value = Maybe(self.X_).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vhmn_cont(RecordBase):
        def get_tag_enum(self):
            return VarHashmapNode.Tag.vhmn_cont

        def get_tag(self):
            return VarHashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarHashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(VarHashmapNode.cons_len_exact, list) else VarHashmapNode.cons_len_exact

        def get_type_class(self):
            return VarHashmapNode

        # n : #
        n: "int" = None
        # branch : Bit
        branch: "bool" = None
        # child : ^(VarHashmap n X)
        child: "Cell" = None
        # value : X
        value: "CellSlice" = None

        def __init__(self, branch: "bool" = None, child: "Cell" = None, value: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.branch = branch    
            self.field_names.append("branch")
            self.child = child    
            self.field_names.append("child")
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.branch = cs.load_bool()
                self.child = cs.load_ref()
                
                if rec_unpack:
                    self.child = RefT(VarHashmap(self.n, self.X_)).fetch(self.child, True, strict) # at 1
                    assert self.child is not None

                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VarHashmapNode")


# class for type `VarHashmapE`
class VarHashmapE(TLBComplex):
    class Tag(Enum):
        vhme_empty = 0
        vhme_root = 1

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

        self.tag_to_class = {VarHashmapE.Tag.vhme_empty: self.get_param_record("Record_vhme_empty"), VarHashmapE.Tag.vhme_root: self.get_param_record("Record_vhme_root")}

    def get_tag(self, cs: CellSlice) -> Optional["VarHashmapE.Tag"]:
        return VarHashmapE.Tag(int(cs.preload_uint(1)))


    class Record_vhme_empty(RecordBase):
        def get_tag_enum(self):
            return VarHashmapE.Tag.vhme_empty

        def get_tag(self):
            return VarHashmapE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarHashmapE.cons_len_exact[self.get_tag_enum().value] if isinstance(VarHashmapE.cons_len_exact, list) else VarHashmapE.cons_len_exact

        def get_type_class(self):
            return VarHashmapE


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vhme_root(RecordBase):
        def get_tag_enum(self):
            return VarHashmapE.Tag.vhme_root

        def get_tag(self):
            return VarHashmapE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarHashmapE.cons_len_exact[self.get_tag_enum().value] if isinstance(VarHashmapE.cons_len_exact, list) else VarHashmapE.cons_len_exact

        def get_type_class(self):
            return VarHashmapE

        # n : #
        n: "int" = None
        # root : ^(VarHashmap n X)
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
                    self.root = RefT(VarHashmap(self.m_, self.X_)).fetch(self.root, True, strict) # at 1
                    assert self.root is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VarHashmapE")


# class for type `PfxHashmap`
class PfxHashmap(TLBComplex):
    class Tag(Enum):
        phm_edge = 0

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

        self.tag_to_class = {PfxHashmap.Tag.phm_edge: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["PfxHashmap.Tag"]:
        return PfxHashmap.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return PfxHashmap.Tag.phm_edge

        def get_tag(self):
            return PfxHashmap.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return PfxHashmap.cons_len_exact[self.get_tag_enum().value] if isinstance(PfxHashmap.cons_len_exact, list) else PfxHashmap.cons_len_exact

        def get_type_class(self):
            return PfxHashmap

        # n : #
        n: "int" = None
        # l : #
        l: "int" = None
        # m : #
        m: "int" = None
        # label : HmLabel ~l n
        label: "CellSlice" = None
        # node : PfxHashmapNode m X
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

                self.node = PfxHashmapNode(self.m, self.X_).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("PfxHashmap")


# class for type `PfxHashmapNode`
class PfxHashmapNode(TLBComplex):
    class Tag(Enum):
        phmn_leaf = 0
        phmn_fork = 1

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

        self.tag_to_class = {PfxHashmapNode.Tag.phmn_leaf: self.get_param_record("Record_phmn_leaf"), PfxHashmapNode.Tag.phmn_fork: self.get_param_record("Record_phmn_fork")}

    def get_tag(self, cs: CellSlice) -> Optional["PfxHashmapNode.Tag"]:
        return PfxHashmapNode.Tag(int(cs.preload_uint(1)))


    class Record_phmn_leaf(RecordBase):
        def get_tag_enum(self):
            return PfxHashmapNode.Tag.phmn_leaf

        def get_tag(self):
            return PfxHashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return PfxHashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(PfxHashmapNode.cons_len_exact, list) else PfxHashmapNode.cons_len_exact

        def get_type_class(self):
            return PfxHashmapNode

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

                self.value = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_phmn_fork(RecordBase):
        def get_tag_enum(self):
            return PfxHashmapNode.Tag.phmn_fork

        def get_tag(self):
            return PfxHashmapNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return PfxHashmapNode.cons_len_exact[self.get_tag_enum().value] if isinstance(PfxHashmapNode.cons_len_exact, list) else PfxHashmapNode.cons_len_exact

        def get_type_class(self):
            return PfxHashmapNode

        # n : #
        n: "int" = None
        # left : ^(PfxHashmap n X)
        left: "Cell" = None
        # right : ^(PfxHashmap n X)
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
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = RefT(PfxHashmap(self.n, self.X_)).fetch(self.left, True, strict) # at 1
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(PfxHashmap(self.n, self.X_)).fetch(self.right, True, strict) # at 1
                    assert self.right is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("PfxHashmapNode")


# class for type `PfxHashmapE`
class PfxHashmapE(TLBComplex):
    class Tag(Enum):
        phme_empty = 0
        phme_root = 1

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

        self.tag_to_class = {PfxHashmapE.Tag.phme_empty: self.get_param_record("Record_phme_empty"), PfxHashmapE.Tag.phme_root: self.get_param_record("Record_phme_root")}

    def get_tag(self, cs: CellSlice) -> Optional["PfxHashmapE.Tag"]:
        return PfxHashmapE.Tag(int(cs.preload_uint(1)))


    class Record_phme_empty(RecordBase):
        def get_tag_enum(self):
            return PfxHashmapE.Tag.phme_empty

        def get_tag(self):
            return PfxHashmapE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return PfxHashmapE.cons_len_exact[self.get_tag_enum().value] if isinstance(PfxHashmapE.cons_len_exact, list) else PfxHashmapE.cons_len_exact

        def get_type_class(self):
            return PfxHashmapE


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_phme_root(RecordBase):
        def get_tag_enum(self):
            return PfxHashmapE.Tag.phme_root

        def get_tag(self):
            return PfxHashmapE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return PfxHashmapE.cons_len_exact[self.get_tag_enum().value] if isinstance(PfxHashmapE.cons_len_exact, list) else PfxHashmapE.cons_len_exact

        def get_type_class(self):
            return PfxHashmapE

        # n : #
        n: "int" = None
        # root : ^(PfxHashmap n X)
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
                    self.root = RefT(PfxHashmap(self.m_, self.X_)).fetch(self.root, True, strict) # at 1
                    assert self.root is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("PfxHashmapE")


# class for type `MsgAddressExt`
class MsgAddressExt(TLBComplex):
    class Tag(Enum):
        addr_none = 0
        addr_extern = 1

    cons_len_exact = 2
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MsgAddressExt.Tag.addr_none: MsgAddressExt.Record_addr_none, MsgAddressExt.Tag.addr_extern: MsgAddressExt.Record_addr_extern}

    def get_tag(self, cs: CellSlice) -> Optional["MsgAddressExt.Tag"]:
        return MsgAddressExt.Tag(int(cs.bselect(2, 3)))


    class Record_addr_none(RecordBase):
        def get_tag_enum(self):
            return MsgAddressExt.Tag.addr_none

        def get_tag(self):
            return MsgAddressExt.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgAddressExt.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgAddressExt.cons_len_exact, list) else MsgAddressExt.cons_len_exact

        def get_type_class(self):
            return MsgAddressExt


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_addr_extern(RecordBase):
        def get_tag_enum(self):
            return MsgAddressExt.Tag.addr_extern

        def get_tag(self):
            return MsgAddressExt.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgAddressExt.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgAddressExt.cons_len_exact, list) else MsgAddressExt.cons_len_exact

        def get_type_class(self):
            return MsgAddressExt

        # len : ## 9
        len: "int" = None
        # external_address : bits len
        external_address: "bitstring.BitArray" = None

        def __init__(self, len: "int" = None, external_address: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.len = len    
            self.field_names.append("len")
            self.external_address = external_address    
            self.field_names.append("external_address")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'

                self.len = cs.load_uint(9)
                self.external_address = cs.load_bitstring(self.len)

                
                if rec_unpack and self.external_address is not None:
                    self.external_address = TLBComplex.constants["t_bits"].fetch(self.external_address, True, strict) # at 3
                    assert self.external_address is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MsgAddressExt")


# class for type `Anycast`
class Anycast(TLBComplex):
    class Tag(Enum):
        anycast_info = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Anycast.Tag.anycast_info: Anycast.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Anycast.Tag"]:
        return Anycast.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Anycast.Tag.anycast_info

        def get_tag(self):
            return Anycast.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Anycast.cons_len_exact[self.get_tag_enum().value] if isinstance(Anycast.cons_len_exact, list) else Anycast.cons_len_exact

        def get_type_class(self):
            return Anycast

        # depth : #<= 30
        depth: "int" = None
        # rewrite_pfx : bits depth
        rewrite_pfx: "bitstring.BitArray" = None

        def __init__(self, depth: "int" = None, rewrite_pfx: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.depth = depth    
            self.field_names.append("depth")
            self.rewrite_pfx = rewrite_pfx    
            self.field_names.append("rewrite_pfx")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.depth = cs.load_uint_leq(30)
                assert 1 <= self.depth, 'Params not equal: 1 and depth'

                self.rewrite_pfx = cs.load_bitstring(self.depth)

                
                if rec_unpack and self.rewrite_pfx is not None:
                    self.rewrite_pfx = TLBComplex.constants["t_bits"].fetch(self.rewrite_pfx, True, strict) # at 3
                    assert self.rewrite_pfx is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Anycast")


# class for type `MsgAddressInt`
class MsgAddressInt(TLBComplex):
    class Tag(Enum):
        addr_std = 0
        addr_var = 1

    cons_len_exact = 2
    cons_tag = [2, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MsgAddressInt.Tag.addr_std: MsgAddressInt.Record_addr_std, MsgAddressInt.Tag.addr_var: MsgAddressInt.Record_addr_var}

    def get_tag(self, cs: CellSlice) -> Optional["MsgAddressInt.Tag"]:
        return MsgAddressInt.Tag(int(cs.bselect(2, 12)))


    class Record_addr_std(RecordBase):
        def get_tag_enum(self):
            return MsgAddressInt.Tag.addr_std

        def get_tag(self):
            return MsgAddressInt.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgAddressInt.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgAddressInt.cons_len_exact, list) else MsgAddressInt.cons_len_exact

        def get_type_class(self):
            return MsgAddressInt

        # anycast : Maybe Anycast
        anycast: "CellSlice" = None
        # workchain_id : int8
        workchain_id: "int" = None
        # address : bits256
        address: "bitstring.BitArray" = None

        def __init__(self, anycast: "CellSlice" = None, workchain_id: "int" = None, address: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.anycast = anycast    
            self.field_names.append("anycast")
            self.workchain_id = workchain_id    
            self.field_names.append("workchain_id")
            self.address = address    
            self.field_names.append("address")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'

                self.anycast = TLBComplex.constants["t_Maybe_Anycast"].fetch(cs) 
                self.workchain_id = cs.load_int(8)
                self.address = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_addr_var(RecordBase):
        def get_tag_enum(self):
            return MsgAddressInt.Tag.addr_var

        def get_tag(self):
            return MsgAddressInt.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgAddressInt.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgAddressInt.cons_len_exact, list) else MsgAddressInt.cons_len_exact

        def get_type_class(self):
            return MsgAddressInt

        # anycast : Maybe Anycast
        anycast: "CellSlice" = None
        # addr_len : ## 9
        addr_len: "int" = None
        # workchain_id : int32
        workchain_id: "int" = None
        # address : bits addr_len
        address: "bitstring.BitArray" = None

        def __init__(self, anycast: "CellSlice" = None, addr_len: "int" = None, workchain_id: "int" = None, address: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.anycast = anycast    
            self.field_names.append("anycast")
            self.addr_len = addr_len    
            self.field_names.append("addr_len")
            self.workchain_id = workchain_id    
            self.field_names.append("workchain_id")
            self.address = address    
            self.field_names.append("address")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'

                self.anycast = TLBComplex.constants["t_Maybe_Anycast"].fetch(cs) 
                self.addr_len = cs.load_uint(9)
                self.workchain_id = cs.load_int(32)
                self.address = cs.load_bitstring(self.addr_len)

                
                if rec_unpack and self.address is not None:
                    self.address = TLBComplex.constants["t_bits"].fetch(self.address, True, strict) # at 3
                    assert self.address is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MsgAddressInt")


# class for type `MsgAddress`
class MsgAddress(TLBComplex):
    class Tag(Enum):
        cons2 = 0
        cons1 = 1

    cons_len_exact = 0
    cons_tag = [0, 0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MsgAddress.Tag.cons1: MsgAddress.Record_cons1, MsgAddress.Tag.cons2: MsgAddress.Record_cons2}

    def get_tag(self, cs: CellSlice) -> Optional["MsgAddress.Tag"]:
        return MsgAddress.Tag(int(cs.preload_uint(1)))


    class Record_cons1(RecordBase):
        def get_tag_enum(self):
            return MsgAddress.Tag.cons1

        def get_tag(self):
            return MsgAddress.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgAddress.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgAddress.cons_len_exact, list) else MsgAddress.cons_len_exact

        def get_type_class(self):
            return MsgAddress

        # MsgAddressInt
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_MsgAddressInt"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons2(RecordBase):
        def get_tag_enum(self):
            return MsgAddress.Tag.cons2

        def get_tag(self):
            return MsgAddress.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgAddress.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgAddress.cons_len_exact, list) else MsgAddress.cons_len_exact

        def get_type_class(self):
            return MsgAddress

        # MsgAddressExt
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_MsgAddressExt"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MsgAddress")


# class for type `VarUInteger`
class VarUInteger(TLBComplex):
    class Tag(Enum):
        var_uint = 0

    cons_len_exact = 0
    cons_tag = [0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {VarUInteger.Tag.var_uint: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["VarUInteger.Tag"]:
        return VarUInteger.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VarUInteger.Tag.var_uint

        def get_tag(self):
            return VarUInteger.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarUInteger.cons_len_exact[self.get_tag_enum().value] if isinstance(VarUInteger.cons_len_exact, list) else VarUInteger.cons_len_exact

        def get_type_class(self):
            return VarUInteger

        # n : #
        n: "int" = None
        # len : #< n
        len: "int" = None
        # value : uint (8 * len)
        value: "int" = None

        def __init__(self, len: "int" = None, value: "int" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.len = len    
            self.field_names.append("len")
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.n = self.m_

                assert self.n >= 0, 'Field is leq than zero'

                self.len = cs.load_uint_less(self.m_)
                self.value = cs.load_uint(8 * self.len)

                
                if rec_unpack and self.value is not None:
                    self.value = TLBComplex.constants["t_uint_mul8"].fetch(self.value, True, strict) # at 3
                    assert self.value is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VarUInteger")


# class for type `VarInteger`
class VarInteger(TLBComplex):
    class Tag(Enum):
        var_int = 0

    cons_len_exact = 0
    cons_tag = [0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {VarInteger.Tag.var_int: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["VarInteger.Tag"]:
        return VarInteger.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VarInteger.Tag.var_int

        def get_tag(self):
            return VarInteger.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VarInteger.cons_len_exact[self.get_tag_enum().value] if isinstance(VarInteger.cons_len_exact, list) else VarInteger.cons_len_exact

        def get_type_class(self):
            return VarInteger

        # n : #
        n: "int" = None
        # len : #< n
        len: "int" = None
        # value : int (8 * len)
        value: "int" = None

        def __init__(self, len: "int" = None, value: "int" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.len = len    
            self.field_names.append("len")
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.n = self.m_

                assert self.n >= 0, 'Field is leq than zero'

                self.len = cs.load_uint_less(self.m_)
                self.value = cs.load_int(8 * self.len)

                
                if rec_unpack and self.value is not None:
                    self.value = TLBComplex.constants["t_int_mul8"].fetch(self.value, True, strict) # at 3
                    assert self.value is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VarInteger")


# class for type `Grams`
class Grams(TLBComplex):
    class Tag(Enum):
        nanograms = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Grams.Tag.nanograms: Grams.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Grams.Tag"]:
        return Grams.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Grams.Tag.nanograms

        def get_tag(self):
            return Grams.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Grams.cons_len_exact[self.get_tag_enum().value] if isinstance(Grams.cons_len_exact, list) else Grams.cons_len_exact

        def get_type_class(self):
            return Grams

        # amount : VarUInteger 16
        amount: "CellSlice" = None

        def __init__(self, amount: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.amount = amount    
            self.field_names.append("amount")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.amount = TLBComplex.constants["t_VarUInteger_16"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Grams")


# class for type `Coins`
class Coins(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Coins.Tag.cons1: Coins.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Coins.Tag"]:
        return Coins.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Coins.Tag.cons1

        def get_tag(self):
            return Coins.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Coins.cons_len_exact[self.get_tag_enum().value] if isinstance(Coins.cons_len_exact, list) else Coins.cons_len_exact

        def get_type_class(self):
            return Coins

        # grams : Grams
        grams: "CellSlice" = None

        def __init__(self, grams: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.grams = grams    
            self.field_names.append("grams")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.grams = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Coins")


# class for type `ExtraCurrencyCollection`
class ExtraCurrencyCollection(TLBComplex):
    class Tag(Enum):
        extra_currencies = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ExtraCurrencyCollection.Tag.extra_currencies: ExtraCurrencyCollection.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ExtraCurrencyCollection.Tag"]:
        return ExtraCurrencyCollection.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ExtraCurrencyCollection.Tag.extra_currencies

        def get_tag(self):
            return ExtraCurrencyCollection.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ExtraCurrencyCollection.cons_len_exact[self.get_tag_enum().value] if isinstance(ExtraCurrencyCollection.cons_len_exact, list) else ExtraCurrencyCollection.cons_len_exact

        def get_type_class(self):
            return ExtraCurrencyCollection

        # dict : HashmapE 32 (VarUInteger 32)
        dict: "CellSlice" = None

        def __init__(self, dict: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.dict = dict    
            self.field_names.append("dict")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.dict = TLBComplex.constants["t_HashmapE_32_VarUInteger_32"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ExtraCurrencyCollection")


# class for type `CurrencyCollection`
class CurrencyCollection(TLBComplex):
    class Tag(Enum):
        currencies = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CurrencyCollection.Tag.currencies: CurrencyCollection.Record}

    def get_tag(self, cs: CellSlice) -> Optional["CurrencyCollection.Tag"]:
        return CurrencyCollection.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return CurrencyCollection.Tag.currencies

        def get_tag(self):
            return CurrencyCollection.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CurrencyCollection.cons_len_exact[self.get_tag_enum().value] if isinstance(CurrencyCollection.cons_len_exact, list) else CurrencyCollection.cons_len_exact

        def get_type_class(self):
            return CurrencyCollection

        # grams : Grams
        grams: "CellSlice" = None
        # other : ExtraCurrencyCollection
        other: "CellSlice" = None

        def __init__(self, grams: "CellSlice" = None, other: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.grams = grams    
            self.field_names.append("grams")
            self.other = other    
            self.field_names.append("other")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.grams = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.other = TLBComplex.constants["t_ExtraCurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CurrencyCollection")


# class for type `CommonMsgInfo`
class CommonMsgInfo(TLBComplex):
    class Tag(Enum):
        int_msg_info = 0
        ext_in_msg_info = 1
        ext_out_msg_info = 2

    cons_len = [1, 2, 2]
    cons_tag = [0, 2, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CommonMsgInfo.Tag.int_msg_info: CommonMsgInfo.Record_int_msg_info, CommonMsgInfo.Tag.ext_in_msg_info: CommonMsgInfo.Record_ext_in_msg_info, CommonMsgInfo.Tag.ext_out_msg_info: CommonMsgInfo.Record_ext_out_msg_info}

    def get_tag(self, cs: CellSlice) -> Optional["CommonMsgInfo.Tag"]:
        return CommonMsgInfo.Tag(int(cs.bselect(2, 13)))


    class Record_int_msg_info(RecordBase):
        def get_tag_enum(self):
            return CommonMsgInfo.Tag.int_msg_info

        def get_tag(self):
            return CommonMsgInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CommonMsgInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(CommonMsgInfo.cons_len_exact, list) else CommonMsgInfo.cons_len_exact

        def get_type_class(self):
            return CommonMsgInfo

        # ihr_disabled : Bool
        ihr_disabled: "bool" = None
        # bounce : Bool
        bounce: "bool" = None
        # bounced : Bool
        bounced: "bool" = None
        # src : MsgAddressInt
        src: "CellSlice" = None
        # dest : MsgAddressInt
        dest: "CellSlice" = None
        # value : CurrencyCollection
        value: "CellSlice" = None
        # ihr_fee : Grams
        ihr_fee: "CellSlice" = None
        # fwd_fee : Grams
        fwd_fee: "CellSlice" = None
        # created_lt : uint64
        created_lt: "int" = None
        # created_at : uint32
        created_at: "int" = None

        def __init__(self, ihr_disabled: "bool" = None, bounce: "bool" = None, bounced: "bool" = None, src: "CellSlice" = None, dest: "CellSlice" = None, value: "CellSlice" = None, ihr_fee: "CellSlice" = None, fwd_fee: "CellSlice" = None, created_lt: "int" = None, created_at: "int" = None):
            super().__init__()
            self.field_names = []
            self.ihr_disabled = ihr_disabled    
            self.field_names.append("ihr_disabled")
            self.bounce = bounce    
            self.field_names.append("bounce")
            self.bounced = bounced    
            self.field_names.append("bounced")
            self.src = src    
            self.field_names.append("src")
            self.dest = dest    
            self.field_names.append("dest")
            self.value = value    
            self.field_names.append("value")
            self.ihr_fee = ihr_fee    
            self.field_names.append("ihr_fee")
            self.fwd_fee = fwd_fee    
            self.field_names.append("fwd_fee")
            self.created_lt = created_lt    
            self.field_names.append("created_lt")
            self.created_at = created_at    
            self.field_names.append("created_at")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.ihr_disabled = cs.load_bool()
                self.bounce = cs.load_bool()
                self.bounced = cs.load_bool()
                self.src = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.dest = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.value = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.ihr_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.fwd_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.created_lt = cs.load_uint(64)
                self.created_at = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_ext_in_msg_info(RecordBase):
        def get_tag_enum(self):
            return CommonMsgInfo.Tag.ext_in_msg_info

        def get_tag(self):
            return CommonMsgInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CommonMsgInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(CommonMsgInfo.cons_len_exact, list) else CommonMsgInfo.cons_len_exact

        def get_type_class(self):
            return CommonMsgInfo

        # src : MsgAddressExt
        src: "CellSlice" = None
        # dest : MsgAddressInt
        dest: "CellSlice" = None
        # import_fee : Grams
        import_fee: "CellSlice" = None

        def __init__(self, src: "CellSlice" = None, dest: "CellSlice" = None, import_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.src = src    
            self.field_names.append("src")
            self.dest = dest    
            self.field_names.append("dest")
            self.import_fee = import_fee    
            self.field_names.append("import_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'

                self.src = TLBComplex.constants["t_MsgAddressExt"].fetch(cs) 
                self.dest = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.import_fee = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_ext_out_msg_info(RecordBase):
        def get_tag_enum(self):
            return CommonMsgInfo.Tag.ext_out_msg_info

        def get_tag(self):
            return CommonMsgInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CommonMsgInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(CommonMsgInfo.cons_len_exact, list) else CommonMsgInfo.cons_len_exact

        def get_type_class(self):
            return CommonMsgInfo

        # src : MsgAddressInt
        src: "CellSlice" = None
        # dest : MsgAddressExt
        dest: "CellSlice" = None
        # created_lt : uint64
        created_lt: "int" = None
        # created_at : uint32
        created_at: "int" = None

        def __init__(self, src: "CellSlice" = None, dest: "CellSlice" = None, created_lt: "int" = None, created_at: "int" = None):
            super().__init__()
            self.field_names = []
            self.src = src    
            self.field_names.append("src")
            self.dest = dest    
            self.field_names.append("dest")
            self.created_lt = created_lt    
            self.field_names.append("created_lt")
            self.created_at = created_at    
            self.field_names.append("created_at")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'

                self.src = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.dest = TLBComplex.constants["t_MsgAddressExt"].fetch(cs) 
                self.created_lt = cs.load_uint(64)
                self.created_at = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CommonMsgInfo")


# class for type `CommonMsgInfoRelaxed`
class CommonMsgInfoRelaxed(TLBComplex):
    class Tag(Enum):
        int_msg_info = 0
        ext_out_msg_info = 1

    cons_len = [1, 2]
    cons_tag = [0, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CommonMsgInfoRelaxed.Tag.int_msg_info: CommonMsgInfoRelaxed.Record_int_msg_info, CommonMsgInfoRelaxed.Tag.ext_out_msg_info: CommonMsgInfoRelaxed.Record_ext_out_msg_info}

    def get_tag(self, cs: CellSlice) -> Optional["CommonMsgInfoRelaxed.Tag"]:
        return CommonMsgInfoRelaxed.Tag(int(cs.preload_uint(1)))


    class Record_int_msg_info(RecordBase):
        def get_tag_enum(self):
            return CommonMsgInfoRelaxed.Tag.int_msg_info

        def get_tag(self):
            return CommonMsgInfoRelaxed.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CommonMsgInfoRelaxed.cons_len_exact[self.get_tag_enum().value] if isinstance(CommonMsgInfoRelaxed.cons_len_exact, list) else CommonMsgInfoRelaxed.cons_len_exact

        def get_type_class(self):
            return CommonMsgInfoRelaxed

        # ihr_disabled : Bool
        ihr_disabled: "bool" = None
        # bounce : Bool
        bounce: "bool" = None
        # bounced : Bool
        bounced: "bool" = None
        # src : MsgAddress
        src: "CellSlice" = None
        # dest : MsgAddressInt
        dest: "CellSlice" = None
        # value : CurrencyCollection
        value: "CellSlice" = None
        # ihr_fee : Grams
        ihr_fee: "CellSlice" = None
        # fwd_fee : Grams
        fwd_fee: "CellSlice" = None
        # created_lt : uint64
        created_lt: "int" = None
        # created_at : uint32
        created_at: "int" = None

        def __init__(self, ihr_disabled: "bool" = None, bounce: "bool" = None, bounced: "bool" = None, src: "CellSlice" = None, dest: "CellSlice" = None, value: "CellSlice" = None, ihr_fee: "CellSlice" = None, fwd_fee: "CellSlice" = None, created_lt: "int" = None, created_at: "int" = None):
            super().__init__()
            self.field_names = []
            self.ihr_disabled = ihr_disabled    
            self.field_names.append("ihr_disabled")
            self.bounce = bounce    
            self.field_names.append("bounce")
            self.bounced = bounced    
            self.field_names.append("bounced")
            self.src = src    
            self.field_names.append("src")
            self.dest = dest    
            self.field_names.append("dest")
            self.value = value    
            self.field_names.append("value")
            self.ihr_fee = ihr_fee    
            self.field_names.append("ihr_fee")
            self.fwd_fee = fwd_fee    
            self.field_names.append("fwd_fee")
            self.created_lt = created_lt    
            self.field_names.append("created_lt")
            self.created_at = created_at    
            self.field_names.append("created_at")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.ihr_disabled = cs.load_bool()
                self.bounce = cs.load_bool()
                self.bounced = cs.load_bool()
                self.src = TLBComplex.constants["t_MsgAddress"].fetch(cs) 
                self.dest = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.value = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.ihr_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.fwd_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.created_lt = cs.load_uint(64)
                self.created_at = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_ext_out_msg_info(RecordBase):
        def get_tag_enum(self):
            return CommonMsgInfoRelaxed.Tag.ext_out_msg_info

        def get_tag(self):
            return CommonMsgInfoRelaxed.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CommonMsgInfoRelaxed.cons_len_exact[self.get_tag_enum().value] if isinstance(CommonMsgInfoRelaxed.cons_len_exact, list) else CommonMsgInfoRelaxed.cons_len_exact

        def get_type_class(self):
            return CommonMsgInfoRelaxed

        # src : MsgAddress
        src: "CellSlice" = None
        # dest : MsgAddressExt
        dest: "CellSlice" = None
        # created_lt : uint64
        created_lt: "int" = None
        # created_at : uint32
        created_at: "int" = None

        def __init__(self, src: "CellSlice" = None, dest: "CellSlice" = None, created_lt: "int" = None, created_at: "int" = None):
            super().__init__()
            self.field_names = []
            self.src = src    
            self.field_names.append("src")
            self.dest = dest    
            self.field_names.append("dest")
            self.created_lt = created_lt    
            self.field_names.append("created_lt")
            self.created_at = created_at    
            self.field_names.append("created_at")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'

                self.src = TLBComplex.constants["t_MsgAddress"].fetch(cs) 
                self.dest = TLBComplex.constants["t_MsgAddressExt"].fetch(cs) 
                self.created_lt = cs.load_uint(64)
                self.created_at = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CommonMsgInfoRelaxed")


# class for type `TickTock`
class TickTock(TLBComplex):
    class Tag(Enum):
        tick_tock = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TickTock.Tag.tick_tock: TickTock.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TickTock.Tag"]:
        return TickTock.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TickTock.Tag.tick_tock

        def get_tag(self):
            return TickTock.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TickTock.cons_len_exact[self.get_tag_enum().value] if isinstance(TickTock.cons_len_exact, list) else TickTock.cons_len_exact

        def get_type_class(self):
            return TickTock

        # tick : Bool
        tick: "bool" = None
        # tock : Bool
        tock: "bool" = None

        def __init__(self, tick: "bool" = None, tock: "bool" = None):
            super().__init__()
            self.field_names = []
            self.tick = tick    
            self.field_names.append("tick")
            self.tock = tock    
            self.field_names.append("tock")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.tick = cs.load_bool()
                self.tock = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TickTock")


# class for type `StateInit`
class StateInit(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {StateInit.Tag.cons1: StateInit.Record}

    def get_tag(self, cs: CellSlice) -> Optional["StateInit.Tag"]:
        return StateInit.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return StateInit.Tag.cons1

        def get_tag(self):
            return StateInit.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return StateInit.cons_len_exact[self.get_tag_enum().value] if isinstance(StateInit.cons_len_exact, list) else StateInit.cons_len_exact

        def get_type_class(self):
            return StateInit

        # split_depth : Maybe (## 5)
        split_depth: "CellSlice" = None
        # special : Maybe TickTock
        special: "CellSlice" = None
        # code : Maybe ^Cell
        code: "CellSlice" = None
        # data : Maybe ^Cell
        data: "CellSlice" = None
        # library : Maybe ^Cell
        library: "CellSlice" = None

        def __init__(self, split_depth: "CellSlice" = None, special: "CellSlice" = None, code: "CellSlice" = None, data: "CellSlice" = None, library: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.split_depth = split_depth    
            self.field_names.append("split_depth")
            self.special = special    
            self.field_names.append("special")
            self.code = code    
            self.field_names.append("code")
            self.data = data    
            self.field_names.append("data")
            self.library = library    
            self.field_names.append("library")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.split_depth = TLBComplex.constants["t_Maybe_natwidth_5"].fetch(cs) 
                self.special = TLBComplex.constants["t_Maybe_TickTock"].fetch(cs) 
                self.code = TLBComplex.constants["t_Maybe_Ref_Cell"].fetch(cs) 
                self.data = TLBComplex.constants["t_Maybe_Ref_Cell"].fetch(cs) 
                self.library = TLBComplex.constants["t_Maybe_Ref_Cell"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("StateInit")


# class for type `StateInitWithLibs`
class StateInitWithLibs(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {StateInitWithLibs.Tag.cons1: StateInitWithLibs.Record}

    def get_tag(self, cs: CellSlice) -> Optional["StateInitWithLibs.Tag"]:
        return StateInitWithLibs.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return StateInitWithLibs.Tag.cons1

        def get_tag(self):
            return StateInitWithLibs.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return StateInitWithLibs.cons_len_exact[self.get_tag_enum().value] if isinstance(StateInitWithLibs.cons_len_exact, list) else StateInitWithLibs.cons_len_exact

        def get_type_class(self):
            return StateInitWithLibs

        # split_depth : Maybe (## 5)
        split_depth: "CellSlice" = None
        # special : Maybe TickTock
        special: "CellSlice" = None
        # code : Maybe ^Cell
        code: "CellSlice" = None
        # data : Maybe ^Cell
        data: "CellSlice" = None
        # library : HashmapE 256 SimpleLib
        library: "CellSlice" = None

        def __init__(self, split_depth: "CellSlice" = None, special: "CellSlice" = None, code: "CellSlice" = None, data: "CellSlice" = None, library: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.split_depth = split_depth    
            self.field_names.append("split_depth")
            self.special = special    
            self.field_names.append("special")
            self.code = code    
            self.field_names.append("code")
            self.data = data    
            self.field_names.append("data")
            self.library = library    
            self.field_names.append("library")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.split_depth = TLBComplex.constants["t_Maybe_natwidth_5"].fetch(cs) 
                self.special = TLBComplex.constants["t_Maybe_TickTock"].fetch(cs) 
                self.code = TLBComplex.constants["t_Maybe_Ref_Cell"].fetch(cs) 
                self.data = TLBComplex.constants["t_Maybe_Ref_Cell"].fetch(cs) 
                self.library = TLBComplex.constants["t_HashmapE_256_SimpleLib"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("StateInitWithLibs")


# class for type `SimpleLib`
class SimpleLib(TLBComplex):
    class Tag(Enum):
        simple_lib = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SimpleLib.Tag.simple_lib: SimpleLib.Record}

    def get_tag(self, cs: CellSlice) -> Optional["SimpleLib.Tag"]:
        return SimpleLib.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return SimpleLib.Tag.simple_lib

        def get_tag(self):
            return SimpleLib.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SimpleLib.cons_len_exact[self.get_tag_enum().value] if isinstance(SimpleLib.cons_len_exact, list) else SimpleLib.cons_len_exact

        def get_type_class(self):
            return SimpleLib

        # public : Bool
        public: "bool" = None
        # root : ^Cell
        root: "Cell" = None

        def __init__(self, public: "bool" = None, root: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.public = public    
            self.field_names.append("public")
            self.root = root    
            self.field_names.append("root")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.public = cs.load_bool()
                self.root = cs.load_ref()
                
                if rec_unpack:
                    self.root = TLBComplex.constants["t_RefCell"].fetch(self.root, True, strict) # at 1
                    assert self.root is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SimpleLib")


# class for type `Message`
class Message(TLBComplex):
    class Tag(Enum):
        message = 0

    cons_len_exact = 0
    cons_tag = [0]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {Message.Tag.message: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["Message.Tag"]:
        return Message.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Message.Tag.message

        def get_tag(self):
            return Message.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Message.cons_len_exact[self.get_tag_enum().value] if isinstance(Message.cons_len_exact, list) else Message.cons_len_exact

        def get_type_class(self):
            return Message

        # info : CommonMsgInfo
        info: "CellSlice" = None
        # init : Maybe (Either StateInit ^StateInit)
        init: "CellSlice" = None
        # body : Either X ^X
        body: "CellSlice" = None

        def __init__(self, info: "CellSlice" = None, init: "CellSlice" = None, body: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.info = info    
            self.field_names.append("info")
            self.init = init    
            self.field_names.append("init")
            self.body = body    
            self.field_names.append("body")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.info = TLBComplex.constants["t_CommonMsgInfo"].fetch(cs) 
                self.init = TLBComplex.constants["t_Maybe_Either_StateInit_Ref_StateInit"].fetch(cs) 
                self.body = Either(self.X_, RefT(self.X_)).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Message")


# class for type `MessageRelaxed`
class MessageRelaxed(TLBComplex):
    class Tag(Enum):
        message = 0

    cons_len_exact = 0
    cons_tag = [0]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {MessageRelaxed.Tag.message: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["MessageRelaxed.Tag"]:
        return MessageRelaxed.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MessageRelaxed.Tag.message

        def get_tag(self):
            return MessageRelaxed.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MessageRelaxed.cons_len_exact[self.get_tag_enum().value] if isinstance(MessageRelaxed.cons_len_exact, list) else MessageRelaxed.cons_len_exact

        def get_type_class(self):
            return MessageRelaxed

        # info : CommonMsgInfoRelaxed
        info: "CellSlice" = None
        # init : Maybe (Either StateInit ^StateInit)
        init: "CellSlice" = None
        # body : Either X ^X
        body: "CellSlice" = None

        def __init__(self, info: "CellSlice" = None, init: "CellSlice" = None, body: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.info = info    
            self.field_names.append("info")
            self.init = init    
            self.field_names.append("init")
            self.body = body    
            self.field_names.append("body")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.info = TLBComplex.constants["t_CommonMsgInfoRelaxed"].fetch(cs) 
                self.init = TLBComplex.constants["t_Maybe_Either_StateInit_Ref_StateInit"].fetch(cs) 
                self.body = Either(self.X_, RefT(self.X_)).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MessageRelaxed")


# class for type `MessageAny`
class MessageAny(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MessageAny.Tag.cons1: MessageAny.Record}

    def get_tag(self, cs: CellSlice) -> Optional["MessageAny.Tag"]:
        return MessageAny.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MessageAny.Tag.cons1

        def get_tag(self):
            return MessageAny.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MessageAny.cons_len_exact[self.get_tag_enum().value] if isinstance(MessageAny.cons_len_exact, list) else MessageAny.cons_len_exact

        def get_type_class(self):
            return MessageAny

        # Message Any
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_Message_Any"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MessageAny")


# class for type `IntermediateAddress`
class IntermediateAddress(TLBComplex):
    class Tag(Enum):
        interm_addr_regular = 0
        interm_addr_simple = 1
        interm_addr_ext = 2

    cons_len = [1, 2, 2]
    cons_tag = [0, 2, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {IntermediateAddress.Tag.interm_addr_regular: IntermediateAddress.Record_interm_addr_regular, IntermediateAddress.Tag.interm_addr_simple: IntermediateAddress.Record_interm_addr_simple, IntermediateAddress.Tag.interm_addr_ext: IntermediateAddress.Record_interm_addr_ext}

    def get_tag(self, cs: CellSlice) -> Optional["IntermediateAddress.Tag"]:
        return IntermediateAddress.Tag(int(cs.bselect(2, 13)))


    class Record_interm_addr_regular(RecordBase):
        def get_tag_enum(self):
            return IntermediateAddress.Tag.interm_addr_regular

        def get_tag(self):
            return IntermediateAddress.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return IntermediateAddress.cons_len_exact[self.get_tag_enum().value] if isinstance(IntermediateAddress.cons_len_exact, list) else IntermediateAddress.cons_len_exact

        def get_type_class(self):
            return IntermediateAddress

        # use_dest_bits : #<= 96
        use_dest_bits: "int" = None

        def __init__(self, use_dest_bits: "int" = None):
            super().__init__()
            self.field_names = []
            self.use_dest_bits = use_dest_bits    
            self.field_names.append("use_dest_bits")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.use_dest_bits = cs.load_uint_leq(96)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_interm_addr_simple(RecordBase):
        def get_tag_enum(self):
            return IntermediateAddress.Tag.interm_addr_simple

        def get_tag(self):
            return IntermediateAddress.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return IntermediateAddress.cons_len_exact[self.get_tag_enum().value] if isinstance(IntermediateAddress.cons_len_exact, list) else IntermediateAddress.cons_len_exact

        def get_type_class(self):
            return IntermediateAddress

        # workchain_id : int8
        workchain_id: "int" = None
        # addr_pfx : uint64
        addr_pfx: "int" = None

        def __init__(self, workchain_id: "int" = None, addr_pfx: "int" = None):
            super().__init__()
            self.field_names = []
            self.workchain_id = workchain_id    
            self.field_names.append("workchain_id")
            self.addr_pfx = addr_pfx    
            self.field_names.append("addr_pfx")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'

                self.workchain_id = cs.load_int(8)
                self.addr_pfx = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_interm_addr_ext(RecordBase):
        def get_tag_enum(self):
            return IntermediateAddress.Tag.interm_addr_ext

        def get_tag(self):
            return IntermediateAddress.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return IntermediateAddress.cons_len_exact[self.get_tag_enum().value] if isinstance(IntermediateAddress.cons_len_exact, list) else IntermediateAddress.cons_len_exact

        def get_type_class(self):
            return IntermediateAddress

        # workchain_id : int32
        workchain_id: "int" = None
        # addr_pfx : uint64
        addr_pfx: "int" = None

        def __init__(self, workchain_id: "int" = None, addr_pfx: "int" = None):
            super().__init__()
            self.field_names = []
            self.workchain_id = workchain_id    
            self.field_names.append("workchain_id")
            self.addr_pfx = addr_pfx    
            self.field_names.append("addr_pfx")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'

                self.workchain_id = cs.load_int(32)
                self.addr_pfx = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("IntermediateAddress")


# class for type `MsgEnvelope`
class MsgEnvelope(TLBComplex):
    class Tag(Enum):
        msg_envelope = 0

    cons_len_exact = 4
    cons_tag = [4]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MsgEnvelope.Tag.msg_envelope: MsgEnvelope.Record}

    def get_tag(self, cs: CellSlice) -> Optional["MsgEnvelope.Tag"]:
        return MsgEnvelope.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MsgEnvelope.Tag.msg_envelope

        def get_tag(self):
            return MsgEnvelope.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgEnvelope.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgEnvelope.cons_len_exact, list) else MsgEnvelope.cons_len_exact

        def get_type_class(self):
            return MsgEnvelope

        # cur_addr : IntermediateAddress
        cur_addr: "CellSlice" = None
        # next_addr : IntermediateAddress
        next_addr: "CellSlice" = None
        # fwd_fee_remaining : Grams
        fwd_fee_remaining: "CellSlice" = None
        # msg : ^(Message Any)
        msg: "Cell" = None

        def __init__(self, cur_addr: "CellSlice" = None, next_addr: "CellSlice" = None, fwd_fee_remaining: "CellSlice" = None, msg: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.cur_addr = cur_addr    
            self.field_names.append("cur_addr")
            self.next_addr = next_addr    
            self.field_names.append("next_addr")
            self.fwd_fee_remaining = fwd_fee_remaining    
            self.field_names.append("fwd_fee_remaining")
            self.msg = msg    
            self.field_names.append("msg")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 4, 'Cons tag check failed'

                self.cur_addr = TLBComplex.constants["t_IntermediateAddress"].fetch(cs) 
                self.next_addr = TLBComplex.constants["t_IntermediateAddress"].fetch(cs) 
                self.fwd_fee_remaining = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.msg = cs.load_ref()
                
                if rec_unpack:
                    self.msg = TLBComplex.constants["t_Ref_Message_Any"].fetch(self.msg, True, strict) # at 1
                    assert self.msg is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MsgEnvelope")


# class for type `InMsg`
class InMsg(TLBComplex):
    class Tag(Enum):
        msg_import_ext = 0
        msg_import_ihr = 1
        msg_import_imm = 2
        msg_import_fin = 3
        msg_import_tr = 4
        msg_discard_fin = 5
        msg_discard_tr = 6

    cons_len_exact = 3
    cons_tag = [0, 2, 3, 4, 5, 6, 7]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {InMsg.Tag.msg_import_ext: InMsg.Record_msg_import_ext, InMsg.Tag.msg_import_ihr: InMsg.Record_msg_import_ihr, InMsg.Tag.msg_import_imm: InMsg.Record_msg_import_imm, InMsg.Tag.msg_import_fin: InMsg.Record_msg_import_fin, InMsg.Tag.msg_import_tr: InMsg.Record_msg_import_tr, InMsg.Tag.msg_discard_fin: InMsg.Record_msg_discard_fin, InMsg.Tag.msg_discard_tr: InMsg.Record_msg_discard_tr}

    def get_tag(self, cs: CellSlice) -> Optional["InMsg.Tag"]:
        return InMsg.Tag(int(cs.bselect(3, 0xfd)))


    class Record_msg_import_ext(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_import_ext

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # msg : ^(Message Any)
        msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None

        def __init__(self, msg: "Cell" = None, transaction: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.msg = msg    
            self.field_names.append("msg")
            self.transaction = transaction    
            self.field_names.append("transaction")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 0, 'Cons tag check failed'

                self.msg = cs.load_ref()
                
                if rec_unpack:
                    self.msg = TLBComplex.constants["t_Ref_Message_Any"].fetch(self.msg, True, strict) # at 1
                    assert self.msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_import_ihr(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_import_ihr

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # msg : ^(Message Any)
        msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None
        # ihr_fee : Grams
        ihr_fee: "CellSlice" = None
        # proof_created : ^Cell
        proof_created: "Cell" = None

        def __init__(self, msg: "Cell" = None, transaction: "Cell" = None, ihr_fee: "CellSlice" = None, proof_created: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.msg = msg    
            self.field_names.append("msg")
            self.transaction = transaction    
            self.field_names.append("transaction")
            self.ihr_fee = ihr_fee    
            self.field_names.append("ihr_fee")
            self.proof_created = proof_created    
            self.field_names.append("proof_created")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 2, 'Cons tag check failed'

                self.msg = cs.load_ref()
                
                if rec_unpack:
                    self.msg = TLBComplex.constants["t_Ref_Message_Any"].fetch(self.msg, True, strict) # at 1
                    assert self.msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None

                self.ihr_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.proof_created = cs.load_ref()
                
                if rec_unpack:
                    self.proof_created = TLBComplex.constants["t_RefCell"].fetch(self.proof_created, True, strict) # at 1
                    assert self.proof_created is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_import_imm(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_import_imm

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # in_msg : ^MsgEnvelope
        in_msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None
        # fwd_fee : Grams
        fwd_fee: "CellSlice" = None

        def __init__(self, in_msg: "Cell" = None, transaction: "Cell" = None, fwd_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.in_msg = in_msg    
            self.field_names.append("in_msg")
            self.transaction = transaction    
            self.field_names.append("transaction")
            self.fwd_fee = fwd_fee    
            self.field_names.append("fwd_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 3, 'Cons tag check failed'

                self.in_msg = cs.load_ref()
                
                if rec_unpack:
                    self.in_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.in_msg, True, strict) # at 1
                    assert self.in_msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None

                self.fwd_fee = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_import_fin(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_import_fin

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # in_msg : ^MsgEnvelope
        in_msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None
        # fwd_fee : Grams
        fwd_fee: "CellSlice" = None

        def __init__(self, in_msg: "Cell" = None, transaction: "Cell" = None, fwd_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.in_msg = in_msg    
            self.field_names.append("in_msg")
            self.transaction = transaction    
            self.field_names.append("transaction")
            self.fwd_fee = fwd_fee    
            self.field_names.append("fwd_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 4, 'Cons tag check failed'

                self.in_msg = cs.load_ref()
                
                if rec_unpack:
                    self.in_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.in_msg, True, strict) # at 1
                    assert self.in_msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None

                self.fwd_fee = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_import_tr(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_import_tr

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # in_msg : ^MsgEnvelope
        in_msg: "Cell" = None
        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # transit_fee : Grams
        transit_fee: "CellSlice" = None

        def __init__(self, in_msg: "Cell" = None, out_msg: "Cell" = None, transit_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.in_msg = in_msg    
            self.field_names.append("in_msg")
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.transit_fee = transit_fee    
            self.field_names.append("transit_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 5, 'Cons tag check failed'

                self.in_msg = cs.load_ref()
                
                if rec_unpack:
                    self.in_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.in_msg, True, strict) # at 1
                    assert self.in_msg is not None

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.transit_fee = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_discard_fin(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_discard_fin

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # in_msg : ^MsgEnvelope
        in_msg: "Cell" = None
        # transaction_id : uint64
        transaction_id: "int" = None
        # fwd_fee : Grams
        fwd_fee: "CellSlice" = None

        def __init__(self, in_msg: "Cell" = None, transaction_id: "int" = None, fwd_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.in_msg = in_msg    
            self.field_names.append("in_msg")
            self.transaction_id = transaction_id    
            self.field_names.append("transaction_id")
            self.fwd_fee = fwd_fee    
            self.field_names.append("fwd_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 6, 'Cons tag check failed'

                self.in_msg = cs.load_ref()
                
                if rec_unpack:
                    self.in_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.in_msg, True, strict) # at 1
                    assert self.in_msg is not None

                self.transaction_id = cs.load_uint(64)
                self.fwd_fee = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_discard_tr(RecordBase):
        def get_tag_enum(self):
            return InMsg.Tag.msg_discard_tr

        def get_tag(self):
            return InMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsg.cons_len_exact, list) else InMsg.cons_len_exact

        def get_type_class(self):
            return InMsg

        # in_msg : ^MsgEnvelope
        in_msg: "Cell" = None
        # transaction_id : uint64
        transaction_id: "int" = None
        # fwd_fee : Grams
        fwd_fee: "CellSlice" = None
        # proof_delivered : ^Cell
        proof_delivered: "Cell" = None

        def __init__(self, in_msg: "Cell" = None, transaction_id: "int" = None, fwd_fee: "CellSlice" = None, proof_delivered: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.in_msg = in_msg    
            self.field_names.append("in_msg")
            self.transaction_id = transaction_id    
            self.field_names.append("transaction_id")
            self.fwd_fee = fwd_fee    
            self.field_names.append("fwd_fee")
            self.proof_delivered = proof_delivered    
            self.field_names.append("proof_delivered")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 7, 'Cons tag check failed'

                self.in_msg = cs.load_ref()
                
                if rec_unpack:
                    self.in_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.in_msg, True, strict) # at 1
                    assert self.in_msg is not None

                self.transaction_id = cs.load_uint(64)
                self.fwd_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.proof_delivered = cs.load_ref()
                
                if rec_unpack:
                    self.proof_delivered = TLBComplex.constants["t_RefCell"].fetch(self.proof_delivered, True, strict) # at 1
                    assert self.proof_delivered is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("InMsg")


# class for type `ImportFees`
class ImportFees(TLBComplex):
    class Tag(Enum):
        import_fees = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ImportFees.Tag.import_fees: ImportFees.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ImportFees.Tag"]:
        return ImportFees.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ImportFees.Tag.import_fees

        def get_tag(self):
            return ImportFees.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ImportFees.cons_len_exact[self.get_tag_enum().value] if isinstance(ImportFees.cons_len_exact, list) else ImportFees.cons_len_exact

        def get_type_class(self):
            return ImportFees

        # fees_collected : Grams
        fees_collected: "CellSlice" = None
        # value_imported : CurrencyCollection
        value_imported: "CellSlice" = None

        def __init__(self, fees_collected: "CellSlice" = None, value_imported: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.fees_collected = fees_collected    
            self.field_names.append("fees_collected")
            self.value_imported = value_imported    
            self.field_names.append("value_imported")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.fees_collected = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.value_imported = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ImportFees")


# class for type `InMsgDescr`
class InMsgDescr(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {InMsgDescr.Tag.cons1: InMsgDescr.Record}

    def get_tag(self, cs: CellSlice) -> Optional["InMsgDescr.Tag"]:
        return InMsgDescr.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return InMsgDescr.Tag.cons1

        def get_tag(self):
            return InMsgDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return InMsgDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(InMsgDescr.cons_len_exact, list) else InMsgDescr.cons_len_exact

        def get_type_class(self):
            return InMsgDescr

        # HashmapAugE 256 InMsg ImportFees
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_256_InMsg_ImportFees"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("InMsgDescr")


# class for type `OutMsg`
class OutMsg(TLBComplex):
    class Tag(Enum):
        msg_export_ext = 0
        msg_export_new = 1
        msg_export_imm = 2
        msg_export_tr = 3
        msg_export_deq_imm = 4
        msg_export_deq = 5
        msg_export_deq_short = 6
        msg_export_tr_req = 7

    cons_len = [3, 3, 3, 3, 3, 4, 4, 3]
    cons_tag = [0, 1, 2, 3, 4, 12, 13, 7]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OutMsg.Tag.msg_export_ext: OutMsg.Record_msg_export_ext, OutMsg.Tag.msg_export_imm: OutMsg.Record_msg_export_imm, OutMsg.Tag.msg_export_new: OutMsg.Record_msg_export_new, OutMsg.Tag.msg_export_tr: OutMsg.Record_msg_export_tr, OutMsg.Tag.msg_export_deq: OutMsg.Record_msg_export_deq, OutMsg.Tag.msg_export_deq_short: OutMsg.Record_msg_export_deq_short, OutMsg.Tag.msg_export_tr_req: OutMsg.Record_msg_export_tr_req, OutMsg.Tag.msg_export_deq_imm: OutMsg.Record_msg_export_deq_imm}

    def get_tag(self, cs: CellSlice) -> Optional["OutMsg.Tag"]:
        return OutMsg.Tag(int(cs.bselect_ext(4, 0x7155)))


    class Record_msg_export_ext(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_ext

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # msg : ^(Message Any)
        msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None

        def __init__(self, msg: "Cell" = None, transaction: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.msg = msg    
            self.field_names.append("msg")
            self.transaction = transaction    
            self.field_names.append("transaction")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 0, 'Cons tag check failed'

                self.msg = cs.load_ref()
                
                if rec_unpack:
                    self.msg = TLBComplex.constants["t_Ref_Message_Any"].fetch(self.msg, True, strict) # at 1
                    assert self.msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_imm(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_imm

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None
        # reimport : ^InMsg
        reimport: "Cell" = None

        def __init__(self, out_msg: "Cell" = None, transaction: "Cell" = None, reimport: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.transaction = transaction    
            self.field_names.append("transaction")
            self.reimport = reimport    
            self.field_names.append("reimport")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 2, 'Cons tag check failed'

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None

                self.reimport = cs.load_ref()
                
                if rec_unpack:
                    self.reimport = TLBComplex.constants["t_Ref_InMsg"].fetch(self.reimport, True, strict) # at 1
                    assert self.reimport is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_new(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_new

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # transaction : ^Transaction
        transaction: "Cell" = None

        def __init__(self, out_msg: "Cell" = None, transaction: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.transaction = transaction    
            self.field_names.append("transaction")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 1, 'Cons tag check failed'

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.transaction = cs.load_ref()
                
                if rec_unpack:
                    self.transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.transaction, True, strict) # at 1
                    assert self.transaction is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_tr(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_tr

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # imported : ^InMsg
        imported: "Cell" = None

        def __init__(self, out_msg: "Cell" = None, imported: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.imported = imported    
            self.field_names.append("imported")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 3, 'Cons tag check failed'

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.imported = cs.load_ref()
                
                if rec_unpack:
                    self.imported = TLBComplex.constants["t_Ref_InMsg"].fetch(self.imported, True, strict) # at 1
                    assert self.imported is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_deq(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_deq

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # import_block_lt : uint63
        import_block_lt: "int" = None

        def __init__(self, out_msg: "Cell" = None, import_block_lt: "int" = None):
            super().__init__()
            self.field_names = []
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.import_block_lt = import_block_lt    
            self.field_names.append("import_block_lt")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 12, 'Cons tag check failed'

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.import_block_lt = cs.load_uint(63)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_deq_short(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_deq_short

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # msg_env_hash : bits256
        msg_env_hash: "bitstring.BitArray" = None
        # next_workchain : int32
        next_workchain: "int" = None
        # next_addr_pfx : uint64
        next_addr_pfx: "int" = None
        # import_block_lt : uint64
        import_block_lt: "int" = None

        def __init__(self, msg_env_hash: "bitstring.BitArray" = None, next_workchain: "int" = None, next_addr_pfx: "int" = None, import_block_lt: "int" = None):
            super().__init__()
            self.field_names = []
            self.msg_env_hash = msg_env_hash    
            self.field_names.append("msg_env_hash")
            self.next_workchain = next_workchain    
            self.field_names.append("next_workchain")
            self.next_addr_pfx = next_addr_pfx    
            self.field_names.append("next_addr_pfx")
            self.import_block_lt = import_block_lt    
            self.field_names.append("import_block_lt")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 13, 'Cons tag check failed'

                self.msg_env_hash = cs.load_bitstring(256)
                self.next_workchain = cs.load_int(32)
                self.next_addr_pfx = cs.load_uint(64)
                self.import_block_lt = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_tr_req(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_tr_req

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # imported : ^InMsg
        imported: "Cell" = None

        def __init__(self, out_msg: "Cell" = None, imported: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.imported = imported    
            self.field_names.append("imported")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 7, 'Cons tag check failed'

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.imported = cs.load_ref()
                
                if rec_unpack:
                    self.imported = TLBComplex.constants["t_Ref_InMsg"].fetch(self.imported, True, strict) # at 1
                    assert self.imported is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_msg_export_deq_imm(RecordBase):
        def get_tag_enum(self):
            return OutMsg.Tag.msg_export_deq_imm

        def get_tag(self):
            return OutMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsg.cons_len_exact, list) else OutMsg.cons_len_exact

        def get_type_class(self):
            return OutMsg

        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None
        # reimport : ^InMsg
        reimport: "Cell" = None

        def __init__(self, out_msg: "Cell" = None, reimport: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.out_msg = out_msg    
            self.field_names.append("out_msg")
            self.reimport = reimport    
            self.field_names.append("reimport")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 4, 'Cons tag check failed'

                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None

                self.reimport = cs.load_ref()
                
                if rec_unpack:
                    self.reimport = TLBComplex.constants["t_Ref_InMsg"].fetch(self.reimport, True, strict) # at 1
                    assert self.reimport is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutMsg")


# class for type `EnqueuedMsg`
class EnqueuedMsg(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {EnqueuedMsg.Tag.cons1: EnqueuedMsg.Record}

    def get_tag(self, cs: CellSlice) -> Optional["EnqueuedMsg.Tag"]:
        return EnqueuedMsg.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return EnqueuedMsg.Tag.cons1

        def get_tag(self):
            return EnqueuedMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return EnqueuedMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(EnqueuedMsg.cons_len_exact, list) else EnqueuedMsg.cons_len_exact

        def get_type_class(self):
            return EnqueuedMsg

        # enqueued_lt : uint64
        enqueued_lt: "int" = None
        # out_msg : ^MsgEnvelope
        out_msg: "Cell" = None

        def __init__(self, enqueued_lt: "int" = None, out_msg: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.enqueued_lt = enqueued_lt    
            self.field_names.append("enqueued_lt")
            self.out_msg = out_msg    
            self.field_names.append("out_msg")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.enqueued_lt = cs.load_uint(64)
                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MsgEnvelope"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("EnqueuedMsg")


# class for type `OutMsgDescr`
class OutMsgDescr(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OutMsgDescr.Tag.cons1: OutMsgDescr.Record}

    def get_tag(self, cs: CellSlice) -> Optional["OutMsgDescr.Tag"]:
        return OutMsgDescr.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return OutMsgDescr.Tag.cons1

        def get_tag(self):
            return OutMsgDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsgDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsgDescr.cons_len_exact, list) else OutMsgDescr.cons_len_exact

        def get_type_class(self):
            return OutMsgDescr

        # HashmapAugE 256 OutMsg CurrencyCollection
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_256_OutMsg_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutMsgDescr")


# class for type `OutMsgQueue`
class OutMsgQueue(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OutMsgQueue.Tag.cons1: OutMsgQueue.Record}

    def get_tag(self, cs: CellSlice) -> Optional["OutMsgQueue.Tag"]:
        return OutMsgQueue.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return OutMsgQueue.Tag.cons1

        def get_tag(self):
            return OutMsgQueue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsgQueue.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsgQueue.cons_len_exact, list) else OutMsgQueue.cons_len_exact

        def get_type_class(self):
            return OutMsgQueue

        # HashmapAugE 352 EnqueuedMsg uint64
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_352_EnqueuedMsg_uint64"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutMsgQueue")


# class for type `ProcessedUpto`
class ProcessedUpto(TLBComplex):
    class Tag(Enum):
        processed_upto = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ProcessedUpto.Tag.processed_upto: ProcessedUpto.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ProcessedUpto.Tag"]:
        return ProcessedUpto.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ProcessedUpto.Tag.processed_upto

        def get_tag(self):
            return ProcessedUpto.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProcessedUpto.cons_len_exact[self.get_tag_enum().value] if isinstance(ProcessedUpto.cons_len_exact, list) else ProcessedUpto.cons_len_exact

        def get_type_class(self):
            return ProcessedUpto

        # last_msg_lt : uint64
        last_msg_lt: "int" = None
        # last_msg_hash : bits256
        last_msg_hash: "bitstring.BitArray" = None

        def __init__(self, last_msg_lt: "int" = None, last_msg_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.last_msg_lt = last_msg_lt    
            self.field_names.append("last_msg_lt")
            self.last_msg_hash = last_msg_hash    
            self.field_names.append("last_msg_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.last_msg_lt = cs.load_uint(64)
                self.last_msg_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ProcessedUpto")


# class for type `ProcessedInfo`
class ProcessedInfo(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ProcessedInfo.Tag.cons1: ProcessedInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ProcessedInfo.Tag"]:
        return ProcessedInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ProcessedInfo.Tag.cons1

        def get_tag(self):
            return ProcessedInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProcessedInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(ProcessedInfo.cons_len_exact, list) else ProcessedInfo.cons_len_exact

        def get_type_class(self):
            return ProcessedInfo

        # HashmapE 96 ProcessedUpto
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapE_96_ProcessedUpto"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ProcessedInfo")


# class for type `IhrPendingSince`
class IhrPendingSince(TLBComplex):
    class Tag(Enum):
        ihr_pending = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {IhrPendingSince.Tag.ihr_pending: IhrPendingSince.Record}

    def get_tag(self, cs: CellSlice) -> Optional["IhrPendingSince.Tag"]:
        return IhrPendingSince.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return IhrPendingSince.Tag.ihr_pending

        def get_tag(self):
            return IhrPendingSince.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return IhrPendingSince.cons_len_exact[self.get_tag_enum().value] if isinstance(IhrPendingSince.cons_len_exact, list) else IhrPendingSince.cons_len_exact

        def get_type_class(self):
            return IhrPendingSince

        # import_lt : uint64
        import_lt: "int" = None

        def __init__(self, import_lt: "int" = None):
            super().__init__()
            self.field_names = []
            self.import_lt = import_lt    
            self.field_names.append("import_lt")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.import_lt = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("IhrPendingSince")


# class for type `IhrPendingInfo`
class IhrPendingInfo(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {IhrPendingInfo.Tag.cons1: IhrPendingInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["IhrPendingInfo.Tag"]:
        return IhrPendingInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return IhrPendingInfo.Tag.cons1

        def get_tag(self):
            return IhrPendingInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return IhrPendingInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(IhrPendingInfo.cons_len_exact, list) else IhrPendingInfo.cons_len_exact

        def get_type_class(self):
            return IhrPendingInfo

        # HashmapE 320 IhrPendingSince
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapE_320_IhrPendingSince"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("IhrPendingInfo")


# class for type `OutMsgQueueInfo`
class OutMsgQueueInfo(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OutMsgQueueInfo.Tag.cons1: OutMsgQueueInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["OutMsgQueueInfo.Tag"]:
        return OutMsgQueueInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return OutMsgQueueInfo.Tag.cons1

        def get_tag(self):
            return OutMsgQueueInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutMsgQueueInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(OutMsgQueueInfo.cons_len_exact, list) else OutMsgQueueInfo.cons_len_exact

        def get_type_class(self):
            return OutMsgQueueInfo

        # out_queue : OutMsgQueue
        out_queue: "CellSlice" = None
        # proc_info : ProcessedInfo
        proc_info: "CellSlice" = None
        # ihr_pending : IhrPendingInfo
        ihr_pending: "CellSlice" = None

        def __init__(self, out_queue: "CellSlice" = None, proc_info: "CellSlice" = None, ihr_pending: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.out_queue = out_queue    
            self.field_names.append("out_queue")
            self.proc_info = proc_info    
            self.field_names.append("proc_info")
            self.ihr_pending = ihr_pending    
            self.field_names.append("ihr_pending")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.out_queue = TLBComplex.constants["t_OutMsgQueue"].fetch(cs) 
                self.proc_info = TLBComplex.constants["t_ProcessedInfo"].fetch(cs) 
                self.ihr_pending = TLBComplex.constants["t_IhrPendingInfo"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutMsgQueueInfo")


# class for type `StorageUsed`
class StorageUsed(TLBComplex):
    class Tag(Enum):
        storage_used = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {StorageUsed.Tag.storage_used: StorageUsed.Record}

    def get_tag(self, cs: CellSlice) -> Optional["StorageUsed.Tag"]:
        return StorageUsed.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return StorageUsed.Tag.storage_used

        def get_tag(self):
            return StorageUsed.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return StorageUsed.cons_len_exact[self.get_tag_enum().value] if isinstance(StorageUsed.cons_len_exact, list) else StorageUsed.cons_len_exact

        def get_type_class(self):
            return StorageUsed

        # cells : VarUInteger 7
        cells: "CellSlice" = None
        # bits : VarUInteger 7
        bits: "CellSlice" = None
        # public_cells : VarUInteger 7
        public_cells: "CellSlice" = None

        def __init__(self, cells: "CellSlice" = None, bits: "CellSlice" = None, public_cells: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cells = cells    
            self.field_names.append("cells")
            self.bits = bits    
            self.field_names.append("bits")
            self.public_cells = public_cells    
            self.field_names.append("public_cells")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cells = TLBComplex.constants["t_VarUInteger_7"].fetch(cs) 
                self.bits = TLBComplex.constants["t_VarUInteger_7"].fetch(cs) 
                self.public_cells = TLBComplex.constants["t_VarUInteger_7"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("StorageUsed")


# class for type `StorageUsedShort`
class StorageUsedShort(TLBComplex):
    class Tag(Enum):
        storage_used_short = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {StorageUsedShort.Tag.storage_used_short: StorageUsedShort.Record}

    def get_tag(self, cs: CellSlice) -> Optional["StorageUsedShort.Tag"]:
        return StorageUsedShort.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return StorageUsedShort.Tag.storage_used_short

        def get_tag(self):
            return StorageUsedShort.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return StorageUsedShort.cons_len_exact[self.get_tag_enum().value] if isinstance(StorageUsedShort.cons_len_exact, list) else StorageUsedShort.cons_len_exact

        def get_type_class(self):
            return StorageUsedShort

        # cells : VarUInteger 7
        cells: "CellSlice" = None
        # bits : VarUInteger 7
        bits: "CellSlice" = None

        def __init__(self, cells: "CellSlice" = None, bits: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cells = cells    
            self.field_names.append("cells")
            self.bits = bits    
            self.field_names.append("bits")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cells = TLBComplex.constants["t_VarUInteger_7"].fetch(cs) 
                self.bits = TLBComplex.constants["t_VarUInteger_7"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("StorageUsedShort")


# class for type `StorageInfo`
class StorageInfo(TLBComplex):
    class Tag(Enum):
        storage_info = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {StorageInfo.Tag.storage_info: StorageInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["StorageInfo.Tag"]:
        return StorageInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return StorageInfo.Tag.storage_info

        def get_tag(self):
            return StorageInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return StorageInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(StorageInfo.cons_len_exact, list) else StorageInfo.cons_len_exact

        def get_type_class(self):
            return StorageInfo

        # used : StorageUsed
        used: "CellSlice" = None
        # last_paid : uint32
        last_paid: "int" = None
        # due_payment : Maybe Grams
        due_payment: "CellSlice" = None

        def __init__(self, used: "CellSlice" = None, last_paid: "int" = None, due_payment: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.used = used    
            self.field_names.append("used")
            self.last_paid = last_paid    
            self.field_names.append("last_paid")
            self.due_payment = due_payment    
            self.field_names.append("due_payment")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.used = TLBComplex.constants["t_StorageUsed"].fetch(cs) 
                self.last_paid = cs.load_uint(32)
                self.due_payment = TLBComplex.constants["t_Maybe_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("StorageInfo")


# class for type `Account`
class Account(TLBComplex):
    class Tag(Enum):
        account_none = 0
        account = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Account.Tag.account_none: Account.Record_account_none, Account.Tag.account: Account.Record_account}

    def get_tag(self, cs: CellSlice) -> Optional["Account.Tag"]:
        return Account.Tag(int(cs.preload_uint(1)))


    class Record_account_none(RecordBase):
        def get_tag_enum(self):
            return Account.Tag.account_none

        def get_tag(self):
            return Account.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Account.cons_len_exact[self.get_tag_enum().value] if isinstance(Account.cons_len_exact, list) else Account.cons_len_exact

        def get_type_class(self):
            return Account


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_account(RecordBase):
        def get_tag_enum(self):
            return Account.Tag.account

        def get_tag(self):
            return Account.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Account.cons_len_exact[self.get_tag_enum().value] if isinstance(Account.cons_len_exact, list) else Account.cons_len_exact

        def get_type_class(self):
            return Account

        # addr : MsgAddressInt
        addr: "CellSlice" = None
        # storage_stat : StorageInfo
        storage_stat: "CellSlice" = None
        # storage : AccountStorage
        storage: "CellSlice" = None

        def __init__(self, addr: "CellSlice" = None, storage_stat: "CellSlice" = None, storage: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.addr = addr    
            self.field_names.append("addr")
            self.storage_stat = storage_stat    
            self.field_names.append("storage_stat")
            self.storage = storage    
            self.field_names.append("storage")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.addr = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.storage_stat = TLBComplex.constants["t_StorageInfo"].fetch(cs) 
                self.storage = TLBComplex.constants["t_AccountStorage"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Account")


# class for type `AccountStorage`
class AccountStorage(TLBComplex):
    class Tag(Enum):
        account_storage = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {AccountStorage.Tag.account_storage: AccountStorage.Record}

    def get_tag(self, cs: CellSlice) -> Optional["AccountStorage.Tag"]:
        return AccountStorage.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return AccountStorage.Tag.account_storage

        def get_tag(self):
            return AccountStorage.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountStorage.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountStorage.cons_len_exact, list) else AccountStorage.cons_len_exact

        def get_type_class(self):
            return AccountStorage

        # last_trans_lt : uint64
        last_trans_lt: "int" = None
        # balance : CurrencyCollection
        balance: "CellSlice" = None
        # state : AccountState
        state: "CellSlice" = None

        def __init__(self, last_trans_lt: "int" = None, balance: "CellSlice" = None, state: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.last_trans_lt = last_trans_lt    
            self.field_names.append("last_trans_lt")
            self.balance = balance    
            self.field_names.append("balance")
            self.state = state    
            self.field_names.append("state")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.last_trans_lt = cs.load_uint(64)
                self.balance = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.state = TLBComplex.constants["t_AccountState"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("AccountStorage")


# class for type `AccountState`
class AccountState(TLBComplex):
    class Tag(Enum):
        account_uninit = 0
        account_frozen = 1
        account_active = 2

    cons_len = [2, 2, 1]
    cons_tag = [0, 1, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {AccountState.Tag.account_uninit: AccountState.Record_account_uninit, AccountState.Tag.account_active: AccountState.Record_account_active, AccountState.Tag.account_frozen: AccountState.Record_account_frozen}

    def get_tag(self, cs: CellSlice) -> Optional["AccountState.Tag"]:
        return AccountState.Tag(int(cs.bselect(2, 7)))


    class Record_account_uninit(RecordBase):
        def get_tag_enum(self):
            return AccountState.Tag.account_uninit

        def get_tag(self):
            return AccountState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountState.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountState.cons_len_exact, list) else AccountState.cons_len_exact

        def get_type_class(self):
            return AccountState


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_account_active(RecordBase):
        def get_tag_enum(self):
            return AccountState.Tag.account_active

        def get_tag(self):
            return AccountState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountState.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountState.cons_len_exact, list) else AccountState.cons_len_exact

        def get_type_class(self):
            return AccountState

        # StateInit
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.x = TLBComplex.constants["t_StateInit"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_account_frozen(RecordBase):
        def get_tag_enum(self):
            return AccountState.Tag.account_frozen

        def get_tag(self):
            return AccountState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountState.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountState.cons_len_exact, list) else AccountState.cons_len_exact

        def get_type_class(self):
            return AccountState

        # state_hash : bits256
        state_hash: "bitstring.BitArray" = None

        def __init__(self, state_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.state_hash = state_hash    
            self.field_names.append("state_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'

                self.state_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("AccountState")


# class for type `AccountStatus`
class AccountStatus(TLBComplex):
    class Tag(Enum):
        acc_state_uninit = 0
        acc_state_frozen = 1
        acc_state_active = 2
        acc_state_nonexist = 3

    cons_len_exact = 2
    cons_tag = [0, 1, 2, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {AccountStatus.Tag.acc_state_uninit: AccountStatus.Record_acc_state_uninit, AccountStatus.Tag.acc_state_frozen: AccountStatus.Record_acc_state_frozen, AccountStatus.Tag.acc_state_active: AccountStatus.Record_acc_state_active, AccountStatus.Tag.acc_state_nonexist: AccountStatus.Record_acc_state_nonexist}

    def get_tag(self, cs: CellSlice) -> Optional["AccountStatus.Tag"]:
        return AccountStatus.Tag(int(cs.preload_uint(2)))


    def fetch_enum(self, cs: CellSlice) -> int:
        value = cs.load_uint(2)
        assert value in self.cons_tag, f'Unexpected value {value} for tag, expected one of: {self.cons_tag}'
        return value


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        assert value is not None, 'You must provide enum to store'
        cb.store_uint(value, 2)
        return True


    class Record_acc_state_uninit(RecordBase):
        def get_tag_enum(self):
            return AccountStatus.Tag.acc_state_uninit

        def get_tag(self):
            return AccountStatus.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountStatus.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountStatus.cons_len_exact, list) else AccountStatus.cons_len_exact

        def get_type_class(self):
            return AccountStatus


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_acc_state_frozen(RecordBase):
        def get_tag_enum(self):
            return AccountStatus.Tag.acc_state_frozen

        def get_tag(self):
            return AccountStatus.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountStatus.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountStatus.cons_len_exact, list) else AccountStatus.cons_len_exact

        def get_type_class(self):
            return AccountStatus


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_acc_state_active(RecordBase):
        def get_tag_enum(self):
            return AccountStatus.Tag.acc_state_active

        def get_tag(self):
            return AccountStatus.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountStatus.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountStatus.cons_len_exact, list) else AccountStatus.cons_len_exact

        def get_type_class(self):
            return AccountStatus


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_acc_state_nonexist(RecordBase):
        def get_tag_enum(self):
            return AccountStatus.Tag.acc_state_nonexist

        def get_tag(self):
            return AccountStatus.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountStatus.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountStatus.cons_len_exact, list) else AccountStatus.cons_len_exact

        def get_type_class(self):
            return AccountStatus


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("AccountStatus")


# class for type `ShardAccount`
class ShardAccount(TLBComplex):
    class Tag(Enum):
        account_descr = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardAccount.Tag.account_descr: ShardAccount.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardAccount.Tag"]:
        return ShardAccount.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardAccount.Tag.account_descr

        def get_tag(self):
            return ShardAccount.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardAccount.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardAccount.cons_len_exact, list) else ShardAccount.cons_len_exact

        def get_type_class(self):
            return ShardAccount

        # account : ^Account
        account: "Cell" = None
        # last_trans_hash : bits256
        last_trans_hash: "bitstring.BitArray" = None
        # last_trans_lt : uint64
        last_trans_lt: "int" = None

        def __init__(self, account: "Cell" = None, last_trans_hash: "bitstring.BitArray" = None, last_trans_lt: "int" = None):
            super().__init__()
            self.field_names = []
            self.account = account    
            self.field_names.append("account")
            self.last_trans_hash = last_trans_hash    
            self.field_names.append("last_trans_hash")
            self.last_trans_lt = last_trans_lt    
            self.field_names.append("last_trans_lt")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.account = cs.load_ref()
                
                if rec_unpack:
                    self.account = TLBComplex.constants["t_Ref_Account"].fetch(self.account, True, strict) # at 1
                    assert self.account is not None

                self.last_trans_hash = cs.load_bitstring(256)
                self.last_trans_lt = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardAccount")


# class for type `DepthBalanceInfo`
class DepthBalanceInfo(TLBComplex):
    class Tag(Enum):
        depth_balance = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {DepthBalanceInfo.Tag.depth_balance: DepthBalanceInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["DepthBalanceInfo.Tag"]:
        return DepthBalanceInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return DepthBalanceInfo.Tag.depth_balance

        def get_tag(self):
            return DepthBalanceInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DepthBalanceInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(DepthBalanceInfo.cons_len_exact, list) else DepthBalanceInfo.cons_len_exact

        def get_type_class(self):
            return DepthBalanceInfo

        # split_depth : #<= 30
        split_depth: "int" = None
        # balance : CurrencyCollection
        balance: "CellSlice" = None

        def __init__(self, split_depth: "int" = None, balance: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.split_depth = split_depth    
            self.field_names.append("split_depth")
            self.balance = balance    
            self.field_names.append("balance")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.split_depth = cs.load_uint_leq(30)
                self.balance = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("DepthBalanceInfo")


# class for type `ShardAccounts`
class ShardAccounts(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardAccounts.Tag.cons1: ShardAccounts.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardAccounts.Tag"]:
        return ShardAccounts.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardAccounts.Tag.cons1

        def get_tag(self):
            return ShardAccounts.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardAccounts.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardAccounts.cons_len_exact, list) else ShardAccounts.cons_len_exact

        def get_type_class(self):
            return ShardAccounts

        # HashmapAugE 256 ShardAccount DepthBalanceInfo
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_256_ShardAccount_DepthBalanceInfo"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardAccounts")


# class for auxiliary type `Transaction_aux`
class Transaction_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Transaction_aux.Tag.cons1: Transaction_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Transaction_aux.Tag"]:
        return Transaction_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Transaction_aux.Tag.cons1

        def get_tag(self):
            return Transaction_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Transaction_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(Transaction_aux.cons_len_exact, list) else Transaction_aux.cons_len_exact

        def get_type_class(self):
            return Transaction_aux

        # in_msg : Maybe ^(Message Any)
        in_msg: "CellSlice" = None
        # out_msgs : HashmapE 15 ^(Message Any)
        out_msgs: "CellSlice" = None

        def __init__(self, in_msg: "CellSlice" = None, out_msgs: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.in_msg = in_msg    
            self.field_names.append("in_msg")
            self.out_msgs = out_msgs    
            self.field_names.append("out_msgs")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.in_msg = TLBComplex.constants["t_Maybe_Ref_Message_Any"].fetch(cs) 
                self.out_msgs = TLBComplex.constants["t_HashmapE_15_Ref_Message_Any"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Transaction_aux")


# class for type `Transaction`
class Transaction(TLBComplex):
    class Tag(Enum):
        transaction = 0

    cons_len_exact = 4
    cons_tag = [7]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Transaction.Tag.transaction: Transaction.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Transaction.Tag"]:
        return Transaction.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Transaction.Tag.transaction

        def get_tag(self):
            return Transaction.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Transaction.cons_len_exact[self.get_tag_enum().value] if isinstance(Transaction.cons_len_exact, list) else Transaction.cons_len_exact

        def get_type_class(self):
            return Transaction

        # account_addr : bits256
        account_addr: "bitstring.BitArray" = None
        # lt : uint64
        lt: "int" = None
        # prev_trans_hash : bits256
        prev_trans_hash: "bitstring.BitArray" = None
        # prev_trans_lt : uint64
        prev_trans_lt: "int" = None
        # now : uint32
        now: "int" = None
        # outmsg_cnt : uint15
        outmsg_cnt: "int" = None
        # orig_status : AccountStatus
        orig_status: "Enum" = None
        # end_status : AccountStatus
        end_status: "Enum" = None
        # ^[$_ in_msg:(Maybe ^(Message Any)) out_msgs:(HashmapE 15 ^(Message Any)) ]
        r1: "Transaction_aux.Record" = None
        # total_fees : CurrencyCollection
        total_fees: "CellSlice" = None
        # state_update : ^(HASH_UPDATE Account)
        state_update: "Cell" = None
        # description : ^TransactionDescr
        description: "Cell" = None

        def __init__(self, account_addr: "bitstring.BitArray" = None, lt: "int" = None, prev_trans_hash: "bitstring.BitArray" = None, prev_trans_lt: "int" = None, now: "int" = None, outmsg_cnt: "int" = None, orig_status: "Enum" = None, end_status: "Enum" = None, r1: "Transaction_aux.Record" = None, total_fees: "CellSlice" = None, state_update: "Cell" = None, description: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.account_addr = account_addr    
            self.field_names.append("account_addr")
            self.lt = lt    
            self.field_names.append("lt")
            self.prev_trans_hash = prev_trans_hash    
            self.field_names.append("prev_trans_hash")
            self.prev_trans_lt = prev_trans_lt    
            self.field_names.append("prev_trans_lt")
            self.now = now    
            self.field_names.append("now")
            self.outmsg_cnt = outmsg_cnt    
            self.field_names.append("outmsg_cnt")
            self.orig_status = orig_status    
            self.field_names.append("orig_status")
            self.end_status = end_status    
            self.field_names.append("end_status")
            self.r1 = r1    
            self.field_names.append("r1")
            self.total_fees = total_fees    
            self.field_names.append("total_fees")
            self.state_update = state_update    
            self.field_names.append("state_update")
            self.description = description    
            self.field_names.append("description")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 7, 'Cons tag check failed'

                self.account_addr = cs.load_bitstring(256)
                self.lt = cs.load_uint(64)
                self.prev_trans_hash = cs.load_bitstring(256)
                self.prev_trans_lt = cs.load_uint(64)
                self.now = cs.load_uint(32)
                self.outmsg_cnt = cs.load_uint(15)
                self.orig_status = TLBComplex.constants["t_AccountStatus"].fetch_enum(cs) 
                self.end_status = TLBComplex.constants["t_AccountStatus"].fetch_enum(cs) 
                self.r1 = TLBComplex.constants["t_Transaction_aux"].fetch(cs.load_ref(), rec_unpack, strict)
                self.total_fees = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.state_update = cs.load_ref()
                
                if rec_unpack:
                    self.state_update = TLBComplex.constants["t_Ref_HASH_UPDATE_Account"].fetch(self.state_update, True, strict) # at 1
                    assert self.state_update is not None

                self.description = cs.load_ref()
                
                if rec_unpack:
                    self.description = TLBComplex.constants["t_Ref_TransactionDescr"].fetch(self.description, True, strict) # at 1
                    assert self.description is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Transaction")


# class for type `MERKLE_UPDATE`
class MERKLE_UPDATE(TLBComplex):
    class Tag(Enum):
        _merkle_update = 0

    cons_len_exact = 8
    cons_tag = [4]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {MERKLE_UPDATE.Tag._merkle_update: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["MERKLE_UPDATE.Tag"]:
        return MERKLE_UPDATE.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MERKLE_UPDATE.Tag._merkle_update

        def get_tag(self):
            return MERKLE_UPDATE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MERKLE_UPDATE.cons_len_exact[self.get_tag_enum().value] if isinstance(MERKLE_UPDATE.cons_len_exact, list) else MERKLE_UPDATE.cons_len_exact

        def get_type_class(self):
            return MERKLE_UPDATE

        # old_hash : bits256
        old_hash: "bitstring.BitArray" = None
        # new_hash : bits256
        new_hash: "bitstring.BitArray" = None
        # old : ^X
        old: "Cell" = None
        # new : ^X
        new: "Cell" = None

        def __init__(self, old_hash: "bitstring.BitArray" = None, new_hash: "bitstring.BitArray" = None, old: "Cell" = None, new: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.old_hash = old_hash    
            self.field_names.append("old_hash")
            self.new_hash = new_hash    
            self.field_names.append("new_hash")
            self.old = old    
            self.field_names.append("old")
            self.new = new    
            self.field_names.append("new")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 4, 'Cons tag check failed'

                self.old_hash = cs.load_bitstring(256)
                self.new_hash = cs.load_bitstring(256)
                self.old = cs.load_ref()
                
                if rec_unpack:
                    self.old = RefT(self.X_).fetch(self.old, True, strict) # at 1
                    assert self.old is not None

                self.new = cs.load_ref()
                
                if rec_unpack:
                    self.new = RefT(self.X_).fetch(self.new, True, strict) # at 1
                    assert self.new is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return True


tlb_classes.append("MERKLE_UPDATE")


# class for type `HASH_UPDATE`
class HASH_UPDATE(TLBComplex):
    class Tag(Enum):
        update_hashes = 0

    cons_len_exact = 8
    cons_tag = [0x72]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {HASH_UPDATE.Tag.update_hashes: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["HASH_UPDATE.Tag"]:
        return HASH_UPDATE.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return HASH_UPDATE.Tag.update_hashes

        def get_tag(self):
            return HASH_UPDATE.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return HASH_UPDATE.cons_len_exact[self.get_tag_enum().value] if isinstance(HASH_UPDATE.cons_len_exact, list) else HASH_UPDATE.cons_len_exact

        def get_type_class(self):
            return HASH_UPDATE

        # old_hash : bits256
        old_hash: "bitstring.BitArray" = None
        # new_hash : bits256
        new_hash: "bitstring.BitArray" = None

        def __init__(self, old_hash: "bitstring.BitArray" = None, new_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.old_hash = old_hash    
            self.field_names.append("old_hash")
            self.new_hash = new_hash    
            self.field_names.append("new_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x72, 'Cons tag check failed'

                self.old_hash = cs.load_bitstring(256)
                self.new_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("HASH_UPDATE")


# class for type `MERKLE_PROOF`
class MERKLE_PROOF(TLBComplex):
    class Tag(Enum):
        _merkle_proof = 0

    cons_len_exact = 8
    cons_tag = [3]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {MERKLE_PROOF.Tag._merkle_proof: self.get_param_record("Record")}

    def get_tag(self, cs: CellSlice) -> Optional["MERKLE_PROOF.Tag"]:
        return MERKLE_PROOF.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MERKLE_PROOF.Tag._merkle_proof

        def get_tag(self):
            return MERKLE_PROOF.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MERKLE_PROOF.cons_len_exact[self.get_tag_enum().value] if isinstance(MERKLE_PROOF.cons_len_exact, list) else MERKLE_PROOF.cons_len_exact

        def get_type_class(self):
            return MERKLE_PROOF

        # virtual_hash : bits256
        virtual_hash: "bitstring.BitArray" = None
        # depth : uint16
        depth: "int" = None
        # virtual_root : ^X
        virtual_root: "Cell" = None

        def __init__(self, virtual_hash: "bitstring.BitArray" = None, depth: "int" = None, virtual_root: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.virtual_hash = virtual_hash    
            self.field_names.append("virtual_hash")
            self.depth = depth    
            self.field_names.append("depth")
            self.virtual_root = virtual_root    
            self.field_names.append("virtual_root")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 3, 'Cons tag check failed'

                self.virtual_hash = cs.load_bitstring(256)
                self.depth = cs.load_uint(16)
                self.virtual_root = cs.load_ref()
                
                if rec_unpack:
                    self.virtual_root = RefT(self.X_).fetch(self.virtual_root, True, strict) # at 1
                    assert self.virtual_root is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return True


tlb_classes.append("MERKLE_PROOF")


# class for type `AccountBlock`
class AccountBlock(TLBComplex):
    class Tag(Enum):
        acc_trans = 0

    cons_len_exact = 4
    cons_tag = [5]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {AccountBlock.Tag.acc_trans: AccountBlock.Record}

    def get_tag(self, cs: CellSlice) -> Optional["AccountBlock.Tag"]:
        return AccountBlock.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return AccountBlock.Tag.acc_trans

        def get_tag(self):
            return AccountBlock.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccountBlock.cons_len_exact[self.get_tag_enum().value] if isinstance(AccountBlock.cons_len_exact, list) else AccountBlock.cons_len_exact

        def get_type_class(self):
            return AccountBlock

        # account_addr : bits256
        account_addr: "bitstring.BitArray" = None
        # transactions : HashmapAug 64 ^Transaction CurrencyCollection
        transactions: "CellSlice" = None
        # state_update : ^(HASH_UPDATE Account)
        state_update: "Cell" = None

        def __init__(self, account_addr: "bitstring.BitArray" = None, transactions: "CellSlice" = None, state_update: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.account_addr = account_addr    
            self.field_names.append("account_addr")
            self.transactions = transactions    
            self.field_names.append("transactions")
            self.state_update = state_update    
            self.field_names.append("state_update")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 5, 'Cons tag check failed'

                self.account_addr = cs.load_bitstring(256)
                self.transactions = TLBComplex.constants["t_HashmapAug_64_Ref_Transaction_CurrencyCollection"].fetch(cs) 
                self.state_update = cs.load_ref()
                
                if rec_unpack:
                    self.state_update = TLBComplex.constants["t_Ref_HASH_UPDATE_Account"].fetch(self.state_update, True, strict) # at 1
                    assert self.state_update is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("AccountBlock")


# class for type `ShardAccountBlocks`
class ShardAccountBlocks(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardAccountBlocks.Tag.cons1: ShardAccountBlocks.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardAccountBlocks.Tag"]:
        return ShardAccountBlocks.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardAccountBlocks.Tag.cons1

        def get_tag(self):
            return ShardAccountBlocks.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardAccountBlocks.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardAccountBlocks.cons_len_exact, list) else ShardAccountBlocks.cons_len_exact

        def get_type_class(self):
            return ShardAccountBlocks

        # HashmapAugE 256 AccountBlock CurrencyCollection
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_256_AccountBlock_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardAccountBlocks")


# class for type `TrStoragePhase`
class TrStoragePhase(TLBComplex):
    class Tag(Enum):
        tr_phase_storage = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TrStoragePhase.Tag.tr_phase_storage: TrStoragePhase.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TrStoragePhase.Tag"]:
        return TrStoragePhase.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TrStoragePhase.Tag.tr_phase_storage

        def get_tag(self):
            return TrStoragePhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrStoragePhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrStoragePhase.cons_len_exact, list) else TrStoragePhase.cons_len_exact

        def get_type_class(self):
            return TrStoragePhase

        # storage_fees_collected : Grams
        storage_fees_collected: "CellSlice" = None
        # storage_fees_due : Maybe Grams
        storage_fees_due: "CellSlice" = None
        # status_change : AccStatusChange
        status_change: "Enum" = None

        def __init__(self, storage_fees_collected: "CellSlice" = None, storage_fees_due: "CellSlice" = None, status_change: "Enum" = None):
            super().__init__()
            self.field_names = []
            self.storage_fees_collected = storage_fees_collected    
            self.field_names.append("storage_fees_collected")
            self.storage_fees_due = storage_fees_due    
            self.field_names.append("storage_fees_due")
            self.status_change = status_change    
            self.field_names.append("status_change")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.storage_fees_collected = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.storage_fees_due = TLBComplex.constants["t_Maybe_Grams"].fetch(cs) 
                self.status_change = TLBComplex.constants["t_AccStatusChange"].fetch_enum(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TrStoragePhase")


# class for type `AccStatusChange`
class AccStatusChange(TLBComplex):
    class Tag(Enum):
        acst_unchanged = 0
        acst_frozen = 1
        acst_deleted = 2

    cons_len = [1, 2, 2]
    cons_tag = [0, 2, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {AccStatusChange.Tag.acst_unchanged: AccStatusChange.Record_acst_unchanged, AccStatusChange.Tag.acst_frozen: AccStatusChange.Record_acst_frozen, AccStatusChange.Tag.acst_deleted: AccStatusChange.Record_acst_deleted}

    def get_tag(self, cs: CellSlice) -> Optional["AccStatusChange.Tag"]:
        return AccStatusChange.Tag(int(cs.bselect_ext(2, 13)))


    def fetch_enum(self, cs: CellSlice) -> int:
        expected_tag = self.get_tag(cs).value
        cs.advance(self.cons_len[expected_tag])
        return expected_tag


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        assert value is not None and value < 3, f'Value {value} must be < then 3'
        cb.store_uint(self.cons_tag[value], self.cons_len[value])
        return True


    class Record_acst_unchanged(RecordBase):
        def get_tag_enum(self):
            return AccStatusChange.Tag.acst_unchanged

        def get_tag(self):
            return AccStatusChange.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccStatusChange.cons_len_exact[self.get_tag_enum().value] if isinstance(AccStatusChange.cons_len_exact, list) else AccStatusChange.cons_len_exact

        def get_type_class(self):
            return AccStatusChange


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_acst_frozen(RecordBase):
        def get_tag_enum(self):
            return AccStatusChange.Tag.acst_frozen

        def get_tag(self):
            return AccStatusChange.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccStatusChange.cons_len_exact[self.get_tag_enum().value] if isinstance(AccStatusChange.cons_len_exact, list) else AccStatusChange.cons_len_exact

        def get_type_class(self):
            return AccStatusChange


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_acst_deleted(RecordBase):
        def get_tag_enum(self):
            return AccStatusChange.Tag.acst_deleted

        def get_tag(self):
            return AccStatusChange.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return AccStatusChange.cons_len_exact[self.get_tag_enum().value] if isinstance(AccStatusChange.cons_len_exact, list) else AccStatusChange.cons_len_exact

        def get_type_class(self):
            return AccStatusChange


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("AccStatusChange")


# class for type `TrCreditPhase`
class TrCreditPhase(TLBComplex):
    class Tag(Enum):
        tr_phase_credit = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TrCreditPhase.Tag.tr_phase_credit: TrCreditPhase.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TrCreditPhase.Tag"]:
        return TrCreditPhase.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TrCreditPhase.Tag.tr_phase_credit

        def get_tag(self):
            return TrCreditPhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrCreditPhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrCreditPhase.cons_len_exact, list) else TrCreditPhase.cons_len_exact

        def get_type_class(self):
            return TrCreditPhase

        # due_fees_collected : Maybe Grams
        due_fees_collected: "CellSlice" = None
        # credit : CurrencyCollection
        credit: "CellSlice" = None

        def __init__(self, due_fees_collected: "CellSlice" = None, credit: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.due_fees_collected = due_fees_collected    
            self.field_names.append("due_fees_collected")
            self.credit = credit    
            self.field_names.append("credit")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.due_fees_collected = TLBComplex.constants["t_Maybe_Grams"].fetch(cs) 
                self.credit = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TrCreditPhase")


# class for auxiliary type `TrComputePhase_aux`
class TrComputePhase_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TrComputePhase_aux.Tag.cons1: TrComputePhase_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TrComputePhase_aux.Tag"]:
        return TrComputePhase_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TrComputePhase_aux.Tag.cons1

        def get_tag(self):
            return TrComputePhase_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrComputePhase_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(TrComputePhase_aux.cons_len_exact, list) else TrComputePhase_aux.cons_len_exact

        def get_type_class(self):
            return TrComputePhase_aux

        # gas_used : VarUInteger 7
        gas_used: "CellSlice" = None
        # gas_limit : VarUInteger 7
        gas_limit: "CellSlice" = None
        # gas_credit : Maybe (VarUInteger 3)
        gas_credit: "CellSlice" = None
        # mode : int8
        mode: "int" = None
        # exit_code : int32
        exit_code: "int" = None
        # exit_arg : Maybe int32
        exit_arg: "CellSlice" = None
        # vm_steps : uint32
        vm_steps: "int" = None
        # vm_init_state_hash : bits256
        vm_init_state_hash: "bitstring.BitArray" = None
        # vm_final_state_hash : bits256
        vm_final_state_hash: "bitstring.BitArray" = None

        def __init__(self, gas_used: "CellSlice" = None, gas_limit: "CellSlice" = None, gas_credit: "CellSlice" = None, mode: "int" = None, exit_code: "int" = None, exit_arg: "CellSlice" = None, vm_steps: "int" = None, vm_init_state_hash: "bitstring.BitArray" = None, vm_final_state_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.gas_used = gas_used    
            self.field_names.append("gas_used")
            self.gas_limit = gas_limit    
            self.field_names.append("gas_limit")
            self.gas_credit = gas_credit    
            self.field_names.append("gas_credit")
            self.mode = mode    
            self.field_names.append("mode")
            self.exit_code = exit_code    
            self.field_names.append("exit_code")
            self.exit_arg = exit_arg    
            self.field_names.append("exit_arg")
            self.vm_steps = vm_steps    
            self.field_names.append("vm_steps")
            self.vm_init_state_hash = vm_init_state_hash    
            self.field_names.append("vm_init_state_hash")
            self.vm_final_state_hash = vm_final_state_hash    
            self.field_names.append("vm_final_state_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.gas_used = TLBComplex.constants["t_VarUInteger_7"].fetch(cs) 
                self.gas_limit = TLBComplex.constants["t_VarUInteger_7"].fetch(cs) 
                self.gas_credit = TLBComplex.constants["t_Maybe_VarUInteger_3"].fetch(cs) 
                self.mode = cs.load_int(8)
                self.exit_code = cs.load_int(32)
                self.exit_arg = TLBComplex.constants["t_Maybe_int32"].fetch(cs) 
                self.vm_steps = cs.load_uint(32)
                self.vm_init_state_hash = cs.load_bitstring(256)
                self.vm_final_state_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TrComputePhase_aux")


# class for type `TrComputePhase`
class TrComputePhase(TLBComplex):
    class Tag(Enum):
        tr_phase_compute_skipped = 0
        tr_phase_compute_vm = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TrComputePhase.Tag.tr_phase_compute_skipped: TrComputePhase.Record_tr_phase_compute_skipped, TrComputePhase.Tag.tr_phase_compute_vm: TrComputePhase.Record_tr_phase_compute_vm}

    def get_tag(self, cs: CellSlice) -> Optional["TrComputePhase.Tag"]:
        return TrComputePhase.Tag(int(cs.preload_uint(1)))


    class Record_tr_phase_compute_skipped(RecordBase):
        def get_tag_enum(self):
            return TrComputePhase.Tag.tr_phase_compute_skipped

        def get_tag(self):
            return TrComputePhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrComputePhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrComputePhase.cons_len_exact, list) else TrComputePhase.cons_len_exact

        def get_type_class(self):
            return TrComputePhase

        # reason : ComputeSkipReason
        reason: "Enum" = None

        def __init__(self, reason: "Enum" = None):
            super().__init__()
            self.field_names = []
            self.reason = reason    
            self.field_names.append("reason")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.reason = TLBComplex.constants["t_ComputeSkipReason"].fetch_enum(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_tr_phase_compute_vm(RecordBase):
        def get_tag_enum(self):
            return TrComputePhase.Tag.tr_phase_compute_vm

        def get_tag(self):
            return TrComputePhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrComputePhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrComputePhase.cons_len_exact, list) else TrComputePhase.cons_len_exact

        def get_type_class(self):
            return TrComputePhase

        # success : Bool
        success: "bool" = None
        # msg_state_used : Bool
        msg_state_used: "bool" = None
        # account_activated : Bool
        account_activated: "bool" = None
        # gas_fees : Grams
        gas_fees: "CellSlice" = None
        # ^[$_ gas_used:(VarUInteger 7) gas_limit:(VarUInteger 7) gas_credit:(Maybe (VarUInteger 3)) mode:int8 exit_code:int32 exit_arg:(Maybe int32) vm_steps:uint32 vm_init_state_hash:bits256 vm_final_state_hash:bits256 ]
        r1: "TrComputePhase_aux.Record" = None

        def __init__(self, success: "bool" = None, msg_state_used: "bool" = None, account_activated: "bool" = None, gas_fees: "CellSlice" = None, r1: "TrComputePhase_aux.Record" = None):
            super().__init__()
            self.field_names = []
            self.success = success    
            self.field_names.append("success")
            self.msg_state_used = msg_state_used    
            self.field_names.append("msg_state_used")
            self.account_activated = account_activated    
            self.field_names.append("account_activated")
            self.gas_fees = gas_fees    
            self.field_names.append("gas_fees")
            self.r1 = r1    
            self.field_names.append("r1")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.success = cs.load_bool()
                self.msg_state_used = cs.load_bool()
                self.account_activated = cs.load_bool()
                self.gas_fees = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.r1 = TLBComplex.constants["t_TrComputePhase_aux"].fetch(cs.load_ref(), rec_unpack, strict)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TrComputePhase")


# class for type `ComputeSkipReason`
class ComputeSkipReason(TLBComplex):
    class Tag(Enum):
        cskip_no_state = 0
        cskip_bad_state = 1
        cskip_no_gas = 2
        cskip_suspended = 3

    cons_len = [2, 2, 2, 3]
    cons_tag = [0, 1, 2, 6]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ComputeSkipReason.Tag.cskip_no_state: ComputeSkipReason.Record_cskip_no_state, ComputeSkipReason.Tag.cskip_bad_state: ComputeSkipReason.Record_cskip_bad_state, ComputeSkipReason.Tag.cskip_no_gas: ComputeSkipReason.Record_cskip_no_gas, ComputeSkipReason.Tag.cskip_suspended: ComputeSkipReason.Record_cskip_suspended}

    def get_tag(self, cs: CellSlice) -> Optional["ComputeSkipReason.Tag"]:
        return ComputeSkipReason.Tag(int(cs.preload_uint(2)))


    def fetch_enum(self, cs: CellSlice) -> int:
        expected_tag = self.get_tag(cs).value
        value = cs.load_uint(self.cons_len[expected_tag])
        assert value == self.cons_tag[expected_tag], f'Not valid tag fetched, got {value}, expected {self.cons_tag[expected_tag]}'
        return value


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        assert value is not None and value < 4, f'Value {value} must be < then 4'
        cb.store_uint(self.cons_tag[value], self.cons_len[value])
        return True


    class Record_cskip_no_state(RecordBase):
        def get_tag_enum(self):
            return ComputeSkipReason.Tag.cskip_no_state

        def get_tag(self):
            return ComputeSkipReason.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComputeSkipReason.cons_len_exact[self.get_tag_enum().value] if isinstance(ComputeSkipReason.cons_len_exact, list) else ComputeSkipReason.cons_len_exact

        def get_type_class(self):
            return ComputeSkipReason


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cskip_bad_state(RecordBase):
        def get_tag_enum(self):
            return ComputeSkipReason.Tag.cskip_bad_state

        def get_tag(self):
            return ComputeSkipReason.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComputeSkipReason.cons_len_exact[self.get_tag_enum().value] if isinstance(ComputeSkipReason.cons_len_exact, list) else ComputeSkipReason.cons_len_exact

        def get_type_class(self):
            return ComputeSkipReason


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cskip_no_gas(RecordBase):
        def get_tag_enum(self):
            return ComputeSkipReason.Tag.cskip_no_gas

        def get_tag(self):
            return ComputeSkipReason.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComputeSkipReason.cons_len_exact[self.get_tag_enum().value] if isinstance(ComputeSkipReason.cons_len_exact, list) else ComputeSkipReason.cons_len_exact

        def get_type_class(self):
            return ComputeSkipReason


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cskip_suspended(RecordBase):
        def get_tag_enum(self):
            return ComputeSkipReason.Tag.cskip_suspended

        def get_tag(self):
            return ComputeSkipReason.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComputeSkipReason.cons_len_exact[self.get_tag_enum().value] if isinstance(ComputeSkipReason.cons_len_exact, list) else ComputeSkipReason.cons_len_exact

        def get_type_class(self):
            return ComputeSkipReason


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 6, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ComputeSkipReason")


# class for type `TrActionPhase`
class TrActionPhase(TLBComplex):
    class Tag(Enum):
        tr_phase_action = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TrActionPhase.Tag.tr_phase_action: TrActionPhase.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TrActionPhase.Tag"]:
        return TrActionPhase.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TrActionPhase.Tag.tr_phase_action

        def get_tag(self):
            return TrActionPhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrActionPhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrActionPhase.cons_len_exact, list) else TrActionPhase.cons_len_exact

        def get_type_class(self):
            return TrActionPhase

        # success : Bool
        success: "bool" = None
        # valid : Bool
        valid: "bool" = None
        # no_funds : Bool
        no_funds: "bool" = None
        # status_change : AccStatusChange
        status_change: "Enum" = None
        # total_fwd_fees : Maybe Grams
        total_fwd_fees: "CellSlice" = None
        # total_action_fees : Maybe Grams
        total_action_fees: "CellSlice" = None
        # result_code : int32
        result_code: "int" = None
        # result_arg : Maybe int32
        result_arg: "CellSlice" = None
        # tot_actions : uint16
        tot_actions: "int" = None
        # spec_actions : uint16
        spec_actions: "int" = None
        # skipped_actions : uint16
        skipped_actions: "int" = None
        # msgs_created : uint16
        msgs_created: "int" = None
        # action_list_hash : bits256
        action_list_hash: "bitstring.BitArray" = None
        # tot_msg_size : StorageUsedShort
        tot_msg_size: "CellSlice" = None

        def __init__(self, success: "bool" = None, valid: "bool" = None, no_funds: "bool" = None, status_change: "Enum" = None, total_fwd_fees: "CellSlice" = None, total_action_fees: "CellSlice" = None, result_code: "int" = None, result_arg: "CellSlice" = None, tot_actions: "int" = None, spec_actions: "int" = None, skipped_actions: "int" = None, msgs_created: "int" = None, action_list_hash: "bitstring.BitArray" = None, tot_msg_size: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.success = success    
            self.field_names.append("success")
            self.valid = valid    
            self.field_names.append("valid")
            self.no_funds = no_funds    
            self.field_names.append("no_funds")
            self.status_change = status_change    
            self.field_names.append("status_change")
            self.total_fwd_fees = total_fwd_fees    
            self.field_names.append("total_fwd_fees")
            self.total_action_fees = total_action_fees    
            self.field_names.append("total_action_fees")
            self.result_code = result_code    
            self.field_names.append("result_code")
            self.result_arg = result_arg    
            self.field_names.append("result_arg")
            self.tot_actions = tot_actions    
            self.field_names.append("tot_actions")
            self.spec_actions = spec_actions    
            self.field_names.append("spec_actions")
            self.skipped_actions = skipped_actions    
            self.field_names.append("skipped_actions")
            self.msgs_created = msgs_created    
            self.field_names.append("msgs_created")
            self.action_list_hash = action_list_hash    
            self.field_names.append("action_list_hash")
            self.tot_msg_size = tot_msg_size    
            self.field_names.append("tot_msg_size")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.success = cs.load_bool()
                self.valid = cs.load_bool()
                self.no_funds = cs.load_bool()
                self.status_change = TLBComplex.constants["t_AccStatusChange"].fetch_enum(cs) 
                self.total_fwd_fees = TLBComplex.constants["t_Maybe_Grams"].fetch(cs) 
                self.total_action_fees = TLBComplex.constants["t_Maybe_Grams"].fetch(cs) 
                self.result_code = cs.load_int(32)
                self.result_arg = TLBComplex.constants["t_Maybe_int32"].fetch(cs) 
                self.tot_actions = cs.load_uint(16)
                self.spec_actions = cs.load_uint(16)
                self.skipped_actions = cs.load_uint(16)
                self.msgs_created = cs.load_uint(16)
                self.action_list_hash = cs.load_bitstring(256)
                self.tot_msg_size = TLBComplex.constants["t_StorageUsedShort"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TrActionPhase")


# class for type `TrBouncePhase`
class TrBouncePhase(TLBComplex):
    class Tag(Enum):
        tr_phase_bounce_negfunds = 0
        tr_phase_bounce_nofunds = 1
        tr_phase_bounce_ok = 2

    cons_len = [2, 2, 1]
    cons_tag = [0, 1, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TrBouncePhase.Tag.tr_phase_bounce_negfunds: TrBouncePhase.Record_tr_phase_bounce_negfunds, TrBouncePhase.Tag.tr_phase_bounce_nofunds: TrBouncePhase.Record_tr_phase_bounce_nofunds, TrBouncePhase.Tag.tr_phase_bounce_ok: TrBouncePhase.Record_tr_phase_bounce_ok}

    def get_tag(self, cs: CellSlice) -> Optional["TrBouncePhase.Tag"]:
        return TrBouncePhase.Tag(int(cs.bselect_ext(2, 7)))


    class Record_tr_phase_bounce_negfunds(RecordBase):
        def get_tag_enum(self):
            return TrBouncePhase.Tag.tr_phase_bounce_negfunds

        def get_tag(self):
            return TrBouncePhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrBouncePhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrBouncePhase.cons_len_exact, list) else TrBouncePhase.cons_len_exact

        def get_type_class(self):
            return TrBouncePhase


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_tr_phase_bounce_nofunds(RecordBase):
        def get_tag_enum(self):
            return TrBouncePhase.Tag.tr_phase_bounce_nofunds

        def get_tag(self):
            return TrBouncePhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrBouncePhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrBouncePhase.cons_len_exact, list) else TrBouncePhase.cons_len_exact

        def get_type_class(self):
            return TrBouncePhase

        # msg_size : StorageUsedShort
        msg_size: "CellSlice" = None
        # req_fwd_fees : Grams
        req_fwd_fees: "CellSlice" = None

        def __init__(self, msg_size: "CellSlice" = None, req_fwd_fees: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.msg_size = msg_size    
            self.field_names.append("msg_size")
            self.req_fwd_fees = req_fwd_fees    
            self.field_names.append("req_fwd_fees")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'

                self.msg_size = TLBComplex.constants["t_StorageUsedShort"].fetch(cs) 
                self.req_fwd_fees = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_tr_phase_bounce_ok(RecordBase):
        def get_tag_enum(self):
            return TrBouncePhase.Tag.tr_phase_bounce_ok

        def get_tag(self):
            return TrBouncePhase.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TrBouncePhase.cons_len_exact[self.get_tag_enum().value] if isinstance(TrBouncePhase.cons_len_exact, list) else TrBouncePhase.cons_len_exact

        def get_type_class(self):
            return TrBouncePhase

        # msg_size : StorageUsedShort
        msg_size: "CellSlice" = None
        # msg_fees : Grams
        msg_fees: "CellSlice" = None
        # fwd_fees : Grams
        fwd_fees: "CellSlice" = None

        def __init__(self, msg_size: "CellSlice" = None, msg_fees: "CellSlice" = None, fwd_fees: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.msg_size = msg_size    
            self.field_names.append("msg_size")
            self.msg_fees = msg_fees    
            self.field_names.append("msg_fees")
            self.fwd_fees = fwd_fees    
            self.field_names.append("fwd_fees")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.msg_size = TLBComplex.constants["t_StorageUsedShort"].fetch(cs) 
                self.msg_fees = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.fwd_fees = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TrBouncePhase")


# class for type `SplitMergeInfo`
class SplitMergeInfo(TLBComplex):
    class Tag(Enum):
        split_merge_info = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SplitMergeInfo.Tag.split_merge_info: SplitMergeInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["SplitMergeInfo.Tag"]:
        return SplitMergeInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return SplitMergeInfo.Tag.split_merge_info

        def get_tag(self):
            return SplitMergeInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SplitMergeInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(SplitMergeInfo.cons_len_exact, list) else SplitMergeInfo.cons_len_exact

        def get_type_class(self):
            return SplitMergeInfo

        # cur_shard_pfx_len : ## 6
        cur_shard_pfx_len: "int" = None
        # acc_split_depth : ## 6
        acc_split_depth: "int" = None
        # this_addr : bits256
        this_addr: "bitstring.BitArray" = None
        # sibling_addr : bits256
        sibling_addr: "bitstring.BitArray" = None

        def __init__(self, cur_shard_pfx_len: "int" = None, acc_split_depth: "int" = None, this_addr: "bitstring.BitArray" = None, sibling_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.cur_shard_pfx_len = cur_shard_pfx_len    
            self.field_names.append("cur_shard_pfx_len")
            self.acc_split_depth = acc_split_depth    
            self.field_names.append("acc_split_depth")
            self.this_addr = this_addr    
            self.field_names.append("this_addr")
            self.sibling_addr = sibling_addr    
            self.field_names.append("sibling_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cur_shard_pfx_len = cs.load_uint(6)
                self.acc_split_depth = cs.load_uint(6)
                self.this_addr = cs.load_bitstring(256)
                self.sibling_addr = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SplitMergeInfo")


# class for type `TransactionDescr`
class TransactionDescr(TLBComplex):
    class Tag(Enum):
        trans_ord = 0
        trans_storage = 1
        trans_tick_tock = 2
        trans_split_prepare = 3
        trans_split_install = 4
        trans_merge_prepare = 5
        trans_merge_install = 6

    cons_len = [4, 4, 3, 4, 4, 4, 4]
    cons_tag = [0, 1, 1, 4, 5, 6, 7]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TransactionDescr.Tag.trans_ord: TransactionDescr.Record_trans_ord, TransactionDescr.Tag.trans_storage: TransactionDescr.Record_trans_storage, TransactionDescr.Tag.trans_tick_tock: TransactionDescr.Record_trans_tick_tock, TransactionDescr.Tag.trans_split_prepare: TransactionDescr.Record_trans_split_prepare, TransactionDescr.Tag.trans_split_install: TransactionDescr.Record_trans_split_install, TransactionDescr.Tag.trans_merge_prepare: TransactionDescr.Record_trans_merge_prepare, TransactionDescr.Tag.trans_merge_install: TransactionDescr.Record_trans_merge_install}

    def get_tag(self, cs: CellSlice) -> Optional["TransactionDescr.Tag"]:
        return TransactionDescr.Tag(int(cs.bselect(4, 0xf7)))


    class Record_trans_ord(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_ord

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # credit_first : Bool
        credit_first: "bool" = None
        # storage_ph : Maybe TrStoragePhase
        storage_ph: "CellSlice" = None
        # credit_ph : Maybe TrCreditPhase
        credit_ph: "CellSlice" = None
        # compute_ph : TrComputePhase
        compute_ph: "CellSlice" = None
        # action : Maybe ^TrActionPhase
        action: "CellSlice" = None
        # aborted : Bool
        aborted: "bool" = None
        # bounce : Maybe TrBouncePhase
        bounce: "CellSlice" = None
        # destroyed : Bool
        destroyed: "bool" = None

        def __init__(self, credit_first: "bool" = None, storage_ph: "CellSlice" = None, credit_ph: "CellSlice" = None, compute_ph: "CellSlice" = None, action: "CellSlice" = None, aborted: "bool" = None, bounce: "CellSlice" = None, destroyed: "bool" = None):
            super().__init__()
            self.field_names = []
            self.credit_first = credit_first    
            self.field_names.append("credit_first")
            self.storage_ph = storage_ph    
            self.field_names.append("storage_ph")
            self.credit_ph = credit_ph    
            self.field_names.append("credit_ph")
            self.compute_ph = compute_ph    
            self.field_names.append("compute_ph")
            self.action = action    
            self.field_names.append("action")
            self.aborted = aborted    
            self.field_names.append("aborted")
            self.bounce = bounce    
            self.field_names.append("bounce")
            self.destroyed = destroyed    
            self.field_names.append("destroyed")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 0, 'Cons tag check failed'

                self.credit_first = cs.load_bool()
                self.storage_ph = TLBComplex.constants["t_Maybe_TrStoragePhase"].fetch(cs) 
                self.credit_ph = TLBComplex.constants["t_Maybe_TrCreditPhase"].fetch(cs) 
                self.compute_ph = TLBComplex.constants["t_TrComputePhase"].fetch(cs) 
                self.action = TLBComplex.constants["t_Maybe_Ref_TrActionPhase"].fetch(cs) 
                self.aborted = cs.load_bool()
                self.bounce = TLBComplex.constants["t_Maybe_TrBouncePhase"].fetch(cs) 
                self.destroyed = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_trans_storage(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_storage

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # storage_ph : TrStoragePhase
        storage_ph: "CellSlice" = None

        def __init__(self, storage_ph: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.storage_ph = storage_ph    
            self.field_names.append("storage_ph")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 1, 'Cons tag check failed'

                self.storage_ph = TLBComplex.constants["t_TrStoragePhase"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_trans_tick_tock(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_tick_tock

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # is_tock : Bool
        is_tock: "bool" = None
        # storage_ph : TrStoragePhase
        storage_ph: "CellSlice" = None
        # compute_ph : TrComputePhase
        compute_ph: "CellSlice" = None
        # action : Maybe ^TrActionPhase
        action: "CellSlice" = None
        # aborted : Bool
        aborted: "bool" = None
        # destroyed : Bool
        destroyed: "bool" = None

        def __init__(self, is_tock: "bool" = None, storage_ph: "CellSlice" = None, compute_ph: "CellSlice" = None, action: "CellSlice" = None, aborted: "bool" = None, destroyed: "bool" = None):
            super().__init__()
            self.field_names = []
            self.is_tock = is_tock    
            self.field_names.append("is_tock")
            self.storage_ph = storage_ph    
            self.field_names.append("storage_ph")
            self.compute_ph = compute_ph    
            self.field_names.append("compute_ph")
            self.action = action    
            self.field_names.append("action")
            self.aborted = aborted    
            self.field_names.append("aborted")
            self.destroyed = destroyed    
            self.field_names.append("destroyed")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 1, 'Cons tag check failed'

                self.is_tock = cs.load_bool()
                self.storage_ph = TLBComplex.constants["t_TrStoragePhase"].fetch(cs) 
                self.compute_ph = TLBComplex.constants["t_TrComputePhase"].fetch(cs) 
                self.action = TLBComplex.constants["t_Maybe_Ref_TrActionPhase"].fetch(cs) 
                self.aborted = cs.load_bool()
                self.destroyed = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_trans_split_prepare(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_split_prepare

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # split_info : SplitMergeInfo
        split_info: "CellSlice" = None
        # storage_ph : Maybe TrStoragePhase
        storage_ph: "CellSlice" = None
        # compute_ph : TrComputePhase
        compute_ph: "CellSlice" = None
        # action : Maybe ^TrActionPhase
        action: "CellSlice" = None
        # aborted : Bool
        aborted: "bool" = None
        # destroyed : Bool
        destroyed: "bool" = None

        def __init__(self, split_info: "CellSlice" = None, storage_ph: "CellSlice" = None, compute_ph: "CellSlice" = None, action: "CellSlice" = None, aborted: "bool" = None, destroyed: "bool" = None):
            super().__init__()
            self.field_names = []
            self.split_info = split_info    
            self.field_names.append("split_info")
            self.storage_ph = storage_ph    
            self.field_names.append("storage_ph")
            self.compute_ph = compute_ph    
            self.field_names.append("compute_ph")
            self.action = action    
            self.field_names.append("action")
            self.aborted = aborted    
            self.field_names.append("aborted")
            self.destroyed = destroyed    
            self.field_names.append("destroyed")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 4, 'Cons tag check failed'

                self.split_info = cs.load_subslice(524)
                
                if rec_unpack:
                    self.split_info = TLBComplex.constants["t_SplitMergeInfo"].fetch(self.split_info, True, strict) # at 1
                    assert self.split_info is not None

                self.storage_ph = TLBComplex.constants["t_Maybe_TrStoragePhase"].fetch(cs) 
                self.compute_ph = TLBComplex.constants["t_TrComputePhase"].fetch(cs) 
                self.action = TLBComplex.constants["t_Maybe_Ref_TrActionPhase"].fetch(cs) 
                self.aborted = cs.load_bool()
                self.destroyed = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_trans_split_install(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_split_install

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # split_info : SplitMergeInfo
        split_info: "CellSlice" = None
        # prepare_transaction : ^Transaction
        prepare_transaction: "Cell" = None
        # installed : Bool
        installed: "bool" = None

        def __init__(self, split_info: "CellSlice" = None, prepare_transaction: "Cell" = None, installed: "bool" = None):
            super().__init__()
            self.field_names = []
            self.split_info = split_info    
            self.field_names.append("split_info")
            self.prepare_transaction = prepare_transaction    
            self.field_names.append("prepare_transaction")
            self.installed = installed    
            self.field_names.append("installed")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 5, 'Cons tag check failed'

                self.split_info = cs.load_subslice(524)
                
                if rec_unpack:
                    self.split_info = TLBComplex.constants["t_SplitMergeInfo"].fetch(self.split_info, True, strict) # at 1
                    assert self.split_info is not None

                self.prepare_transaction = cs.load_ref()
                
                if rec_unpack:
                    self.prepare_transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.prepare_transaction, True, strict) # at 1
                    assert self.prepare_transaction is not None

                self.installed = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_trans_merge_prepare(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_merge_prepare

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # split_info : SplitMergeInfo
        split_info: "CellSlice" = None
        # storage_ph : TrStoragePhase
        storage_ph: "CellSlice" = None
        # aborted : Bool
        aborted: "bool" = None

        def __init__(self, split_info: "CellSlice" = None, storage_ph: "CellSlice" = None, aborted: "bool" = None):
            super().__init__()
            self.field_names = []
            self.split_info = split_info    
            self.field_names.append("split_info")
            self.storage_ph = storage_ph    
            self.field_names.append("storage_ph")
            self.aborted = aborted    
            self.field_names.append("aborted")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 6, 'Cons tag check failed'

                self.split_info = cs.load_subslice(524)
                
                if rec_unpack:
                    self.split_info = TLBComplex.constants["t_SplitMergeInfo"].fetch(self.split_info, True, strict) # at 1
                    assert self.split_info is not None

                self.storage_ph = TLBComplex.constants["t_TrStoragePhase"].fetch(cs) 
                self.aborted = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_trans_merge_install(RecordBase):
        def get_tag_enum(self):
            return TransactionDescr.Tag.trans_merge_install

        def get_tag(self):
            return TransactionDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TransactionDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TransactionDescr.cons_len_exact, list) else TransactionDescr.cons_len_exact

        def get_type_class(self):
            return TransactionDescr

        # split_info : SplitMergeInfo
        split_info: "CellSlice" = None
        # prepare_transaction : ^Transaction
        prepare_transaction: "Cell" = None
        # storage_ph : Maybe TrStoragePhase
        storage_ph: "CellSlice" = None
        # credit_ph : Maybe TrCreditPhase
        credit_ph: "CellSlice" = None
        # compute_ph : TrComputePhase
        compute_ph: "CellSlice" = None
        # action : Maybe ^TrActionPhase
        action: "CellSlice" = None
        # aborted : Bool
        aborted: "bool" = None
        # destroyed : Bool
        destroyed: "bool" = None

        def __init__(self, split_info: "CellSlice" = None, prepare_transaction: "Cell" = None, storage_ph: "CellSlice" = None, credit_ph: "CellSlice" = None, compute_ph: "CellSlice" = None, action: "CellSlice" = None, aborted: "bool" = None, destroyed: "bool" = None):
            super().__init__()
            self.field_names = []
            self.split_info = split_info    
            self.field_names.append("split_info")
            self.prepare_transaction = prepare_transaction    
            self.field_names.append("prepare_transaction")
            self.storage_ph = storage_ph    
            self.field_names.append("storage_ph")
            self.credit_ph = credit_ph    
            self.field_names.append("credit_ph")
            self.compute_ph = compute_ph    
            self.field_names.append("compute_ph")
            self.action = action    
            self.field_names.append("action")
            self.aborted = aborted    
            self.field_names.append("aborted")
            self.destroyed = destroyed    
            self.field_names.append("destroyed")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 7, 'Cons tag check failed'

                self.split_info = cs.load_subslice(524)
                
                if rec_unpack:
                    self.split_info = TLBComplex.constants["t_SplitMergeInfo"].fetch(self.split_info, True, strict) # at 1
                    assert self.split_info is not None

                self.prepare_transaction = cs.load_ref()
                
                if rec_unpack:
                    self.prepare_transaction = TLBComplex.constants["t_Ref_Transaction"].fetch(self.prepare_transaction, True, strict) # at 1
                    assert self.prepare_transaction is not None

                self.storage_ph = TLBComplex.constants["t_Maybe_TrStoragePhase"].fetch(cs) 
                self.credit_ph = TLBComplex.constants["t_Maybe_TrCreditPhase"].fetch(cs) 
                self.compute_ph = TLBComplex.constants["t_TrComputePhase"].fetch(cs) 
                self.action = TLBComplex.constants["t_Maybe_Ref_TrActionPhase"].fetch(cs) 
                self.aborted = cs.load_bool()
                self.destroyed = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TransactionDescr")


# class for type `SmartContractInfo`
class SmartContractInfo(TLBComplex):
    class Tag(Enum):
        smc_info = 0

    cons_len_exact = 32
    cons_tag = [0x76ef1ea]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SmartContractInfo.Tag.smc_info: SmartContractInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["SmartContractInfo.Tag"]:
        return SmartContractInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return SmartContractInfo.Tag.smc_info

        def get_tag(self):
            return SmartContractInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmartContractInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(SmartContractInfo.cons_len_exact, list) else SmartContractInfo.cons_len_exact

        def get_type_class(self):
            return SmartContractInfo

        # actions : uint16
        actions: "int" = None
        # msgs_sent : uint16
        msgs_sent: "int" = None
        # unixtime : uint32
        unixtime: "int" = None
        # block_lt : uint64
        block_lt: "int" = None
        # trans_lt : uint64
        trans_lt: "int" = None
        # rand_seed : bits256
        rand_seed: "bitstring.BitArray" = None
        # balance_remaining : CurrencyCollection
        balance_remaining: "CellSlice" = None
        # myself : MsgAddressInt
        myself: "CellSlice" = None
        # global_config : Maybe Cell
        global_config: "CellSlice" = None

        def __init__(self, actions: "int" = None, msgs_sent: "int" = None, unixtime: "int" = None, block_lt: "int" = None, trans_lt: "int" = None, rand_seed: "bitstring.BitArray" = None, balance_remaining: "CellSlice" = None, myself: "CellSlice" = None, global_config: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.actions = actions    
            self.field_names.append("actions")
            self.msgs_sent = msgs_sent    
            self.field_names.append("msgs_sent")
            self.unixtime = unixtime    
            self.field_names.append("unixtime")
            self.block_lt = block_lt    
            self.field_names.append("block_lt")
            self.trans_lt = trans_lt    
            self.field_names.append("trans_lt")
            self.rand_seed = rand_seed    
            self.field_names.append("rand_seed")
            self.balance_remaining = balance_remaining    
            self.field_names.append("balance_remaining")
            self.myself = myself    
            self.field_names.append("myself")
            self.global_config = global_config    
            self.field_names.append("global_config")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x76ef1ea, 'Cons tag check failed'

                self.actions = cs.load_uint(16)
                self.msgs_sent = cs.load_uint(16)
                self.unixtime = cs.load_uint(32)
                self.block_lt = cs.load_uint(64)
                self.trans_lt = cs.load_uint(64)
                self.rand_seed = cs.load_bitstring(256)
                self.balance_remaining = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.myself = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.global_config = TLBComplex.constants["t_Maybe_Cell"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SmartContractInfo")


# class for type `OutList`
class OutList(TLBComplex):
    class Tag(Enum):
        out_list = 0
        out_list_empty = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {OutList.Tag.out_list_empty: self.get_param_record("Record_out_list_empty"), OutList.Tag.out_list: self.get_param_record("Record_out_list")}

    def get_tag(self, cs: CellSlice) -> Optional["OutList.Tag"]:
        # distinguish by parameter `m_` using 1 2 2 2
        return OutList.Tag.out_list if self.m_ else OutList.Tag.out_list_empty




    class Record_out_list_empty(RecordBase):
        def get_tag_enum(self):
            return OutList.Tag.out_list_empty

        def get_tag(self):
            return OutList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutList.cons_len_exact[self.get_tag_enum().value] if isinstance(OutList.cons_len_exact, list) else OutList.cons_len_exact

        def get_type_class(self):
            return OutList


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_out_list(RecordBase):
        def get_tag_enum(self):
            return OutList.Tag.out_list

        def get_tag(self):
            return OutList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutList.cons_len_exact[self.get_tag_enum().value] if isinstance(OutList.cons_len_exact, list) else OutList.cons_len_exact

        def get_type_class(self):
            return OutList

        # n : #
        n: "int" = None
        # prev : ^(OutList n)
        prev: "Cell" = None
        # action : OutAction
        action: "CellSlice" = None

        def __init__(self, prev: "Cell" = None, action: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.prev = prev    
            self.field_names.append("prev")
            self.action = action    
            self.field_names.append("action")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.prev = cs.load_ref()
                
                if rec_unpack:
                    self.prev = RefT(OutList(self.n)).fetch(self.prev, True, strict) # at 1
                    assert self.prev is not None

                self.action = TLBComplex.constants["t_OutAction"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutList")


# class for type `LibRef`
class LibRef(TLBComplex):
    class Tag(Enum):
        libref_hash = 0
        libref_ref = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {LibRef.Tag.libref_hash: LibRef.Record_libref_hash, LibRef.Tag.libref_ref: LibRef.Record_libref_ref}

    def get_tag(self, cs: CellSlice) -> Optional["LibRef.Tag"]:
        return LibRef.Tag(int(cs.preload_uint(1)))


    class Record_libref_hash(RecordBase):
        def get_tag_enum(self):
            return LibRef.Tag.libref_hash

        def get_tag(self):
            return LibRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return LibRef.cons_len_exact[self.get_tag_enum().value] if isinstance(LibRef.cons_len_exact, list) else LibRef.cons_len_exact

        def get_type_class(self):
            return LibRef

        # lib_hash : bits256
        lib_hash: "bitstring.BitArray" = None

        def __init__(self, lib_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.lib_hash = lib_hash    
            self.field_names.append("lib_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.lib_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_libref_ref(RecordBase):
        def get_tag_enum(self):
            return LibRef.Tag.libref_ref

        def get_tag(self):
            return LibRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return LibRef.cons_len_exact[self.get_tag_enum().value] if isinstance(LibRef.cons_len_exact, list) else LibRef.cons_len_exact

        def get_type_class(self):
            return LibRef

        # library : ^Cell
        library: "Cell" = None

        def __init__(self, library: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.library = library    
            self.field_names.append("library")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.library = cs.load_ref()
                
                if rec_unpack:
                    self.library = TLBComplex.constants["t_RefCell"].fetch(self.library, True, strict) # at 1
                    assert self.library is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("LibRef")


# class for type `OutAction`
class OutAction(TLBComplex):
    class Tag(Enum):
        action_send_msg = 0
        action_change_library = 1
        action_reserve_currency = 2
        action_set_code = 3

    cons_len_exact = 32
    cons_tag = [0xec3c86d, 0x26fa1dd4, 0x36e6b809, 0xad4de08e]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OutAction.Tag.action_send_msg: OutAction.Record_action_send_msg, OutAction.Tag.action_set_code: OutAction.Record_action_set_code, OutAction.Tag.action_reserve_currency: OutAction.Record_action_reserve_currency, OutAction.Tag.action_change_library: OutAction.Record_action_change_library}

    def get_tag(self, cs: CellSlice) -> Optional["OutAction.Tag"]:
        return OutAction.Tag(int(cs.bselect(4, 0x40d)))


    class Record_action_send_msg(RecordBase):
        def get_tag_enum(self):
            return OutAction.Tag.action_send_msg

        def get_tag(self):
            return OutAction.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutAction.cons_len_exact[self.get_tag_enum().value] if isinstance(OutAction.cons_len_exact, list) else OutAction.cons_len_exact

        def get_type_class(self):
            return OutAction

        # mode : ## 8
        mode: "int" = None
        # out_msg : ^(MessageRelaxed Any)
        out_msg: "Cell" = None

        def __init__(self, mode: "int" = None, out_msg: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.mode = mode    
            self.field_names.append("mode")
            self.out_msg = out_msg    
            self.field_names.append("out_msg")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0xec3c86d, 'Cons tag check failed'

                self.mode = cs.load_uint(8)
                self.out_msg = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg = TLBComplex.constants["t_Ref_MessageRelaxed_Any"].fetch(self.out_msg, True, strict) # at 1
                    assert self.out_msg is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_action_set_code(RecordBase):
        def get_tag_enum(self):
            return OutAction.Tag.action_set_code

        def get_tag(self):
            return OutAction.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutAction.cons_len_exact[self.get_tag_enum().value] if isinstance(OutAction.cons_len_exact, list) else OutAction.cons_len_exact

        def get_type_class(self):
            return OutAction

        # new_code : ^Cell
        new_code: "Cell" = None

        def __init__(self, new_code: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.new_code = new_code    
            self.field_names.append("new_code")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0xad4de08e, 'Cons tag check failed'

                self.new_code = cs.load_ref()
                
                if rec_unpack:
                    self.new_code = TLBComplex.constants["t_RefCell"].fetch(self.new_code, True, strict) # at 1
                    assert self.new_code is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_action_reserve_currency(RecordBase):
        def get_tag_enum(self):
            return OutAction.Tag.action_reserve_currency

        def get_tag(self):
            return OutAction.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutAction.cons_len_exact[self.get_tag_enum().value] if isinstance(OutAction.cons_len_exact, list) else OutAction.cons_len_exact

        def get_type_class(self):
            return OutAction

        # mode : ## 8
        mode: "int" = None
        # currency : CurrencyCollection
        currency: "CellSlice" = None

        def __init__(self, mode: "int" = None, currency: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.mode = mode    
            self.field_names.append("mode")
            self.currency = currency    
            self.field_names.append("currency")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x36e6b809, 'Cons tag check failed'

                self.mode = cs.load_uint(8)
                self.currency = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_action_change_library(RecordBase):
        def get_tag_enum(self):
            return OutAction.Tag.action_change_library

        def get_tag(self):
            return OutAction.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutAction.cons_len_exact[self.get_tag_enum().value] if isinstance(OutAction.cons_len_exact, list) else OutAction.cons_len_exact

        def get_type_class(self):
            return OutAction

        # mode : ## 7
        mode: "int" = None
        # libref : LibRef
        libref: "CellSlice" = None

        def __init__(self, mode: "int" = None, libref: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.mode = mode    
            self.field_names.append("mode")
            self.libref = libref    
            self.field_names.append("libref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x26fa1dd4, 'Cons tag check failed'

                self.mode = cs.load_uint(7)
                self.libref = TLBComplex.constants["t_LibRef"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutAction")


# class for type `OutListNode`
class OutListNode(TLBComplex):
    class Tag(Enum):
        out_list_node = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OutListNode.Tag.out_list_node: OutListNode.Record}

    def get_tag(self, cs: CellSlice) -> Optional["OutListNode.Tag"]:
        return OutListNode.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return OutListNode.Tag.out_list_node

        def get_tag(self):
            return OutListNode.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OutListNode.cons_len_exact[self.get_tag_enum().value] if isinstance(OutListNode.cons_len_exact, list) else OutListNode.cons_len_exact

        def get_type_class(self):
            return OutListNode

        # prev : ^Cell
        prev: "Cell" = None
        # action : OutAction
        action: "CellSlice" = None

        def __init__(self, prev: "Cell" = None, action: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.prev = prev    
            self.field_names.append("prev")
            self.action = action    
            self.field_names.append("action")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev = cs.load_ref()
                
                if rec_unpack:
                    self.prev = TLBComplex.constants["t_RefCell"].fetch(self.prev, True, strict) # at 1
                    assert self.prev is not None

                self.action = TLBComplex.constants["t_OutAction"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OutListNode")


# class for type `ShardIdent`
class ShardIdent(TLBComplex):
    class Tag(Enum):
        shard_ident = 0

    cons_len_exact = 2
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardIdent.Tag.shard_ident: ShardIdent.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardIdent.Tag"]:
        return ShardIdent.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardIdent.Tag.shard_ident

        def get_tag(self):
            return ShardIdent.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardIdent.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardIdent.cons_len_exact, list) else ShardIdent.cons_len_exact

        def get_type_class(self):
            return ShardIdent

        # shard_pfx_bits : #<= 60
        shard_pfx_bits: "int" = None
        # workchain_id : int32
        workchain_id: "int" = None
        # shard_prefix : uint64
        shard_prefix: "int" = None

        def __init__(self, shard_pfx_bits: "int" = None, workchain_id: "int" = None, shard_prefix: "int" = None):
            super().__init__()
            self.field_names = []
            self.shard_pfx_bits = shard_pfx_bits    
            self.field_names.append("shard_pfx_bits")
            self.workchain_id = workchain_id    
            self.field_names.append("workchain_id")
            self.shard_prefix = shard_prefix    
            self.field_names.append("shard_prefix")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'

                self.shard_pfx_bits = cs.load_uint_leq(60)
                self.workchain_id = cs.load_int(32)
                self.shard_prefix = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardIdent")


# class for type `ExtBlkRef`
class ExtBlkRef(TLBComplex):
    class Tag(Enum):
        ext_blk_ref = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ExtBlkRef.Tag.ext_blk_ref: ExtBlkRef.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ExtBlkRef.Tag"]:
        return ExtBlkRef.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ExtBlkRef.Tag.ext_blk_ref

        def get_tag(self):
            return ExtBlkRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ExtBlkRef.cons_len_exact[self.get_tag_enum().value] if isinstance(ExtBlkRef.cons_len_exact, list) else ExtBlkRef.cons_len_exact

        def get_type_class(self):
            return ExtBlkRef

        # end_lt : uint64
        end_lt: "int" = None
        # seq_no : uint32
        seq_no: "int" = None
        # root_hash : bits256
        root_hash: "bitstring.BitArray" = None
        # file_hash : bits256
        file_hash: "bitstring.BitArray" = None

        def __init__(self, end_lt: "int" = None, seq_no: "int" = None, root_hash: "bitstring.BitArray" = None, file_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.end_lt = end_lt    
            self.field_names.append("end_lt")
            self.seq_no = seq_no    
            self.field_names.append("seq_no")
            self.root_hash = root_hash    
            self.field_names.append("root_hash")
            self.file_hash = file_hash    
            self.field_names.append("file_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.end_lt = cs.load_uint(64)
                self.seq_no = cs.load_uint(32)
                self.root_hash = cs.load_bitstring(256)
                self.file_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ExtBlkRef")


# class for type `BlockIdExt`
class BlockIdExt(TLBComplex):
    class Tag(Enum):
        block_id_ext = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockIdExt.Tag.block_id_ext: BlockIdExt.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockIdExt.Tag"]:
        return BlockIdExt.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockIdExt.Tag.block_id_ext

        def get_tag(self):
            return BlockIdExt.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockIdExt.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockIdExt.cons_len_exact, list) else BlockIdExt.cons_len_exact

        def get_type_class(self):
            return BlockIdExt

        # shard_id : ShardIdent
        shard_id: "CellSlice" = None
        # seq_no : uint32
        seq_no: "int" = None
        # root_hash : bits256
        root_hash: "bitstring.BitArray" = None
        # file_hash : bits256
        file_hash: "bitstring.BitArray" = None

        def __init__(self, shard_id: "CellSlice" = None, seq_no: "int" = None, root_hash: "bitstring.BitArray" = None, file_hash: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.shard_id = shard_id    
            self.field_names.append("shard_id")
            self.seq_no = seq_no    
            self.field_names.append("seq_no")
            self.root_hash = root_hash    
            self.field_names.append("root_hash")
            self.file_hash = file_hash    
            self.field_names.append("file_hash")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.shard_id = cs.load_subslice(104)
                
                if rec_unpack:
                    self.shard_id = TLBComplex.constants["t_ShardIdent"].fetch(self.shard_id, True, strict) # at 1
                    assert self.shard_id is not None

                self.seq_no = cs.load_uint(32)
                self.root_hash = cs.load_bitstring(256)
                self.file_hash = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockIdExt")


# class for type `BlkMasterInfo`
class BlkMasterInfo(TLBComplex):
    class Tag(Enum):
        master_info = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlkMasterInfo.Tag.master_info: BlkMasterInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlkMasterInfo.Tag"]:
        return BlkMasterInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlkMasterInfo.Tag.master_info

        def get_tag(self):
            return BlkMasterInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlkMasterInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(BlkMasterInfo.cons_len_exact, list) else BlkMasterInfo.cons_len_exact

        def get_type_class(self):
            return BlkMasterInfo

        # master : ExtBlkRef
        master: "CellSlice" = None

        def __init__(self, master: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.master = master    
            self.field_names.append("master")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.master = cs.load_subslice(608)
                
                if rec_unpack:
                    self.master = TLBComplex.constants["t_ExtBlkRef"].fetch(self.master, True, strict) # at 1
                    assert self.master is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlkMasterInfo")


# class for auxiliary type `ShardStateUnsplit_aux`
class ShardStateUnsplit_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardStateUnsplit_aux.Tag.cons1: ShardStateUnsplit_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardStateUnsplit_aux.Tag"]:
        return ShardStateUnsplit_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardStateUnsplit_aux.Tag.cons1

        def get_tag(self):
            return ShardStateUnsplit_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardStateUnsplit_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardStateUnsplit_aux.cons_len_exact, list) else ShardStateUnsplit_aux.cons_len_exact

        def get_type_class(self):
            return ShardStateUnsplit_aux

        # overload_history : uint64
        overload_history: "int" = None
        # underload_history : uint64
        underload_history: "int" = None
        # total_balance : CurrencyCollection
        total_balance: "CellSlice" = None
        # total_validator_fees : CurrencyCollection
        total_validator_fees: "CellSlice" = None
        # libraries : HashmapE 256 LibDescr
        libraries: "CellSlice" = None
        # master_ref : Maybe BlkMasterInfo
        master_ref: "CellSlice" = None

        def __init__(self, overload_history: "int" = None, underload_history: "int" = None, total_balance: "CellSlice" = None, total_validator_fees: "CellSlice" = None, libraries: "CellSlice" = None, master_ref: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.overload_history = overload_history    
            self.field_names.append("overload_history")
            self.underload_history = underload_history    
            self.field_names.append("underload_history")
            self.total_balance = total_balance    
            self.field_names.append("total_balance")
            self.total_validator_fees = total_validator_fees    
            self.field_names.append("total_validator_fees")
            self.libraries = libraries    
            self.field_names.append("libraries")
            self.master_ref = master_ref    
            self.field_names.append("master_ref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.overload_history = cs.load_uint(64)
                self.underload_history = cs.load_uint(64)
                self.total_balance = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.total_validator_fees = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.libraries = TLBComplex.constants["t_HashmapE_256_LibDescr"].fetch(cs) 
                self.master_ref = TLBComplex.constants["t_Maybe_BlkMasterInfo"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardStateUnsplit_aux")


# class for type `ShardStateUnsplit`
class ShardStateUnsplit(TLBComplex):
    class Tag(Enum):
        shard_state = 0

    cons_len_exact = 32
    cons_tag = [0x9023afe2]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardStateUnsplit.Tag.shard_state: ShardStateUnsplit.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardStateUnsplit.Tag"]:
        return ShardStateUnsplit.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardStateUnsplit.Tag.shard_state

        def get_tag(self):
            return ShardStateUnsplit.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardStateUnsplit.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardStateUnsplit.cons_len_exact, list) else ShardStateUnsplit.cons_len_exact

        def get_type_class(self):
            return ShardStateUnsplit

        # global_id : int32
        global_id: "int" = None
        # shard_id : ShardIdent
        shard_id: "CellSlice" = None
        # seq_no : uint32
        seq_no: "int" = None
        # vert_seq_no : #
        vert_seq_no: "int" = None
        # gen_utime : uint32
        gen_utime: "int" = None
        # gen_lt : uint64
        gen_lt: "int" = None
        # min_ref_mc_seqno : uint32
        min_ref_mc_seqno: "int" = None
        # out_msg_queue_info : ^OutMsgQueueInfo
        out_msg_queue_info: "Cell" = None
        # before_split : ## 1
        before_split: "bool" = None
        # accounts : ^ShardAccounts
        accounts: "Cell" = None
        # ^[$_ overload_history:uint64 underload_history:uint64 total_balance:CurrencyCollection total_validator_fees:CurrencyCollection libraries:(HashmapE 256 LibDescr) master_ref:(Maybe BlkMasterInfo) ]
        r1: "ShardStateUnsplit_aux.Record" = None
        # custom : Maybe ^McStateExtra
        custom: "CellSlice" = None

        def __init__(self, global_id: "int" = None, shard_id: "CellSlice" = None, seq_no: "int" = None, vert_seq_no: "int" = None, gen_utime: "int" = None, gen_lt: "int" = None, min_ref_mc_seqno: "int" = None, out_msg_queue_info: "Cell" = None, before_split: "bool" = None, accounts: "Cell" = None, r1: "ShardStateUnsplit_aux.Record" = None, custom: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.global_id = global_id    
            self.field_names.append("global_id")
            self.shard_id = shard_id    
            self.field_names.append("shard_id")
            self.seq_no = seq_no    
            self.field_names.append("seq_no")
            self.vert_seq_no = vert_seq_no    
            self.field_names.append("vert_seq_no")
            self.gen_utime = gen_utime    
            self.field_names.append("gen_utime")
            self.gen_lt = gen_lt    
            self.field_names.append("gen_lt")
            self.min_ref_mc_seqno = min_ref_mc_seqno    
            self.field_names.append("min_ref_mc_seqno")
            self.out_msg_queue_info = out_msg_queue_info    
            self.field_names.append("out_msg_queue_info")
            self.before_split = before_split    
            self.field_names.append("before_split")
            self.accounts = accounts    
            self.field_names.append("accounts")
            self.r1 = r1    
            self.field_names.append("r1")
            self.custom = custom    
            self.field_names.append("custom")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x9023afe2, 'Cons tag check failed'

                self.global_id = cs.load_int(32)
                self.shard_id = cs.load_subslice(104)
                
                if rec_unpack:
                    self.shard_id = TLBComplex.constants["t_ShardIdent"].fetch(self.shard_id, True, strict) # at 1
                    assert self.shard_id is not None

                self.seq_no = cs.load_uint(32)
                self.vert_seq_no = cs.load_uint(32)

                self.gen_utime = cs.load_uint(32)
                self.gen_lt = cs.load_uint(64)
                self.min_ref_mc_seqno = cs.load_uint(32)
                self.out_msg_queue_info = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg_queue_info = TLBComplex.constants["t_Ref_OutMsgQueueInfo"].fetch(self.out_msg_queue_info, True, strict) # at 1
                    assert self.out_msg_queue_info is not None

                self.before_split = cs.load_bool()

                self.accounts = cs.load_ref()
                
                if rec_unpack:
                    self.accounts = TLBComplex.constants["t_Ref_ShardAccounts"].fetch(self.accounts, True, strict) # at 1
                    assert self.accounts is not None

                self.r1 = TLBComplex.constants["t_ShardStateUnsplit_aux"].fetch(cs.load_ref(), rec_unpack, strict)
                self.custom = TLBComplex.constants["t_Maybe_Ref_McStateExtra"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardStateUnsplit")


# class for type `ShardState`
class ShardState(TLBComplex):
    class Tag(Enum):
        split_state = 0
        cons1 = 1

    cons_len = [32, 0]
    cons_tag = [0x5f327da5, 0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardState.Tag.cons1: ShardState.Record_cons1, ShardState.Tag.split_state: ShardState.Record_split_state}

    def get_tag(self, cs: CellSlice) -> Optional["ShardState.Tag"]:
        return ShardState.Tag(int(cs.preload_uint(1)))


    class Record_cons1(RecordBase):
        def get_tag_enum(self):
            return ShardState.Tag.cons1

        def get_tag(self):
            return ShardState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardState.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardState.cons_len_exact, list) else ShardState.cons_len_exact

        def get_type_class(self):
            return ShardState

        # ShardStateUnsplit
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_ShardStateUnsplit"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_split_state(RecordBase):
        def get_tag_enum(self):
            return ShardState.Tag.split_state

        def get_tag(self):
            return ShardState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardState.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardState.cons_len_exact, list) else ShardState.cons_len_exact

        def get_type_class(self):
            return ShardState

        # left : ^ShardStateUnsplit
        left: "Cell" = None
        # right : ^ShardStateUnsplit
        right: "Cell" = None

        def __init__(self, left: "Cell" = None, right: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.left = left    
            self.field_names.append("left")
            self.right = right    
            self.field_names.append("right")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x5f327da5, 'Cons tag check failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = TLBComplex.constants["t_Ref_ShardStateUnsplit"].fetch(self.left, True, strict) # at 1
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = TLBComplex.constants["t_Ref_ShardStateUnsplit"].fetch(self.right, True, strict) # at 1
                    assert self.right is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardState")


# class for type `LibDescr`
class LibDescr(TLBComplex):
    class Tag(Enum):
        shared_lib_descr = 0

    cons_len_exact = 2
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {LibDescr.Tag.shared_lib_descr: LibDescr.Record}

    def get_tag(self, cs: CellSlice) -> Optional["LibDescr.Tag"]:
        return LibDescr.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return LibDescr.Tag.shared_lib_descr

        def get_tag(self):
            return LibDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return LibDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(LibDescr.cons_len_exact, list) else LibDescr.cons_len_exact

        def get_type_class(self):
            return LibDescr

        # lib : ^Cell
        lib: "Cell" = None
        # publishers : Hashmap 256 Truet
        publishers: "CellSlice" = None

        def __init__(self, lib: "Cell" = None, publishers: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.lib = lib    
            self.field_names.append("lib")
            self.publishers = publishers    
            self.field_names.append("publishers")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'

                self.lib = cs.load_ref()
                
                if rec_unpack:
                    self.lib = TLBComplex.constants["t_RefCell"].fetch(self.lib, True, strict) # at 1
                    assert self.lib is not None

                self.publishers = TLBComplex.constants["t_Hashmap_256_Truet"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("LibDescr")


# class for type `BlockInfo`
class BlockInfo(TLBComplex):
    class Tag(Enum):
        block_info = 0

    cons_len_exact = 32
    cons_tag = [0x9bc7a987]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockInfo.Tag.block_info: BlockInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockInfo.Tag"]:
        return BlockInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockInfo.Tag.block_info

        def get_tag(self):
            return BlockInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockInfo.cons_len_exact, list) else BlockInfo.cons_len_exact

        def get_type_class(self):
            return BlockInfo

        # version : uint32
        version: "int" = None
        # not_master : ## 1
        not_master: "bool" = None
        # after_merge : ## 1
        after_merge: "bool" = None
        # before_split : ## 1
        before_split: "bool" = None
        # after_split : ## 1
        after_split: "bool" = None
        # want_split : Bool
        want_split: "bool" = None
        # want_merge : Bool
        want_merge: "bool" = None
        # key_block : Bool
        key_block: "bool" = None
        # vert_seqno_incr : ## 1
        vert_seqno_incr: "bool" = None
        # flags : ## 8
        flags: "int" = None
        # seq_no : #
        seq_no: "int" = None
        # vert_seq_no : #
        vert_seq_no: "int" = None
        # shard : ShardIdent
        shard: "CellSlice" = None
        # gen_utime : uint32
        gen_utime: "int" = None
        # start_lt : uint64
        start_lt: "int" = None
        # end_lt : uint64
        end_lt: "int" = None
        # gen_validator_list_hash_short : uint32
        gen_validator_list_hash_short: "int" = None
        # gen_catchain_seqno : uint32
        gen_catchain_seqno: "int" = None
        # min_ref_mc_seqno : uint32
        min_ref_mc_seqno: "int" = None
        # prev_key_block_seqno : uint32
        prev_key_block_seqno: "int" = None
        # gen_software : flags.0?GlobalVersion
        gen_software: "CellSlice" = None
        # master_ref : not_master?^BlkMasterInfo
        master_ref: "Cell" = None
        # prev_ref : ^(BlkPrevInfo after_merge)
        prev_ref: "Cell" = None
        # prev_vert_ref : vert_seqno_incr?^(BlkPrevInfo 0)
        prev_vert_ref: "Cell" = None

        def __init__(self, version: "int" = None, not_master: "bool" = None, after_merge: "bool" = None, before_split: "bool" = None, after_split: "bool" = None, want_split: "bool" = None, want_merge: "bool" = None, key_block: "bool" = None, vert_seqno_incr: "bool" = None, flags: "int" = None, seq_no: "int" = None, vert_seq_no: "int" = None, shard: "CellSlice" = None, gen_utime: "int" = None, start_lt: "int" = None, end_lt: "int" = None, gen_validator_list_hash_short: "int" = None, gen_catchain_seqno: "int" = None, min_ref_mc_seqno: "int" = None, prev_key_block_seqno: "int" = None, gen_software: "CellSlice" = None, master_ref: "Cell" = None, prev_ref: "Cell" = None, prev_vert_ref: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.version = version    
            self.field_names.append("version")
            self.not_master = not_master    
            self.field_names.append("not_master")
            self.after_merge = after_merge    
            self.field_names.append("after_merge")
            self.before_split = before_split    
            self.field_names.append("before_split")
            self.after_split = after_split    
            self.field_names.append("after_split")
            self.want_split = want_split    
            self.field_names.append("want_split")
            self.want_merge = want_merge    
            self.field_names.append("want_merge")
            self.key_block = key_block    
            self.field_names.append("key_block")
            self.vert_seqno_incr = vert_seqno_incr    
            self.field_names.append("vert_seqno_incr")
            self.flags = flags    
            self.field_names.append("flags")
            self.seq_no = seq_no    
            self.field_names.append("seq_no")
            self.vert_seq_no = vert_seq_no    
            self.field_names.append("vert_seq_no")
            self.shard = shard    
            self.field_names.append("shard")
            self.gen_utime = gen_utime    
            self.field_names.append("gen_utime")
            self.start_lt = start_lt    
            self.field_names.append("start_lt")
            self.end_lt = end_lt    
            self.field_names.append("end_lt")
            self.gen_validator_list_hash_short = gen_validator_list_hash_short    
            self.field_names.append("gen_validator_list_hash_short")
            self.gen_catchain_seqno = gen_catchain_seqno    
            self.field_names.append("gen_catchain_seqno")
            self.min_ref_mc_seqno = min_ref_mc_seqno    
            self.field_names.append("min_ref_mc_seqno")
            self.prev_key_block_seqno = prev_key_block_seqno    
            self.field_names.append("prev_key_block_seqno")
            self.gen_software = gen_software    
            self.conditional_fields.append("gen_software")    
            self.field_names.append("gen_software")
            self.master_ref = master_ref    
            self.conditional_fields.append("master_ref")    
            self.field_names.append("master_ref")
            self.prev_ref = prev_ref    
            self.field_names.append("prev_ref")
            self.prev_vert_ref = prev_vert_ref    
            self.conditional_fields.append("prev_vert_ref")    
            self.field_names.append("prev_vert_ref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev_seq_no = None
                assert cs.load_uint(32) == 0x9bc7a987, 'Cons tag check failed'

                self.version = cs.load_uint(32)
                self.not_master = cs.load_bool()

                self.after_merge = cs.load_bool()

                self.before_split = cs.load_bool()

                self.after_split = cs.load_bool()

                self.want_split = cs.load_bool()
                self.want_merge = cs.load_bool()
                self.key_block = cs.load_bool()
                self.vert_seqno_incr = cs.load_bool()

                self.flags = cs.load_uint(8)
                assert self.flags <= 1, 'Params not equal: flags and 1'

                self.seq_no = cs.load_uint(32)

                self.vert_seq_no = cs.load_uint(32)

                assert self.vert_seqno_incr <= self.vert_seq_no, 'Params not equal: vert_seqno_incr and vert_seq_no'

                assert self.add_r1("prev_seq_no", 1, self.seq_no), 'Add_r1 failed'

                self.shard = cs.load_subslice(104)
                
                if rec_unpack:
                    self.shard = TLBComplex.constants["t_ShardIdent"].fetch(self.shard, True, strict) # at 1
                    assert self.shard is not None

                self.gen_utime = cs.load_uint(32)
                self.start_lt = cs.load_uint(64)
                self.end_lt = cs.load_uint(64)
                self.gen_validator_list_hash_short = cs.load_uint(32)
                self.gen_catchain_seqno = cs.load_uint(32)
                self.min_ref_mc_seqno = cs.load_uint(32)
                self.prev_key_block_seqno = cs.load_uint(32)
                if ((self.flags & (1 << 0)) != 0):
                    self.gen_software = cs.load_subslice(104)

                    
                if rec_unpack and self.gen_software is not None:
                    self.gen_software = TLBComplex.constants["t_GlobalVersion"].fetch(self.gen_software, True, strict) # at 3
                    assert self.gen_software is not None

                if (self.not_master > 0):
                    
                    self.master_ref = cs.load_ref()
                    
                if rec_unpack and self.master_ref is not None:
                    self.master_ref = TLBComplex.constants["t_Ref_BlkMasterInfo"].fetch(self.master_ref, True, strict) # at 3
                    assert self.master_ref is not None

                self.prev_ref = cs.load_ref()
                
                if rec_unpack:
                    self.prev_ref = RefT(BlkPrevInfo(self.after_merge)).fetch(self.prev_ref, True, strict) # at 1
                    assert self.prev_ref is not None

                if (self.vert_seqno_incr > 0):
                    
                    self.prev_vert_ref = cs.load_ref()
                    
                if rec_unpack and self.prev_vert_ref is not None:
                    self.prev_vert_ref = TLBComplex.constants["t_Ref_BlkPrevInfo_0"].fetch(self.prev_vert_ref, True, strict) # at 3
                    assert self.prev_vert_ref is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockInfo")


# class for type `BlkPrevInfo`
class BlkPrevInfo(TLBComplex):
    class Tag(Enum):
        prev_blk_info = 0
        prev_blks_info = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {BlkPrevInfo.Tag.prev_blk_info: self.get_param_record("Record_prev_blk_info"), BlkPrevInfo.Tag.prev_blks_info: self.get_param_record("Record_prev_blks_info")}

    def get_tag(self, cs: CellSlice) -> Optional["BlkPrevInfo.Tag"]:
        tag = self.m_

        if tag == 0:
            return BlkPrevInfo.Tag.prev_blk_info

        if tag == 1:
            return BlkPrevInfo.Tag.prev_blks_info

        return None


    class Record_prev_blk_info(RecordBase):
        def get_tag_enum(self):
            return BlkPrevInfo.Tag.prev_blk_info

        def get_tag(self):
            return BlkPrevInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlkPrevInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(BlkPrevInfo.cons_len_exact, list) else BlkPrevInfo.cons_len_exact

        def get_type_class(self):
            return BlkPrevInfo

        # prev : ExtBlkRef
        prev: "CellSlice" = None

        def __init__(self, prev: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.prev = prev    
            self.field_names.append("prev")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev = cs.load_subslice(608)
                
                if rec_unpack:
                    self.prev = TLBComplex.constants["t_ExtBlkRef"].fetch(self.prev, True, strict) # at 1
                    assert self.prev is not None

                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_prev_blks_info(RecordBase):
        def get_tag_enum(self):
            return BlkPrevInfo.Tag.prev_blks_info

        def get_tag(self):
            return BlkPrevInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlkPrevInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(BlkPrevInfo.cons_len_exact, list) else BlkPrevInfo.cons_len_exact

        def get_type_class(self):
            return BlkPrevInfo

        # prev1 : ^ExtBlkRef
        prev1: "Cell" = None
        # prev2 : ^ExtBlkRef
        prev2: "Cell" = None

        def __init__(self, prev1: "Cell" = None, prev2: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.prev1 = prev1    
            self.field_names.append("prev1")
            self.prev2 = prev2    
            self.field_names.append("prev2")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev1 = cs.load_ref()
                
                if rec_unpack:
                    self.prev1 = TLBComplex.constants["t_Ref_ExtBlkRef"].fetch(self.prev1, True, strict) # at 1
                    assert self.prev1 is not None

                self.prev2 = cs.load_ref()
                
                if rec_unpack:
                    self.prev2 = TLBComplex.constants["t_Ref_ExtBlkRef"].fetch(self.prev2, True, strict) # at 1
                    assert self.prev2 is not None

                self.m_ == 1                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlkPrevInfo")


# class for type `Block`
class Block(TLBComplex):
    class Tag(Enum):
        block = 0

    cons_len_exact = 32
    cons_tag = [0x11ef55aa]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Block.Tag.block: Block.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Block.Tag"]:
        return Block.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Block.Tag.block

        def get_tag(self):
            return Block.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Block.cons_len_exact[self.get_tag_enum().value] if isinstance(Block.cons_len_exact, list) else Block.cons_len_exact

        def get_type_class(self):
            return Block

        # global_id : int32
        global_id: "int" = None
        # info : ^BlockInfo
        info: "Cell" = None
        # value_flow : ^ValueFlow
        value_flow: "Cell" = None
        # state_update : ^(MERKLE_UPDATE ShardState)
        state_update: "Cell" = None
        # extra : ^BlockExtra
        extra: "Cell" = None

        def __init__(self, global_id: "int" = None, info: "Cell" = None, value_flow: "Cell" = None, state_update: "Cell" = None, extra: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.global_id = global_id    
            self.field_names.append("global_id")
            self.info = info    
            self.field_names.append("info")
            self.value_flow = value_flow    
            self.field_names.append("value_flow")
            self.state_update = state_update    
            self.field_names.append("state_update")
            self.extra = extra    
            self.field_names.append("extra")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x11ef55aa, 'Cons tag check failed'

                self.global_id = cs.load_int(32)
                self.info = cs.load_ref()
                
                if rec_unpack:
                    self.info = TLBComplex.constants["t_Ref_BlockInfo"].fetch(self.info, True, strict) # at 1
                    assert self.info is not None

                self.value_flow = cs.load_ref()
                
                if rec_unpack:
                    self.value_flow = TLBComplex.constants["t_Ref_ValueFlow"].fetch(self.value_flow, True, strict) # at 1
                    assert self.value_flow is not None

                self.state_update = cs.load_ref()
                
                if rec_unpack:
                    self.state_update = TLBComplex.constants["t_Ref_MERKLE_UPDATE_ShardState"].fetch(self.state_update, True, strict) # at 1
                    assert self.state_update is not None

                self.extra = cs.load_ref()
                
                if rec_unpack:
                    self.extra = TLBComplex.constants["t_Ref_BlockExtra"].fetch(self.extra, True, strict) # at 1
                    assert self.extra is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Block")


# class for type `BlockExtra`
class BlockExtra(TLBComplex):
    class Tag(Enum):
        block_extra = 0

    cons_len_exact = 32
    cons_tag = [0x4a33f6fd]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockExtra.Tag.block_extra: BlockExtra.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockExtra.Tag"]:
        return BlockExtra.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockExtra.Tag.block_extra

        def get_tag(self):
            return BlockExtra.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockExtra.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockExtra.cons_len_exact, list) else BlockExtra.cons_len_exact

        def get_type_class(self):
            return BlockExtra

        # in_msg_descr : ^InMsgDescr
        in_msg_descr: "Cell" = None
        # out_msg_descr : ^OutMsgDescr
        out_msg_descr: "Cell" = None
        # account_blocks : ^ShardAccountBlocks
        account_blocks: "Cell" = None
        # rand_seed : bits256
        rand_seed: "bitstring.BitArray" = None
        # created_by : bits256
        created_by: "bitstring.BitArray" = None
        # custom : Maybe ^McBlockExtra
        custom: "CellSlice" = None

        def __init__(self, in_msg_descr: "Cell" = None, out_msg_descr: "Cell" = None, account_blocks: "Cell" = None, rand_seed: "bitstring.BitArray" = None, created_by: "bitstring.BitArray" = None, custom: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.in_msg_descr = in_msg_descr    
            self.field_names.append("in_msg_descr")
            self.out_msg_descr = out_msg_descr    
            self.field_names.append("out_msg_descr")
            self.account_blocks = account_blocks    
            self.field_names.append("account_blocks")
            self.rand_seed = rand_seed    
            self.field_names.append("rand_seed")
            self.created_by = created_by    
            self.field_names.append("created_by")
            self.custom = custom    
            self.field_names.append("custom")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x4a33f6fd, 'Cons tag check failed'

                self.in_msg_descr = cs.load_ref()
                
                if rec_unpack:
                    self.in_msg_descr = TLBComplex.constants["t_Ref_InMsgDescr"].fetch(self.in_msg_descr, True, strict) # at 1
                    assert self.in_msg_descr is not None

                self.out_msg_descr = cs.load_ref()
                
                if rec_unpack:
                    self.out_msg_descr = TLBComplex.constants["t_Ref_OutMsgDescr"].fetch(self.out_msg_descr, True, strict) # at 1
                    assert self.out_msg_descr is not None

                self.account_blocks = cs.load_ref()
                
                if rec_unpack:
                    self.account_blocks = TLBComplex.constants["t_Ref_ShardAccountBlocks"].fetch(self.account_blocks, True, strict) # at 1
                    assert self.account_blocks is not None

                self.rand_seed = cs.load_bitstring(256)
                self.created_by = cs.load_bitstring(256)
                self.custom = TLBComplex.constants["t_Maybe_Ref_McBlockExtra"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockExtra")


# class for auxiliary type `TYPE_1653`
class TYPE_1653(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TYPE_1653.Tag.cons1: TYPE_1653.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TYPE_1653.Tag"]:
        return TYPE_1653.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TYPE_1653.Tag.cons1

        def get_tag(self):
            return TYPE_1653.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TYPE_1653.cons_len_exact[self.get_tag_enum().value] if isinstance(TYPE_1653.cons_len_exact, list) else TYPE_1653.cons_len_exact

        def get_type_class(self):
            return TYPE_1653

        # from_prev_blk : CurrencyCollection
        from_prev_blk: "CellSlice" = None
        # to_next_blk : CurrencyCollection
        to_next_blk: "CellSlice" = None
        # imported : CurrencyCollection
        imported: "CellSlice" = None
        # exported : CurrencyCollection
        exported: "CellSlice" = None

        def __init__(self, from_prev_blk: "CellSlice" = None, to_next_blk: "CellSlice" = None, imported: "CellSlice" = None, exported: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.from_prev_blk = from_prev_blk    
            self.field_names.append("from_prev_blk")
            self.to_next_blk = to_next_blk    
            self.field_names.append("to_next_blk")
            self.imported = imported    
            self.field_names.append("imported")
            self.exported = exported    
            self.field_names.append("exported")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.from_prev_blk = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.to_next_blk = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.imported = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.exported = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TYPE_1653")


# class for auxiliary type `TYPE_1654`
class TYPE_1654(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TYPE_1654.Tag.cons1: TYPE_1654.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TYPE_1654.Tag"]:
        return TYPE_1654.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TYPE_1654.Tag.cons1

        def get_tag(self):
            return TYPE_1654.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TYPE_1654.cons_len_exact[self.get_tag_enum().value] if isinstance(TYPE_1654.cons_len_exact, list) else TYPE_1654.cons_len_exact

        def get_type_class(self):
            return TYPE_1654

        # fees_imported : CurrencyCollection
        fees_imported: "CellSlice" = None
        # recovered : CurrencyCollection
        recovered: "CellSlice" = None
        # created : CurrencyCollection
        created: "CellSlice" = None
        # minted : CurrencyCollection
        minted: "CellSlice" = None

        def __init__(self, fees_imported: "CellSlice" = None, recovered: "CellSlice" = None, created: "CellSlice" = None, minted: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.fees_imported = fees_imported    
            self.field_names.append("fees_imported")
            self.recovered = recovered    
            self.field_names.append("recovered")
            self.created = created    
            self.field_names.append("created")
            self.minted = minted    
            self.field_names.append("minted")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.fees_imported = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.recovered = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.created = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.minted = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TYPE_1654")


# class for type `ValueFlow`
class ValueFlow(TLBComplex):
    class Tag(Enum):
        value_flow_v2 = 0
        value_flow = 1

    cons_len_exact = 32
    cons_tag = [0x3ebf98b7, 0xb8e48dfb]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValueFlow.Tag.value_flow: ValueFlow.Record_value_flow, ValueFlow.Tag.value_flow_v2: ValueFlow.Record_value_flow_v2}

    def get_tag(self, cs: CellSlice) -> Optional["ValueFlow.Tag"]:
        return ValueFlow.Tag(int(cs.preload_uint(1)))


    class Record_value_flow(RecordBase):
        def get_tag_enum(self):
            return ValueFlow.Tag.value_flow

        def get_tag(self):
            return ValueFlow.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValueFlow.cons_len_exact[self.get_tag_enum().value] if isinstance(ValueFlow.cons_len_exact, list) else ValueFlow.cons_len_exact

        def get_type_class(self):
            return ValueFlow

        # ^[$_ from_prev_blk:CurrencyCollection to_next_blk:CurrencyCollection imported:CurrencyCollection exported:CurrencyCollection ]
        r1: "TYPE_1653.Record" = None
        # fees_collected : CurrencyCollection
        fees_collected: "CellSlice" = None
        # ^[$_ fees_imported:CurrencyCollection recovered:CurrencyCollection created:CurrencyCollection minted:CurrencyCollection ]
        r2: "TYPE_1654.Record" = None

        def __init__(self, r1: "TYPE_1653.Record" = None, fees_collected: "CellSlice" = None, r2: "TYPE_1654.Record" = None):
            super().__init__()
            self.field_names = []
            self.r1 = r1    
            self.field_names.append("r1")
            self.fees_collected = fees_collected    
            self.field_names.append("fees_collected")
            self.r2 = r2    
            self.field_names.append("r2")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0xb8e48dfb, 'Cons tag check failed'

                self.r1 = TLBComplex.constants["t_TYPE_1653"].fetch(cs.load_ref(), rec_unpack, strict)
                self.fees_collected = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.r2 = TLBComplex.constants["t_TYPE_1654"].fetch(cs.load_ref(), rec_unpack, strict)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_value_flow_v2(RecordBase):
        def get_tag_enum(self):
            return ValueFlow.Tag.value_flow_v2

        def get_tag(self):
            return ValueFlow.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValueFlow.cons_len_exact[self.get_tag_enum().value] if isinstance(ValueFlow.cons_len_exact, list) else ValueFlow.cons_len_exact

        def get_type_class(self):
            return ValueFlow

        # ^[$_ from_prev_blk:CurrencyCollection to_next_blk:CurrencyCollection imported:CurrencyCollection exported:CurrencyCollection ]
        r1: "TYPE_1653.Record" = None
        # fees_collected : CurrencyCollection
        fees_collected: "CellSlice" = None
        # burned : CurrencyCollection
        burned: "CellSlice" = None
        # ^[$_ fees_imported:CurrencyCollection recovered:CurrencyCollection created:CurrencyCollection minted:CurrencyCollection ]
        r2: "TYPE_1654.Record" = None

        def __init__(self, r1: "TYPE_1653.Record" = None, fees_collected: "CellSlice" = None, burned: "CellSlice" = None, r2: "TYPE_1654.Record" = None):
            super().__init__()
            self.field_names = []
            self.r1 = r1    
            self.field_names.append("r1")
            self.fees_collected = fees_collected    
            self.field_names.append("fees_collected")
            self.burned = burned    
            self.field_names.append("burned")
            self.r2 = r2    
            self.field_names.append("r2")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x3ebf98b7, 'Cons tag check failed'

                self.r1 = TLBComplex.constants["t_TYPE_1653"].fetch(cs.load_ref(), rec_unpack, strict)
                self.fees_collected = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.burned = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.r2 = TLBComplex.constants["t_TYPE_1654"].fetch(cs.load_ref(), rec_unpack, strict)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValueFlow")


# class for type `BinTree`
class BinTree(TLBComplex):
    class Tag(Enum):
        bt_leaf = 0
        bt_fork = 1

    cons_len_exact = 1
    cons_tag = [0, 1]

    X_: TLB = None

    def __init__(self, X_: TLB):
        super().__init__()
        self.X_ = X_
        self.params_attrs.append("X_")

        self.has_params = True

        self.tag_to_class = {BinTree.Tag.bt_leaf: self.get_param_record("Record_bt_leaf"), BinTree.Tag.bt_fork: self.get_param_record("Record_bt_fork")}

    def get_tag(self, cs: CellSlice) -> Optional["BinTree.Tag"]:
        return BinTree.Tag(int(cs.preload_uint(1)))


    class Record_bt_leaf(RecordBase):
        def get_tag_enum(self):
            return BinTree.Tag.bt_leaf

        def get_tag(self):
            return BinTree.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BinTree.cons_len_exact[self.get_tag_enum().value] if isinstance(BinTree.cons_len_exact, list) else BinTree.cons_len_exact

        def get_type_class(self):
            return BinTree

        # leaf : X
        leaf: "CellSlice" = None

        def __init__(self, leaf: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.leaf = leaf    
            self.field_names.append("leaf")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.leaf = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_bt_fork(RecordBase):
        def get_tag_enum(self):
            return BinTree.Tag.bt_fork

        def get_tag(self):
            return BinTree.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BinTree.cons_len_exact[self.get_tag_enum().value] if isinstance(BinTree.cons_len_exact, list) else BinTree.cons_len_exact

        def get_type_class(self):
            return BinTree

        # left : ^(BinTree X)
        left: "Cell" = None
        # right : ^(BinTree X)
        right: "Cell" = None

        def __init__(self, left: "Cell" = None, right: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.left = left    
            self.field_names.append("left")
            self.right = right    
            self.field_names.append("right")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = RefT(BinTree(self.X_)).fetch(self.left, True, strict) # at 1
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(BinTree(self.X_)).fetch(self.right, True, strict) # at 1
                    assert self.right is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BinTree")


# class for type `FutureSplitMerge`
class FutureSplitMerge(TLBComplex):
    class Tag(Enum):
        fsm_none = 0
        fsm_split = 1
        fsm_merge = 2

    cons_len = [1, 2, 2]
    cons_tag = [0, 2, 3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {FutureSplitMerge.Tag.fsm_none: FutureSplitMerge.Record_fsm_none, FutureSplitMerge.Tag.fsm_split: FutureSplitMerge.Record_fsm_split, FutureSplitMerge.Tag.fsm_merge: FutureSplitMerge.Record_fsm_merge}

    def get_tag(self, cs: CellSlice) -> Optional["FutureSplitMerge.Tag"]:
        return FutureSplitMerge.Tag(int(cs.bselect_ext(2, 13)))


    class Record_fsm_none(RecordBase):
        def get_tag_enum(self):
            return FutureSplitMerge.Tag.fsm_none

        def get_tag(self):
            return FutureSplitMerge.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return FutureSplitMerge.cons_len_exact[self.get_tag_enum().value] if isinstance(FutureSplitMerge.cons_len_exact, list) else FutureSplitMerge.cons_len_exact

        def get_type_class(self):
            return FutureSplitMerge


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_fsm_split(RecordBase):
        def get_tag_enum(self):
            return FutureSplitMerge.Tag.fsm_split

        def get_tag(self):
            return FutureSplitMerge.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return FutureSplitMerge.cons_len_exact[self.get_tag_enum().value] if isinstance(FutureSplitMerge.cons_len_exact, list) else FutureSplitMerge.cons_len_exact

        def get_type_class(self):
            return FutureSplitMerge

        # split_utime : uint32
        split_utime: "int" = None
        # interval : uint32
        interval: "int" = None

        def __init__(self, split_utime: "int" = None, interval: "int" = None):
            super().__init__()
            self.field_names = []
            self.split_utime = split_utime    
            self.field_names.append("split_utime")
            self.interval = interval    
            self.field_names.append("interval")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 2, 'Cons tag check failed'

                self.split_utime = cs.load_uint(32)
                self.interval = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_fsm_merge(RecordBase):
        def get_tag_enum(self):
            return FutureSplitMerge.Tag.fsm_merge

        def get_tag(self):
            return FutureSplitMerge.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return FutureSplitMerge.cons_len_exact[self.get_tag_enum().value] if isinstance(FutureSplitMerge.cons_len_exact, list) else FutureSplitMerge.cons_len_exact

        def get_type_class(self):
            return FutureSplitMerge

        # merge_utime : uint32
        merge_utime: "int" = None
        # interval : uint32
        interval: "int" = None

        def __init__(self, merge_utime: "int" = None, interval: "int" = None):
            super().__init__()
            self.field_names = []
            self.merge_utime = merge_utime    
            self.field_names.append("merge_utime")
            self.interval = interval    
            self.field_names.append("interval")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 3, 'Cons tag check failed'

                self.merge_utime = cs.load_uint(32)
                self.interval = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("FutureSplitMerge")


# class for auxiliary type `ShardDescr_aux`
class ShardDescr_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardDescr_aux.Tag.cons1: ShardDescr_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardDescr_aux.Tag"]:
        return ShardDescr_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardDescr_aux.Tag.cons1

        def get_tag(self):
            return ShardDescr_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardDescr_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardDescr_aux.cons_len_exact, list) else ShardDescr_aux.cons_len_exact

        def get_type_class(self):
            return ShardDescr_aux

        # fees_collected : CurrencyCollection
        fees_collected: "CellSlice" = None
        # funds_created : CurrencyCollection
        funds_created: "CellSlice" = None

        def __init__(self, fees_collected: "CellSlice" = None, funds_created: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.fees_collected = fees_collected    
            self.field_names.append("fees_collected")
            self.funds_created = funds_created    
            self.field_names.append("funds_created")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.fees_collected = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.funds_created = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardDescr_aux")


# class for type `ShardDescr`
class ShardDescr(TLBComplex):
    class Tag(Enum):
        shard_descr_new = 0
        shard_descr = 1

    cons_len_exact = 4
    cons_tag = [10, 11]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardDescr.Tag.shard_descr: ShardDescr.Record_shard_descr, ShardDescr.Tag.shard_descr_new: ShardDescr.Record_shard_descr_new}

    def get_tag(self, cs: CellSlice) -> Optional["ShardDescr.Tag"]:
        return ShardDescr.Tag(int(cs.bselect(4, 0xc00)))


    class Record_shard_descr(RecordBase):
        def get_tag_enum(self):
            return ShardDescr.Tag.shard_descr

        def get_tag(self):
            return ShardDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardDescr.cons_len_exact, list) else ShardDescr.cons_len_exact

        def get_type_class(self):
            return ShardDescr

        # seq_no : uint32
        seq_no: "int" = None
        # reg_mc_seqno : uint32
        reg_mc_seqno: "int" = None
        # start_lt : uint64
        start_lt: "int" = None
        # end_lt : uint64
        end_lt: "int" = None
        # root_hash : bits256
        root_hash: "bitstring.BitArray" = None
        # file_hash : bits256
        file_hash: "bitstring.BitArray" = None
        # before_split : Bool
        before_split: "bool" = None
        # before_merge : Bool
        before_merge: "bool" = None
        # want_split : Bool
        want_split: "bool" = None
        # want_merge : Bool
        want_merge: "bool" = None
        # nx_cc_updated : Bool
        nx_cc_updated: "bool" = None
        # flags : ## 3
        flags: "int" = None
        # next_catchain_seqno : uint32
        next_catchain_seqno: "int" = None
        # next_validator_shard : uint64
        next_validator_shard: "int" = None
        # min_ref_mc_seqno : uint32
        min_ref_mc_seqno: "int" = None
        # gen_utime : uint32
        gen_utime: "int" = None
        # split_merge_at : FutureSplitMerge
        split_merge_at: "CellSlice" = None
        # fees_collected : CurrencyCollection
        fees_collected: "CellSlice" = None
        # funds_created : CurrencyCollection
        funds_created: "CellSlice" = None

        def __init__(self, seq_no: "int" = None, reg_mc_seqno: "int" = None, start_lt: "int" = None, end_lt: "int" = None, root_hash: "bitstring.BitArray" = None, file_hash: "bitstring.BitArray" = None, before_split: "bool" = None, before_merge: "bool" = None, want_split: "bool" = None, want_merge: "bool" = None, nx_cc_updated: "bool" = None, flags: "int" = None, next_catchain_seqno: "int" = None, next_validator_shard: "int" = None, min_ref_mc_seqno: "int" = None, gen_utime: "int" = None, split_merge_at: "CellSlice" = None, fees_collected: "CellSlice" = None, funds_created: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.seq_no = seq_no    
            self.field_names.append("seq_no")
            self.reg_mc_seqno = reg_mc_seqno    
            self.field_names.append("reg_mc_seqno")
            self.start_lt = start_lt    
            self.field_names.append("start_lt")
            self.end_lt = end_lt    
            self.field_names.append("end_lt")
            self.root_hash = root_hash    
            self.field_names.append("root_hash")
            self.file_hash = file_hash    
            self.field_names.append("file_hash")
            self.before_split = before_split    
            self.field_names.append("before_split")
            self.before_merge = before_merge    
            self.field_names.append("before_merge")
            self.want_split = want_split    
            self.field_names.append("want_split")
            self.want_merge = want_merge    
            self.field_names.append("want_merge")
            self.nx_cc_updated = nx_cc_updated    
            self.field_names.append("nx_cc_updated")
            self.flags = flags    
            self.field_names.append("flags")
            self.next_catchain_seqno = next_catchain_seqno    
            self.field_names.append("next_catchain_seqno")
            self.next_validator_shard = next_validator_shard    
            self.field_names.append("next_validator_shard")
            self.min_ref_mc_seqno = min_ref_mc_seqno    
            self.field_names.append("min_ref_mc_seqno")
            self.gen_utime = gen_utime    
            self.field_names.append("gen_utime")
            self.split_merge_at = split_merge_at    
            self.field_names.append("split_merge_at")
            self.fees_collected = fees_collected    
            self.field_names.append("fees_collected")
            self.funds_created = funds_created    
            self.field_names.append("funds_created")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 11, 'Cons tag check failed'

                self.seq_no = cs.load_uint(32)
                self.reg_mc_seqno = cs.load_uint(32)
                self.start_lt = cs.load_uint(64)
                self.end_lt = cs.load_uint(64)
                self.root_hash = cs.load_bitstring(256)
                self.file_hash = cs.load_bitstring(256)
                self.before_split = cs.load_bool()
                self.before_merge = cs.load_bool()
                self.want_split = cs.load_bool()
                self.want_merge = cs.load_bool()
                self.nx_cc_updated = cs.load_bool()
                self.flags = cs.load_uint(3)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.next_catchain_seqno = cs.load_uint(32)
                self.next_validator_shard = cs.load_uint(64)
                self.min_ref_mc_seqno = cs.load_uint(32)
                self.gen_utime = cs.load_uint(32)
                self.split_merge_at = TLBComplex.constants["t_FutureSplitMerge"].fetch(cs) 
                self.fees_collected = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.funds_created = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_shard_descr_new(RecordBase):
        def get_tag_enum(self):
            return ShardDescr.Tag.shard_descr_new

        def get_tag(self):
            return ShardDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardDescr.cons_len_exact, list) else ShardDescr.cons_len_exact

        def get_type_class(self):
            return ShardDescr

        # seq_no : uint32
        seq_no: "int" = None
        # reg_mc_seqno : uint32
        reg_mc_seqno: "int" = None
        # start_lt : uint64
        start_lt: "int" = None
        # end_lt : uint64
        end_lt: "int" = None
        # root_hash : bits256
        root_hash: "bitstring.BitArray" = None
        # file_hash : bits256
        file_hash: "bitstring.BitArray" = None
        # before_split : Bool
        before_split: "bool" = None
        # before_merge : Bool
        before_merge: "bool" = None
        # want_split : Bool
        want_split: "bool" = None
        # want_merge : Bool
        want_merge: "bool" = None
        # nx_cc_updated : Bool
        nx_cc_updated: "bool" = None
        # flags : ## 3
        flags: "int" = None
        # next_catchain_seqno : uint32
        next_catchain_seqno: "int" = None
        # next_validator_shard : uint64
        next_validator_shard: "int" = None
        # min_ref_mc_seqno : uint32
        min_ref_mc_seqno: "int" = None
        # gen_utime : uint32
        gen_utime: "int" = None
        # split_merge_at : FutureSplitMerge
        split_merge_at: "CellSlice" = None
        # ^[$_ fees_collected:CurrencyCollection funds_created:CurrencyCollection ]
        r1: "ShardDescr_aux.Record" = None

        def __init__(self, seq_no: "int" = None, reg_mc_seqno: "int" = None, start_lt: "int" = None, end_lt: "int" = None, root_hash: "bitstring.BitArray" = None, file_hash: "bitstring.BitArray" = None, before_split: "bool" = None, before_merge: "bool" = None, want_split: "bool" = None, want_merge: "bool" = None, nx_cc_updated: "bool" = None, flags: "int" = None, next_catchain_seqno: "int" = None, next_validator_shard: "int" = None, min_ref_mc_seqno: "int" = None, gen_utime: "int" = None, split_merge_at: "CellSlice" = None, r1: "ShardDescr_aux.Record" = None):
            super().__init__()
            self.field_names = []
            self.seq_no = seq_no    
            self.field_names.append("seq_no")
            self.reg_mc_seqno = reg_mc_seqno    
            self.field_names.append("reg_mc_seqno")
            self.start_lt = start_lt    
            self.field_names.append("start_lt")
            self.end_lt = end_lt    
            self.field_names.append("end_lt")
            self.root_hash = root_hash    
            self.field_names.append("root_hash")
            self.file_hash = file_hash    
            self.field_names.append("file_hash")
            self.before_split = before_split    
            self.field_names.append("before_split")
            self.before_merge = before_merge    
            self.field_names.append("before_merge")
            self.want_split = want_split    
            self.field_names.append("want_split")
            self.want_merge = want_merge    
            self.field_names.append("want_merge")
            self.nx_cc_updated = nx_cc_updated    
            self.field_names.append("nx_cc_updated")
            self.flags = flags    
            self.field_names.append("flags")
            self.next_catchain_seqno = next_catchain_seqno    
            self.field_names.append("next_catchain_seqno")
            self.next_validator_shard = next_validator_shard    
            self.field_names.append("next_validator_shard")
            self.min_ref_mc_seqno = min_ref_mc_seqno    
            self.field_names.append("min_ref_mc_seqno")
            self.gen_utime = gen_utime    
            self.field_names.append("gen_utime")
            self.split_merge_at = split_merge_at    
            self.field_names.append("split_merge_at")
            self.r1 = r1    
            self.field_names.append("r1")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 10, 'Cons tag check failed'

                self.seq_no = cs.load_uint(32)
                self.reg_mc_seqno = cs.load_uint(32)
                self.start_lt = cs.load_uint(64)
                self.end_lt = cs.load_uint(64)
                self.root_hash = cs.load_bitstring(256)
                self.file_hash = cs.load_bitstring(256)
                self.before_split = cs.load_bool()
                self.before_merge = cs.load_bool()
                self.want_split = cs.load_bool()
                self.want_merge = cs.load_bool()
                self.nx_cc_updated = cs.load_bool()
                self.flags = cs.load_uint(3)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.next_catchain_seqno = cs.load_uint(32)
                self.next_validator_shard = cs.load_uint(64)
                self.min_ref_mc_seqno = cs.load_uint(32)
                self.gen_utime = cs.load_uint(32)
                self.split_merge_at = TLBComplex.constants["t_FutureSplitMerge"].fetch(cs) 
                self.r1 = TLBComplex.constants["t_ShardDescr_aux"].fetch(cs.load_ref(), rec_unpack, strict)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardDescr")


# class for type `ShardHashes`
class ShardHashes(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardHashes.Tag.cons1: ShardHashes.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardHashes.Tag"]:
        return ShardHashes.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardHashes.Tag.cons1

        def get_tag(self):
            return ShardHashes.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardHashes.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardHashes.cons_len_exact, list) else ShardHashes.cons_len_exact

        def get_type_class(self):
            return ShardHashes

        # HashmapE 32 ^(BinTree ShardDescr)
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapE_32_Ref_BinTree_ShardDescr"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardHashes")


# class for type `BinTreeAug`
class BinTreeAug(TLBComplex):
    class Tag(Enum):
        bta_leaf = 0
        bta_fork = 1

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

        self.tag_to_class = {BinTreeAug.Tag.bta_leaf: self.get_param_record("Record_bta_leaf"), BinTreeAug.Tag.bta_fork: self.get_param_record("Record_bta_fork")}

    def get_tag(self, cs: CellSlice) -> Optional["BinTreeAug.Tag"]:
        return BinTreeAug.Tag(int(cs.preload_uint(1)))


    class Record_bta_leaf(RecordBase):
        def get_tag_enum(self):
            return BinTreeAug.Tag.bta_leaf

        def get_tag(self):
            return BinTreeAug.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BinTreeAug.cons_len_exact[self.get_tag_enum().value] if isinstance(BinTreeAug.cons_len_exact, list) else BinTreeAug.cons_len_exact

        def get_type_class(self):
            return BinTreeAug

        # extra : Y
        extra: "CellSlice" = None
        # leaf : X
        leaf: "CellSlice" = None

        def __init__(self, extra: "CellSlice" = None, leaf: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.extra = extra    
            self.field_names.append("extra")
            self.leaf = leaf    
            self.field_names.append("leaf")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'

                self.extra = self.Y_.fetch(cs) 
                self.leaf = self.X_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_bta_fork(RecordBase):
        def get_tag_enum(self):
            return BinTreeAug.Tag.bta_fork

        def get_tag(self):
            return BinTreeAug.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BinTreeAug.cons_len_exact[self.get_tag_enum().value] if isinstance(BinTreeAug.cons_len_exact, list) else BinTreeAug.cons_len_exact

        def get_type_class(self):
            return BinTreeAug

        # left : ^(BinTreeAug X Y)
        left: "Cell" = None
        # right : ^(BinTreeAug X Y)
        right: "Cell" = None
        # extra : Y
        extra: "CellSlice" = None

        def __init__(self, left: "Cell" = None, right: "Cell" = None, extra: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.left = left    
            self.field_names.append("left")
            self.right = right    
            self.field_names.append("right")
            self.extra = extra    
            self.field_names.append("extra")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.left = cs.load_ref()
                
                if rec_unpack:
                    self.left = RefT(BinTreeAug(self.X_, self.Y_)).fetch(self.left, True, strict) # at 1
                    assert self.left is not None

                self.right = cs.load_ref()
                
                if rec_unpack:
                    self.right = RefT(BinTreeAug(self.X_, self.Y_)).fetch(self.right, True, strict) # at 1
                    assert self.right is not None

                self.extra = self.Y_.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BinTreeAug")


# class for type `ShardFeeCreated`
class ShardFeeCreated(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardFeeCreated.Tag.cons1: ShardFeeCreated.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardFeeCreated.Tag"]:
        return ShardFeeCreated.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardFeeCreated.Tag.cons1

        def get_tag(self):
            return ShardFeeCreated.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardFeeCreated.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardFeeCreated.cons_len_exact, list) else ShardFeeCreated.cons_len_exact

        def get_type_class(self):
            return ShardFeeCreated

        # fees : CurrencyCollection
        fees: "CellSlice" = None
        # create : CurrencyCollection
        create: "CellSlice" = None

        def __init__(self, fees: "CellSlice" = None, create: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.fees = fees    
            self.field_names.append("fees")
            self.create = create    
            self.field_names.append("create")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.fees = TLBComplex.constants["t_CurrencyCollection"].fetch(cs) 
                self.create = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardFeeCreated")


# class for type `ShardFees`
class ShardFees(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ShardFees.Tag.cons1: ShardFees.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ShardFees.Tag"]:
        return ShardFees.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ShardFees.Tag.cons1

        def get_tag(self):
            return ShardFees.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ShardFees.cons_len_exact[self.get_tag_enum().value] if isinstance(ShardFees.cons_len_exact, list) else ShardFees.cons_len_exact

        def get_type_class(self):
            return ShardFees

        # HashmapAugE 96 ShardFeeCreated ShardFeeCreated
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_96_ShardFeeCreated_ShardFeeCreated"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ShardFees")


# class for type `ConfigParams`
class ConfigParams(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ConfigParams.Tag.cons1: ConfigParams.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ConfigParams.Tag"]:
        return ConfigParams.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ConfigParams.Tag.cons1

        def get_tag(self):
            return ConfigParams.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParams.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParams.cons_len_exact, list) else ConfigParams.cons_len_exact

        def get_type_class(self):
            return ConfigParams

        # config_addr : bits256
        config_addr: "bitstring.BitArray" = None
        # config : ^(Hashmap 32 ^Cell)
        config: "Cell" = None

        def __init__(self, config_addr: "bitstring.BitArray" = None, config: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.config_addr = config_addr    
            self.field_names.append("config_addr")
            self.config = config    
            self.field_names.append("config")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.config_addr = cs.load_bitstring(256)
                self.config = cs.load_ref()
                
                if rec_unpack:
                    self.config = TLBComplex.constants["t_Ref_Hashmap_32_Ref_Cell"].fetch(self.config, True, strict) # at 1
                    assert self.config is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConfigParams")


# class for type `ValidatorInfo`
class ValidatorInfo(TLBComplex):
    class Tag(Enum):
        validator_info = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorInfo.Tag.validator_info: ValidatorInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorInfo.Tag"]:
        return ValidatorInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ValidatorInfo.Tag.validator_info

        def get_tag(self):
            return ValidatorInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorInfo.cons_len_exact, list) else ValidatorInfo.cons_len_exact

        def get_type_class(self):
            return ValidatorInfo

        # validator_list_hash_short : uint32
        validator_list_hash_short: "int" = None
        # catchain_seqno : uint32
        catchain_seqno: "int" = None
        # nx_cc_updated : Bool
        nx_cc_updated: "bool" = None

        def __init__(self, validator_list_hash_short: "int" = None, catchain_seqno: "int" = None, nx_cc_updated: "bool" = None):
            super().__init__()
            self.field_names = []
            self.validator_list_hash_short = validator_list_hash_short    
            self.field_names.append("validator_list_hash_short")
            self.catchain_seqno = catchain_seqno    
            self.field_names.append("catchain_seqno")
            self.nx_cc_updated = nx_cc_updated    
            self.field_names.append("nx_cc_updated")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.validator_list_hash_short = cs.load_uint(32)
                self.catchain_seqno = cs.load_uint(32)
                self.nx_cc_updated = cs.load_bool()                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorInfo")


# class for type `ValidatorBaseInfo`
class ValidatorBaseInfo(TLBComplex):
    class Tag(Enum):
        validator_base_info = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorBaseInfo.Tag.validator_base_info: ValidatorBaseInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorBaseInfo.Tag"]:
        return ValidatorBaseInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ValidatorBaseInfo.Tag.validator_base_info

        def get_tag(self):
            return ValidatorBaseInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorBaseInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorBaseInfo.cons_len_exact, list) else ValidatorBaseInfo.cons_len_exact

        def get_type_class(self):
            return ValidatorBaseInfo

        # validator_list_hash_short : uint32
        validator_list_hash_short: "int" = None
        # catchain_seqno : uint32
        catchain_seqno: "int" = None

        def __init__(self, validator_list_hash_short: "int" = None, catchain_seqno: "int" = None):
            super().__init__()
            self.field_names = []
            self.validator_list_hash_short = validator_list_hash_short    
            self.field_names.append("validator_list_hash_short")
            self.catchain_seqno = catchain_seqno    
            self.field_names.append("catchain_seqno")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.validator_list_hash_short = cs.load_uint(32)
                self.catchain_seqno = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorBaseInfo")


# class for type `KeyMaxLt`
class KeyMaxLt(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {KeyMaxLt.Tag.cons1: KeyMaxLt.Record}

    def get_tag(self, cs: CellSlice) -> Optional["KeyMaxLt.Tag"]:
        return KeyMaxLt.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return KeyMaxLt.Tag.cons1

        def get_tag(self):
            return KeyMaxLt.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return KeyMaxLt.cons_len_exact[self.get_tag_enum().value] if isinstance(KeyMaxLt.cons_len_exact, list) else KeyMaxLt.cons_len_exact

        def get_type_class(self):
            return KeyMaxLt

        # key : Bool
        key: "bool" = None
        # max_end_lt : uint64
        max_end_lt: "int" = None

        def __init__(self, key: "bool" = None, max_end_lt: "int" = None):
            super().__init__()
            self.field_names = []
            self.key = key    
            self.field_names.append("key")
            self.max_end_lt = max_end_lt    
            self.field_names.append("max_end_lt")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.key = cs.load_bool()
                self.max_end_lt = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("KeyMaxLt")


# class for type `KeyExtBlkRef`
class KeyExtBlkRef(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {KeyExtBlkRef.Tag.cons1: KeyExtBlkRef.Record}

    def get_tag(self, cs: CellSlice) -> Optional["KeyExtBlkRef.Tag"]:
        return KeyExtBlkRef.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return KeyExtBlkRef.Tag.cons1

        def get_tag(self):
            return KeyExtBlkRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return KeyExtBlkRef.cons_len_exact[self.get_tag_enum().value] if isinstance(KeyExtBlkRef.cons_len_exact, list) else KeyExtBlkRef.cons_len_exact

        def get_type_class(self):
            return KeyExtBlkRef

        # key : Bool
        key: "bool" = None
        # blk_ref : ExtBlkRef
        blk_ref: "CellSlice" = None

        def __init__(self, key: "bool" = None, blk_ref: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.key = key    
            self.field_names.append("key")
            self.blk_ref = blk_ref    
            self.field_names.append("blk_ref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.key = cs.load_bool()
                self.blk_ref = cs.load_subslice(608)
                
                if rec_unpack:
                    self.blk_ref = TLBComplex.constants["t_ExtBlkRef"].fetch(self.blk_ref, True, strict) # at 1
                    assert self.blk_ref is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("KeyExtBlkRef")


# class for type `OldMcBlocksInfo`
class OldMcBlocksInfo(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OldMcBlocksInfo.Tag.cons1: OldMcBlocksInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["OldMcBlocksInfo.Tag"]:
        return OldMcBlocksInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return OldMcBlocksInfo.Tag.cons1

        def get_tag(self):
            return OldMcBlocksInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OldMcBlocksInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(OldMcBlocksInfo.cons_len_exact, list) else OldMcBlocksInfo.cons_len_exact

        def get_type_class(self):
            return OldMcBlocksInfo

        # HashmapAugE 32 KeyExtBlkRef KeyMaxLt
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapAugE_32_KeyExtBlkRef_KeyMaxLt"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OldMcBlocksInfo")


# class for type `Counters`
class Counters(TLBComplex):
    class Tag(Enum):
        counters = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Counters.Tag.counters: Counters.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Counters.Tag"]:
        return Counters.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Counters.Tag.counters

        def get_tag(self):
            return Counters.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Counters.cons_len_exact[self.get_tag_enum().value] if isinstance(Counters.cons_len_exact, list) else Counters.cons_len_exact

        def get_type_class(self):
            return Counters

        # last_updated : uint32
        last_updated: "int" = None
        # total : uint64
        total: "int" = None
        # cnt2048 : uint64
        cnt2048: "int" = None
        # cnt65536 : uint64
        cnt65536: "int" = None

        def __init__(self, last_updated: "int" = None, total: "int" = None, cnt2048: "int" = None, cnt65536: "int" = None):
            super().__init__()
            self.field_names = []
            self.last_updated = last_updated    
            self.field_names.append("last_updated")
            self.total = total    
            self.field_names.append("total")
            self.cnt2048 = cnt2048    
            self.field_names.append("cnt2048")
            self.cnt65536 = cnt65536    
            self.field_names.append("cnt65536")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.last_updated = cs.load_uint(32)
                self.total = cs.load_uint(64)
                self.cnt2048 = cs.load_uint(64)
                self.cnt65536 = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Counters")


# class for type `CreatorStats`
class CreatorStats(TLBComplex):
    class Tag(Enum):
        creator_info = 0

    cons_len_exact = 4
    cons_tag = [4]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CreatorStats.Tag.creator_info: CreatorStats.Record}

    def get_tag(self, cs: CellSlice) -> Optional["CreatorStats.Tag"]:
        return CreatorStats.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return CreatorStats.Tag.creator_info

        def get_tag(self):
            return CreatorStats.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CreatorStats.cons_len_exact[self.get_tag_enum().value] if isinstance(CreatorStats.cons_len_exact, list) else CreatorStats.cons_len_exact

        def get_type_class(self):
            return CreatorStats

        # mc_blocks : Counters
        mc_blocks: "CellSlice" = None
        # shard_blocks : Counters
        shard_blocks: "CellSlice" = None

        def __init__(self, mc_blocks: "CellSlice" = None, shard_blocks: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.mc_blocks = mc_blocks    
            self.field_names.append("mc_blocks")
            self.shard_blocks = shard_blocks    
            self.field_names.append("shard_blocks")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 4, 'Cons tag check failed'

                self.mc_blocks = cs.load_subslice(224)
                
                if rec_unpack:
                    self.mc_blocks = TLBComplex.constants["t_Counters"].fetch(self.mc_blocks, True, strict) # at 1
                    assert self.mc_blocks is not None

                self.shard_blocks = cs.load_subslice(224)
                
                if rec_unpack:
                    self.shard_blocks = TLBComplex.constants["t_Counters"].fetch(self.shard_blocks, True, strict) # at 1
                    assert self.shard_blocks is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CreatorStats")


# class for type `BlockCreateStats`
class BlockCreateStats(TLBComplex):
    class Tag(Enum):
        block_create_stats = 0
        block_create_stats_ext = 1

    cons_len_exact = 8
    cons_tag = [23, 0x34]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockCreateStats.Tag.block_create_stats: BlockCreateStats.Record_block_create_stats, BlockCreateStats.Tag.block_create_stats_ext: BlockCreateStats.Record_block_create_stats_ext}

    def get_tag(self, cs: CellSlice) -> Optional["BlockCreateStats.Tag"]:
        return BlockCreateStats.Tag(int(cs.bselect(3, 3)))


    class Record_block_create_stats(RecordBase):
        def get_tag_enum(self):
            return BlockCreateStats.Tag.block_create_stats

        def get_tag(self):
            return BlockCreateStats.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockCreateStats.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockCreateStats.cons_len_exact, list) else BlockCreateStats.cons_len_exact

        def get_type_class(self):
            return BlockCreateStats

        # counters : HashmapE 256 CreatorStats
        counters: "CellSlice" = None

        def __init__(self, counters: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.counters = counters    
            self.field_names.append("counters")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 23, 'Cons tag check failed'

                self.counters = TLBComplex.constants["t_HashmapE_256_CreatorStats"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_block_create_stats_ext(RecordBase):
        def get_tag_enum(self):
            return BlockCreateStats.Tag.block_create_stats_ext

        def get_tag(self):
            return BlockCreateStats.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockCreateStats.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockCreateStats.cons_len_exact, list) else BlockCreateStats.cons_len_exact

        def get_type_class(self):
            return BlockCreateStats

        # counters : HashmapAugE 256 CreatorStats uint32
        counters: "CellSlice" = None

        def __init__(self, counters: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.counters = counters    
            self.field_names.append("counters")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x34, 'Cons tag check failed'

                self.counters = TLBComplex.constants["t_HashmapAugE_256_CreatorStats_uint32"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockCreateStats")


# class for auxiliary type `McStateExtra_aux`
class McStateExtra_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {McStateExtra_aux.Tag.cons1: McStateExtra_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["McStateExtra_aux.Tag"]:
        return McStateExtra_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return McStateExtra_aux.Tag.cons1

        def get_tag(self):
            return McStateExtra_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return McStateExtra_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(McStateExtra_aux.cons_len_exact, list) else McStateExtra_aux.cons_len_exact

        def get_type_class(self):
            return McStateExtra_aux

        # flags : ## 16
        flags: "int" = None
        # validator_info : ValidatorInfo
        validator_info: "CellSlice" = None
        # prev_blocks : OldMcBlocksInfo
        prev_blocks: "CellSlice" = None
        # after_key_block : Bool
        after_key_block: "bool" = None
        # last_key_block : Maybe ExtBlkRef
        last_key_block: "CellSlice" = None
        # block_create_stats : flags.0?BlockCreateStats
        block_create_stats: "CellSlice" = None

        def __init__(self, flags: "int" = None, validator_info: "CellSlice" = None, prev_blocks: "CellSlice" = None, after_key_block: "bool" = None, last_key_block: "CellSlice" = None, block_create_stats: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.flags = flags    
            self.field_names.append("flags")
            self.validator_info = validator_info    
            self.field_names.append("validator_info")
            self.prev_blocks = prev_blocks    
            self.field_names.append("prev_blocks")
            self.after_key_block = after_key_block    
            self.field_names.append("after_key_block")
            self.last_key_block = last_key_block    
            self.field_names.append("last_key_block")
            self.block_create_stats = block_create_stats    
            self.conditional_fields.append("block_create_stats")    
            self.field_names.append("block_create_stats")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.flags = cs.load_uint(16)
                assert self.flags <= 1, 'Params not equal: flags and 1'

                self.validator_info = cs.load_subslice(65)
                
                if rec_unpack:
                    self.validator_info = TLBComplex.constants["t_ValidatorInfo"].fetch(self.validator_info, True, strict) # at 1
                    assert self.validator_info is not None

                self.prev_blocks = TLBComplex.constants["t_OldMcBlocksInfo"].fetch(cs) 
                self.after_key_block = cs.load_bool()
                self.last_key_block = TLBComplex.constants["t_Maybe_ExtBlkRef"].fetch(cs) 
                if ((self.flags & (1 << 0)) != 0):
                    self.block_create_stats = TLBComplex.constants["t_BlockCreateStats"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("McStateExtra_aux")


# class for type `McStateExtra`
class McStateExtra(TLBComplex):
    class Tag(Enum):
        masterchain_state_extra = 0

    cons_len_exact = 16
    cons_tag = [0xcc26]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {McStateExtra.Tag.masterchain_state_extra: McStateExtra.Record}

    def get_tag(self, cs: CellSlice) -> Optional["McStateExtra.Tag"]:
        return McStateExtra.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return McStateExtra.Tag.masterchain_state_extra

        def get_tag(self):
            return McStateExtra.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return McStateExtra.cons_len_exact[self.get_tag_enum().value] if isinstance(McStateExtra.cons_len_exact, list) else McStateExtra.cons_len_exact

        def get_type_class(self):
            return McStateExtra

        # shard_hashes : ShardHashes
        shard_hashes: "CellSlice" = None
        # config : ConfigParams
        config: "CellSlice" = None
        # ^[$_ flags:(## 16) {<= flags 1} validator_info:ValidatorInfo prev_blocks:OldMcBlocksInfo after_key_block:Bool last_key_block:(Maybe ExtBlkRef) block_create_stats:flags.0?BlockCreateStats ]
        r1: "McStateExtra_aux.Record" = None
        # global_balance : CurrencyCollection
        global_balance: "CellSlice" = None

        def __init__(self, shard_hashes: "CellSlice" = None, config: "CellSlice" = None, r1: "McStateExtra_aux.Record" = None, global_balance: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.shard_hashes = shard_hashes    
            self.field_names.append("shard_hashes")
            self.config = config    
            self.field_names.append("config")
            self.r1 = r1    
            self.field_names.append("r1")
            self.global_balance = global_balance    
            self.field_names.append("global_balance")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0xcc26, 'Cons tag check failed'

                self.shard_hashes = TLBComplex.constants["t_ShardHashes"].fetch(cs) 
                self.config = cs.load_subslice_ext(0x10100)
                
                if rec_unpack:
                    self.config = TLBComplex.constants["t_ConfigParams"].fetch(self.config, True, strict) # at 1
                    assert self.config is not None

                self.r1 = TLBComplex.constants["t_McStateExtra_aux"].fetch(cs.load_ref(), rec_unpack, strict)
                self.global_balance = TLBComplex.constants["t_CurrencyCollection"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("McStateExtra")


# class for type `SigPubKey`
class SigPubKey(TLBComplex):
    class Tag(Enum):
        ed25519_pubkey = 0

    cons_len_exact = 32
    cons_tag = [0x8e81278a]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SigPubKey.Tag.ed25519_pubkey: SigPubKey.Record}

    def get_tag(self, cs: CellSlice) -> Optional["SigPubKey.Tag"]:
        return SigPubKey.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return SigPubKey.Tag.ed25519_pubkey

        def get_tag(self):
            return SigPubKey.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SigPubKey.cons_len_exact[self.get_tag_enum().value] if isinstance(SigPubKey.cons_len_exact, list) else SigPubKey.cons_len_exact

        def get_type_class(self):
            return SigPubKey

        # pubkey : bits256
        pubkey: "bitstring.BitArray" = None

        def __init__(self, pubkey: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.pubkey = pubkey    
            self.field_names.append("pubkey")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x8e81278a, 'Cons tag check failed'

                self.pubkey = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SigPubKey")


# class for type `CryptoSignatureSimple`
class CryptoSignatureSimple(TLBComplex):
    class Tag(Enum):
        ed25519_signature = 0

    cons_len_exact = 4
    cons_tag = [5]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CryptoSignatureSimple.Tag.ed25519_signature: CryptoSignatureSimple.Record}

    def get_tag(self, cs: CellSlice) -> Optional["CryptoSignatureSimple.Tag"]:
        return CryptoSignatureSimple.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return CryptoSignatureSimple.Tag.ed25519_signature

        def get_tag(self):
            return CryptoSignatureSimple.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CryptoSignatureSimple.cons_len_exact[self.get_tag_enum().value] if isinstance(CryptoSignatureSimple.cons_len_exact, list) else CryptoSignatureSimple.cons_len_exact

        def get_type_class(self):
            return CryptoSignatureSimple

        # R : bits256
        R: "bitstring.BitArray" = None
        # s : bits256
        s: "bitstring.BitArray" = None

        def __init__(self, R: "bitstring.BitArray" = None, s: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.R = R    
            self.field_names.append("R")
            self.s = s    
            self.field_names.append("s")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 5, 'Cons tag check failed'

                self.R = cs.load_bitstring(256)
                self.s = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CryptoSignatureSimple")


# class for type `CryptoSignaturePair`
class CryptoSignaturePair(TLBComplex):
    class Tag(Enum):
        sig_pair = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CryptoSignaturePair.Tag.sig_pair: CryptoSignaturePair.Record}

    def get_tag(self, cs: CellSlice) -> Optional["CryptoSignaturePair.Tag"]:
        return CryptoSignaturePair.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return CryptoSignaturePair.Tag.sig_pair

        def get_tag(self):
            return CryptoSignaturePair.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CryptoSignaturePair.cons_len_exact[self.get_tag_enum().value] if isinstance(CryptoSignaturePair.cons_len_exact, list) else CryptoSignaturePair.cons_len_exact

        def get_type_class(self):
            return CryptoSignaturePair

        # node_id_short : bits256
        node_id_short: "bitstring.BitArray" = None
        # sign : CryptoSignature
        sign: "CellSlice" = None

        def __init__(self, node_id_short: "bitstring.BitArray" = None, sign: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.node_id_short = node_id_short    
            self.field_names.append("node_id_short")
            self.sign = sign    
            self.field_names.append("sign")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.node_id_short = cs.load_bitstring(256)
                self.sign = TLBComplex.constants["t_CryptoSignature"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CryptoSignaturePair")


# class for type `Certificate`
class Certificate(TLBComplex):
    class Tag(Enum):
        certificate = 0

    cons_len_exact = 4
    cons_tag = [4]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Certificate.Tag.certificate: Certificate.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Certificate.Tag"]:
        return Certificate.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Certificate.Tag.certificate

        def get_tag(self):
            return Certificate.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Certificate.cons_len_exact[self.get_tag_enum().value] if isinstance(Certificate.cons_len_exact, list) else Certificate.cons_len_exact

        def get_type_class(self):
            return Certificate

        # temp_key : SigPubKey
        temp_key: "CellSlice" = None
        # valid_since : uint32
        valid_since: "int" = None
        # valid_until : uint32
        valid_until: "int" = None

        def __init__(self, temp_key: "CellSlice" = None, valid_since: "int" = None, valid_until: "int" = None):
            super().__init__()
            self.field_names = []
            self.temp_key = temp_key    
            self.field_names.append("temp_key")
            self.valid_since = valid_since    
            self.field_names.append("valid_since")
            self.valid_until = valid_until    
            self.field_names.append("valid_until")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 4, 'Cons tag check failed'

                self.temp_key = cs.load_subslice(288)
                
                if rec_unpack:
                    self.temp_key = TLBComplex.constants["t_SigPubKey"].fetch(self.temp_key, True, strict) # at 1
                    assert self.temp_key is not None

                self.valid_since = cs.load_uint(32)
                self.valid_until = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Certificate")


# class for type `CertificateEnv`
class CertificateEnv(TLBComplex):
    class Tag(Enum):
        certificate_env = 0

    cons_len_exact = 28
    cons_tag = [0xa419b7d]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CertificateEnv.Tag.certificate_env: CertificateEnv.Record}

    def get_tag(self, cs: CellSlice) -> Optional["CertificateEnv.Tag"]:
        return CertificateEnv.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return CertificateEnv.Tag.certificate_env

        def get_tag(self):
            return CertificateEnv.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CertificateEnv.cons_len_exact[self.get_tag_enum().value] if isinstance(CertificateEnv.cons_len_exact, list) else CertificateEnv.cons_len_exact

        def get_type_class(self):
            return CertificateEnv

        # certificate : Certificate
        certificate: "CellSlice" = None

        def __init__(self, certificate: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.certificate = certificate    
            self.field_names.append("certificate")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(28) == 0xa419b7d, 'Cons tag check failed'

                self.certificate = cs.load_subslice(356)
                
                if rec_unpack:
                    self.certificate = TLBComplex.constants["t_Certificate"].fetch(self.certificate, True, strict) # at 1
                    assert self.certificate is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CertificateEnv")


# class for type `SignedCertificate`
class SignedCertificate(TLBComplex):
    class Tag(Enum):
        signed_certificate = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SignedCertificate.Tag.signed_certificate: SignedCertificate.Record}

    def get_tag(self, cs: CellSlice) -> Optional["SignedCertificate.Tag"]:
        return SignedCertificate.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return SignedCertificate.Tag.signed_certificate

        def get_tag(self):
            return SignedCertificate.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SignedCertificate.cons_len_exact[self.get_tag_enum().value] if isinstance(SignedCertificate.cons_len_exact, list) else SignedCertificate.cons_len_exact

        def get_type_class(self):
            return SignedCertificate

        # certificate : Certificate
        certificate: "CellSlice" = None
        # certificate_signature : CryptoSignature
        certificate_signature: "CellSlice" = None

        def __init__(self, certificate: "CellSlice" = None, certificate_signature: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.certificate = certificate    
            self.field_names.append("certificate")
            self.certificate_signature = certificate_signature    
            self.field_names.append("certificate_signature")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.certificate = cs.load_subslice(356)
                
                if rec_unpack:
                    self.certificate = TLBComplex.constants["t_Certificate"].fetch(self.certificate, True, strict) # at 1
                    assert self.certificate is not None

                self.certificate_signature = TLBComplex.constants["t_CryptoSignature"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SignedCertificate")


# class for type `CryptoSignature`
class CryptoSignature(TLBComplex):
    class Tag(Enum):
        cons1 = 0
        chained_signature = 1

    cons_len = [0, 4]
    cons_tag = [0, 15]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CryptoSignature.Tag.cons1: CryptoSignature.Record_cons1, CryptoSignature.Tag.chained_signature: CryptoSignature.Record_chained_signature}

    def get_tag(self, cs: CellSlice) -> Optional["CryptoSignature.Tag"]:
        return CryptoSignature.Tag(int(cs.preload_uint(1)))


    class Record_cons1(RecordBase):
        def get_tag_enum(self):
            return CryptoSignature.Tag.cons1

        def get_tag(self):
            return CryptoSignature.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CryptoSignature.cons_len_exact[self.get_tag_enum().value] if isinstance(CryptoSignature.cons_len_exact, list) else CryptoSignature.cons_len_exact

        def get_type_class(self):
            return CryptoSignature

        # CryptoSignatureSimple
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice(516)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_CryptoSignatureSimple"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chained_signature(RecordBase):
        def get_tag_enum(self):
            return CryptoSignature.Tag.chained_signature

        def get_tag(self):
            return CryptoSignature.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CryptoSignature.cons_len_exact[self.get_tag_enum().value] if isinstance(CryptoSignature.cons_len_exact, list) else CryptoSignature.cons_len_exact

        def get_type_class(self):
            return CryptoSignature

        # signed_cert : ^SignedCertificate
        signed_cert: "Cell" = None
        # temp_key_signature : CryptoSignatureSimple
        temp_key_signature: "CellSlice" = None

        def __init__(self, signed_cert: "Cell" = None, temp_key_signature: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.signed_cert = signed_cert    
            self.field_names.append("signed_cert")
            self.temp_key_signature = temp_key_signature    
            self.field_names.append("temp_key_signature")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 15, 'Cons tag check failed'

                self.signed_cert = cs.load_ref()
                
                if rec_unpack:
                    self.signed_cert = TLBComplex.constants["t_Ref_SignedCertificate"].fetch(self.signed_cert, True, strict) # at 1
                    assert self.signed_cert is not None

                self.temp_key_signature = cs.load_subslice(516)
                
                if rec_unpack:
                    self.temp_key_signature = TLBComplex.constants["t_CryptoSignatureSimple"].fetch(self.temp_key_signature, True, strict) # at 1
                    assert self.temp_key_signature is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CryptoSignature")


# class for auxiliary type `McBlockExtra_aux`
class McBlockExtra_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {McBlockExtra_aux.Tag.cons1: McBlockExtra_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["McBlockExtra_aux.Tag"]:
        return McBlockExtra_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return McBlockExtra_aux.Tag.cons1

        def get_tag(self):
            return McBlockExtra_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return McBlockExtra_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(McBlockExtra_aux.cons_len_exact, list) else McBlockExtra_aux.cons_len_exact

        def get_type_class(self):
            return McBlockExtra_aux

        # prev_blk_signatures : HashmapE 16 CryptoSignaturePair
        prev_blk_signatures: "CellSlice" = None
        # recover_create_msg : Maybe ^InMsg
        recover_create_msg: "CellSlice" = None
        # mint_msg : Maybe ^InMsg
        mint_msg: "CellSlice" = None

        def __init__(self, prev_blk_signatures: "CellSlice" = None, recover_create_msg: "CellSlice" = None, mint_msg: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.prev_blk_signatures = prev_blk_signatures    
            self.field_names.append("prev_blk_signatures")
            self.recover_create_msg = recover_create_msg    
            self.field_names.append("recover_create_msg")
            self.mint_msg = mint_msg    
            self.field_names.append("mint_msg")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev_blk_signatures = TLBComplex.constants["t_HashmapE_16_CryptoSignaturePair"].fetch(cs) 
                self.recover_create_msg = TLBComplex.constants["t_Maybe_Ref_InMsg"].fetch(cs) 
                self.mint_msg = TLBComplex.constants["t_Maybe_Ref_InMsg"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("McBlockExtra_aux")


# class for type `McBlockExtra`
class McBlockExtra(TLBComplex):
    class Tag(Enum):
        masterchain_block_extra = 0

    cons_len_exact = 16
    cons_tag = [0xcca5]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {McBlockExtra.Tag.masterchain_block_extra: McBlockExtra.Record}

    def get_tag(self, cs: CellSlice) -> Optional["McBlockExtra.Tag"]:
        return McBlockExtra.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return McBlockExtra.Tag.masterchain_block_extra

        def get_tag(self):
            return McBlockExtra.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return McBlockExtra.cons_len_exact[self.get_tag_enum().value] if isinstance(McBlockExtra.cons_len_exact, list) else McBlockExtra.cons_len_exact

        def get_type_class(self):
            return McBlockExtra

        # key_block : ## 1
        key_block: "bool" = None
        # shard_hashes : ShardHashes
        shard_hashes: "CellSlice" = None
        # shard_fees : ShardFees
        shard_fees: "CellSlice" = None
        # ^[$_ prev_blk_signatures:(HashmapE 16 CryptoSignaturePair) recover_create_msg:(Maybe ^InMsg) mint_msg:(Maybe ^InMsg) ]
        r1: "McBlockExtra_aux.Record" = None
        # config : key_block?ConfigParams
        config: "CellSlice" = None

        def __init__(self, key_block: "bool" = None, shard_hashes: "CellSlice" = None, shard_fees: "CellSlice" = None, r1: "McBlockExtra_aux.Record" = None, config: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.key_block = key_block    
            self.field_names.append("key_block")
            self.shard_hashes = shard_hashes    
            self.field_names.append("shard_hashes")
            self.shard_fees = shard_fees    
            self.field_names.append("shard_fees")
            self.r1 = r1    
            self.field_names.append("r1")
            self.config = config    
            self.conditional_fields.append("config")    
            self.field_names.append("config")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0xcca5, 'Cons tag check failed'

                self.key_block = cs.load_bool()

                self.shard_hashes = TLBComplex.constants["t_ShardHashes"].fetch(cs) 
                self.shard_fees = TLBComplex.constants["t_ShardFees"].fetch(cs) 
                self.r1 = TLBComplex.constants["t_McBlockExtra_aux"].fetch(cs.load_ref(), rec_unpack, strict)
                if (self.key_block > 0):
                    self.config = TLBComplex.constants["t_ConfigParams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("McBlockExtra")


# class for type `ValidatorDescr`
class ValidatorDescr(TLBComplex):
    class Tag(Enum):
        validator = 0
        validator_addr = 1

    cons_len_exact = 8
    cons_tag = [0x53, 0x73]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorDescr.Tag.validator: ValidatorDescr.Record_validator, ValidatorDescr.Tag.validator_addr: ValidatorDescr.Record_validator_addr}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorDescr.Tag"]:
        return ValidatorDescr.Tag(int(cs.bselect(3, 12)))


    class Record_validator(RecordBase):
        def get_tag_enum(self):
            return ValidatorDescr.Tag.validator

        def get_tag(self):
            return ValidatorDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorDescr.cons_len_exact, list) else ValidatorDescr.cons_len_exact

        def get_type_class(self):
            return ValidatorDescr

        # public_key : SigPubKey
        public_key: "CellSlice" = None
        # weight : uint64
        weight: "int" = None

        def __init__(self, public_key: "CellSlice" = None, weight: "int" = None):
            super().__init__()
            self.field_names = []
            self.public_key = public_key    
            self.field_names.append("public_key")
            self.weight = weight    
            self.field_names.append("weight")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x53, 'Cons tag check failed'

                self.public_key = cs.load_subslice(288)
                
                if rec_unpack:
                    self.public_key = TLBComplex.constants["t_SigPubKey"].fetch(self.public_key, True, strict) # at 1
                    assert self.public_key is not None

                self.weight = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_validator_addr(RecordBase):
        def get_tag_enum(self):
            return ValidatorDescr.Tag.validator_addr

        def get_tag(self):
            return ValidatorDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorDescr.cons_len_exact, list) else ValidatorDescr.cons_len_exact

        def get_type_class(self):
            return ValidatorDescr

        # public_key : SigPubKey
        public_key: "CellSlice" = None
        # weight : uint64
        weight: "int" = None
        # adnl_addr : bits256
        adnl_addr: "bitstring.BitArray" = None

        def __init__(self, public_key: "CellSlice" = None, weight: "int" = None, adnl_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.public_key = public_key    
            self.field_names.append("public_key")
            self.weight = weight    
            self.field_names.append("weight")
            self.adnl_addr = adnl_addr    
            self.field_names.append("adnl_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x73, 'Cons tag check failed'

                self.public_key = cs.load_subslice(288)
                
                if rec_unpack:
                    self.public_key = TLBComplex.constants["t_SigPubKey"].fetch(self.public_key, True, strict) # at 1
                    assert self.public_key is not None

                self.weight = cs.load_uint(64)
                self.adnl_addr = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorDescr")


# class for type `ValidatorSet`
class ValidatorSet(TLBComplex):
    class Tag(Enum):
        validators = 0
        validators_ext = 1

    cons_len_exact = 8
    cons_tag = [17, 18]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorSet.Tag.validators: ValidatorSet.Record_validators, ValidatorSet.Tag.validators_ext: ValidatorSet.Record_validators_ext}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorSet.Tag"]:
        tag = int(cs.bselect(6, 0x30))
        if tag == 0:
            return ValidatorSet.Tag.validators_ext if cs.bit_at(6) else ValidatorSet.Tag.validators
        return None



    class Record_validators(RecordBase):
        def get_tag_enum(self):
            return ValidatorSet.Tag.validators

        def get_tag(self):
            return ValidatorSet.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorSet.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorSet.cons_len_exact, list) else ValidatorSet.cons_len_exact

        def get_type_class(self):
            return ValidatorSet

        # utime_since : uint32
        utime_since: "int" = None
        # utime_until : uint32
        utime_until: "int" = None
        # total : ## 16
        total: "int" = None
        # main : ## 16
        main: "int" = None
        # list : Hashmap 16 ValidatorDescr
        list: "CellSlice" = None

        def __init__(self, utime_since: "int" = None, utime_until: "int" = None, total: "int" = None, main: "int" = None, list: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.utime_since = utime_since    
            self.field_names.append("utime_since")
            self.utime_until = utime_until    
            self.field_names.append("utime_until")
            self.total = total    
            self.field_names.append("total")
            self.main = main    
            self.field_names.append("main")
            self.list = list    
            self.field_names.append("list")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 17, 'Cons tag check failed'

                self.utime_since = cs.load_uint(32)
                self.utime_until = cs.load_uint(32)
                self.total = cs.load_uint(16)
                self.main = cs.load_uint(16)
                assert self.main <= self.total, 'Params not equal: main and total'

                assert 1 <= self.main, 'Params not equal: 1 and main'

                self.list = TLBComplex.constants["t_Hashmap_16_ValidatorDescr"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_validators_ext(RecordBase):
        def get_tag_enum(self):
            return ValidatorSet.Tag.validators_ext

        def get_tag(self):
            return ValidatorSet.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorSet.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorSet.cons_len_exact, list) else ValidatorSet.cons_len_exact

        def get_type_class(self):
            return ValidatorSet

        # utime_since : uint32
        utime_since: "int" = None
        # utime_until : uint32
        utime_until: "int" = None
        # total : ## 16
        total: "int" = None
        # main : ## 16
        main: "int" = None
        # total_weight : uint64
        total_weight: "int" = None
        # list : HashmapE 16 ValidatorDescr
        list: "CellSlice" = None

        def __init__(self, utime_since: "int" = None, utime_until: "int" = None, total: "int" = None, main: "int" = None, total_weight: "int" = None, list: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.utime_since = utime_since    
            self.field_names.append("utime_since")
            self.utime_until = utime_until    
            self.field_names.append("utime_until")
            self.total = total    
            self.field_names.append("total")
            self.main = main    
            self.field_names.append("main")
            self.total_weight = total_weight    
            self.field_names.append("total_weight")
            self.list = list    
            self.field_names.append("list")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 18, 'Cons tag check failed'

                self.utime_since = cs.load_uint(32)
                self.utime_until = cs.load_uint(32)
                self.total = cs.load_uint(16)
                self.main = cs.load_uint(16)
                assert self.main <= self.total, 'Params not equal: main and total'

                assert 1 <= self.main, 'Params not equal: 1 and main'

                self.total_weight = cs.load_uint(64)
                self.list = TLBComplex.constants["t_HashmapE_16_ValidatorDescr"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorSet")


# class for type `BurningConfig`
class BurningConfig(TLBComplex):
    class Tag(Enum):
        burning_config = 0

    cons_len_exact = 8
    cons_tag = [1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BurningConfig.Tag.burning_config: BurningConfig.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BurningConfig.Tag"]:
        return BurningConfig.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BurningConfig.Tag.burning_config

        def get_tag(self):
            return BurningConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BurningConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(BurningConfig.cons_len_exact, list) else BurningConfig.cons_len_exact

        def get_type_class(self):
            return BurningConfig

        # blackhole_addr : Maybe bits256
        blackhole_addr: "CellSlice" = None
        # fee_burn_num : #
        fee_burn_num: "int" = None
        # fee_burn_denom : #
        fee_burn_denom: "int" = None

        def __init__(self, blackhole_addr: "CellSlice" = None, fee_burn_num: "int" = None, fee_burn_denom: "int" = None):
            super().__init__()
            self.field_names = []
            self.blackhole_addr = blackhole_addr    
            self.field_names.append("blackhole_addr")
            self.fee_burn_num = fee_burn_num    
            self.field_names.append("fee_burn_num")
            self.fee_burn_denom = fee_burn_denom    
            self.field_names.append("fee_burn_denom")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 1, 'Cons tag check failed'

                self.blackhole_addr = TLBComplex.constants["t_Maybe_bits256"].fetch(cs) 
                self.fee_burn_num = cs.load_uint(32)

                self.fee_burn_denom = cs.load_uint(32)

                assert self.fee_burn_num <= self.fee_burn_denom, 'Params not equal: fee_burn_num and fee_burn_denom'

                assert 1 <= self.fee_burn_denom, 'Params not equal: 1 and fee_burn_denom'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BurningConfig")


# class for type `GlobalVersion`
class GlobalVersion(TLBComplex):
    class Tag(Enum):
        capabilities = 0

    cons_len_exact = 8
    cons_tag = [0xc4]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {GlobalVersion.Tag.capabilities: GlobalVersion.Record}

    def get_tag(self, cs: CellSlice) -> Optional["GlobalVersion.Tag"]:
        return GlobalVersion.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return GlobalVersion.Tag.capabilities

        def get_tag(self):
            return GlobalVersion.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return GlobalVersion.cons_len_exact[self.get_tag_enum().value] if isinstance(GlobalVersion.cons_len_exact, list) else GlobalVersion.cons_len_exact

        def get_type_class(self):
            return GlobalVersion

        # version : uint32
        version: "int" = None
        # capabilities : uint64
        capabilities: "int" = None

        def __init__(self, version: "int" = None, capabilities: "int" = None):
            super().__init__()
            self.field_names = []
            self.version = version    
            self.field_names.append("version")
            self.capabilities = capabilities    
            self.field_names.append("capabilities")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xc4, 'Cons tag check failed'

                self.version = cs.load_uint(32)
                self.capabilities = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("GlobalVersion")


# class for type `ConfigProposalSetup`
class ConfigProposalSetup(TLBComplex):
    class Tag(Enum):
        cfg_vote_cfg = 0

    cons_len_exact = 8
    cons_tag = [0x36]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ConfigProposalSetup.Tag.cfg_vote_cfg: ConfigProposalSetup.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ConfigProposalSetup.Tag"]:
        return ConfigProposalSetup.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ConfigProposalSetup.Tag.cfg_vote_cfg

        def get_tag(self):
            return ConfigProposalSetup.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigProposalSetup.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigProposalSetup.cons_len_exact, list) else ConfigProposalSetup.cons_len_exact

        def get_type_class(self):
            return ConfigProposalSetup

        # min_tot_rounds : uint8
        min_tot_rounds: "int" = None
        # max_tot_rounds : uint8
        max_tot_rounds: "int" = None
        # min_wins : uint8
        min_wins: "int" = None
        # max_losses : uint8
        max_losses: "int" = None
        # min_store_sec : uint32
        min_store_sec: "int" = None
        # max_store_sec : uint32
        max_store_sec: "int" = None
        # bit_price : uint32
        bit_price: "int" = None
        # cell_price : uint32
        cell_price: "int" = None

        def __init__(self, min_tot_rounds: "int" = None, max_tot_rounds: "int" = None, min_wins: "int" = None, max_losses: "int" = None, min_store_sec: "int" = None, max_store_sec: "int" = None, bit_price: "int" = None, cell_price: "int" = None):
            super().__init__()
            self.field_names = []
            self.min_tot_rounds = min_tot_rounds    
            self.field_names.append("min_tot_rounds")
            self.max_tot_rounds = max_tot_rounds    
            self.field_names.append("max_tot_rounds")
            self.min_wins = min_wins    
            self.field_names.append("min_wins")
            self.max_losses = max_losses    
            self.field_names.append("max_losses")
            self.min_store_sec = min_store_sec    
            self.field_names.append("min_store_sec")
            self.max_store_sec = max_store_sec    
            self.field_names.append("max_store_sec")
            self.bit_price = bit_price    
            self.field_names.append("bit_price")
            self.cell_price = cell_price    
            self.field_names.append("cell_price")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x36, 'Cons tag check failed'

                self.min_tot_rounds = cs.load_uint(8)
                self.max_tot_rounds = cs.load_uint(8)
                self.min_wins = cs.load_uint(8)
                self.max_losses = cs.load_uint(8)
                self.min_store_sec = cs.load_uint(32)
                self.max_store_sec = cs.load_uint(32)
                self.bit_price = cs.load_uint(32)
                self.cell_price = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConfigProposalSetup")


# class for type `ConfigVotingSetup`
class ConfigVotingSetup(TLBComplex):
    class Tag(Enum):
        cfg_vote_setup = 0

    cons_len_exact = 8
    cons_tag = [0x91]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ConfigVotingSetup.Tag.cfg_vote_setup: ConfigVotingSetup.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ConfigVotingSetup.Tag"]:
        return ConfigVotingSetup.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ConfigVotingSetup.Tag.cfg_vote_setup

        def get_tag(self):
            return ConfigVotingSetup.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigVotingSetup.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigVotingSetup.cons_len_exact, list) else ConfigVotingSetup.cons_len_exact

        def get_type_class(self):
            return ConfigVotingSetup

        # normal_params : ^ConfigProposalSetup
        normal_params: "Cell" = None
        # critical_params : ^ConfigProposalSetup
        critical_params: "Cell" = None

        def __init__(self, normal_params: "Cell" = None, critical_params: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.normal_params = normal_params    
            self.field_names.append("normal_params")
            self.critical_params = critical_params    
            self.field_names.append("critical_params")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x91, 'Cons tag check failed'

                self.normal_params = cs.load_ref()
                
                if rec_unpack:
                    self.normal_params = TLBComplex.constants["t_Ref_ConfigProposalSetup"].fetch(self.normal_params, True, strict) # at 1
                    assert self.normal_params is not None

                self.critical_params = cs.load_ref()
                
                if rec_unpack:
                    self.critical_params = TLBComplex.constants["t_Ref_ConfigProposalSetup"].fetch(self.critical_params, True, strict) # at 1
                    assert self.critical_params is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConfigVotingSetup")


# class for type `ConfigProposal`
class ConfigProposal(TLBComplex):
    class Tag(Enum):
        cfg_proposal = 0

    cons_len_exact = 8
    cons_tag = [0xf3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ConfigProposal.Tag.cfg_proposal: ConfigProposal.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ConfigProposal.Tag"]:
        return ConfigProposal.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ConfigProposal.Tag.cfg_proposal

        def get_tag(self):
            return ConfigProposal.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigProposal.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigProposal.cons_len_exact, list) else ConfigProposal.cons_len_exact

        def get_type_class(self):
            return ConfigProposal

        # param_id : int32
        param_id: "int" = None
        # param_value : Maybe ^Cell
        param_value: "CellSlice" = None
        # if_hash_equal : Maybe uint256
        if_hash_equal: "CellSlice" = None

        def __init__(self, param_id: "int" = None, param_value: "CellSlice" = None, if_hash_equal: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.param_id = param_id    
            self.field_names.append("param_id")
            self.param_value = param_value    
            self.field_names.append("param_value")
            self.if_hash_equal = if_hash_equal    
            self.field_names.append("if_hash_equal")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xf3, 'Cons tag check failed'

                self.param_id = cs.load_int(32)
                self.param_value = TLBComplex.constants["t_Maybe_Ref_Cell"].fetch(cs) 
                self.if_hash_equal = TLBComplex.constants["t_Maybe_uint256"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConfigProposal")


# class for type `ConfigProposalStatus`
class ConfigProposalStatus(TLBComplex):
    class Tag(Enum):
        cfg_proposal_status = 0

    cons_len_exact = 8
    cons_tag = [0xce]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ConfigProposalStatus.Tag.cfg_proposal_status: ConfigProposalStatus.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ConfigProposalStatus.Tag"]:
        return ConfigProposalStatus.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ConfigProposalStatus.Tag.cfg_proposal_status

        def get_tag(self):
            return ConfigProposalStatus.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigProposalStatus.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigProposalStatus.cons_len_exact, list) else ConfigProposalStatus.cons_len_exact

        def get_type_class(self):
            return ConfigProposalStatus

        # expires : uint32
        expires: "int" = None
        # proposal : ^ConfigProposal
        proposal: "Cell" = None
        # is_critical : Bool
        is_critical: "bool" = None
        # voters : HashmapE 16 Truet
        voters: "CellSlice" = None
        # remaining_weight : int64
        remaining_weight: "int" = None
        # validator_set_id : uint256
        validator_set_id: "int" = None
        # rounds_remaining : uint8
        rounds_remaining: "int" = None
        # wins : uint8
        wins: "int" = None
        # losses : uint8
        losses: "int" = None

        def __init__(self, expires: "int" = None, proposal: "Cell" = None, is_critical: "bool" = None, voters: "CellSlice" = None, remaining_weight: "int" = None, validator_set_id: "int" = None, rounds_remaining: "int" = None, wins: "int" = None, losses: "int" = None):
            super().__init__()
            self.field_names = []
            self.expires = expires    
            self.field_names.append("expires")
            self.proposal = proposal    
            self.field_names.append("proposal")
            self.is_critical = is_critical    
            self.field_names.append("is_critical")
            self.voters = voters    
            self.field_names.append("voters")
            self.remaining_weight = remaining_weight    
            self.field_names.append("remaining_weight")
            self.validator_set_id = validator_set_id    
            self.field_names.append("validator_set_id")
            self.rounds_remaining = rounds_remaining    
            self.field_names.append("rounds_remaining")
            self.wins = wins    
            self.field_names.append("wins")
            self.losses = losses    
            self.field_names.append("losses")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xce, 'Cons tag check failed'

                self.expires = cs.load_uint(32)
                self.proposal = cs.load_ref()
                
                if rec_unpack:
                    self.proposal = TLBComplex.constants["t_Ref_ConfigProposal"].fetch(self.proposal, True, strict) # at 1
                    assert self.proposal is not None

                self.is_critical = cs.load_bool()
                self.voters = TLBComplex.constants["t_HashmapE_16_Truet"].fetch(cs) 
                self.remaining_weight = cs.load_int(64)
                self.validator_set_id = cs.load_uint(256)
                self.rounds_remaining = cs.load_uint(8)
                self.wins = cs.load_uint(8)
                self.losses = cs.load_uint(8)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConfigProposalStatus")


# class for type `WorkchainFormat`
class WorkchainFormat(TLBComplex):
    class Tag(Enum):
        wfmt_ext = 0
        wfmt_basic = 1

    cons_len_exact = 4
    cons_tag = [0, 1]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {WorkchainFormat.Tag.wfmt_basic: self.get_param_record("Record_wfmt_basic"), WorkchainFormat.Tag.wfmt_ext: self.get_param_record("Record_wfmt_ext")}

    def get_tag(self, cs: CellSlice) -> Optional["WorkchainFormat.Tag"]:
        return WorkchainFormat.Tag(int(cs.bselect(4, 3)))


    class Record_wfmt_basic(RecordBase):
        def get_tag_enum(self):
            return WorkchainFormat.Tag.wfmt_basic

        def get_tag(self):
            return WorkchainFormat.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return WorkchainFormat.cons_len_exact[self.get_tag_enum().value] if isinstance(WorkchainFormat.cons_len_exact, list) else WorkchainFormat.cons_len_exact

        def get_type_class(self):
            return WorkchainFormat

        # vm_version : int32
        vm_version: "int" = None
        # vm_mode : uint64
        vm_mode: "int" = None

        def __init__(self, vm_version: "int" = None, vm_mode: "int" = None):
            super().__init__()
            self.field_names = []
            self.vm_version = vm_version    
            self.field_names.append("vm_version")
            self.vm_mode = vm_mode    
            self.field_names.append("vm_mode")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 1, 'Cons tag check failed'

                self.vm_version = cs.load_int(32)
                self.vm_mode = cs.load_uint(64)
                self.m_ == 1                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_wfmt_ext(RecordBase):
        def get_tag_enum(self):
            return WorkchainFormat.Tag.wfmt_ext

        def get_tag(self):
            return WorkchainFormat.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return WorkchainFormat.cons_len_exact[self.get_tag_enum().value] if isinstance(WorkchainFormat.cons_len_exact, list) else WorkchainFormat.cons_len_exact

        def get_type_class(self):
            return WorkchainFormat

        # min_addr_len : ## 12
        min_addr_len: "int" = None
        # max_addr_len : ## 12
        max_addr_len: "int" = None
        # addr_len_step : ## 12
        addr_len_step: "int" = None
        # workchain_type_id : ## 32
        workchain_type_id: "int" = None

        def __init__(self, min_addr_len: "int" = None, max_addr_len: "int" = None, addr_len_step: "int" = None, workchain_type_id: "int" = None):
            super().__init__()
            self.field_names = []
            self.min_addr_len = min_addr_len    
            self.field_names.append("min_addr_len")
            self.max_addr_len = max_addr_len    
            self.field_names.append("max_addr_len")
            self.addr_len_step = addr_len_step    
            self.field_names.append("addr_len_step")
            self.workchain_type_id = workchain_type_id    
            self.field_names.append("workchain_type_id")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 0, 'Cons tag check failed'

                self.min_addr_len = cs.load_uint(12)
                self.max_addr_len = cs.load_uint(12)
                self.addr_len_step = cs.load_uint(12)
                assert 64 <= self.min_addr_len, 'Params not equal: 64 and min_addr_len'

                assert self.min_addr_len <= self.max_addr_len, 'Params not equal: min_addr_len and max_addr_len'

                assert self.max_addr_len <= 1023, 'Params not equal: max_addr_len and 1023'

                assert self.addr_len_step <= 1023, 'Params not equal: addr_len_step and 1023'

                self.workchain_type_id = cs.load_uint(32)
                assert 1 <= self.workchain_type_id, 'Params not equal: 1 and workchain_type_id'

                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("WorkchainFormat")


# class for type `WcSplitMergeTimings`
class WcSplitMergeTimings(TLBComplex):
    class Tag(Enum):
        wc_split_merge_timings = 0

    cons_len_exact = 4
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {WcSplitMergeTimings.Tag.wc_split_merge_timings: WcSplitMergeTimings.Record}

    def get_tag(self, cs: CellSlice) -> Optional["WcSplitMergeTimings.Tag"]:
        return WcSplitMergeTimings.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return WcSplitMergeTimings.Tag.wc_split_merge_timings

        def get_tag(self):
            return WcSplitMergeTimings.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return WcSplitMergeTimings.cons_len_exact[self.get_tag_enum().value] if isinstance(WcSplitMergeTimings.cons_len_exact, list) else WcSplitMergeTimings.cons_len_exact

        def get_type_class(self):
            return WcSplitMergeTimings

        # split_merge_delay : uint32
        split_merge_delay: "int" = None
        # split_merge_interval : uint32
        split_merge_interval: "int" = None
        # min_split_merge_interval : uint32
        min_split_merge_interval: "int" = None
        # max_split_merge_delay : uint32
        max_split_merge_delay: "int" = None

        def __init__(self, split_merge_delay: "int" = None, split_merge_interval: "int" = None, min_split_merge_interval: "int" = None, max_split_merge_delay: "int" = None):
            super().__init__()
            self.field_names = []
            self.split_merge_delay = split_merge_delay    
            self.field_names.append("split_merge_delay")
            self.split_merge_interval = split_merge_interval    
            self.field_names.append("split_merge_interval")
            self.min_split_merge_interval = min_split_merge_interval    
            self.field_names.append("min_split_merge_interval")
            self.max_split_merge_delay = max_split_merge_delay    
            self.field_names.append("max_split_merge_delay")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 0, 'Cons tag check failed'

                self.split_merge_delay = cs.load_uint(32)
                self.split_merge_interval = cs.load_uint(32)
                self.min_split_merge_interval = cs.load_uint(32)
                self.max_split_merge_delay = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("WcSplitMergeTimings")


# class for type `WorkchainDescr`
class WorkchainDescr(TLBComplex):
    class Tag(Enum):
        workchain = 0
        workchain_v2 = 1

    cons_len_exact = 8
    cons_tag = [0xa6, 0xa7]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {WorkchainDescr.Tag.workchain: WorkchainDescr.Record_workchain, WorkchainDescr.Tag.workchain_v2: WorkchainDescr.Record_workchain_v2}

    def get_tag(self, cs: CellSlice) -> Optional["WorkchainDescr.Tag"]:
        tag = int(cs.bselect(6, 0x60000000000))
        if tag == 0:
            return WorkchainDescr.Tag.workchain_v2 if cs.bit_at(7) else WorkchainDescr.Tag.workchain
        return None



    class Record_workchain(RecordBase):
        def get_tag_enum(self):
            return WorkchainDescr.Tag.workchain

        def get_tag(self):
            return WorkchainDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return WorkchainDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(WorkchainDescr.cons_len_exact, list) else WorkchainDescr.cons_len_exact

        def get_type_class(self):
            return WorkchainDescr

        # enabled_since : uint32
        enabled_since: "int" = None
        # actual_min_split : ## 8
        actual_min_split: "int" = None
        # min_split : ## 8
        min_split: "int" = None
        # max_split : ## 8
        max_split: "int" = None
        # basic : ## 1
        basic: "bool" = None
        # active : Bool
        active: "bool" = None
        # accept_msgs : Bool
        accept_msgs: "bool" = None
        # flags : ## 13
        flags: "int" = None
        # zerostate_root_hash : bits256
        zerostate_root_hash: "bitstring.BitArray" = None
        # zerostate_file_hash : bits256
        zerostate_file_hash: "bitstring.BitArray" = None
        # version : uint32
        version: "int" = None
        # format : WorkchainFormat basic
        format: "CellSlice" = None

        def __init__(self, enabled_since: "int" = None, actual_min_split: "int" = None, min_split: "int" = None, max_split: "int" = None, basic: "bool" = None, active: "bool" = None, accept_msgs: "bool" = None, flags: "int" = None, zerostate_root_hash: "bitstring.BitArray" = None, zerostate_file_hash: "bitstring.BitArray" = None, version: "int" = None, format: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.enabled_since = enabled_since    
            self.field_names.append("enabled_since")
            self.actual_min_split = actual_min_split    
            self.field_names.append("actual_min_split")
            self.min_split = min_split    
            self.field_names.append("min_split")
            self.max_split = max_split    
            self.field_names.append("max_split")
            self.basic = basic    
            self.field_names.append("basic")
            self.active = active    
            self.field_names.append("active")
            self.accept_msgs = accept_msgs    
            self.field_names.append("accept_msgs")
            self.flags = flags    
            self.field_names.append("flags")
            self.zerostate_root_hash = zerostate_root_hash    
            self.field_names.append("zerostate_root_hash")
            self.zerostate_file_hash = zerostate_file_hash    
            self.field_names.append("zerostate_file_hash")
            self.version = version    
            self.field_names.append("version")
            self.format = format    
            self.field_names.append("format")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xa6, 'Cons tag check failed'

                self.enabled_since = cs.load_uint(32)
                self.actual_min_split = cs.load_uint(8)
                self.min_split = cs.load_uint(8)
                self.max_split = cs.load_uint(8)
                assert self.actual_min_split <= self.min_split, 'Params not equal: actual_min_split and min_split'

                self.basic = cs.load_bool()

                self.active = cs.load_bool()
                self.accept_msgs = cs.load_bool()
                self.flags = cs.load_uint(13)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.zerostate_root_hash = cs.load_bitstring(256)
                self.zerostate_file_hash = cs.load_bitstring(256)
                self.version = cs.load_uint(32)
                self.format = WorkchainFormat(self.basic).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_workchain_v2(RecordBase):
        def get_tag_enum(self):
            return WorkchainDescr.Tag.workchain_v2

        def get_tag(self):
            return WorkchainDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return WorkchainDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(WorkchainDescr.cons_len_exact, list) else WorkchainDescr.cons_len_exact

        def get_type_class(self):
            return WorkchainDescr

        # enabled_since : uint32
        enabled_since: "int" = None
        # actual_min_split : ## 8
        actual_min_split: "int" = None
        # min_split : ## 8
        min_split: "int" = None
        # max_split : ## 8
        max_split: "int" = None
        # basic : ## 1
        basic: "bool" = None
        # active : Bool
        active: "bool" = None
        # accept_msgs : Bool
        accept_msgs: "bool" = None
        # flags : ## 13
        flags: "int" = None
        # zerostate_root_hash : bits256
        zerostate_root_hash: "bitstring.BitArray" = None
        # zerostate_file_hash : bits256
        zerostate_file_hash: "bitstring.BitArray" = None
        # version : uint32
        version: "int" = None
        # format : WorkchainFormat basic
        format: "CellSlice" = None
        # split_merge_timings : WcSplitMergeTimings
        split_merge_timings: "CellSlice" = None

        def __init__(self, enabled_since: "int" = None, actual_min_split: "int" = None, min_split: "int" = None, max_split: "int" = None, basic: "bool" = None, active: "bool" = None, accept_msgs: "bool" = None, flags: "int" = None, zerostate_root_hash: "bitstring.BitArray" = None, zerostate_file_hash: "bitstring.BitArray" = None, version: "int" = None, format: "CellSlice" = None, split_merge_timings: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.enabled_since = enabled_since    
            self.field_names.append("enabled_since")
            self.actual_min_split = actual_min_split    
            self.field_names.append("actual_min_split")
            self.min_split = min_split    
            self.field_names.append("min_split")
            self.max_split = max_split    
            self.field_names.append("max_split")
            self.basic = basic    
            self.field_names.append("basic")
            self.active = active    
            self.field_names.append("active")
            self.accept_msgs = accept_msgs    
            self.field_names.append("accept_msgs")
            self.flags = flags    
            self.field_names.append("flags")
            self.zerostate_root_hash = zerostate_root_hash    
            self.field_names.append("zerostate_root_hash")
            self.zerostate_file_hash = zerostate_file_hash    
            self.field_names.append("zerostate_file_hash")
            self.version = version    
            self.field_names.append("version")
            self.format = format    
            self.field_names.append("format")
            self.split_merge_timings = split_merge_timings    
            self.field_names.append("split_merge_timings")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xa7, 'Cons tag check failed'

                self.enabled_since = cs.load_uint(32)
                self.actual_min_split = cs.load_uint(8)
                self.min_split = cs.load_uint(8)
                self.max_split = cs.load_uint(8)
                assert self.actual_min_split <= self.min_split, 'Params not equal: actual_min_split and min_split'

                self.basic = cs.load_bool()

                self.active = cs.load_bool()
                self.accept_msgs = cs.load_bool()
                self.flags = cs.load_uint(13)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.zerostate_root_hash = cs.load_bitstring(256)
                self.zerostate_file_hash = cs.load_bitstring(256)
                self.version = cs.load_uint(32)
                self.format = WorkchainFormat(self.basic).fetch(cs) 
                self.split_merge_timings = cs.load_subslice(132)
                
                if rec_unpack:
                    self.split_merge_timings = TLBComplex.constants["t_WcSplitMergeTimings"].fetch(self.split_merge_timings, True, strict) # at 1
                    assert self.split_merge_timings is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("WorkchainDescr")


# class for type `ComplaintPricing`
class ComplaintPricing(TLBComplex):
    class Tag(Enum):
        complaint_prices = 0

    cons_len_exact = 8
    cons_tag = [26]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ComplaintPricing.Tag.complaint_prices: ComplaintPricing.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ComplaintPricing.Tag"]:
        return ComplaintPricing.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ComplaintPricing.Tag.complaint_prices

        def get_tag(self):
            return ComplaintPricing.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComplaintPricing.cons_len_exact[self.get_tag_enum().value] if isinstance(ComplaintPricing.cons_len_exact, list) else ComplaintPricing.cons_len_exact

        def get_type_class(self):
            return ComplaintPricing

        # deposit : Grams
        deposit: "CellSlice" = None
        # bit_price : Grams
        bit_price: "CellSlice" = None
        # cell_price : Grams
        cell_price: "CellSlice" = None

        def __init__(self, deposit: "CellSlice" = None, bit_price: "CellSlice" = None, cell_price: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.deposit = deposit    
            self.field_names.append("deposit")
            self.bit_price = bit_price    
            self.field_names.append("bit_price")
            self.cell_price = cell_price    
            self.field_names.append("cell_price")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 26, 'Cons tag check failed'

                self.deposit = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.bit_price = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.cell_price = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ComplaintPricing")


# class for type `BlockCreateFees`
class BlockCreateFees(TLBComplex):
    class Tag(Enum):
        block_grams_created = 0

    cons_len_exact = 8
    cons_tag = [0x6b]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockCreateFees.Tag.block_grams_created: BlockCreateFees.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockCreateFees.Tag"]:
        return BlockCreateFees.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockCreateFees.Tag.block_grams_created

        def get_tag(self):
            return BlockCreateFees.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockCreateFees.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockCreateFees.cons_len_exact, list) else BlockCreateFees.cons_len_exact

        def get_type_class(self):
            return BlockCreateFees

        # masterchain_block_fee : Grams
        masterchain_block_fee: "CellSlice" = None
        # basechain_block_fee : Grams
        basechain_block_fee: "CellSlice" = None

        def __init__(self, masterchain_block_fee: "CellSlice" = None, basechain_block_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.masterchain_block_fee = masterchain_block_fee    
            self.field_names.append("masterchain_block_fee")
            self.basechain_block_fee = basechain_block_fee    
            self.field_names.append("basechain_block_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x6b, 'Cons tag check failed'

                self.masterchain_block_fee = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.basechain_block_fee = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockCreateFees")


# class for type `StoragePrices`
class StoragePrices(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 8
    cons_tag = [0xcc]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {StoragePrices.Tag.cons1: StoragePrices.Record}

    def get_tag(self, cs: CellSlice) -> Optional["StoragePrices.Tag"]:
        return StoragePrices.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return StoragePrices.Tag.cons1

        def get_tag(self):
            return StoragePrices.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return StoragePrices.cons_len_exact[self.get_tag_enum().value] if isinstance(StoragePrices.cons_len_exact, list) else StoragePrices.cons_len_exact

        def get_type_class(self):
            return StoragePrices

        # utime_since : uint32
        utime_since: "int" = None
        # bit_price_ps : uint64
        bit_price_ps: "int" = None
        # cell_price_ps : uint64
        cell_price_ps: "int" = None
        # mc_bit_price_ps : uint64
        mc_bit_price_ps: "int" = None
        # mc_cell_price_ps : uint64
        mc_cell_price_ps: "int" = None

        def __init__(self, utime_since: "int" = None, bit_price_ps: "int" = None, cell_price_ps: "int" = None, mc_bit_price_ps: "int" = None, mc_cell_price_ps: "int" = None):
            super().__init__()
            self.field_names = []
            self.utime_since = utime_since    
            self.field_names.append("utime_since")
            self.bit_price_ps = bit_price_ps    
            self.field_names.append("bit_price_ps")
            self.cell_price_ps = cell_price_ps    
            self.field_names.append("cell_price_ps")
            self.mc_bit_price_ps = mc_bit_price_ps    
            self.field_names.append("mc_bit_price_ps")
            self.mc_cell_price_ps = mc_cell_price_ps    
            self.field_names.append("mc_cell_price_ps")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xcc, 'Cons tag check failed'

                self.utime_since = cs.load_uint(32)
                self.bit_price_ps = cs.load_uint(64)
                self.cell_price_ps = cs.load_uint(64)
                self.mc_bit_price_ps = cs.load_uint(64)
                self.mc_cell_price_ps = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("StoragePrices")


# class for type `GasLimitsPrices`
class GasLimitsPrices(TLBComplex):
    class Tag(Enum):
        gas_flat_pfx = 0
        gas_prices = 1
        gas_prices_ext = 2

    cons_len_exact = 8
    cons_tag = [0xd1, 0xdd, 0xde]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {GasLimitsPrices.Tag.gas_prices: GasLimitsPrices.Record_gas_prices, GasLimitsPrices.Tag.gas_prices_ext: GasLimitsPrices.Record_gas_prices_ext, GasLimitsPrices.Tag.gas_flat_pfx: GasLimitsPrices.Record_gas_flat_pfx}

    def get_tag(self, cs: CellSlice) -> Optional["GasLimitsPrices.Tag"]:
        tag = int(cs.bselect(6, 0x1b0000000000000))
        if tag == 0:
            return GasLimitsPrices.Tag.gas_flat_pfx

        if tag == 2:
            return GasLimitsPrices.Tag.gas_prices_ext if cs.bit_at(6) else GasLimitsPrices.Tag.gas_prices
        return None



    class Record_gas_prices(RecordBase):
        def get_tag_enum(self):
            return GasLimitsPrices.Tag.gas_prices

        def get_tag(self):
            return GasLimitsPrices.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return GasLimitsPrices.cons_len_exact[self.get_tag_enum().value] if isinstance(GasLimitsPrices.cons_len_exact, list) else GasLimitsPrices.cons_len_exact

        def get_type_class(self):
            return GasLimitsPrices

        # gas_price : uint64
        gas_price: "int" = None
        # gas_limit : uint64
        gas_limit: "int" = None
        # gas_credit : uint64
        gas_credit: "int" = None
        # block_gas_limit : uint64
        block_gas_limit: "int" = None
        # freeze_due_limit : uint64
        freeze_due_limit: "int" = None
        # delete_due_limit : uint64
        delete_due_limit: "int" = None

        def __init__(self, gas_price: "int" = None, gas_limit: "int" = None, gas_credit: "int" = None, block_gas_limit: "int" = None, freeze_due_limit: "int" = None, delete_due_limit: "int" = None):
            super().__init__()
            self.field_names = []
            self.gas_price = gas_price    
            self.field_names.append("gas_price")
            self.gas_limit = gas_limit    
            self.field_names.append("gas_limit")
            self.gas_credit = gas_credit    
            self.field_names.append("gas_credit")
            self.block_gas_limit = block_gas_limit    
            self.field_names.append("block_gas_limit")
            self.freeze_due_limit = freeze_due_limit    
            self.field_names.append("freeze_due_limit")
            self.delete_due_limit = delete_due_limit    
            self.field_names.append("delete_due_limit")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xdd, 'Cons tag check failed'

                self.gas_price = cs.load_uint(64)
                self.gas_limit = cs.load_uint(64)
                self.gas_credit = cs.load_uint(64)
                self.block_gas_limit = cs.load_uint(64)
                self.freeze_due_limit = cs.load_uint(64)
                self.delete_due_limit = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_gas_prices_ext(RecordBase):
        def get_tag_enum(self):
            return GasLimitsPrices.Tag.gas_prices_ext

        def get_tag(self):
            return GasLimitsPrices.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return GasLimitsPrices.cons_len_exact[self.get_tag_enum().value] if isinstance(GasLimitsPrices.cons_len_exact, list) else GasLimitsPrices.cons_len_exact

        def get_type_class(self):
            return GasLimitsPrices

        # gas_price : uint64
        gas_price: "int" = None
        # gas_limit : uint64
        gas_limit: "int" = None
        # special_gas_limit : uint64
        special_gas_limit: "int" = None
        # gas_credit : uint64
        gas_credit: "int" = None
        # block_gas_limit : uint64
        block_gas_limit: "int" = None
        # freeze_due_limit : uint64
        freeze_due_limit: "int" = None
        # delete_due_limit : uint64
        delete_due_limit: "int" = None

        def __init__(self, gas_price: "int" = None, gas_limit: "int" = None, special_gas_limit: "int" = None, gas_credit: "int" = None, block_gas_limit: "int" = None, freeze_due_limit: "int" = None, delete_due_limit: "int" = None):
            super().__init__()
            self.field_names = []
            self.gas_price = gas_price    
            self.field_names.append("gas_price")
            self.gas_limit = gas_limit    
            self.field_names.append("gas_limit")
            self.special_gas_limit = special_gas_limit    
            self.field_names.append("special_gas_limit")
            self.gas_credit = gas_credit    
            self.field_names.append("gas_credit")
            self.block_gas_limit = block_gas_limit    
            self.field_names.append("block_gas_limit")
            self.freeze_due_limit = freeze_due_limit    
            self.field_names.append("freeze_due_limit")
            self.delete_due_limit = delete_due_limit    
            self.field_names.append("delete_due_limit")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xde, 'Cons tag check failed'

                self.gas_price = cs.load_uint(64)
                self.gas_limit = cs.load_uint(64)
                self.special_gas_limit = cs.load_uint(64)
                self.gas_credit = cs.load_uint(64)
                self.block_gas_limit = cs.load_uint(64)
                self.freeze_due_limit = cs.load_uint(64)
                self.delete_due_limit = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_gas_flat_pfx(RecordBase):
        def get_tag_enum(self):
            return GasLimitsPrices.Tag.gas_flat_pfx

        def get_tag(self):
            return GasLimitsPrices.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return GasLimitsPrices.cons_len_exact[self.get_tag_enum().value] if isinstance(GasLimitsPrices.cons_len_exact, list) else GasLimitsPrices.cons_len_exact

        def get_type_class(self):
            return GasLimitsPrices

        # flat_gas_limit : uint64
        flat_gas_limit: "int" = None
        # flat_gas_price : uint64
        flat_gas_price: "int" = None
        # other : GasLimitsPrices
        other: "CellSlice" = None

        def __init__(self, flat_gas_limit: "int" = None, flat_gas_price: "int" = None, other: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.flat_gas_limit = flat_gas_limit    
            self.field_names.append("flat_gas_limit")
            self.flat_gas_price = flat_gas_price    
            self.field_names.append("flat_gas_price")
            self.other = other    
            self.field_names.append("other")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xd1, 'Cons tag check failed'

                self.flat_gas_limit = cs.load_uint(64)
                self.flat_gas_price = cs.load_uint(64)
                self.other = self.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("GasLimitsPrices")


# class for type `ParamLimits`
class ParamLimits(TLBComplex):
    class Tag(Enum):
        param_limits = 0

    cons_len_exact = 8
    cons_tag = [0xc3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ParamLimits.Tag.param_limits: ParamLimits.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ParamLimits.Tag"]:
        return ParamLimits.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ParamLimits.Tag.param_limits

        def get_tag(self):
            return ParamLimits.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ParamLimits.cons_len_exact[self.get_tag_enum().value] if isinstance(ParamLimits.cons_len_exact, list) else ParamLimits.cons_len_exact

        def get_type_class(self):
            return ParamLimits

        # underload : #
        underload: "int" = None
        # soft_limit : #
        soft_limit: "int" = None
        # hard_limit : #
        hard_limit: "int" = None

        def __init__(self, underload: "int" = None, soft_limit: "int" = None, hard_limit: "int" = None):
            super().__init__()
            self.field_names = []
            self.underload = underload    
            self.field_names.append("underload")
            self.soft_limit = soft_limit    
            self.field_names.append("soft_limit")
            self.hard_limit = hard_limit    
            self.field_names.append("hard_limit")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xc3, 'Cons tag check failed'

                self.underload = cs.load_uint(32)

                self.soft_limit = cs.load_uint(32)

                assert self.underload <= self.soft_limit, 'Params not equal: underload and soft_limit'

                self.hard_limit = cs.load_uint(32)

                assert self.soft_limit <= self.hard_limit, 'Params not equal: soft_limit and hard_limit'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ParamLimits")


# class for type `BlockLimits`
class BlockLimits(TLBComplex):
    class Tag(Enum):
        block_limits = 0

    cons_len_exact = 8
    cons_tag = [0x5d]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockLimits.Tag.block_limits: BlockLimits.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockLimits.Tag"]:
        return BlockLimits.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockLimits.Tag.block_limits

        def get_tag(self):
            return BlockLimits.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockLimits.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockLimits.cons_len_exact, list) else BlockLimits.cons_len_exact

        def get_type_class(self):
            return BlockLimits

        # bytes : ParamLimits
        bytes: "CellSlice" = None
        # gas : ParamLimits
        gas: "CellSlice" = None
        # lt_delta : ParamLimits
        lt_delta: "CellSlice" = None

        def __init__(self, bytes: "CellSlice" = None, gas: "CellSlice" = None, lt_delta: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.bytes = bytes    
            self.field_names.append("bytes")
            self.gas = gas    
            self.field_names.append("gas")
            self.lt_delta = lt_delta    
            self.field_names.append("lt_delta")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x5d, 'Cons tag check failed'

                self.bytes = cs.load_subslice(104)
                
                if rec_unpack:
                    self.bytes = TLBComplex.constants["t_ParamLimits"].fetch(self.bytes, True, strict) # at 1
                    assert self.bytes is not None

                self.gas = cs.load_subslice(104)
                
                if rec_unpack:
                    self.gas = TLBComplex.constants["t_ParamLimits"].fetch(self.gas, True, strict) # at 1
                    assert self.gas is not None

                self.lt_delta = cs.load_subslice(104)
                
                if rec_unpack:
                    self.lt_delta = TLBComplex.constants["t_ParamLimits"].fetch(self.lt_delta, True, strict) # at 1
                    assert self.lt_delta is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockLimits")


# class for type `MsgForwardPrices`
class MsgForwardPrices(TLBComplex):
    class Tag(Enum):
        msg_forward_prices = 0

    cons_len_exact = 8
    cons_tag = [0xea]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MsgForwardPrices.Tag.msg_forward_prices: MsgForwardPrices.Record}

    def get_tag(self, cs: CellSlice) -> Optional["MsgForwardPrices.Tag"]:
        return MsgForwardPrices.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MsgForwardPrices.Tag.msg_forward_prices

        def get_tag(self):
            return MsgForwardPrices.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MsgForwardPrices.cons_len_exact[self.get_tag_enum().value] if isinstance(MsgForwardPrices.cons_len_exact, list) else MsgForwardPrices.cons_len_exact

        def get_type_class(self):
            return MsgForwardPrices

        # lump_price : uint64
        lump_price: "int" = None
        # bit_price : uint64
        bit_price: "int" = None
        # cell_price : uint64
        cell_price: "int" = None
        # ihr_price_factor : uint32
        ihr_price_factor: "int" = None
        # first_frac : uint16
        first_frac: "int" = None
        # next_frac : uint16
        next_frac: "int" = None

        def __init__(self, lump_price: "int" = None, bit_price: "int" = None, cell_price: "int" = None, ihr_price_factor: "int" = None, first_frac: "int" = None, next_frac: "int" = None):
            super().__init__()
            self.field_names = []
            self.lump_price = lump_price    
            self.field_names.append("lump_price")
            self.bit_price = bit_price    
            self.field_names.append("bit_price")
            self.cell_price = cell_price    
            self.field_names.append("cell_price")
            self.ihr_price_factor = ihr_price_factor    
            self.field_names.append("ihr_price_factor")
            self.first_frac = first_frac    
            self.field_names.append("first_frac")
            self.next_frac = next_frac    
            self.field_names.append("next_frac")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xea, 'Cons tag check failed'

                self.lump_price = cs.load_uint(64)
                self.bit_price = cs.load_uint(64)
                self.cell_price = cs.load_uint(64)
                self.ihr_price_factor = cs.load_uint(32)
                self.first_frac = cs.load_uint(16)
                self.next_frac = cs.load_uint(16)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MsgForwardPrices")


# class for type `CatchainConfig`
class CatchainConfig(TLBComplex):
    class Tag(Enum):
        catchain_config = 0
        catchain_config_new = 1

    cons_len_exact = 8
    cons_tag = [0xc1, 0xc2]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {CatchainConfig.Tag.catchain_config: CatchainConfig.Record_catchain_config, CatchainConfig.Tag.catchain_config_new: CatchainConfig.Record_catchain_config_new}

    def get_tag(self, cs: CellSlice) -> Optional["CatchainConfig.Tag"]:
        tag = int(cs.bselect(6, 0x3000000000000))
        if tag == 0:
            return CatchainConfig.Tag.catchain_config_new if cs.bit_at(6) else CatchainConfig.Tag.catchain_config
        return None



    class Record_catchain_config(RecordBase):
        def get_tag_enum(self):
            return CatchainConfig.Tag.catchain_config

        def get_tag(self):
            return CatchainConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CatchainConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(CatchainConfig.cons_len_exact, list) else CatchainConfig.cons_len_exact

        def get_type_class(self):
            return CatchainConfig

        # mc_catchain_lifetime : uint32
        mc_catchain_lifetime: "int" = None
        # shard_catchain_lifetime : uint32
        shard_catchain_lifetime: "int" = None
        # shard_validators_lifetime : uint32
        shard_validators_lifetime: "int" = None
        # shard_validators_num : uint32
        shard_validators_num: "int" = None

        def __init__(self, mc_catchain_lifetime: "int" = None, shard_catchain_lifetime: "int" = None, shard_validators_lifetime: "int" = None, shard_validators_num: "int" = None):
            super().__init__()
            self.field_names = []
            self.mc_catchain_lifetime = mc_catchain_lifetime    
            self.field_names.append("mc_catchain_lifetime")
            self.shard_catchain_lifetime = shard_catchain_lifetime    
            self.field_names.append("shard_catchain_lifetime")
            self.shard_validators_lifetime = shard_validators_lifetime    
            self.field_names.append("shard_validators_lifetime")
            self.shard_validators_num = shard_validators_num    
            self.field_names.append("shard_validators_num")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xc1, 'Cons tag check failed'

                self.mc_catchain_lifetime = cs.load_uint(32)
                self.shard_catchain_lifetime = cs.load_uint(32)
                self.shard_validators_lifetime = cs.load_uint(32)
                self.shard_validators_num = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_catchain_config_new(RecordBase):
        def get_tag_enum(self):
            return CatchainConfig.Tag.catchain_config_new

        def get_tag(self):
            return CatchainConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return CatchainConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(CatchainConfig.cons_len_exact, list) else CatchainConfig.cons_len_exact

        def get_type_class(self):
            return CatchainConfig

        # flags : ## 7
        flags: "int" = None
        # shuffle_mc_validators : Bool
        shuffle_mc_validators: "bool" = None
        # mc_catchain_lifetime : uint32
        mc_catchain_lifetime: "int" = None
        # shard_catchain_lifetime : uint32
        shard_catchain_lifetime: "int" = None
        # shard_validators_lifetime : uint32
        shard_validators_lifetime: "int" = None
        # shard_validators_num : uint32
        shard_validators_num: "int" = None

        def __init__(self, flags: "int" = None, shuffle_mc_validators: "bool" = None, mc_catchain_lifetime: "int" = None, shard_catchain_lifetime: "int" = None, shard_validators_lifetime: "int" = None, shard_validators_num: "int" = None):
            super().__init__()
            self.field_names = []
            self.flags = flags    
            self.field_names.append("flags")
            self.shuffle_mc_validators = shuffle_mc_validators    
            self.field_names.append("shuffle_mc_validators")
            self.mc_catchain_lifetime = mc_catchain_lifetime    
            self.field_names.append("mc_catchain_lifetime")
            self.shard_catchain_lifetime = shard_catchain_lifetime    
            self.field_names.append("shard_catchain_lifetime")
            self.shard_validators_lifetime = shard_validators_lifetime    
            self.field_names.append("shard_validators_lifetime")
            self.shard_validators_num = shard_validators_num    
            self.field_names.append("shard_validators_num")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xc2, 'Cons tag check failed'

                self.flags = cs.load_uint(7)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.shuffle_mc_validators = cs.load_bool()
                self.mc_catchain_lifetime = cs.load_uint(32)
                self.shard_catchain_lifetime = cs.load_uint(32)
                self.shard_validators_lifetime = cs.load_uint(32)
                self.shard_validators_num = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("CatchainConfig")


# class for type `ConsensusConfig`
class ConsensusConfig(TLBComplex):
    class Tag(Enum):
        consensus_config = 0
        consensus_config_new = 1
        consensus_config_v3 = 2
        consensus_config_v4 = 3

    cons_len_exact = 8
    cons_tag = [0xd6, 0xd7, 0xd8, 0xd9]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ConsensusConfig.Tag.consensus_config: ConsensusConfig.Record_consensus_config, ConsensusConfig.Tag.consensus_config_new: ConsensusConfig.Record_consensus_config_new, ConsensusConfig.Tag.consensus_config_v3: ConsensusConfig.Record_consensus_config_v3, ConsensusConfig.Tag.consensus_config_v4: ConsensusConfig.Record_consensus_config_v4}

    def get_tag(self, cs: CellSlice) -> Optional["ConsensusConfig.Tag"]:
        tag = int(cs.bselect(6, 0xe0000000000000))
        if tag == 0:
            return ConsensusConfig.Tag.consensus_config_new if cs.bit_at(7) else ConsensusConfig.Tag.consensus_config
        if tag == 1:
            return ConsensusConfig.Tag.consensus_config_v4 if cs.bit_at(7) else ConsensusConfig.Tag.consensus_config_v3
        return None



    class Record_consensus_config(RecordBase):
        def get_tag_enum(self):
            return ConsensusConfig.Tag.consensus_config

        def get_tag(self):
            return ConsensusConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConsensusConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(ConsensusConfig.cons_len_exact, list) else ConsensusConfig.cons_len_exact

        def get_type_class(self):
            return ConsensusConfig

        # round_candidates : #
        round_candidates: "int" = None
        # next_candidate_delay_ms : uint32
        next_candidate_delay_ms: "int" = None
        # consensus_timeout_ms : uint32
        consensus_timeout_ms: "int" = None
        # fast_attempts : uint32
        fast_attempts: "int" = None
        # attempt_duration : uint32
        attempt_duration: "int" = None
        # catchain_max_deps : uint32
        catchain_max_deps: "int" = None
        # max_block_bytes : uint32
        max_block_bytes: "int" = None
        # max_collated_bytes : uint32
        max_collated_bytes: "int" = None

        def __init__(self, round_candidates: "int" = None, next_candidate_delay_ms: "int" = None, consensus_timeout_ms: "int" = None, fast_attempts: "int" = None, attempt_duration: "int" = None, catchain_max_deps: "int" = None, max_block_bytes: "int" = None, max_collated_bytes: "int" = None):
            super().__init__()
            self.field_names = []
            self.round_candidates = round_candidates    
            self.field_names.append("round_candidates")
            self.next_candidate_delay_ms = next_candidate_delay_ms    
            self.field_names.append("next_candidate_delay_ms")
            self.consensus_timeout_ms = consensus_timeout_ms    
            self.field_names.append("consensus_timeout_ms")
            self.fast_attempts = fast_attempts    
            self.field_names.append("fast_attempts")
            self.attempt_duration = attempt_duration    
            self.field_names.append("attempt_duration")
            self.catchain_max_deps = catchain_max_deps    
            self.field_names.append("catchain_max_deps")
            self.max_block_bytes = max_block_bytes    
            self.field_names.append("max_block_bytes")
            self.max_collated_bytes = max_collated_bytes    
            self.field_names.append("max_collated_bytes")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xd6, 'Cons tag check failed'

                self.round_candidates = cs.load_uint(32)

                assert 1 <= self.round_candidates, 'Params not equal: 1 and round_candidates'

                self.next_candidate_delay_ms = cs.load_uint(32)
                self.consensus_timeout_ms = cs.load_uint(32)
                self.fast_attempts = cs.load_uint(32)
                self.attempt_duration = cs.load_uint(32)
                self.catchain_max_deps = cs.load_uint(32)
                self.max_block_bytes = cs.load_uint(32)
                self.max_collated_bytes = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_consensus_config_new(RecordBase):
        def get_tag_enum(self):
            return ConsensusConfig.Tag.consensus_config_new

        def get_tag(self):
            return ConsensusConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConsensusConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(ConsensusConfig.cons_len_exact, list) else ConsensusConfig.cons_len_exact

        def get_type_class(self):
            return ConsensusConfig

        # flags : ## 7
        flags: "int" = None
        # new_catchain_ids : Bool
        new_catchain_ids: "bool" = None
        # round_candidates : ## 8
        round_candidates: "int" = None
        # next_candidate_delay_ms : uint32
        next_candidate_delay_ms: "int" = None
        # consensus_timeout_ms : uint32
        consensus_timeout_ms: "int" = None
        # fast_attempts : uint32
        fast_attempts: "int" = None
        # attempt_duration : uint32
        attempt_duration: "int" = None
        # catchain_max_deps : uint32
        catchain_max_deps: "int" = None
        # max_block_bytes : uint32
        max_block_bytes: "int" = None
        # max_collated_bytes : uint32
        max_collated_bytes: "int" = None

        def __init__(self, flags: "int" = None, new_catchain_ids: "bool" = None, round_candidates: "int" = None, next_candidate_delay_ms: "int" = None, consensus_timeout_ms: "int" = None, fast_attempts: "int" = None, attempt_duration: "int" = None, catchain_max_deps: "int" = None, max_block_bytes: "int" = None, max_collated_bytes: "int" = None):
            super().__init__()
            self.field_names = []
            self.flags = flags    
            self.field_names.append("flags")
            self.new_catchain_ids = new_catchain_ids    
            self.field_names.append("new_catchain_ids")
            self.round_candidates = round_candidates    
            self.field_names.append("round_candidates")
            self.next_candidate_delay_ms = next_candidate_delay_ms    
            self.field_names.append("next_candidate_delay_ms")
            self.consensus_timeout_ms = consensus_timeout_ms    
            self.field_names.append("consensus_timeout_ms")
            self.fast_attempts = fast_attempts    
            self.field_names.append("fast_attempts")
            self.attempt_duration = attempt_duration    
            self.field_names.append("attempt_duration")
            self.catchain_max_deps = catchain_max_deps    
            self.field_names.append("catchain_max_deps")
            self.max_block_bytes = max_block_bytes    
            self.field_names.append("max_block_bytes")
            self.max_collated_bytes = max_collated_bytes    
            self.field_names.append("max_collated_bytes")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xd7, 'Cons tag check failed'

                self.flags = cs.load_uint(7)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.new_catchain_ids = cs.load_bool()
                self.round_candidates = cs.load_uint(8)
                assert 1 <= self.round_candidates, 'Params not equal: 1 and round_candidates'

                self.next_candidate_delay_ms = cs.load_uint(32)
                self.consensus_timeout_ms = cs.load_uint(32)
                self.fast_attempts = cs.load_uint(32)
                self.attempt_duration = cs.load_uint(32)
                self.catchain_max_deps = cs.load_uint(32)
                self.max_block_bytes = cs.load_uint(32)
                self.max_collated_bytes = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_consensus_config_v3(RecordBase):
        def get_tag_enum(self):
            return ConsensusConfig.Tag.consensus_config_v3

        def get_tag(self):
            return ConsensusConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConsensusConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(ConsensusConfig.cons_len_exact, list) else ConsensusConfig.cons_len_exact

        def get_type_class(self):
            return ConsensusConfig

        # flags : ## 7
        flags: "int" = None
        # new_catchain_ids : Bool
        new_catchain_ids: "bool" = None
        # round_candidates : ## 8
        round_candidates: "int" = None
        # next_candidate_delay_ms : uint32
        next_candidate_delay_ms: "int" = None
        # consensus_timeout_ms : uint32
        consensus_timeout_ms: "int" = None
        # fast_attempts : uint32
        fast_attempts: "int" = None
        # attempt_duration : uint32
        attempt_duration: "int" = None
        # catchain_max_deps : uint32
        catchain_max_deps: "int" = None
        # max_block_bytes : uint32
        max_block_bytes: "int" = None
        # max_collated_bytes : uint32
        max_collated_bytes: "int" = None
        # proto_version : uint16
        proto_version: "int" = None

        def __init__(self, flags: "int" = None, new_catchain_ids: "bool" = None, round_candidates: "int" = None, next_candidate_delay_ms: "int" = None, consensus_timeout_ms: "int" = None, fast_attempts: "int" = None, attempt_duration: "int" = None, catchain_max_deps: "int" = None, max_block_bytes: "int" = None, max_collated_bytes: "int" = None, proto_version: "int" = None):
            super().__init__()
            self.field_names = []
            self.flags = flags    
            self.field_names.append("flags")
            self.new_catchain_ids = new_catchain_ids    
            self.field_names.append("new_catchain_ids")
            self.round_candidates = round_candidates    
            self.field_names.append("round_candidates")
            self.next_candidate_delay_ms = next_candidate_delay_ms    
            self.field_names.append("next_candidate_delay_ms")
            self.consensus_timeout_ms = consensus_timeout_ms    
            self.field_names.append("consensus_timeout_ms")
            self.fast_attempts = fast_attempts    
            self.field_names.append("fast_attempts")
            self.attempt_duration = attempt_duration    
            self.field_names.append("attempt_duration")
            self.catchain_max_deps = catchain_max_deps    
            self.field_names.append("catchain_max_deps")
            self.max_block_bytes = max_block_bytes    
            self.field_names.append("max_block_bytes")
            self.max_collated_bytes = max_collated_bytes    
            self.field_names.append("max_collated_bytes")
            self.proto_version = proto_version    
            self.field_names.append("proto_version")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xd8, 'Cons tag check failed'

                self.flags = cs.load_uint(7)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.new_catchain_ids = cs.load_bool()
                self.round_candidates = cs.load_uint(8)
                assert 1 <= self.round_candidates, 'Params not equal: 1 and round_candidates'

                self.next_candidate_delay_ms = cs.load_uint(32)
                self.consensus_timeout_ms = cs.load_uint(32)
                self.fast_attempts = cs.load_uint(32)
                self.attempt_duration = cs.load_uint(32)
                self.catchain_max_deps = cs.load_uint(32)
                self.max_block_bytes = cs.load_uint(32)
                self.max_collated_bytes = cs.load_uint(32)
                self.proto_version = cs.load_uint(16)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_consensus_config_v4(RecordBase):
        def get_tag_enum(self):
            return ConsensusConfig.Tag.consensus_config_v4

        def get_tag(self):
            return ConsensusConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConsensusConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(ConsensusConfig.cons_len_exact, list) else ConsensusConfig.cons_len_exact

        def get_type_class(self):
            return ConsensusConfig

        # flags : ## 7
        flags: "int" = None
        # new_catchain_ids : Bool
        new_catchain_ids: "bool" = None
        # round_candidates : ## 8
        round_candidates: "int" = None
        # next_candidate_delay_ms : uint32
        next_candidate_delay_ms: "int" = None
        # consensus_timeout_ms : uint32
        consensus_timeout_ms: "int" = None
        # fast_attempts : uint32
        fast_attempts: "int" = None
        # attempt_duration : uint32
        attempt_duration: "int" = None
        # catchain_max_deps : uint32
        catchain_max_deps: "int" = None
        # max_block_bytes : uint32
        max_block_bytes: "int" = None
        # max_collated_bytes : uint32
        max_collated_bytes: "int" = None
        # proto_version : uint16
        proto_version: "int" = None
        # catchain_max_blocks_coeff : uint32
        catchain_max_blocks_coeff: "int" = None

        def __init__(self, flags: "int" = None, new_catchain_ids: "bool" = None, round_candidates: "int" = None, next_candidate_delay_ms: "int" = None, consensus_timeout_ms: "int" = None, fast_attempts: "int" = None, attempt_duration: "int" = None, catchain_max_deps: "int" = None, max_block_bytes: "int" = None, max_collated_bytes: "int" = None, proto_version: "int" = None, catchain_max_blocks_coeff: "int" = None):
            super().__init__()
            self.field_names = []
            self.flags = flags    
            self.field_names.append("flags")
            self.new_catchain_ids = new_catchain_ids    
            self.field_names.append("new_catchain_ids")
            self.round_candidates = round_candidates    
            self.field_names.append("round_candidates")
            self.next_candidate_delay_ms = next_candidate_delay_ms    
            self.field_names.append("next_candidate_delay_ms")
            self.consensus_timeout_ms = consensus_timeout_ms    
            self.field_names.append("consensus_timeout_ms")
            self.fast_attempts = fast_attempts    
            self.field_names.append("fast_attempts")
            self.attempt_duration = attempt_duration    
            self.field_names.append("attempt_duration")
            self.catchain_max_deps = catchain_max_deps    
            self.field_names.append("catchain_max_deps")
            self.max_block_bytes = max_block_bytes    
            self.field_names.append("max_block_bytes")
            self.max_collated_bytes = max_collated_bytes    
            self.field_names.append("max_collated_bytes")
            self.proto_version = proto_version    
            self.field_names.append("proto_version")
            self.catchain_max_blocks_coeff = catchain_max_blocks_coeff    
            self.field_names.append("catchain_max_blocks_coeff")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xd9, 'Cons tag check failed'

                self.flags = cs.load_uint(7)
                assert self.flags == 0, 'Params not equal: flags and 0'

                self.new_catchain_ids = cs.load_bool()
                self.round_candidates = cs.load_uint(8)
                assert 1 <= self.round_candidates, 'Params not equal: 1 and round_candidates'

                self.next_candidate_delay_ms = cs.load_uint(32)
                self.consensus_timeout_ms = cs.load_uint(32)
                self.fast_attempts = cs.load_uint(32)
                self.attempt_duration = cs.load_uint(32)
                self.catchain_max_deps = cs.load_uint(32)
                self.max_block_bytes = cs.load_uint(32)
                self.max_collated_bytes = cs.load_uint(32)
                self.proto_version = cs.load_uint(16)
                self.catchain_max_blocks_coeff = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConsensusConfig")


# class for type `ValidatorTempKey`
class ValidatorTempKey(TLBComplex):
    class Tag(Enum):
        validator_temp_key = 0

    cons_len_exact = 4
    cons_tag = [3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorTempKey.Tag.validator_temp_key: ValidatorTempKey.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorTempKey.Tag"]:
        return ValidatorTempKey.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ValidatorTempKey.Tag.validator_temp_key

        def get_tag(self):
            return ValidatorTempKey.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorTempKey.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorTempKey.cons_len_exact, list) else ValidatorTempKey.cons_len_exact

        def get_type_class(self):
            return ValidatorTempKey

        # adnl_addr : bits256
        adnl_addr: "bitstring.BitArray" = None
        # temp_public_key : SigPubKey
        temp_public_key: "CellSlice" = None
        # seqno : #
        seqno: "int" = None
        # valid_until : uint32
        valid_until: "int" = None

        def __init__(self, adnl_addr: "bitstring.BitArray" = None, temp_public_key: "CellSlice" = None, seqno: "int" = None, valid_until: "int" = None):
            super().__init__()
            self.field_names = []
            self.adnl_addr = adnl_addr    
            self.field_names.append("adnl_addr")
            self.temp_public_key = temp_public_key    
            self.field_names.append("temp_public_key")
            self.seqno = seqno    
            self.field_names.append("seqno")
            self.valid_until = valid_until    
            self.field_names.append("valid_until")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 3, 'Cons tag check failed'

                self.adnl_addr = cs.load_bitstring(256)
                self.temp_public_key = cs.load_subslice(288)
                
                if rec_unpack:
                    self.temp_public_key = TLBComplex.constants["t_SigPubKey"].fetch(self.temp_public_key, True, strict) # at 1
                    assert self.temp_public_key is not None

                self.seqno = cs.load_uint(32)

                self.valid_until = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorTempKey")


# class for type `ValidatorSignedTempKey`
class ValidatorSignedTempKey(TLBComplex):
    class Tag(Enum):
        signed_temp_key = 0

    cons_len_exact = 4
    cons_tag = [4]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorSignedTempKey.Tag.signed_temp_key: ValidatorSignedTempKey.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorSignedTempKey.Tag"]:
        return ValidatorSignedTempKey.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ValidatorSignedTempKey.Tag.signed_temp_key

        def get_tag(self):
            return ValidatorSignedTempKey.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorSignedTempKey.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorSignedTempKey.cons_len_exact, list) else ValidatorSignedTempKey.cons_len_exact

        def get_type_class(self):
            return ValidatorSignedTempKey

        # key : ^ValidatorTempKey
        key: "Cell" = None
        # signature : CryptoSignature
        signature: "CellSlice" = None

        def __init__(self, key: "Cell" = None, signature: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.key = key    
            self.field_names.append("key")
            self.signature = signature    
            self.field_names.append("signature")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 4, 'Cons tag check failed'

                self.key = cs.load_ref()
                
                if rec_unpack:
                    self.key = TLBComplex.constants["t_Ref_ValidatorTempKey"].fetch(self.key, True, strict) # at 1
                    assert self.key is not None

                self.signature = TLBComplex.constants["t_CryptoSignature"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorSignedTempKey")


# class for type `MisbehaviourPunishmentConfig`
class MisbehaviourPunishmentConfig(TLBComplex):
    class Tag(Enum):
        misbehaviour_punishment_config_v1 = 0

    cons_len_exact = 8
    cons_tag = [1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {MisbehaviourPunishmentConfig.Tag.misbehaviour_punishment_config_v1: MisbehaviourPunishmentConfig.Record}

    def get_tag(self, cs: CellSlice) -> Optional["MisbehaviourPunishmentConfig.Tag"]:
        return MisbehaviourPunishmentConfig.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return MisbehaviourPunishmentConfig.Tag.misbehaviour_punishment_config_v1

        def get_tag(self):
            return MisbehaviourPunishmentConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return MisbehaviourPunishmentConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(MisbehaviourPunishmentConfig.cons_len_exact, list) else MisbehaviourPunishmentConfig.cons_len_exact

        def get_type_class(self):
            return MisbehaviourPunishmentConfig

        # default_flat_fine : Grams
        default_flat_fine: "CellSlice" = None
        # default_proportional_fine : uint32
        default_proportional_fine: "int" = None
        # severity_flat_mult : uint16
        severity_flat_mult: "int" = None
        # severity_proportional_mult : uint16
        severity_proportional_mult: "int" = None
        # unpunishable_interval : uint16
        unpunishable_interval: "int" = None
        # long_interval : uint16
        long_interval: "int" = None
        # long_flat_mult : uint16
        long_flat_mult: "int" = None
        # long_proportional_mult : uint16
        long_proportional_mult: "int" = None
        # medium_interval : uint16
        medium_interval: "int" = None
        # medium_flat_mult : uint16
        medium_flat_mult: "int" = None
        # medium_proportional_mult : uint16
        medium_proportional_mult: "int" = None

        def __init__(self, default_flat_fine: "CellSlice" = None, default_proportional_fine: "int" = None, severity_flat_mult: "int" = None, severity_proportional_mult: "int" = None, unpunishable_interval: "int" = None, long_interval: "int" = None, long_flat_mult: "int" = None, long_proportional_mult: "int" = None, medium_interval: "int" = None, medium_flat_mult: "int" = None, medium_proportional_mult: "int" = None):
            super().__init__()
            self.field_names = []
            self.default_flat_fine = default_flat_fine    
            self.field_names.append("default_flat_fine")
            self.default_proportional_fine = default_proportional_fine    
            self.field_names.append("default_proportional_fine")
            self.severity_flat_mult = severity_flat_mult    
            self.field_names.append("severity_flat_mult")
            self.severity_proportional_mult = severity_proportional_mult    
            self.field_names.append("severity_proportional_mult")
            self.unpunishable_interval = unpunishable_interval    
            self.field_names.append("unpunishable_interval")
            self.long_interval = long_interval    
            self.field_names.append("long_interval")
            self.long_flat_mult = long_flat_mult    
            self.field_names.append("long_flat_mult")
            self.long_proportional_mult = long_proportional_mult    
            self.field_names.append("long_proportional_mult")
            self.medium_interval = medium_interval    
            self.field_names.append("medium_interval")
            self.medium_flat_mult = medium_flat_mult    
            self.field_names.append("medium_flat_mult")
            self.medium_proportional_mult = medium_proportional_mult    
            self.field_names.append("medium_proportional_mult")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 1, 'Cons tag check failed'

                self.default_flat_fine = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.default_proportional_fine = cs.load_uint(32)
                self.severity_flat_mult = cs.load_uint(16)
                self.severity_proportional_mult = cs.load_uint(16)
                self.unpunishable_interval = cs.load_uint(16)
                self.long_interval = cs.load_uint(16)
                self.long_flat_mult = cs.load_uint(16)
                self.long_proportional_mult = cs.load_uint(16)
                self.medium_interval = cs.load_uint(16)
                self.medium_flat_mult = cs.load_uint(16)
                self.medium_proportional_mult = cs.load_uint(16)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("MisbehaviourPunishmentConfig")


# class for type `SizeLimitsConfig`
class SizeLimitsConfig(TLBComplex):
    class Tag(Enum):
        size_limits_config = 0
        size_limits_config_v2 = 1

    cons_len_exact = 8
    cons_tag = [1, 2]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SizeLimitsConfig.Tag.size_limits_config: SizeLimitsConfig.Record_size_limits_config, SizeLimitsConfig.Tag.size_limits_config_v2: SizeLimitsConfig.Record_size_limits_config_v2}

    def get_tag(self, cs: CellSlice) -> Optional["SizeLimitsConfig.Tag"]:
        tag = int(cs.bselect(6, 3))
        if tag == 0:
            return SizeLimitsConfig.Tag.size_limits_config_v2 if cs.bit_at(6) else SizeLimitsConfig.Tag.size_limits_config
        return None



    class Record_size_limits_config(RecordBase):
        def get_tag_enum(self):
            return SizeLimitsConfig.Tag.size_limits_config

        def get_tag(self):
            return SizeLimitsConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SizeLimitsConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(SizeLimitsConfig.cons_len_exact, list) else SizeLimitsConfig.cons_len_exact

        def get_type_class(self):
            return SizeLimitsConfig

        # max_msg_bits : uint32
        max_msg_bits: "int" = None
        # max_msg_cells : uint32
        max_msg_cells: "int" = None
        # max_library_cells : uint32
        max_library_cells: "int" = None
        # max_vm_data_depth : uint16
        max_vm_data_depth: "int" = None
        # max_ext_msg_size : uint32
        max_ext_msg_size: "int" = None
        # max_ext_msg_depth : uint16
        max_ext_msg_depth: "int" = None

        def __init__(self, max_msg_bits: "int" = None, max_msg_cells: "int" = None, max_library_cells: "int" = None, max_vm_data_depth: "int" = None, max_ext_msg_size: "int" = None, max_ext_msg_depth: "int" = None):
            super().__init__()
            self.field_names = []
            self.max_msg_bits = max_msg_bits    
            self.field_names.append("max_msg_bits")
            self.max_msg_cells = max_msg_cells    
            self.field_names.append("max_msg_cells")
            self.max_library_cells = max_library_cells    
            self.field_names.append("max_library_cells")
            self.max_vm_data_depth = max_vm_data_depth    
            self.field_names.append("max_vm_data_depth")
            self.max_ext_msg_size = max_ext_msg_size    
            self.field_names.append("max_ext_msg_size")
            self.max_ext_msg_depth = max_ext_msg_depth    
            self.field_names.append("max_ext_msg_depth")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 1, 'Cons tag check failed'

                self.max_msg_bits = cs.load_uint(32)
                self.max_msg_cells = cs.load_uint(32)
                self.max_library_cells = cs.load_uint(32)
                self.max_vm_data_depth = cs.load_uint(16)
                self.max_ext_msg_size = cs.load_uint(32)
                self.max_ext_msg_depth = cs.load_uint(16)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_size_limits_config_v2(RecordBase):
        def get_tag_enum(self):
            return SizeLimitsConfig.Tag.size_limits_config_v2

        def get_tag(self):
            return SizeLimitsConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SizeLimitsConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(SizeLimitsConfig.cons_len_exact, list) else SizeLimitsConfig.cons_len_exact

        def get_type_class(self):
            return SizeLimitsConfig

        # max_msg_bits : uint32
        max_msg_bits: "int" = None
        # max_msg_cells : uint32
        max_msg_cells: "int" = None
        # max_library_cells : uint32
        max_library_cells: "int" = None
        # max_vm_data_depth : uint16
        max_vm_data_depth: "int" = None
        # max_ext_msg_size : uint32
        max_ext_msg_size: "int" = None
        # max_ext_msg_depth : uint16
        max_ext_msg_depth: "int" = None
        # max_acc_state_cells : uint32
        max_acc_state_cells: "int" = None
        # max_acc_state_bits : uint32
        max_acc_state_bits: "int" = None

        def __init__(self, max_msg_bits: "int" = None, max_msg_cells: "int" = None, max_library_cells: "int" = None, max_vm_data_depth: "int" = None, max_ext_msg_size: "int" = None, max_ext_msg_depth: "int" = None, max_acc_state_cells: "int" = None, max_acc_state_bits: "int" = None):
            super().__init__()
            self.field_names = []
            self.max_msg_bits = max_msg_bits    
            self.field_names.append("max_msg_bits")
            self.max_msg_cells = max_msg_cells    
            self.field_names.append("max_msg_cells")
            self.max_library_cells = max_library_cells    
            self.field_names.append("max_library_cells")
            self.max_vm_data_depth = max_vm_data_depth    
            self.field_names.append("max_vm_data_depth")
            self.max_ext_msg_size = max_ext_msg_size    
            self.field_names.append("max_ext_msg_size")
            self.max_ext_msg_depth = max_ext_msg_depth    
            self.field_names.append("max_ext_msg_depth")
            self.max_acc_state_cells = max_acc_state_cells    
            self.field_names.append("max_acc_state_cells")
            self.max_acc_state_bits = max_acc_state_bits    
            self.field_names.append("max_acc_state_bits")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 2, 'Cons tag check failed'

                self.max_msg_bits = cs.load_uint(32)
                self.max_msg_cells = cs.load_uint(32)
                self.max_library_cells = cs.load_uint(32)
                self.max_vm_data_depth = cs.load_uint(16)
                self.max_ext_msg_size = cs.load_uint(32)
                self.max_ext_msg_depth = cs.load_uint(16)
                self.max_acc_state_cells = cs.load_uint(32)
                self.max_acc_state_bits = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SizeLimitsConfig")


# class for type `SuspendedAddressList`
class SuspendedAddressList(TLBComplex):
    class Tag(Enum):
        suspended_address_list = 0

    cons_len_exact = 8
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SuspendedAddressList.Tag.suspended_address_list: SuspendedAddressList.Record}

    def get_tag(self, cs: CellSlice) -> Optional["SuspendedAddressList.Tag"]:
        return SuspendedAddressList.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return SuspendedAddressList.Tag.suspended_address_list

        def get_tag(self):
            return SuspendedAddressList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SuspendedAddressList.cons_len_exact[self.get_tag_enum().value] if isinstance(SuspendedAddressList.cons_len_exact, list) else SuspendedAddressList.cons_len_exact

        def get_type_class(self):
            return SuspendedAddressList

        # addresses : HashmapE 288 Unit
        addresses: "CellSlice" = None
        # suspended_until : uint32
        suspended_until: "int" = None

        def __init__(self, addresses: "CellSlice" = None, suspended_until: "int" = None):
            super().__init__()
            self.field_names = []
            self.addresses = addresses    
            self.field_names.append("addresses")
            self.suspended_until = suspended_until    
            self.field_names.append("suspended_until")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0, 'Cons tag check failed'

                self.addresses = TLBComplex.constants["t_HashmapE_288_Unit"].fetch(cs) 
                self.suspended_until = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SuspendedAddressList")


# class for type `OracleBridgeParams`
class OracleBridgeParams(TLBComplex):
    class Tag(Enum):
        oracle_bridge_params = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {OracleBridgeParams.Tag.oracle_bridge_params: OracleBridgeParams.Record}

    def get_tag(self, cs: CellSlice) -> Optional["OracleBridgeParams.Tag"]:
        return OracleBridgeParams.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return OracleBridgeParams.Tag.oracle_bridge_params

        def get_tag(self):
            return OracleBridgeParams.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return OracleBridgeParams.cons_len_exact[self.get_tag_enum().value] if isinstance(OracleBridgeParams.cons_len_exact, list) else OracleBridgeParams.cons_len_exact

        def get_type_class(self):
            return OracleBridgeParams

        # bridge_address : bits256
        bridge_address: "bitstring.BitArray" = None
        # oracle_mutlisig_address : bits256
        oracle_mutlisig_address: "bitstring.BitArray" = None
        # oracles : HashmapE 256 uint256
        oracles: "CellSlice" = None
        # external_chain_address : bits256
        external_chain_address: "bitstring.BitArray" = None

        def __init__(self, bridge_address: "bitstring.BitArray" = None, oracle_mutlisig_address: "bitstring.BitArray" = None, oracles: "CellSlice" = None, external_chain_address: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.bridge_address = bridge_address    
            self.field_names.append("bridge_address")
            self.oracle_mutlisig_address = oracle_mutlisig_address    
            self.field_names.append("oracle_mutlisig_address")
            self.oracles = oracles    
            self.field_names.append("oracles")
            self.external_chain_address = external_chain_address    
            self.field_names.append("external_chain_address")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.bridge_address = cs.load_bitstring(256)
                self.oracle_mutlisig_address = cs.load_bitstring(256)
                self.oracles = TLBComplex.constants["t_HashmapE_256_uint256"].fetch(cs) 
                self.external_chain_address = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("OracleBridgeParams")


# class for type `JettonBridgePrices`
class JettonBridgePrices(TLBComplex):
    class Tag(Enum):
        jetton_bridge_prices = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {JettonBridgePrices.Tag.jetton_bridge_prices: JettonBridgePrices.Record}

    def get_tag(self, cs: CellSlice) -> Optional["JettonBridgePrices.Tag"]:
        return JettonBridgePrices.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return JettonBridgePrices.Tag.jetton_bridge_prices

        def get_tag(self):
            return JettonBridgePrices.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return JettonBridgePrices.cons_len_exact[self.get_tag_enum().value] if isinstance(JettonBridgePrices.cons_len_exact, list) else JettonBridgePrices.cons_len_exact

        def get_type_class(self):
            return JettonBridgePrices

        # bridge_burn_fee : Coins
        bridge_burn_fee: "CellSlice" = None
        # bridge_mint_fee : Coins
        bridge_mint_fee: "CellSlice" = None
        # wallet_min_tons_for_storage : Coins
        wallet_min_tons_for_storage: "CellSlice" = None
        # wallet_gas_consumption : Coins
        wallet_gas_consumption: "CellSlice" = None
        # minter_min_tons_for_storage : Coins
        minter_min_tons_for_storage: "CellSlice" = None
        # discover_gas_consumption : Coins
        discover_gas_consumption: "CellSlice" = None

        def __init__(self, bridge_burn_fee: "CellSlice" = None, bridge_mint_fee: "CellSlice" = None, wallet_min_tons_for_storage: "CellSlice" = None, wallet_gas_consumption: "CellSlice" = None, minter_min_tons_for_storage: "CellSlice" = None, discover_gas_consumption: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.bridge_burn_fee = bridge_burn_fee    
            self.field_names.append("bridge_burn_fee")
            self.bridge_mint_fee = bridge_mint_fee    
            self.field_names.append("bridge_mint_fee")
            self.wallet_min_tons_for_storage = wallet_min_tons_for_storage    
            self.field_names.append("wallet_min_tons_for_storage")
            self.wallet_gas_consumption = wallet_gas_consumption    
            self.field_names.append("wallet_gas_consumption")
            self.minter_min_tons_for_storage = minter_min_tons_for_storage    
            self.field_names.append("minter_min_tons_for_storage")
            self.discover_gas_consumption = discover_gas_consumption    
            self.field_names.append("discover_gas_consumption")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.bridge_burn_fee = TLBComplex.constants["t_Coins"].fetch(cs) 
                self.bridge_mint_fee = TLBComplex.constants["t_Coins"].fetch(cs) 
                self.wallet_min_tons_for_storage = TLBComplex.constants["t_Coins"].fetch(cs) 
                self.wallet_gas_consumption = TLBComplex.constants["t_Coins"].fetch(cs) 
                self.minter_min_tons_for_storage = TLBComplex.constants["t_Coins"].fetch(cs) 
                self.discover_gas_consumption = TLBComplex.constants["t_Coins"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("JettonBridgePrices")


# class for type `JettonBridgeParams`
class JettonBridgeParams(TLBComplex):
    class Tag(Enum):
        jetton_bridge_params_v0 = 0
        jetton_bridge_params_v1 = 1

    cons_len_exact = 8
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {JettonBridgeParams.Tag.jetton_bridge_params_v0: JettonBridgeParams.Record_jetton_bridge_params_v0, JettonBridgeParams.Tag.jetton_bridge_params_v1: JettonBridgeParams.Record_jetton_bridge_params_v1}

    def get_tag(self, cs: CellSlice) -> Optional["JettonBridgeParams.Tag"]:
        tag = int(cs.bselect(6, 3))
        if tag == 0:
            return JettonBridgeParams.Tag.jetton_bridge_params_v1 if cs.bit_at(7) else JettonBridgeParams.Tag.jetton_bridge_params_v0
        return None



    class Record_jetton_bridge_params_v0(RecordBase):
        def get_tag_enum(self):
            return JettonBridgeParams.Tag.jetton_bridge_params_v0

        def get_tag(self):
            return JettonBridgeParams.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return JettonBridgeParams.cons_len_exact[self.get_tag_enum().value] if isinstance(JettonBridgeParams.cons_len_exact, list) else JettonBridgeParams.cons_len_exact

        def get_type_class(self):
            return JettonBridgeParams

        # bridge_address : bits256
        bridge_address: "bitstring.BitArray" = None
        # oracles_address : bits256
        oracles_address: "bitstring.BitArray" = None
        # oracles : HashmapE 256 uint256
        oracles: "CellSlice" = None
        # state_flags : uint8
        state_flags: "int" = None
        # burn_bridge_fee : Coins
        burn_bridge_fee: "CellSlice" = None

        def __init__(self, bridge_address: "bitstring.BitArray" = None, oracles_address: "bitstring.BitArray" = None, oracles: "CellSlice" = None, state_flags: "int" = None, burn_bridge_fee: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.bridge_address = bridge_address    
            self.field_names.append("bridge_address")
            self.oracles_address = oracles_address    
            self.field_names.append("oracles_address")
            self.oracles = oracles    
            self.field_names.append("oracles")
            self.state_flags = state_flags    
            self.field_names.append("state_flags")
            self.burn_bridge_fee = burn_bridge_fee    
            self.field_names.append("burn_bridge_fee")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0, 'Cons tag check failed'

                self.bridge_address = cs.load_bitstring(256)
                self.oracles_address = cs.load_bitstring(256)
                self.oracles = TLBComplex.constants["t_HashmapE_256_uint256"].fetch(cs) 
                self.state_flags = cs.load_uint(8)
                self.burn_bridge_fee = TLBComplex.constants["t_Coins"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_jetton_bridge_params_v1(RecordBase):
        def get_tag_enum(self):
            return JettonBridgeParams.Tag.jetton_bridge_params_v1

        def get_tag(self):
            return JettonBridgeParams.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return JettonBridgeParams.cons_len_exact[self.get_tag_enum().value] if isinstance(JettonBridgeParams.cons_len_exact, list) else JettonBridgeParams.cons_len_exact

        def get_type_class(self):
            return JettonBridgeParams

        # bridge_address : bits256
        bridge_address: "bitstring.BitArray" = None
        # oracles_address : bits256
        oracles_address: "bitstring.BitArray" = None
        # oracles : HashmapE 256 uint256
        oracles: "CellSlice" = None
        # state_flags : uint8
        state_flags: "int" = None
        # prices : ^JettonBridgePrices
        prices: "Cell" = None
        # external_chain_address : bits256
        external_chain_address: "bitstring.BitArray" = None

        def __init__(self, bridge_address: "bitstring.BitArray" = None, oracles_address: "bitstring.BitArray" = None, oracles: "CellSlice" = None, state_flags: "int" = None, prices: "Cell" = None, external_chain_address: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.bridge_address = bridge_address    
            self.field_names.append("bridge_address")
            self.oracles_address = oracles_address    
            self.field_names.append("oracles_address")
            self.oracles = oracles    
            self.field_names.append("oracles")
            self.state_flags = state_flags    
            self.field_names.append("state_flags")
            self.prices = prices    
            self.field_names.append("prices")
            self.external_chain_address = external_chain_address    
            self.field_names.append("external_chain_address")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 1, 'Cons tag check failed'

                self.bridge_address = cs.load_bitstring(256)
                self.oracles_address = cs.load_bitstring(256)
                self.oracles = TLBComplex.constants["t_HashmapE_256_uint256"].fetch(cs) 
                self.state_flags = cs.load_uint(8)
                self.prices = cs.load_ref()
                
                if rec_unpack:
                    self.prices = TLBComplex.constants["t_Ref_JettonBridgePrices"].fetch(self.prices, True, strict) # at 1
                    assert self.prices is not None

                self.external_chain_address = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("JettonBridgeParams")


# class for type `ConfigParam`
class ConfigParam(TLBComplex):
    class Tag(Enum):
        cons44 = 0
        cons79 = 1
        cons81 = 2
        cons82 = 3
        cons5 = 4
        cons40 = 5
        cons43 = 6
        cons32 = 7
        cons33 = 8
        cons34 = 9
        cons35 = 10
        cons36 = 11
        cons37 = 12
        cons13 = 13
        config_mc_block_limits = 14
        config_block_limits = 15
        cons14 = 16
        cons0 = 17
        cons1 = 18
        cons2 = 19
        cons3 = 20
        cons4 = 21
        cons6 = 22
        cons7 = 23
        cons9 = 24
        cons10 = 25
        cons12 = 26
        cons15 = 27
        cons16 = 28
        cons17 = 29
        cons18 = 30
        cons19 = 31
        cons31 = 32
        cons39 = 33
        cons71 = 34
        cons72 = 35
        cons73 = 36
        cons11 = 37
        cons28 = 38
        cons8 = 39
        config_mc_gas_prices = 40
        config_gas_prices = 41
        cons29 = 42
        config_mc_fwd_prices = 43
        config_fwd_prices = 44

    cons_len_exact = 0
    cons_tag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {ConfigParam.Tag.cons0: self.get_param_record("Record_cons0"), ConfigParam.Tag.cons1: self.get_param_record("Record_cons1"), ConfigParam.Tag.cons2: self.get_param_record("Record_cons2"), ConfigParam.Tag.cons3: self.get_param_record("Record_cons3"), ConfigParam.Tag.cons4: self.get_param_record("Record_cons4"), ConfigParam.Tag.cons5: self.get_param_record("Record_cons5"), ConfigParam.Tag.cons6: self.get_param_record("Record_cons6"), ConfigParam.Tag.cons7: self.get_param_record("Record_cons7"), ConfigParam.Tag.cons8: self.get_param_record("Record_cons8"), ConfigParam.Tag.cons9: self.get_param_record("Record_cons9"), ConfigParam.Tag.cons10: self.get_param_record("Record_cons10"), ConfigParam.Tag.cons11: self.get_param_record("Record_cons11"), ConfigParam.Tag.cons12: self.get_param_record("Record_cons12"), ConfigParam.Tag.cons13: self.get_param_record("Record_cons13"), ConfigParam.Tag.cons14: self.get_param_record("Record_cons14"), ConfigParam.Tag.cons15: self.get_param_record("Record_cons15"), ConfigParam.Tag.cons16: self.get_param_record("Record_cons16"), ConfigParam.Tag.cons17: self.get_param_record("Record_cons17"), ConfigParam.Tag.cons18: self.get_param_record("Record_cons18"), ConfigParam.Tag.cons19: self.get_param_record("Record_cons19"), ConfigParam.Tag.config_mc_gas_prices: self.get_param_record("Record_config_mc_gas_prices"), ConfigParam.Tag.config_gas_prices: self.get_param_record("Record_config_gas_prices"), ConfigParam.Tag.config_mc_block_limits: self.get_param_record("Record_config_mc_block_limits"), ConfigParam.Tag.config_block_limits: self.get_param_record("Record_config_block_limits"), ConfigParam.Tag.config_mc_fwd_prices: self.get_param_record("Record_config_mc_fwd_prices"), ConfigParam.Tag.config_fwd_prices: self.get_param_record("Record_config_fwd_prices"), ConfigParam.Tag.cons28: self.get_param_record("Record_cons28"), ConfigParam.Tag.cons29: self.get_param_record("Record_cons29"), ConfigParam.Tag.cons31: self.get_param_record("Record_cons31"), ConfigParam.Tag.cons32: self.get_param_record("Record_cons32"), ConfigParam.Tag.cons33: self.get_param_record("Record_cons33"), ConfigParam.Tag.cons34: self.get_param_record("Record_cons34"), ConfigParam.Tag.cons35: self.get_param_record("Record_cons35"), ConfigParam.Tag.cons36: self.get_param_record("Record_cons36"), ConfigParam.Tag.cons37: self.get_param_record("Record_cons37"), ConfigParam.Tag.cons39: self.get_param_record("Record_cons39"), ConfigParam.Tag.cons40: self.get_param_record("Record_cons40"), ConfigParam.Tag.cons43: self.get_param_record("Record_cons43"), ConfigParam.Tag.cons44: self.get_param_record("Record_cons44"), ConfigParam.Tag.cons71: self.get_param_record("Record_cons71"), ConfigParam.Tag.cons72: self.get_param_record("Record_cons72"), ConfigParam.Tag.cons73: self.get_param_record("Record_cons73"), ConfigParam.Tag.cons79: self.get_param_record("Record_cons79"), ConfigParam.Tag.cons81: self.get_param_record("Record_cons81"), ConfigParam.Tag.cons82: self.get_param_record("Record_cons82")}

    def get_tag(self, cs: CellSlice) -> Optional["ConfigParam.Tag"]:
        tag = self.m_

        if tag == 0:
            return ConfigParam.Tag.cons0

        if tag == 1:
            return ConfigParam.Tag.cons1

        if tag == 2:
            return ConfigParam.Tag.cons2

        if tag == 3:
            return ConfigParam.Tag.cons3

        if tag == 4:
            return ConfigParam.Tag.cons4

        if tag == 5:
            return ConfigParam.Tag.cons5

        if tag == 6:
            return ConfigParam.Tag.cons6

        if tag == 7:
            return ConfigParam.Tag.cons7

        if tag == 8:
            return ConfigParam.Tag.cons8

        if tag == 9:
            return ConfigParam.Tag.cons9

        if tag == 10:
            return ConfigParam.Tag.cons10

        if tag == 11:
            return ConfigParam.Tag.cons11

        if tag == 12:
            return ConfigParam.Tag.cons12

        if tag == 13:
            return ConfigParam.Tag.cons13

        if tag == 14:
            return ConfigParam.Tag.cons14

        if tag == 15:
            return ConfigParam.Tag.cons15

        if tag == 16:
            return ConfigParam.Tag.cons16

        if tag == 17:
            return ConfigParam.Tag.cons17

        if tag == 18:
            return ConfigParam.Tag.cons18

        if tag == 19:
            return ConfigParam.Tag.cons19

        if tag == 20:
            return ConfigParam.Tag.config_mc_gas_prices

        if tag == 21:
            return ConfigParam.Tag.config_gas_prices

        if tag == 22:
            return ConfigParam.Tag.config_mc_block_limits

        if tag == 23:
            return ConfigParam.Tag.config_block_limits

        if tag == 24:
            return ConfigParam.Tag.config_mc_fwd_prices

        if tag == 25:
            return ConfigParam.Tag.config_fwd_prices

        if tag == 28:
            return ConfigParam.Tag.cons28

        if tag == 29:
            return ConfigParam.Tag.cons29

        if tag == 31:
            return ConfigParam.Tag.cons31

        if tag == 32:
            return ConfigParam.Tag.cons32

        if tag == 33:
            return ConfigParam.Tag.cons33

        if tag == 34:
            return ConfigParam.Tag.cons34

        if tag == 35:
            return ConfigParam.Tag.cons35

        if tag == 36:
            return ConfigParam.Tag.cons36

        if tag == 37:
            return ConfigParam.Tag.cons37

        if tag == 39:
            return ConfigParam.Tag.cons39

        if tag == 40:
            return ConfigParam.Tag.cons40

        if tag == 43:
            return ConfigParam.Tag.cons43

        if tag == 44:
            return ConfigParam.Tag.cons44

        if tag == 71:
            return ConfigParam.Tag.cons71

        if tag == 72:
            return ConfigParam.Tag.cons72

        if tag == 73:
            return ConfigParam.Tag.cons73

        if tag == 79:
            return ConfigParam.Tag.cons79

        if tag == 81:
            return ConfigParam.Tag.cons81

        if tag == 82:
            return ConfigParam.Tag.cons82

        return None


    class Record_cons0(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons0

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # config_addr : bits256
        config_addr: "bitstring.BitArray" = None

        def __init__(self, config_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.config_addr = config_addr    
            self.field_names.append("config_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.config_addr = cs.load_bitstring(256)
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons1(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons1

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # elector_addr : bits256
        elector_addr: "bitstring.BitArray" = None

        def __init__(self, elector_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.elector_addr = elector_addr    
            self.field_names.append("elector_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.elector_addr = cs.load_bitstring(256)
                self.m_ == 1                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons2(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons2

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # minter_addr : bits256
        minter_addr: "bitstring.BitArray" = None

        def __init__(self, minter_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.minter_addr = minter_addr    
            self.field_names.append("minter_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.minter_addr = cs.load_bitstring(256)
                self.m_ == 2                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons3(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons3

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # fee_collector_addr : bits256
        fee_collector_addr: "bitstring.BitArray" = None

        def __init__(self, fee_collector_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.fee_collector_addr = fee_collector_addr    
            self.field_names.append("fee_collector_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.fee_collector_addr = cs.load_bitstring(256)
                self.m_ == 3                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons4(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons4

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # dns_root_addr : bits256
        dns_root_addr: "bitstring.BitArray" = None

        def __init__(self, dns_root_addr: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.dns_root_addr = dns_root_addr    
            self.field_names.append("dns_root_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.dns_root_addr = cs.load_bitstring(256)
                self.m_ == 4                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons5(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons5

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # BurningConfig
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_BurningConfig"].fetch(cs) 
                self.m_ == 5                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons6(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons6

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # mint_new_price : Grams
        mint_new_price: "CellSlice" = None
        # mint_add_price : Grams
        mint_add_price: "CellSlice" = None

        def __init__(self, mint_new_price: "CellSlice" = None, mint_add_price: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.mint_new_price = mint_new_price    
            self.field_names.append("mint_new_price")
            self.mint_add_price = mint_add_price    
            self.field_names.append("mint_add_price")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.mint_new_price = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.mint_add_price = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.m_ == 6                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons7(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons7

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # to_mint : ExtraCurrencyCollection
        to_mint: "CellSlice" = None

        def __init__(self, to_mint: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.to_mint = to_mint    
            self.field_names.append("to_mint")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.to_mint = TLBComplex.constants["t_ExtraCurrencyCollection"].fetch(cs) 
                self.m_ == 7                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons8(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons8

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # GlobalVersion
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice(104)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_GlobalVersion"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None

                self.m_ == 8                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons9(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons9

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # mandatory_params : Hashmap 32 Truet
        mandatory_params: "CellSlice" = None

        def __init__(self, mandatory_params: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.mandatory_params = mandatory_params    
            self.field_names.append("mandatory_params")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.mandatory_params = TLBComplex.constants["t_Hashmap_32_Truet"].fetch(cs) 
                self.m_ == 9                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons10(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons10

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # critical_params : Hashmap 32 Truet
        critical_params: "CellSlice" = None

        def __init__(self, critical_params: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.critical_params = critical_params    
            self.field_names.append("critical_params")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.critical_params = TLBComplex.constants["t_Hashmap_32_Truet"].fetch(cs) 
                self.m_ == 10                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons11(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons11

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # ConfigVotingSetup
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice_ext(0x20008)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_ConfigVotingSetup"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None

                self.m_ == 11                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons12(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons12

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # workchains : HashmapE 32 WorkchainDescr
        workchains: "CellSlice" = None

        def __init__(self, workchains: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.workchains = workchains    
            self.field_names.append("workchains")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.workchains = TLBComplex.constants["t_HashmapE_32_WorkchainDescr"].fetch(cs) 
                self.m_ == 12                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons13(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons13

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # ComplaintPricing
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_ComplaintPricing"].fetch(cs) 
                self.m_ == 13                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons14(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons14

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # BlockCreateFees
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_BlockCreateFees"].fetch(cs) 
                self.m_ == 14                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons15(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons15

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # validators_elected_for : uint32
        validators_elected_for: "int" = None
        # elections_start_before : uint32
        elections_start_before: "int" = None
        # elections_end_before : uint32
        elections_end_before: "int" = None
        # stake_held_for : uint32
        stake_held_for: "int" = None

        def __init__(self, validators_elected_for: "int" = None, elections_start_before: "int" = None, elections_end_before: "int" = None, stake_held_for: "int" = None):
            super().__init__()
            self.field_names = []
            self.validators_elected_for = validators_elected_for    
            self.field_names.append("validators_elected_for")
            self.elections_start_before = elections_start_before    
            self.field_names.append("elections_start_before")
            self.elections_end_before = elections_end_before    
            self.field_names.append("elections_end_before")
            self.stake_held_for = stake_held_for    
            self.field_names.append("stake_held_for")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.validators_elected_for = cs.load_uint(32)
                self.elections_start_before = cs.load_uint(32)
                self.elections_end_before = cs.load_uint(32)
                self.stake_held_for = cs.load_uint(32)
                self.m_ == 15                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons16(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons16

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # max_validators : ## 16
        max_validators: "int" = None
        # max_main_validators : ## 16
        max_main_validators: "int" = None
        # min_validators : ## 16
        min_validators: "int" = None

        def __init__(self, max_validators: "int" = None, max_main_validators: "int" = None, min_validators: "int" = None):
            super().__init__()
            self.field_names = []
            self.max_validators = max_validators    
            self.field_names.append("max_validators")
            self.max_main_validators = max_main_validators    
            self.field_names.append("max_main_validators")
            self.min_validators = min_validators    
            self.field_names.append("min_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.max_validators = cs.load_uint(16)
                self.max_main_validators = cs.load_uint(16)
                self.min_validators = cs.load_uint(16)
                assert self.max_main_validators <= self.max_validators, 'Params not equal: max_main_validators and max_validators'

                assert self.min_validators <= self.max_main_validators, 'Params not equal: min_validators and max_main_validators'

                assert 1 <= self.min_validators, 'Params not equal: 1 and min_validators'

                self.m_ == 16                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons17(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons17

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # min_stake : Grams
        min_stake: "CellSlice" = None
        # max_stake : Grams
        max_stake: "CellSlice" = None
        # min_total_stake : Grams
        min_total_stake: "CellSlice" = None
        # max_stake_factor : uint32
        max_stake_factor: "int" = None

        def __init__(self, min_stake: "CellSlice" = None, max_stake: "CellSlice" = None, min_total_stake: "CellSlice" = None, max_stake_factor: "int" = None):
            super().__init__()
            self.field_names = []
            self.min_stake = min_stake    
            self.field_names.append("min_stake")
            self.max_stake = max_stake    
            self.field_names.append("max_stake")
            self.min_total_stake = min_total_stake    
            self.field_names.append("min_total_stake")
            self.max_stake_factor = max_stake_factor    
            self.field_names.append("max_stake_factor")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.min_stake = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.max_stake = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.min_total_stake = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.max_stake_factor = cs.load_uint(32)
                self.m_ == 17                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons18(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons18

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # Hashmap 32 StoragePrices
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_Hashmap_32_StoragePrices"].fetch(cs) 
                self.m_ == 18                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons19(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons19

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # global_id : int32
        global_id: "int" = None

        def __init__(self, global_id: "int" = None):
            super().__init__()
            self.field_names = []
            self.global_id = global_id    
            self.field_names.append("global_id")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.global_id = cs.load_int(32)
                self.m_ == 19                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_config_mc_gas_prices(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.config_mc_gas_prices

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # GasLimitsPrices
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_GasLimitsPrices"].fetch(cs) 
                self.m_ == 20                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_config_gas_prices(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.config_gas_prices

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # GasLimitsPrices
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_GasLimitsPrices"].fetch(cs) 
                self.m_ == 21                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_config_mc_block_limits(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.config_mc_block_limits

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # BlockLimits
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice(320)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_BlockLimits"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None

                self.m_ == 22                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_config_block_limits(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.config_block_limits

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # BlockLimits
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice(320)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_BlockLimits"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None

                self.m_ == 23                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_config_mc_fwd_prices(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.config_mc_fwd_prices

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # MsgForwardPrices
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice(264)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_MsgForwardPrices"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None

                self.m_ == 24                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_config_fwd_prices(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.config_fwd_prices

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # MsgForwardPrices
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = cs.load_subslice(264)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_MsgForwardPrices"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None

                self.m_ == 25                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons28(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons28

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # CatchainConfig
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_CatchainConfig"].fetch(cs) 
                self.m_ == 28                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons29(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons29

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # ConsensusConfig
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_ConsensusConfig"].fetch(cs) 
                self.m_ == 29                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons31(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons31

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # fundamental_smc_addr : HashmapE 256 Truet
        fundamental_smc_addr: "CellSlice" = None

        def __init__(self, fundamental_smc_addr: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.fundamental_smc_addr = fundamental_smc_addr    
            self.field_names.append("fundamental_smc_addr")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.fundamental_smc_addr = TLBComplex.constants["t_HashmapE_256_Truet"].fetch(cs) 
                self.m_ == 31                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons32(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons32

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # prev_validators : ValidatorSet
        prev_validators: "CellSlice" = None

        def __init__(self, prev_validators: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.prev_validators = prev_validators    
            self.field_names.append("prev_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev_validators = TLBComplex.constants["t_ValidatorSet"].fetch(cs) 
                self.m_ == 32                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons33(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons33

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # prev_temp_validators : ValidatorSet
        prev_temp_validators: "CellSlice" = None

        def __init__(self, prev_temp_validators: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.prev_temp_validators = prev_temp_validators    
            self.field_names.append("prev_temp_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.prev_temp_validators = TLBComplex.constants["t_ValidatorSet"].fetch(cs) 
                self.m_ == 33                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons34(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons34

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # cur_validators : ValidatorSet
        cur_validators: "CellSlice" = None

        def __init__(self, cur_validators: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cur_validators = cur_validators    
            self.field_names.append("cur_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cur_validators = TLBComplex.constants["t_ValidatorSet"].fetch(cs) 
                self.m_ == 34                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons35(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons35

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # cur_temp_validators : ValidatorSet
        cur_temp_validators: "CellSlice" = None

        def __init__(self, cur_temp_validators: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cur_temp_validators = cur_temp_validators    
            self.field_names.append("cur_temp_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cur_temp_validators = TLBComplex.constants["t_ValidatorSet"].fetch(cs) 
                self.m_ == 35                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons36(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons36

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # next_validators : ValidatorSet
        next_validators: "CellSlice" = None

        def __init__(self, next_validators: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.next_validators = next_validators    
            self.field_names.append("next_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.next_validators = TLBComplex.constants["t_ValidatorSet"].fetch(cs) 
                self.m_ == 36                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons37(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons37

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # next_temp_validators : ValidatorSet
        next_temp_validators: "CellSlice" = None

        def __init__(self, next_temp_validators: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.next_temp_validators = next_temp_validators    
            self.field_names.append("next_temp_validators")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.next_temp_validators = TLBComplex.constants["t_ValidatorSet"].fetch(cs) 
                self.m_ == 37                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons39(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons39

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # HashmapE 256 ValidatorSignedTempKey
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapE_256_ValidatorSignedTempKey"].fetch(cs) 
                self.m_ == 39                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons40(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons40

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # MisbehaviourPunishmentConfig
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_MisbehaviourPunishmentConfig"].fetch(cs) 
                self.m_ == 40                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons43(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons43

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # SizeLimitsConfig
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_SizeLimitsConfig"].fetch(cs) 
                self.m_ == 43                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons44(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons44

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # SuspendedAddressList
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_SuspendedAddressList"].fetch(cs) 
                self.m_ == 44                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons71(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons71

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # OracleBridgeParams
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_OracleBridgeParams"].fetch(cs) 
                self.m_ == 71                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons72(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons72

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # OracleBridgeParams
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_OracleBridgeParams"].fetch(cs) 
                self.m_ == 72                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons73(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons73

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # OracleBridgeParams
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_OracleBridgeParams"].fetch(cs) 
                self.m_ == 73                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons79(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons79

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # JettonBridgeParams
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_JettonBridgeParams"].fetch(cs) 
                self.m_ == 79                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons81(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons81

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # JettonBridgeParams
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_JettonBridgeParams"].fetch(cs) 
                self.m_ == 81                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cons82(RecordBase):
        def get_tag_enum(self):
            return ConfigParam.Tag.cons82

        def get_tag(self):
            return ConfigParam.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ConfigParam.cons_len_exact[self.get_tag_enum().value] if isinstance(ConfigParam.cons_len_exact, list) else ConfigParam.cons_len_exact

        def get_type_class(self):
            return ConfigParam

        # JettonBridgeParams
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_JettonBridgeParams"].fetch(cs) 
                self.m_ == 82                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ConfigParam")


# class for type `BlockSignaturesPure`
class BlockSignaturesPure(TLBComplex):
    class Tag(Enum):
        block_signatures_pure = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockSignaturesPure.Tag.block_signatures_pure: BlockSignaturesPure.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockSignaturesPure.Tag"]:
        return BlockSignaturesPure.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockSignaturesPure.Tag.block_signatures_pure

        def get_tag(self):
            return BlockSignaturesPure.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockSignaturesPure.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockSignaturesPure.cons_len_exact, list) else BlockSignaturesPure.cons_len_exact

        def get_type_class(self):
            return BlockSignaturesPure

        # sig_count : uint32
        sig_count: "int" = None
        # sig_weight : uint64
        sig_weight: "int" = None
        # signatures : HashmapE 16 CryptoSignaturePair
        signatures: "CellSlice" = None

        def __init__(self, sig_count: "int" = None, sig_weight: "int" = None, signatures: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.sig_count = sig_count    
            self.field_names.append("sig_count")
            self.sig_weight = sig_weight    
            self.field_names.append("sig_weight")
            self.signatures = signatures    
            self.field_names.append("signatures")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.sig_count = cs.load_uint(32)
                self.sig_weight = cs.load_uint(64)
                self.signatures = TLBComplex.constants["t_HashmapE_16_CryptoSignaturePair"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockSignaturesPure")


# class for type `BlockSignatures`
class BlockSignatures(TLBComplex):
    class Tag(Enum):
        block_signatures = 0

    cons_len_exact = 8
    cons_tag = [17]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockSignatures.Tag.block_signatures: BlockSignatures.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockSignatures.Tag"]:
        return BlockSignatures.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockSignatures.Tag.block_signatures

        def get_tag(self):
            return BlockSignatures.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockSignatures.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockSignatures.cons_len_exact, list) else BlockSignatures.cons_len_exact

        def get_type_class(self):
            return BlockSignatures

        # validator_info : ValidatorBaseInfo
        validator_info: "CellSlice" = None
        # pure_signatures : BlockSignaturesPure
        pure_signatures: "CellSlice" = None

        def __init__(self, validator_info: "CellSlice" = None, pure_signatures: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.validator_info = validator_info    
            self.field_names.append("validator_info")
            self.pure_signatures = pure_signatures    
            self.field_names.append("pure_signatures")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 17, 'Cons tag check failed'

                self.validator_info = cs.load_subslice(64)
                
                if rec_unpack:
                    self.validator_info = TLBComplex.constants["t_ValidatorBaseInfo"].fetch(self.validator_info, True, strict) # at 1
                    assert self.validator_info is not None

                self.pure_signatures = TLBComplex.constants["t_BlockSignaturesPure"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockSignatures")


# class for type `BlockProof`
class BlockProof(TLBComplex):
    class Tag(Enum):
        block_proof = 0

    cons_len_exact = 8
    cons_tag = [0xc3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {BlockProof.Tag.block_proof: BlockProof.Record}

    def get_tag(self, cs: CellSlice) -> Optional["BlockProof.Tag"]:
        return BlockProof.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return BlockProof.Tag.block_proof

        def get_tag(self):
            return BlockProof.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return BlockProof.cons_len_exact[self.get_tag_enum().value] if isinstance(BlockProof.cons_len_exact, list) else BlockProof.cons_len_exact

        def get_type_class(self):
            return BlockProof

        # proof_for : BlockIdExt
        proof_for: "CellSlice" = None
        # root : ^Cell
        root: "Cell" = None
        # signatures : Maybe ^BlockSignatures
        signatures: "CellSlice" = None

        def __init__(self, proof_for: "CellSlice" = None, root: "Cell" = None, signatures: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.proof_for = proof_for    
            self.field_names.append("proof_for")
            self.root = root    
            self.field_names.append("root")
            self.signatures = signatures    
            self.field_names.append("signatures")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xc3, 'Cons tag check failed'

                self.proof_for = cs.load_subslice(648)
                
                if rec_unpack:
                    self.proof_for = TLBComplex.constants["t_BlockIdExt"].fetch(self.proof_for, True, strict) # at 1
                    assert self.proof_for is not None

                self.root = cs.load_ref()
                
                if rec_unpack:
                    self.root = TLBComplex.constants["t_RefCell"].fetch(self.root, True, strict) # at 1
                    assert self.root is not None

                self.signatures = TLBComplex.constants["t_Maybe_Ref_BlockSignatures"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("BlockProof")


# class for type `ProofChain`
class ProofChain(TLBComplex):
    class Tag(Enum):
        chain_empty = 0
        chain_link = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {ProofChain.Tag.chain_empty: self.get_param_record("Record_chain_empty"), ProofChain.Tag.chain_link: self.get_param_record("Record_chain_link")}

    def get_tag(self, cs: CellSlice) -> Optional["ProofChain.Tag"]:
        # distinguish by parameter `m_` using 1 2 2 2
        return ProofChain.Tag.chain_link if self.m_ else ProofChain.Tag.chain_empty




    class Record_chain_empty(RecordBase):
        def get_tag_enum(self):
            return ProofChain.Tag.chain_empty

        def get_tag(self):
            return ProofChain.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProofChain.cons_len_exact[self.get_tag_enum().value] if isinstance(ProofChain.cons_len_exact, list) else ProofChain.cons_len_exact

        def get_type_class(self):
            return ProofChain


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chain_link(RecordBase):
        def get_tag_enum(self):
            return ProofChain.Tag.chain_link

        def get_tag(self):
            return ProofChain.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProofChain.cons_len_exact[self.get_tag_enum().value] if isinstance(ProofChain.cons_len_exact, list) else ProofChain.cons_len_exact

        def get_type_class(self):
            return ProofChain

        # n : #
        n: "int" = None
        # root : ^Cell
        root: "Cell" = None
        # prev : n?^(ProofChain n)
        prev: "Cell" = None

        def __init__(self, root: "Cell" = None, prev: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.root = root    
            self.field_names.append("root")
            self.prev = prev    
            self.conditional_fields.append("prev")    
            self.field_names.append("prev")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.root = cs.load_ref()
                
                if rec_unpack:
                    self.root = TLBComplex.constants["t_RefCell"].fetch(self.root, True, strict) # at 1
                    assert self.root is not None

                if (self.n > 0):
                    
                    self.prev = cs.load_ref()
                    
                if rec_unpack and self.prev is not None:
                    self.prev = TLBComplex.constants["t_Ref_ProofChain"].fetch(self.prev, True, strict) # at 3
                    assert self.prev is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ProofChain")


# class for type `TopBlockDescr`
class TopBlockDescr(TLBComplex):
    class Tag(Enum):
        top_block_descr = 0

    cons_len_exact = 8
    cons_tag = [0xd5]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TopBlockDescr.Tag.top_block_descr: TopBlockDescr.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TopBlockDescr.Tag"]:
        return TopBlockDescr.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TopBlockDescr.Tag.top_block_descr

        def get_tag(self):
            return TopBlockDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TopBlockDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(TopBlockDescr.cons_len_exact, list) else TopBlockDescr.cons_len_exact

        def get_type_class(self):
            return TopBlockDescr

        # proof_for : BlockIdExt
        proof_for: "CellSlice" = None
        # signatures : Maybe ^BlockSignatures
        signatures: "CellSlice" = None
        # len : ## 8
        len: "int" = None
        # chain : ProofChain len
        chain: "CellSlice" = None

        def __init__(self, proof_for: "CellSlice" = None, signatures: "CellSlice" = None, len: "int" = None, chain: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.proof_for = proof_for    
            self.field_names.append("proof_for")
            self.signatures = signatures    
            self.field_names.append("signatures")
            self.len = len    
            self.field_names.append("len")
            self.chain = chain    
            self.field_names.append("chain")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xd5, 'Cons tag check failed'

                self.proof_for = cs.load_subslice(648)
                
                if rec_unpack:
                    self.proof_for = TLBComplex.constants["t_BlockIdExt"].fetch(self.proof_for, True, strict) # at 1
                    assert self.proof_for is not None

                self.signatures = TLBComplex.constants["t_Maybe_Ref_BlockSignatures"].fetch(cs) 
                self.len = cs.load_uint(8)
                assert 1 <= self.len, 'Params not equal: 1 and len'

                assert self.len <= 8, 'Params not equal: len and 8'

                self.chain = ProofChain(self.len).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TopBlockDescr")


# class for type `TopBlockDescrSet`
class TopBlockDescrSet(TLBComplex):
    class Tag(Enum):
        top_block_descr_set = 0

    cons_len_exact = 32
    cons_tag = [0x4ac789f3]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {TopBlockDescrSet.Tag.top_block_descr_set: TopBlockDescrSet.Record}

    def get_tag(self, cs: CellSlice) -> Optional["TopBlockDescrSet.Tag"]:
        return TopBlockDescrSet.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return TopBlockDescrSet.Tag.top_block_descr_set

        def get_tag(self):
            return TopBlockDescrSet.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TopBlockDescrSet.cons_len_exact[self.get_tag_enum().value] if isinstance(TopBlockDescrSet.cons_len_exact, list) else TopBlockDescrSet.cons_len_exact

        def get_type_class(self):
            return TopBlockDescrSet

        # collection : HashmapE 96 ^TopBlockDescr
        collection: "CellSlice" = None

        def __init__(self, collection: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.collection = collection    
            self.field_names.append("collection")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x4ac789f3, 'Cons tag check failed'

                self.collection = TLBComplex.constants["t_HashmapE_96_Ref_TopBlockDescr"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TopBlockDescrSet")


# class for type `ProducerInfo`
class ProducerInfo(TLBComplex):
    class Tag(Enum):
        prod_info = 0

    cons_len_exact = 8
    cons_tag = [0x34]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ProducerInfo.Tag.prod_info: ProducerInfo.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ProducerInfo.Tag"]:
        return ProducerInfo.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ProducerInfo.Tag.prod_info

        def get_tag(self):
            return ProducerInfo.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProducerInfo.cons_len_exact[self.get_tag_enum().value] if isinstance(ProducerInfo.cons_len_exact, list) else ProducerInfo.cons_len_exact

        def get_type_class(self):
            return ProducerInfo

        # utime : uint32
        utime: "int" = None
        # mc_blk_ref : ExtBlkRef
        mc_blk_ref: "CellSlice" = None
        # state_proof : ^(MERKLE_PROOF Block)
        state_proof: "Cell" = None
        # prod_proof : ^(MERKLE_PROOF ShardState)
        prod_proof: "Cell" = None

        def __init__(self, utime: "int" = None, mc_blk_ref: "CellSlice" = None, state_proof: "Cell" = None, prod_proof: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.utime = utime    
            self.field_names.append("utime")
            self.mc_blk_ref = mc_blk_ref    
            self.field_names.append("mc_blk_ref")
            self.state_proof = state_proof    
            self.field_names.append("state_proof")
            self.prod_proof = prod_proof    
            self.field_names.append("prod_proof")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x34, 'Cons tag check failed'

                self.utime = cs.load_uint(32)
                self.mc_blk_ref = cs.load_subslice(608)
                
                if rec_unpack:
                    self.mc_blk_ref = TLBComplex.constants["t_ExtBlkRef"].fetch(self.mc_blk_ref, True, strict) # at 1
                    assert self.mc_blk_ref is not None

                self.state_proof = cs.load_ref()
                
                if rec_unpack:
                    self.state_proof = TLBComplex.constants["t_Ref_MERKLE_PROOF_Block"].fetch(self.state_proof, True, strict) # at 1
                    assert self.state_proof is not None

                self.prod_proof = cs.load_ref()
                
                if rec_unpack:
                    self.prod_proof = TLBComplex.constants["t_Ref_MERKLE_PROOF_ShardState"].fetch(self.prod_proof, True, strict) # at 1
                    assert self.prod_proof is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ProducerInfo")


# class for type `ComplaintDescr`
class ComplaintDescr(TLBComplex):
    class Tag(Enum):
        no_blk_gen = 0
        no_blk_gen_diff = 1

    cons_len_exact = 32
    cons_tag = [0x450e8bd9, 0xc737b0ca]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ComplaintDescr.Tag.no_blk_gen: ComplaintDescr.Record_no_blk_gen, ComplaintDescr.Tag.no_blk_gen_diff: ComplaintDescr.Record_no_blk_gen_diff}

    def get_tag(self, cs: CellSlice) -> Optional["ComplaintDescr.Tag"]:
        return ComplaintDescr.Tag(int(cs.preload_uint(1)))


    class Record_no_blk_gen(RecordBase):
        def get_tag_enum(self):
            return ComplaintDescr.Tag.no_blk_gen

        def get_tag(self):
            return ComplaintDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComplaintDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(ComplaintDescr.cons_len_exact, list) else ComplaintDescr.cons_len_exact

        def get_type_class(self):
            return ComplaintDescr

        # from_utime : uint32
        from_utime: "int" = None
        # prod_info : ^ProducerInfo
        prod_info: "Cell" = None

        def __init__(self, from_utime: "int" = None, prod_info: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.from_utime = from_utime    
            self.field_names.append("from_utime")
            self.prod_info = prod_info    
            self.field_names.append("prod_info")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x450e8bd9, 'Cons tag check failed'

                self.from_utime = cs.load_uint(32)
                self.prod_info = cs.load_ref()
                
                if rec_unpack:
                    self.prod_info = TLBComplex.constants["t_Ref_ProducerInfo"].fetch(self.prod_info, True, strict) # at 1
                    assert self.prod_info is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_no_blk_gen_diff(RecordBase):
        def get_tag_enum(self):
            return ComplaintDescr.Tag.no_blk_gen_diff

        def get_tag(self):
            return ComplaintDescr.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ComplaintDescr.cons_len_exact[self.get_tag_enum().value] if isinstance(ComplaintDescr.cons_len_exact, list) else ComplaintDescr.cons_len_exact

        def get_type_class(self):
            return ComplaintDescr

        # prod_info_old : ^ProducerInfo
        prod_info_old: "Cell" = None
        # prod_info_new : ^ProducerInfo
        prod_info_new: "Cell" = None

        def __init__(self, prod_info_old: "Cell" = None, prod_info_new: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.prod_info_old = prod_info_old    
            self.field_names.append("prod_info_old")
            self.prod_info_new = prod_info_new    
            self.field_names.append("prod_info_new")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0xc737b0ca, 'Cons tag check failed'

                self.prod_info_old = cs.load_ref()
                
                if rec_unpack:
                    self.prod_info_old = TLBComplex.constants["t_Ref_ProducerInfo"].fetch(self.prod_info_old, True, strict) # at 1
                    assert self.prod_info_old is not None

                self.prod_info_new = cs.load_ref()
                
                if rec_unpack:
                    self.prod_info_new = TLBComplex.constants["t_Ref_ProducerInfo"].fetch(self.prod_info_new, True, strict) # at 1
                    assert self.prod_info_new is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ComplaintDescr")


# class for type `ValidatorComplaint`
class ValidatorComplaint(TLBComplex):
    class Tag(Enum):
        validator_complaint = 0

    cons_len_exact = 8
    cons_tag = [0xbc]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorComplaint.Tag.validator_complaint: ValidatorComplaint.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorComplaint.Tag"]:
        return ValidatorComplaint.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ValidatorComplaint.Tag.validator_complaint

        def get_tag(self):
            return ValidatorComplaint.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorComplaint.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorComplaint.cons_len_exact, list) else ValidatorComplaint.cons_len_exact

        def get_type_class(self):
            return ValidatorComplaint

        # validator_pubkey : bits256
        validator_pubkey: "bitstring.BitArray" = None
        # description : ^ComplaintDescr
        description: "Cell" = None
        # created_at : uint32
        created_at: "int" = None
        # severity : uint8
        severity: "int" = None
        # reward_addr : uint256
        reward_addr: "int" = None
        # paid : Grams
        paid: "CellSlice" = None
        # suggested_fine : Grams
        suggested_fine: "CellSlice" = None
        # suggested_fine_part : uint32
        suggested_fine_part: "int" = None

        def __init__(self, validator_pubkey: "bitstring.BitArray" = None, description: "Cell" = None, created_at: "int" = None, severity: "int" = None, reward_addr: "int" = None, paid: "CellSlice" = None, suggested_fine: "CellSlice" = None, suggested_fine_part: "int" = None):
            super().__init__()
            self.field_names = []
            self.validator_pubkey = validator_pubkey    
            self.field_names.append("validator_pubkey")
            self.description = description    
            self.field_names.append("description")
            self.created_at = created_at    
            self.field_names.append("created_at")
            self.severity = severity    
            self.field_names.append("severity")
            self.reward_addr = reward_addr    
            self.field_names.append("reward_addr")
            self.paid = paid    
            self.field_names.append("paid")
            self.suggested_fine = suggested_fine    
            self.field_names.append("suggested_fine")
            self.suggested_fine_part = suggested_fine_part    
            self.field_names.append("suggested_fine_part")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xbc, 'Cons tag check failed'

                self.validator_pubkey = cs.load_bitstring(256)
                self.description = cs.load_ref()
                
                if rec_unpack:
                    self.description = TLBComplex.constants["t_Ref_ComplaintDescr"].fetch(self.description, True, strict) # at 1
                    assert self.description is not None

                self.created_at = cs.load_uint(32)
                self.severity = cs.load_uint(8)
                self.reward_addr = cs.load_uint(256)
                self.paid = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.suggested_fine = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.suggested_fine_part = cs.load_uint(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorComplaint")


# class for type `ValidatorComplaintStatus`
class ValidatorComplaintStatus(TLBComplex):
    class Tag(Enum):
        complaint_status = 0

    cons_len_exact = 8
    cons_tag = [0x2d]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ValidatorComplaintStatus.Tag.complaint_status: ValidatorComplaintStatus.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ValidatorComplaintStatus.Tag"]:
        return ValidatorComplaintStatus.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ValidatorComplaintStatus.Tag.complaint_status

        def get_tag(self):
            return ValidatorComplaintStatus.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ValidatorComplaintStatus.cons_len_exact[self.get_tag_enum().value] if isinstance(ValidatorComplaintStatus.cons_len_exact, list) else ValidatorComplaintStatus.cons_len_exact

        def get_type_class(self):
            return ValidatorComplaintStatus

        # complaint : ^ValidatorComplaint
        complaint: "Cell" = None
        # voters : HashmapE 16 Truet
        voters: "CellSlice" = None
        # vset_id : uint256
        vset_id: "int" = None
        # weight_remaining : int64
        weight_remaining: "int" = None

        def __init__(self, complaint: "Cell" = None, voters: "CellSlice" = None, vset_id: "int" = None, weight_remaining: "int" = None):
            super().__init__()
            self.field_names = []
            self.complaint = complaint    
            self.field_names.append("complaint")
            self.voters = voters    
            self.field_names.append("voters")
            self.vset_id = vset_id    
            self.field_names.append("vset_id")
            self.weight_remaining = weight_remaining    
            self.field_names.append("weight_remaining")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0x2d, 'Cons tag check failed'

                self.complaint = cs.load_ref()
                
                if rec_unpack:
                    self.complaint = TLBComplex.constants["t_Ref_ValidatorComplaint"].fetch(self.complaint, True, strict) # at 1
                    assert self.complaint is not None

                self.voters = TLBComplex.constants["t_HashmapE_16_Truet"].fetch(cs) 
                self.vset_id = cs.load_uint(256)
                self.weight_remaining = cs.load_int(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ValidatorComplaintStatus")


# class for type `VmCellSlice`
class VmCellSlice(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmCellSlice.Tag.cons1: VmCellSlice.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmCellSlice.Tag"]:
        return VmCellSlice.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmCellSlice.Tag.cons1

        def get_tag(self):
            return VmCellSlice.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCellSlice.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCellSlice.cons_len_exact, list) else VmCellSlice.cons_len_exact

        def get_type_class(self):
            return VmCellSlice

        # cell : ^Cell
        cell: "Cell" = None
        # st_bits : ## 10
        st_bits: "int" = None
        # end_bits : ## 10
        end_bits: "int" = None
        # st_ref : #<= 4
        st_ref: "int" = None
        # end_ref : #<= 4
        end_ref: "int" = None

        def __init__(self, cell: "Cell" = None, st_bits: "int" = None, end_bits: "int" = None, st_ref: "int" = None, end_ref: "int" = None):
            super().__init__()
            self.field_names = []
            self.cell = cell    
            self.field_names.append("cell")
            self.st_bits = st_bits    
            self.field_names.append("st_bits")
            self.end_bits = end_bits    
            self.field_names.append("end_bits")
            self.st_ref = st_ref    
            self.field_names.append("st_ref")
            self.end_ref = end_ref    
            self.field_names.append("end_ref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cell = cs.load_ref()
                
                if rec_unpack:
                    self.cell = TLBComplex.constants["t_RefCell"].fetch(self.cell, True, strict) # at 1
                    assert self.cell is not None

                self.st_bits = cs.load_uint(10)
                self.end_bits = cs.load_uint(10)
                assert self.st_bits <= self.end_bits, 'Params not equal: st_bits and end_bits'

                self.st_ref = cs.load_uint_leq(4)
                self.end_ref = cs.load_uint_leq(4)
                assert self.st_ref <= self.end_ref, 'Params not equal: st_ref and end_ref'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmCellSlice")


# class for type `VmTupleRef`
class VmTupleRef(TLBComplex):
    class Tag(Enum):
        vm_tupref_nil = 0
        vm_tupref_single = 1
        vm_tupref_any = 2

    cons_len_exact = 0
    cons_tag = [0, 0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {VmTupleRef.Tag.vm_tupref_nil: self.get_param_record("Record_vm_tupref_nil"), VmTupleRef.Tag.vm_tupref_single: self.get_param_record("Record_vm_tupref_single"), VmTupleRef.Tag.vm_tupref_any: self.get_param_record("Record_vm_tupref_any")}

    def get_tag(self, cs: CellSlice) -> Optional["VmTupleRef.Tag"]:
        # distinguish by parameter `m_` using 1 2 3 3
        ctab = [VmTupleRef.Tag.vm_tupref_nil, VmTupleRef.Tag.vm_tupref_single, VmTupleRef.Tag.vm_tupref_any, VmTupleRef.Tag.vm_tupref_any ]
        return ctab[self.nat_abs(self.m_)]



    class Record_vm_tupref_nil(RecordBase):
        def get_tag_enum(self):
            return VmTupleRef.Tag.vm_tupref_nil

        def get_tag(self):
            return VmTupleRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmTupleRef.cons_len_exact[self.get_tag_enum().value] if isinstance(VmTupleRef.cons_len_exact, list) else VmTupleRef.cons_len_exact

        def get_type_class(self):
            return VmTupleRef


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_tupref_single(RecordBase):
        def get_tag_enum(self):
            return VmTupleRef.Tag.vm_tupref_single

        def get_tag(self):
            return VmTupleRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmTupleRef.cons_len_exact[self.get_tag_enum().value] if isinstance(VmTupleRef.cons_len_exact, list) else VmTupleRef.cons_len_exact

        def get_type_class(self):
            return VmTupleRef

        # entry : ^VmStackValue
        entry: "Cell" = None

        def __init__(self, entry: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.entry = entry    
            self.field_names.append("entry")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.entry = cs.load_ref()
                
                if rec_unpack:
                    self.entry = TLBComplex.constants["t_Ref_VmStackValue"].fetch(self.entry, True, strict) # at 1
                    assert self.entry is not None

                self.m_ == 1                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_tupref_any(RecordBase):
        def get_tag_enum(self):
            return VmTupleRef.Tag.vm_tupref_any

        def get_tag(self):
            return VmTupleRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmTupleRef.cons_len_exact[self.get_tag_enum().value] if isinstance(VmTupleRef.cons_len_exact, list) else VmTupleRef.cons_len_exact

        def get_type_class(self):
            return VmTupleRef

        # n : #
        n: "int" = None
        # ref : ^(VmTuple (n + 2))
        ref: "Cell" = None

        def __init__(self, ref: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.ref = ref    
            self.field_names.append("ref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 2, self.m_), 'Add_r1 failed'

                self.ref = cs.load_ref()
                
                if rec_unpack:
                    self.ref = RefT(VmTuple(self.n + 2)).fetch(self.ref, True, strict) # at 1
                    assert self.ref is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmTupleRef")


# class for type `VmTuple`
class VmTuple(TLBComplex):
    class Tag(Enum):
        vm_tuple_nil = 0
        vm_tuple_tcons = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {VmTuple.Tag.vm_tuple_nil: self.get_param_record("Record_vm_tuple_nil"), VmTuple.Tag.vm_tuple_tcons: self.get_param_record("Record_vm_tuple_tcons")}

    def get_tag(self, cs: CellSlice) -> Optional["VmTuple.Tag"]:
        # distinguish by parameter `m_` using 1 2 2 2
        return VmTuple.Tag.vm_tuple_tcons if self.m_ else VmTuple.Tag.vm_tuple_nil




    class Record_vm_tuple_nil(RecordBase):
        def get_tag_enum(self):
            return VmTuple.Tag.vm_tuple_nil

        def get_tag(self):
            return VmTuple.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmTuple.cons_len_exact[self.get_tag_enum().value] if isinstance(VmTuple.cons_len_exact, list) else VmTuple.cons_len_exact

        def get_type_class(self):
            return VmTuple


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_tuple_tcons(RecordBase):
        def get_tag_enum(self):
            return VmTuple.Tag.vm_tuple_tcons

        def get_tag(self):
            return VmTuple.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmTuple.cons_len_exact[self.get_tag_enum().value] if isinstance(VmTuple.cons_len_exact, list) else VmTuple.cons_len_exact

        def get_type_class(self):
            return VmTuple

        # n : #
        n: "int" = None
        # head : VmTupleRef n
        head: "CellSlice" = None
        # tail : ^VmStackValue
        tail: "Cell" = None

        def __init__(self, head: "CellSlice" = None, tail: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.head = head    
            self.field_names.append("head")
            self.tail = tail    
            self.field_names.append("tail")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.head = VmTupleRef(self.n).fetch(cs) 
                self.tail = cs.load_ref()
                
                if rec_unpack:
                    self.tail = TLBComplex.constants["t_Ref_VmStackValue"].fetch(self.tail, True, strict) # at 1
                    assert self.tail is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmTuple")


# class for type `VmStackValue`
class VmStackValue(TLBComplex):
    class Tag(Enum):
        vm_stk_null = 0
        vm_stk_tinyint = 1
        vm_stk_int = 2
        vm_stk_nan = 3
        vm_stk_cell = 4
        vm_stk_slice = 5
        vm_stk_builder = 6
        vm_stk_cont = 7
        vm_stk_tuple = 8

    cons_len = [8, 8, 15, 16, 8, 8, 8, 8, 8]
    cons_tag = [0, 1, 0x100, 0x2ff, 3, 4, 5, 6, 7]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmStackValue.Tag.vm_stk_null: VmStackValue.Record_vm_stk_null, VmStackValue.Tag.vm_stk_tinyint: VmStackValue.Record_vm_stk_tinyint, VmStackValue.Tag.vm_stk_int: VmStackValue.Record_vm_stk_int, VmStackValue.Tag.vm_stk_nan: VmStackValue.Record_vm_stk_nan, VmStackValue.Tag.vm_stk_cell: VmStackValue.Record_vm_stk_cell, VmStackValue.Tag.vm_stk_slice: VmStackValue.Record_vm_stk_slice, VmStackValue.Tag.vm_stk_builder: VmStackValue.Record_vm_stk_builder, VmStackValue.Tag.vm_stk_cont: VmStackValue.Record_vm_stk_cont, VmStackValue.Tag.vm_stk_tuple: VmStackValue.Record_vm_stk_tuple}

    def get_tag(self, cs: CellSlice) -> Optional["VmStackValue.Tag"]:
        tag = int(cs.bselect(6, 7))
        if tag == 0:
            if cs.bit_at(6):
                if cs.bit_at(7):
                    return VmStackValue.Tag.vm_stk_cell
                else:
                    return VmStackValue.Tag.vm_stk_nan if cs.bit_at(8) else VmStackValue.Tag.vm_stk_int

            else:
                return VmStackValue.Tag.vm_stk_tinyint if cs.bit_at(7) else VmStackValue.Tag.vm_stk_null

        if tag == 1:
            if cs.bit_at(6):
                return VmStackValue.Tag.vm_stk_tuple if cs.bit_at(7) else VmStackValue.Tag.vm_stk_cont
            else:
                return VmStackValue.Tag.vm_stk_builder if cs.bit_at(7) else VmStackValue.Tag.vm_stk_slice

        return None



    class Record_vm_stk_null(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_null

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_tinyint(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_tinyint

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # value : int64
        value: "int" = None

        def __init__(self, value: "int" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 1, 'Cons tag check failed'

                self.value = cs.load_int(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_int(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_int

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # value : int257
        value: "int" = None

        def __init__(self, value: "int" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(15) == 0x100, 'Cons tag check failed'

                self.value = cs.load_int(257)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_nan(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_nan

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x2ff, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_cell(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_cell

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # cell : ^Cell
        cell: "Cell" = None

        def __init__(self, cell: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.cell = cell    
            self.field_names.append("cell")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 3, 'Cons tag check failed'

                self.cell = cs.load_ref()
                
                if rec_unpack:
                    self.cell = TLBComplex.constants["t_RefCell"].fetch(self.cell, True, strict) # at 1
                    assert self.cell is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_slice(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_slice

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # VmCellSlice
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 4, 'Cons tag check failed'

                self.x = cs.load_subslice_ext(0x1001a)
                
                if rec_unpack:
                    self.x = TLBComplex.constants["t_VmCellSlice"].fetch(self.x, True, strict) # at 1
                    assert self.x is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_builder(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_builder

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # cell : ^Cell
        cell: "Cell" = None

        def __init__(self, cell: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.cell = cell    
            self.field_names.append("cell")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 5, 'Cons tag check failed'

                self.cell = cs.load_ref()
                
                if rec_unpack:
                    self.cell = TLBComplex.constants["t_RefCell"].fetch(self.cell, True, strict) # at 1
                    assert self.cell is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_cont(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_cont

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # cont : VmCont
        cont: "CellSlice" = None

        def __init__(self, cont: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cont = cont    
            self.field_names.append("cont")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 6, 'Cons tag check failed'

                self.cont = TLBComplex.constants["t_VmCont"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_tuple(RecordBase):
        def get_tag_enum(self):
            return VmStackValue.Tag.vm_stk_tuple

        def get_tag(self):
            return VmStackValue.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackValue.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackValue.cons_len_exact, list) else VmStackValue.cons_len_exact

        def get_type_class(self):
            return VmStackValue

        # len : ## 16
        len: "int" = None
        # data : VmTuple len
        data: "CellSlice" = None

        def __init__(self, len: "int" = None, data: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.len = len    
            self.field_names.append("len")
            self.data = data    
            self.field_names.append("data")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 7, 'Cons tag check failed'

                self.len = cs.load_uint(16)
                self.data = VmTuple(self.len).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmStackValue")


# class for type `VmStack`
class VmStack(TLBComplex):
    class Tag(Enum):
        vm_stack = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmStack.Tag.vm_stack: VmStack.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmStack.Tag"]:
        return VmStack.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmStack.Tag.vm_stack

        def get_tag(self):
            return VmStack.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStack.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStack.cons_len_exact, list) else VmStack.cons_len_exact

        def get_type_class(self):
            return VmStack

        # depth : ## 24
        depth: "int" = None
        # stack : VmStackList depth
        stack: "CellSlice" = None

        def __init__(self, depth: "int" = None, stack: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.depth = depth    
            self.field_names.append("depth")
            self.stack = stack    
            self.field_names.append("stack")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.depth = cs.load_uint(24)
                self.stack = VmStackList(self.depth).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmStack")


# class for type `VmStackList`
class VmStackList(TLBComplex):
    class Tag(Enum):
        vm_stk_cons = 0
        vm_stk_nil = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {VmStackList.Tag.vm_stk_cons: self.get_param_record("Record_vm_stk_cons"), VmStackList.Tag.vm_stk_nil: self.get_param_record("Record_vm_stk_nil")}

    def get_tag(self, cs: CellSlice) -> Optional["VmStackList.Tag"]:
        # distinguish by parameter `m_` using 2 1 1 1
        return VmStackList.Tag.vm_stk_cons if self.m_ else VmStackList.Tag.vm_stk_nil




    class Record_vm_stk_cons(RecordBase):
        def get_tag_enum(self):
            return VmStackList.Tag.vm_stk_cons

        def get_tag(self):
            return VmStackList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackList.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackList.cons_len_exact, list) else VmStackList.cons_len_exact

        def get_type_class(self):
            return VmStackList

        # n : #
        n: "int" = None
        # rest : ^(VmStackList n)
        rest: "Cell" = None
        # tos : VmStackValue
        tos: "CellSlice" = None

        def __init__(self, rest: "Cell" = None, tos: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.rest = rest    
            self.field_names.append("rest")
            self.tos = tos    
            self.field_names.append("tos")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.rest = cs.load_ref()
                
                if rec_unpack:
                    self.rest = RefT(VmStackList(self.n)).fetch(self.rest, True, strict) # at 1
                    assert self.rest is not None

                self.tos = TLBComplex.constants["t_VmStackValue"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vm_stk_nil(RecordBase):
        def get_tag_enum(self):
            return VmStackList.Tag.vm_stk_nil

        def get_tag(self):
            return VmStackList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmStackList.cons_len_exact[self.get_tag_enum().value] if isinstance(VmStackList.cons_len_exact, list) else VmStackList.cons_len_exact

        def get_type_class(self):
            return VmStackList


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmStackList")


# class for type `VmSaveList`
class VmSaveList(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmSaveList.Tag.cons1: VmSaveList.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmSaveList.Tag"]:
        return VmSaveList.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmSaveList.Tag.cons1

        def get_tag(self):
            return VmSaveList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmSaveList.cons_len_exact[self.get_tag_enum().value] if isinstance(VmSaveList.cons_len_exact, list) else VmSaveList.cons_len_exact

        def get_type_class(self):
            return VmSaveList

        # cregs : HashmapE 4 VmStackValue
        cregs: "CellSlice" = None

        def __init__(self, cregs: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cregs = cregs    
            self.field_names.append("cregs")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.cregs = TLBComplex.constants["t_HashmapE_4_VmStackValue"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmSaveList")


# class for auxiliary type `VmGasLimits_aux`
class VmGasLimits_aux(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmGasLimits_aux.Tag.cons1: VmGasLimits_aux.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmGasLimits_aux.Tag"]:
        return VmGasLimits_aux.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmGasLimits_aux.Tag.cons1

        def get_tag(self):
            return VmGasLimits_aux.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmGasLimits_aux.cons_len_exact[self.get_tag_enum().value] if isinstance(VmGasLimits_aux.cons_len_exact, list) else VmGasLimits_aux.cons_len_exact

        def get_type_class(self):
            return VmGasLimits_aux

        # max_limit : int64
        max_limit: "int" = None
        # cur_limit : int64
        cur_limit: "int" = None
        # credit : int64
        credit: "int" = None

        def __init__(self, max_limit: "int" = None, cur_limit: "int" = None, credit: "int" = None):
            super().__init__()
            self.field_names = []
            self.max_limit = max_limit    
            self.field_names.append("max_limit")
            self.cur_limit = cur_limit    
            self.field_names.append("cur_limit")
            self.credit = credit    
            self.field_names.append("credit")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.max_limit = cs.load_int(64)
                self.cur_limit = cs.load_int(64)
                self.credit = cs.load_int(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmGasLimits_aux")


# class for type `VmGasLimits`
class VmGasLimits(TLBComplex):
    class Tag(Enum):
        gas_limits = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmGasLimits.Tag.gas_limits: VmGasLimits.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmGasLimits.Tag"]:
        return VmGasLimits.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmGasLimits.Tag.gas_limits

        def get_tag(self):
            return VmGasLimits.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmGasLimits.cons_len_exact[self.get_tag_enum().value] if isinstance(VmGasLimits.cons_len_exact, list) else VmGasLimits.cons_len_exact

        def get_type_class(self):
            return VmGasLimits

        # remaining : int64
        remaining: "int" = None
        # ^[$_ max_limit:int64 cur_limit:int64 credit:int64 ]
        r1: "VmGasLimits_aux.Record" = None

        def __init__(self, remaining: "int" = None, r1: "VmGasLimits_aux.Record" = None):
            super().__init__()
            self.field_names = []
            self.remaining = remaining    
            self.field_names.append("remaining")
            self.r1 = r1    
            self.field_names.append("r1")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.remaining = cs.load_int(64)
                self.r1 = TLBComplex.constants["t_VmGasLimits_aux"].fetch(cs.load_ref(), rec_unpack, strict)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmGasLimits")


# class for type `VmLibraries`
class VmLibraries(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmLibraries.Tag.cons1: VmLibraries.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmLibraries.Tag"]:
        return VmLibraries.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmLibraries.Tag.cons1

        def get_tag(self):
            return VmLibraries.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmLibraries.cons_len_exact[self.get_tag_enum().value] if isinstance(VmLibraries.cons_len_exact, list) else VmLibraries.cons_len_exact

        def get_type_class(self):
            return VmLibraries

        # libraries : HashmapE 256 ^Cell
        libraries: "CellSlice" = None

        def __init__(self, libraries: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.libraries = libraries    
            self.field_names.append("libraries")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.libraries = TLBComplex.constants["t_HashmapE_256_Ref_Cell"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmLibraries")


# class for type `VmControlData`
class VmControlData(TLBComplex):
    class Tag(Enum):
        vm_ctl_data = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmControlData.Tag.vm_ctl_data: VmControlData.Record}

    def get_tag(self, cs: CellSlice) -> Optional["VmControlData.Tag"]:
        return VmControlData.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return VmControlData.Tag.vm_ctl_data

        def get_tag(self):
            return VmControlData.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmControlData.cons_len_exact[self.get_tag_enum().value] if isinstance(VmControlData.cons_len_exact, list) else VmControlData.cons_len_exact

        def get_type_class(self):
            return VmControlData

        # nargs : Maybe uint13
        nargs: "CellSlice" = None
        # stack : Maybe VmStack
        stack: "CellSlice" = None
        # save : VmSaveList
        save: "CellSlice" = None
        # cp : Maybe int16
        cp: "CellSlice" = None

        def __init__(self, nargs: "CellSlice" = None, stack: "CellSlice" = None, save: "CellSlice" = None, cp: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.nargs = nargs    
            self.field_names.append("nargs")
            self.stack = stack    
            self.field_names.append("stack")
            self.save = save    
            self.field_names.append("save")
            self.cp = cp    
            self.field_names.append("cp")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.nargs = TLBComplex.constants["t_Maybe_uint13"].fetch(cs) 
                self.stack = TLBComplex.constants["t_Maybe_VmStack"].fetch(cs) 
                self.save = TLBComplex.constants["t_VmSaveList"].fetch(cs) 
                self.cp = TLBComplex.constants["t_Maybe_int16"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmControlData")


# class for type `VmCont`
class VmCont(TLBComplex):
    class Tag(Enum):
        vmc_std = 0
        vmc_envelope = 1
        vmc_quit = 2
        vmc_quit_exc = 3
        vmc_repeat = 4
        vmc_until = 5
        vmc_again = 6
        vmc_while_cond = 7
        vmc_while_body = 8
        vmc_pushint = 9

    cons_len = [2, 2, 4, 4, 5, 6, 6, 6, 6, 4]
    cons_tag = [0, 1, 8, 9, 20, 0x30, 0x31, 0x32, 0x33, 15]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {VmCont.Tag.vmc_std: VmCont.Record_vmc_std, VmCont.Tag.vmc_envelope: VmCont.Record_vmc_envelope, VmCont.Tag.vmc_quit: VmCont.Record_vmc_quit, VmCont.Tag.vmc_quit_exc: VmCont.Record_vmc_quit_exc, VmCont.Tag.vmc_repeat: VmCont.Record_vmc_repeat, VmCont.Tag.vmc_until: VmCont.Record_vmc_until, VmCont.Tag.vmc_again: VmCont.Record_vmc_again, VmCont.Tag.vmc_while_cond: VmCont.Record_vmc_while_cond, VmCont.Tag.vmc_while_body: VmCont.Record_vmc_while_body, VmCont.Tag.vmc_pushint: VmCont.Record_vmc_pushint}

    def get_tag(self, cs: CellSlice) -> Optional["VmCont.Tag"]:
        return VmCont.Tag(int(cs.bselect_ext(6, 0x100f011100010001)))


    class Record_vmc_std(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_std

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # cdata : VmControlData
        cdata: "CellSlice" = None
        # code : VmCellSlice
        code: "CellSlice" = None

        def __init__(self, cdata: "CellSlice" = None, code: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.cdata = cdata    
            self.field_names.append("cdata")
            self.code = code    
            self.field_names.append("code")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 0, 'Cons tag check failed'

                self.cdata = TLBComplex.constants["t_VmControlData"].fetch(cs) 
                self.code = cs.load_subslice_ext(0x1001a)
                
                if rec_unpack:
                    self.code = TLBComplex.constants["t_VmCellSlice"].fetch(self.code, True, strict) # at 1
                    assert self.code is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_envelope(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_envelope

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # cdata : VmControlData
        cdata: "CellSlice" = None
        # next : ^VmCont
        next: "Cell" = None

        def __init__(self, cdata: "CellSlice" = None, next: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.cdata = cdata    
            self.field_names.append("cdata")
            self.next = next    
            self.field_names.append("next")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(2) == 1, 'Cons tag check failed'

                self.cdata = TLBComplex.constants["t_VmControlData"].fetch(cs) 
                self.next = cs.load_ref()
                
                if rec_unpack:
                    self.next = TLBComplex.constants["t_Ref_VmCont"].fetch(self.next, True, strict) # at 1
                    assert self.next is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_quit(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_quit

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # exit_code : int32
        exit_code: "int" = None

        def __init__(self, exit_code: "int" = None):
            super().__init__()
            self.field_names = []
            self.exit_code = exit_code    
            self.field_names.append("exit_code")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 8, 'Cons tag check failed'

                self.exit_code = cs.load_int(32)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_quit_exc(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_quit_exc

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 9, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_repeat(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_repeat

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # count : uint63
        count: "int" = None
        # body : ^VmCont
        body: "Cell" = None
        # after : ^VmCont
        after: "Cell" = None

        def __init__(self, count: "int" = None, body: "Cell" = None, after: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.count = count    
            self.field_names.append("count")
            self.body = body    
            self.field_names.append("body")
            self.after = after    
            self.field_names.append("after")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(5) == 20, 'Cons tag check failed'

                self.count = cs.load_uint(63)
                self.body = cs.load_ref()
                
                if rec_unpack:
                    self.body = TLBComplex.constants["t_Ref_VmCont"].fetch(self.body, True, strict) # at 1
                    assert self.body is not None

                self.after = cs.load_ref()
                
                if rec_unpack:
                    self.after = TLBComplex.constants["t_Ref_VmCont"].fetch(self.after, True, strict) # at 1
                    assert self.after is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_until(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_until

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # body : ^VmCont
        body: "Cell" = None
        # after : ^VmCont
        after: "Cell" = None

        def __init__(self, body: "Cell" = None, after: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.body = body    
            self.field_names.append("body")
            self.after = after    
            self.field_names.append("after")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(6) == 0x30, 'Cons tag check failed'

                self.body = cs.load_ref()
                
                if rec_unpack:
                    self.body = TLBComplex.constants["t_Ref_VmCont"].fetch(self.body, True, strict) # at 1
                    assert self.body is not None

                self.after = cs.load_ref()
                
                if rec_unpack:
                    self.after = TLBComplex.constants["t_Ref_VmCont"].fetch(self.after, True, strict) # at 1
                    assert self.after is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_again(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_again

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # body : ^VmCont
        body: "Cell" = None

        def __init__(self, body: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.body = body    
            self.field_names.append("body")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(6) == 0x31, 'Cons tag check failed'

                self.body = cs.load_ref()
                
                if rec_unpack:
                    self.body = TLBComplex.constants["t_Ref_VmCont"].fetch(self.body, True, strict) # at 1
                    assert self.body is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_while_cond(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_while_cond

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # cond : ^VmCont
        cond: "Cell" = None
        # body : ^VmCont
        body: "Cell" = None
        # after : ^VmCont
        after: "Cell" = None

        def __init__(self, cond: "Cell" = None, body: "Cell" = None, after: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.cond = cond    
            self.field_names.append("cond")
            self.body = body    
            self.field_names.append("body")
            self.after = after    
            self.field_names.append("after")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(6) == 0x32, 'Cons tag check failed'

                self.cond = cs.load_ref()
                
                if rec_unpack:
                    self.cond = TLBComplex.constants["t_Ref_VmCont"].fetch(self.cond, True, strict) # at 1
                    assert self.cond is not None

                self.body = cs.load_ref()
                
                if rec_unpack:
                    self.body = TLBComplex.constants["t_Ref_VmCont"].fetch(self.body, True, strict) # at 1
                    assert self.body is not None

                self.after = cs.load_ref()
                
                if rec_unpack:
                    self.after = TLBComplex.constants["t_Ref_VmCont"].fetch(self.after, True, strict) # at 1
                    assert self.after is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_while_body(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_while_body

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # cond : ^VmCont
        cond: "Cell" = None
        # body : ^VmCont
        body: "Cell" = None
        # after : ^VmCont
        after: "Cell" = None

        def __init__(self, cond: "Cell" = None, body: "Cell" = None, after: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.cond = cond    
            self.field_names.append("cond")
            self.body = body    
            self.field_names.append("body")
            self.after = after    
            self.field_names.append("after")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(6) == 0x33, 'Cons tag check failed'

                self.cond = cs.load_ref()
                
                if rec_unpack:
                    self.cond = TLBComplex.constants["t_Ref_VmCont"].fetch(self.cond, True, strict) # at 1
                    assert self.cond is not None

                self.body = cs.load_ref()
                
                if rec_unpack:
                    self.body = TLBComplex.constants["t_Ref_VmCont"].fetch(self.body, True, strict) # at 1
                    assert self.body is not None

                self.after = cs.load_ref()
                
                if rec_unpack:
                    self.after = TLBComplex.constants["t_Ref_VmCont"].fetch(self.after, True, strict) # at 1
                    assert self.after is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_vmc_pushint(RecordBase):
        def get_tag_enum(self):
            return VmCont.Tag.vmc_pushint

        def get_tag(self):
            return VmCont.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return VmCont.cons_len_exact[self.get_tag_enum().value] if isinstance(VmCont.cons_len_exact, list) else VmCont.cons_len_exact

        def get_type_class(self):
            return VmCont

        # value : int32
        value: "int" = None
        # next : ^VmCont
        next: "Cell" = None

        def __init__(self, value: "int" = None, next: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.value = value    
            self.field_names.append("value")
            self.next = next    
            self.field_names.append("next")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(4) == 15, 'Cons tag check failed'

                self.value = cs.load_int(32)
                self.next = cs.load_ref()
                
                if rec_unpack:
                    self.next = TLBComplex.constants["t_Ref_VmCont"].fetch(self.next, True, strict) # at 1
                    assert self.next is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("VmCont")


# class for type `DNS_RecordSet`
class DNS_RecordSet(TLBComplex):
    class Tag(Enum):
        cons1 = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {DNS_RecordSet.Tag.cons1: DNS_RecordSet.Record}

    def get_tag(self, cs: CellSlice) -> Optional["DNS_RecordSet.Tag"]:
        return DNS_RecordSet.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return DNS_RecordSet.Tag.cons1

        def get_tag(self):
            return DNS_RecordSet.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DNS_RecordSet.cons_len_exact[self.get_tag_enum().value] if isinstance(DNS_RecordSet.cons_len_exact, list) else DNS_RecordSet.cons_len_exact

        def get_type_class(self):
            return DNS_RecordSet

        # HashmapE 256 ^DNSRecord
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.x = TLBComplex.constants["t_HashmapE_256_Ref_DNSRecord"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("DNS_RecordSet")


# class for type `TextChunkRef`
class TextChunkRef(TLBComplex):
    class Tag(Enum):
        chunk_ref = 0
        chunk_ref_empty = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {TextChunkRef.Tag.chunk_ref: self.get_param_record("Record_chunk_ref"), TextChunkRef.Tag.chunk_ref_empty: self.get_param_record("Record_chunk_ref_empty")}

    def get_tag(self, cs: CellSlice) -> Optional["TextChunkRef.Tag"]:
        # distinguish by parameter `m_` using 2 1 1 1
        return TextChunkRef.Tag.chunk_ref if self.m_ else TextChunkRef.Tag.chunk_ref_empty




    class Record_chunk_ref(RecordBase):
        def get_tag_enum(self):
            return TextChunkRef.Tag.chunk_ref

        def get_tag(self):
            return TextChunkRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TextChunkRef.cons_len_exact[self.get_tag_enum().value] if isinstance(TextChunkRef.cons_len_exact, list) else TextChunkRef.cons_len_exact

        def get_type_class(self):
            return TextChunkRef

        # n : #
        n: "int" = None
        # ref : ^(TextChunks (n + 1))
        ref: "Cell" = None

        def __init__(self, ref: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.ref = ref    
            self.field_names.append("ref")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.ref = cs.load_ref()
                
                if rec_unpack:
                    self.ref = RefT(TextChunks(self.n + 1)).fetch(self.ref, True, strict) # at 1
                    assert self.ref is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chunk_ref_empty(RecordBase):
        def get_tag_enum(self):
            return TextChunkRef.Tag.chunk_ref_empty

        def get_tag(self):
            return TextChunkRef.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TextChunkRef.cons_len_exact[self.get_tag_enum().value] if isinstance(TextChunkRef.cons_len_exact, list) else TextChunkRef.cons_len_exact

        def get_type_class(self):
            return TextChunkRef


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TextChunkRef")


# class for type `TextChunks`
class TextChunks(TLBComplex):
    class Tag(Enum):
        text_chunk = 0
        text_chunk_empty = 1

    cons_len_exact = 0
    cons_tag = [0, 0]

    m_: int = None

    def __init__(self, m_: int):
        super().__init__()
        self.m_ = m_
        self.params_attrs.append("m_")

        self.has_params = True

        self.tag_to_class = {TextChunks.Tag.text_chunk: self.get_param_record("Record_text_chunk"), TextChunks.Tag.text_chunk_empty: self.get_param_record("Record_text_chunk_empty")}

    def get_tag(self, cs: CellSlice) -> Optional["TextChunks.Tag"]:
        # distinguish by parameter `m_` using 2 1 1 1
        return TextChunks.Tag.text_chunk if self.m_ else TextChunks.Tag.text_chunk_empty




    class Record_text_chunk(RecordBase):
        def get_tag_enum(self):
            return TextChunks.Tag.text_chunk

        def get_tag(self):
            return TextChunks.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TextChunks.cons_len_exact[self.get_tag_enum().value] if isinstance(TextChunks.cons_len_exact, list) else TextChunks.cons_len_exact

        def get_type_class(self):
            return TextChunks

        # n : #
        n: "int" = None
        # len : ## 8
        len: "int" = None
        # data : bits (8 * len)
        data: "bitstring.BitArray" = None
        # next : TextChunkRef n
        next: "CellSlice" = None

        def __init__(self, len: "int" = None, data: "bitstring.BitArray" = None, next: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.n = -1    
            self.field_names.append("n")
            self.len = len    
            self.field_names.append("len")
            self.data = data    
            self.field_names.append("data")
            self.next = next    
            self.field_names.append("next")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert self.add_r1("n", 1, self.m_), 'Add_r1 failed'

                self.len = cs.load_uint(8)
                self.data = cs.load_bitstring(8 * self.len)

                
                if rec_unpack and self.data is not None:
                    self.data = TLBComplex.constants["t_bits_mul8"].fetch(self.data, True, strict) # at 3
                    assert self.data is not None

                self.next = TextChunkRef(self.n).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_text_chunk_empty(RecordBase):
        def get_tag_enum(self):
            return TextChunks.Tag.text_chunk_empty

        def get_tag(self):
            return TextChunks.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return TextChunks.cons_len_exact[self.get_tag_enum().value] if isinstance(TextChunks.cons_len_exact, list) else TextChunks.cons_len_exact

        def get_type_class(self):
            return TextChunks


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.m_ == 0                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("TextChunks")


# class for type `Text`
class Text(TLBComplex):
    class Tag(Enum):
        text = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Text.Tag.text: Text.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Text.Tag"]:
        return Text.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return Text.Tag.text

        def get_tag(self):
            return Text.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Text.cons_len_exact[self.get_tag_enum().value] if isinstance(Text.cons_len_exact, list) else Text.cons_len_exact

        def get_type_class(self):
            return Text

        # chunks : ## 8
        chunks: "int" = None
        # rest : TextChunks chunks
        rest: "CellSlice" = None

        def __init__(self, chunks: "int" = None, rest: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.chunks = chunks    
            self.field_names.append("chunks")
            self.rest = rest    
            self.field_names.append("rest")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.chunks = cs.load_uint(8)
                self.rest = TextChunks(self.chunks).fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Text")


# class for type `ProtoList`
class ProtoList(TLBComplex):
    class Tag(Enum):
        proto_list_nil = 0
        proto_list_next = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ProtoList.Tag.proto_list_nil: ProtoList.Record_proto_list_nil, ProtoList.Tag.proto_list_next: ProtoList.Record_proto_list_next}

    def get_tag(self, cs: CellSlice) -> Optional["ProtoList.Tag"]:
        return ProtoList.Tag(int(cs.preload_uint(1)))


    class Record_proto_list_nil(RecordBase):
        def get_tag_enum(self):
            return ProtoList.Tag.proto_list_nil

        def get_tag(self):
            return ProtoList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProtoList.cons_len_exact[self.get_tag_enum().value] if isinstance(ProtoList.cons_len_exact, list) else ProtoList.cons_len_exact

        def get_type_class(self):
            return ProtoList


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_proto_list_next(RecordBase):
        def get_tag_enum(self):
            return ProtoList.Tag.proto_list_next

        def get_tag(self):
            return ProtoList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ProtoList.cons_len_exact[self.get_tag_enum().value] if isinstance(ProtoList.cons_len_exact, list) else ProtoList.cons_len_exact

        def get_type_class(self):
            return ProtoList

        # head : Protocol
        head: "Enum" = None
        # tail : ProtoList
        tail: "CellSlice" = None

        def __init__(self, head: "Enum" = None, tail: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.head = head    
            self.field_names.append("head")
            self.tail = tail    
            self.field_names.append("tail")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.head = TLBComplex.constants["t_Protocol"].fetch_enum(cs) 
                self.tail = self.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ProtoList")


# class for type `Protocol`
class Protocol(TLBComplex):
    class Tag(Enum):
        proto_http = 0

    cons_len_exact = 16
    cons_tag = [0x4854]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {Protocol.Tag.proto_http: Protocol.Record}

    def get_tag(self, cs: CellSlice) -> Optional["Protocol.Tag"]:
        return Protocol.Tag(0)


    def fetch_enum(self, cs: CellSlice) -> int:
        value = cs.load_uint(16)
        assert value == 0x4854, 'Not valid tag fetched'
        return value


    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        cb.store_uint(0x4854, 16)
        return True


    class Record(RecordBase):
        def get_tag_enum(self):
            return Protocol.Tag.proto_http

        def get_tag(self):
            return Protocol.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return Protocol.cons_len_exact[self.get_tag_enum().value] if isinstance(Protocol.cons_len_exact, list) else Protocol.cons_len_exact

        def get_type_class(self):
            return Protocol


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x4854, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("Protocol")


# class for type `SmcCapList`
class SmcCapList(TLBComplex):
    class Tag(Enum):
        cap_list_nil = 0
        cap_list_next = 1

    cons_len_exact = 1
    cons_tag = [0, 1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SmcCapList.Tag.cap_list_nil: SmcCapList.Record_cap_list_nil, SmcCapList.Tag.cap_list_next: SmcCapList.Record_cap_list_next}

    def get_tag(self, cs: CellSlice) -> Optional["SmcCapList.Tag"]:
        return SmcCapList.Tag(int(cs.preload_uint(1)))


    class Record_cap_list_nil(RecordBase):
        def get_tag_enum(self):
            return SmcCapList.Tag.cap_list_nil

        def get_tag(self):
            return SmcCapList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmcCapList.cons_len_exact[self.get_tag_enum().value] if isinstance(SmcCapList.cons_len_exact, list) else SmcCapList.cons_len_exact

        def get_type_class(self):
            return SmcCapList


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 0, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cap_list_next(RecordBase):
        def get_tag_enum(self):
            return SmcCapList.Tag.cap_list_next

        def get_tag(self):
            return SmcCapList.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmcCapList.cons_len_exact[self.get_tag_enum().value] if isinstance(SmcCapList.cons_len_exact, list) else SmcCapList.cons_len_exact

        def get_type_class(self):
            return SmcCapList

        # head : SmcCapability
        head: "CellSlice" = None
        # tail : SmcCapList
        tail: "CellSlice" = None

        def __init__(self, head: "CellSlice" = None, tail: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.head = head    
            self.field_names.append("head")
            self.tail = tail    
            self.field_names.append("tail")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(1) == 1, 'Cons tag check failed'

                self.head = TLBComplex.constants["t_SmcCapability"].fetch(cs) 
                self.tail = self.fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SmcCapList")


# class for type `SmcCapability`
class SmcCapability(TLBComplex):
    class Tag(Enum):
        cap_is_wallet = 0
        cap_method_seqno = 1
        cap_method_pubkey = 2
        cap_name = 3

    cons_len = [16, 16, 16, 8]
    cons_tag = [0x2177, 0x5371, 0x71f4, 0xff]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {SmcCapability.Tag.cap_method_seqno: SmcCapability.Record_cap_method_seqno, SmcCapability.Tag.cap_method_pubkey: SmcCapability.Record_cap_method_pubkey, SmcCapability.Tag.cap_is_wallet: SmcCapability.Record_cap_is_wallet, SmcCapability.Tag.cap_name: SmcCapability.Record_cap_name}

    def get_tag(self, cs: CellSlice) -> Optional["SmcCapability.Tag"]:
        return SmcCapability.Tag(int(cs.bselect(3, 0x8e)))


    class Record_cap_method_seqno(RecordBase):
        def get_tag_enum(self):
            return SmcCapability.Tag.cap_method_seqno

        def get_tag(self):
            return SmcCapability.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmcCapability.cons_len_exact[self.get_tag_enum().value] if isinstance(SmcCapability.cons_len_exact, list) else SmcCapability.cons_len_exact

        def get_type_class(self):
            return SmcCapability


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x5371, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cap_method_pubkey(RecordBase):
        def get_tag_enum(self):
            return SmcCapability.Tag.cap_method_pubkey

        def get_tag(self):
            return SmcCapability.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmcCapability.cons_len_exact[self.get_tag_enum().value] if isinstance(SmcCapability.cons_len_exact, list) else SmcCapability.cons_len_exact

        def get_type_class(self):
            return SmcCapability


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x71f4, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cap_is_wallet(RecordBase):
        def get_tag_enum(self):
            return SmcCapability.Tag.cap_is_wallet

        def get_tag(self):
            return SmcCapability.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmcCapability.cons_len_exact[self.get_tag_enum().value] if isinstance(SmcCapability.cons_len_exact, list) else SmcCapability.cons_len_exact

        def get_type_class(self):
            return SmcCapability


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x2177, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_cap_name(RecordBase):
        def get_tag_enum(self):
            return SmcCapability.Tag.cap_name

        def get_tag(self):
            return SmcCapability.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return SmcCapability.cons_len_exact[self.get_tag_enum().value] if isinstance(SmcCapability.cons_len_exact, list) else SmcCapability.cons_len_exact

        def get_type_class(self):
            return SmcCapability

        # name : Text
        name: "CellSlice" = None

        def __init__(self, name: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.name = name    
            self.field_names.append("name")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(8) == 0xff, 'Cons tag check failed'

                self.name = TLBComplex.constants["t_Text"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("SmcCapability")


# class for type `DNSRecord`
class DNSRecord(TLBComplex):
    class Tag(Enum):
        dns_text = 0
        dns_storage_address = 1
        dns_smc_address = 2
        dns_adnl_address = 3
        dns_next_resolver = 4

    cons_len_exact = 16
    cons_tag = [0x1eda, 0x7473, 0x9fd3, 0xad01, 0xba93]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {DNSRecord.Tag.dns_text: DNSRecord.Record_dns_text, DNSRecord.Tag.dns_next_resolver: DNSRecord.Record_dns_next_resolver, DNSRecord.Tag.dns_adnl_address: DNSRecord.Record_dns_adnl_address, DNSRecord.Tag.dns_smc_address: DNSRecord.Record_dns_smc_address, DNSRecord.Tag.dns_storage_address: DNSRecord.Record_dns_storage_address}

    def get_tag(self, cs: CellSlice) -> Optional["DNSRecord.Tag"]:
        return DNSRecord.Tag(int(cs.bselect(4, 0xe82)))


    class Record_dns_text(RecordBase):
        def get_tag_enum(self):
            return DNSRecord.Tag.dns_text

        def get_tag(self):
            return DNSRecord.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DNSRecord.cons_len_exact[self.get_tag_enum().value] if isinstance(DNSRecord.cons_len_exact, list) else DNSRecord.cons_len_exact

        def get_type_class(self):
            return DNSRecord

        # Text
        x: "CellSlice" = None

        def __init__(self, x: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.x = x    
            self.field_names.append("x")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x1eda, 'Cons tag check failed'

                self.x = TLBComplex.constants["t_Text"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_dns_next_resolver(RecordBase):
        def get_tag_enum(self):
            return DNSRecord.Tag.dns_next_resolver

        def get_tag(self):
            return DNSRecord.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DNSRecord.cons_len_exact[self.get_tag_enum().value] if isinstance(DNSRecord.cons_len_exact, list) else DNSRecord.cons_len_exact

        def get_type_class(self):
            return DNSRecord

        # resolver : MsgAddressInt
        resolver: "CellSlice" = None

        def __init__(self, resolver: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.resolver = resolver    
            self.field_names.append("resolver")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0xba93, 'Cons tag check failed'

                self.resolver = TLBComplex.constants["t_MsgAddressInt"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_dns_adnl_address(RecordBase):
        def get_tag_enum(self):
            return DNSRecord.Tag.dns_adnl_address

        def get_tag(self):
            return DNSRecord.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DNSRecord.cons_len_exact[self.get_tag_enum().value] if isinstance(DNSRecord.cons_len_exact, list) else DNSRecord.cons_len_exact

        def get_type_class(self):
            return DNSRecord

        # adnl_addr : bits256
        adnl_addr: "bitstring.BitArray" = None
        # flags : ## 8
        flags: "int" = None
        # proto_list : flags.0?ProtoList
        proto_list: "CellSlice" = None

        def __init__(self, adnl_addr: "bitstring.BitArray" = None, flags: "int" = None, proto_list: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.adnl_addr = adnl_addr    
            self.field_names.append("adnl_addr")
            self.flags = flags    
            self.field_names.append("flags")
            self.proto_list = proto_list    
            self.conditional_fields.append("proto_list")    
            self.field_names.append("proto_list")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0xad01, 'Cons tag check failed'

                self.adnl_addr = cs.load_bitstring(256)
                self.flags = cs.load_uint(8)
                assert self.flags <= 1, 'Params not equal: flags and 1'

                if ((self.flags & (1 << 0)) != 0):
                    self.proto_list = TLBComplex.constants["t_ProtoList"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_dns_smc_address(RecordBase):
        def get_tag_enum(self):
            return DNSRecord.Tag.dns_smc_address

        def get_tag(self):
            return DNSRecord.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DNSRecord.cons_len_exact[self.get_tag_enum().value] if isinstance(DNSRecord.cons_len_exact, list) else DNSRecord.cons_len_exact

        def get_type_class(self):
            return DNSRecord

        # smc_addr : MsgAddressInt
        smc_addr: "CellSlice" = None
        # flags : ## 8
        flags: "int" = None
        # cap_list : flags.0?SmcCapList
        cap_list: "CellSlice" = None

        def __init__(self, smc_addr: "CellSlice" = None, flags: "int" = None, cap_list: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.smc_addr = smc_addr    
            self.field_names.append("smc_addr")
            self.flags = flags    
            self.field_names.append("flags")
            self.cap_list = cap_list    
            self.conditional_fields.append("cap_list")    
            self.field_names.append("cap_list")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x9fd3, 'Cons tag check failed'

                self.smc_addr = TLBComplex.constants["t_MsgAddressInt"].fetch(cs) 
                self.flags = cs.load_uint(8)
                assert self.flags <= 1, 'Params not equal: flags and 1'

                if ((self.flags & (1 << 0)) != 0):
                    self.cap_list = TLBComplex.constants["t_SmcCapList"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_dns_storage_address(RecordBase):
        def get_tag_enum(self):
            return DNSRecord.Tag.dns_storage_address

        def get_tag(self):
            return DNSRecord.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return DNSRecord.cons_len_exact[self.get_tag_enum().value] if isinstance(DNSRecord.cons_len_exact, list) else DNSRecord.cons_len_exact

        def get_type_class(self):
            return DNSRecord

        # bag_id : bits256
        bag_id: "bitstring.BitArray" = None

        def __init__(self, bag_id: "bitstring.BitArray" = None):
            super().__init__()
            self.field_names = []
            self.bag_id = bag_id    
            self.field_names.append("bag_id")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(16) == 0x7473, 'Cons tag check failed'

                self.bag_id = cs.load_bitstring(256)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("DNSRecord")


# class for type `ChanConfig`
class ChanConfig(TLBComplex):
    class Tag(Enum):
        chan_config = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanConfig.Tag.chan_config: ChanConfig.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ChanConfig.Tag"]:
        return ChanConfig.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ChanConfig.Tag.chan_config

        def get_tag(self):
            return ChanConfig.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanConfig.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanConfig.cons_len_exact, list) else ChanConfig.cons_len_exact

        def get_type_class(self):
            return ChanConfig

        # init_timeout : uint32
        init_timeout: "int" = None
        # close_timeout : uint32
        close_timeout: "int" = None
        # a_key : bits256
        a_key: "bitstring.BitArray" = None
        # b_key : bits256
        b_key: "bitstring.BitArray" = None
        # a_addr : ^MsgAddressInt
        a_addr: "Cell" = None
        # b_addr : ^MsgAddressInt
        b_addr: "Cell" = None
        # channel_id : uint64
        channel_id: "int" = None
        # min_A_extra : Grams
        min_A_extra: "CellSlice" = None

        def __init__(self, init_timeout: "int" = None, close_timeout: "int" = None, a_key: "bitstring.BitArray" = None, b_key: "bitstring.BitArray" = None, a_addr: "Cell" = None, b_addr: "Cell" = None, channel_id: "int" = None, min_A_extra: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.init_timeout = init_timeout    
            self.field_names.append("init_timeout")
            self.close_timeout = close_timeout    
            self.field_names.append("close_timeout")
            self.a_key = a_key    
            self.field_names.append("a_key")
            self.b_key = b_key    
            self.field_names.append("b_key")
            self.a_addr = a_addr    
            self.field_names.append("a_addr")
            self.b_addr = b_addr    
            self.field_names.append("b_addr")
            self.channel_id = channel_id    
            self.field_names.append("channel_id")
            self.min_A_extra = min_A_extra    
            self.field_names.append("min_A_extra")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.init_timeout = cs.load_uint(32)
                self.close_timeout = cs.load_uint(32)
                self.a_key = cs.load_bitstring(256)
                self.b_key = cs.load_bitstring(256)
                self.a_addr = cs.load_ref()
                
                if rec_unpack:
                    self.a_addr = TLBComplex.constants["t_Ref_MsgAddressInt"].fetch(self.a_addr, True, strict) # at 1
                    assert self.a_addr is not None

                self.b_addr = cs.load_ref()
                
                if rec_unpack:
                    self.b_addr = TLBComplex.constants["t_Ref_MsgAddressInt"].fetch(self.b_addr, True, strict) # at 1
                    assert self.b_addr is not None

                self.channel_id = cs.load_uint(64)
                self.min_A_extra = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanConfig")


# class for type `ChanState`
class ChanState(TLBComplex):
    class Tag(Enum):
        chan_state_init = 0
        chan_state_close = 1
        chan_state_payout = 2

    cons_len_exact = 3
    cons_tag = [0, 1, 2]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanState.Tag.chan_state_init: ChanState.Record_chan_state_init, ChanState.Tag.chan_state_close: ChanState.Record_chan_state_close, ChanState.Tag.chan_state_payout: ChanState.Record_chan_state_payout}

    def get_tag(self, cs: CellSlice) -> Optional["ChanState.Tag"]:
        return ChanState.Tag(int(cs.bselect(3, 7)))


    class Record_chan_state_init(RecordBase):
        def get_tag_enum(self):
            return ChanState.Tag.chan_state_init

        def get_tag(self):
            return ChanState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanState.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanState.cons_len_exact, list) else ChanState.cons_len_exact

        def get_type_class(self):
            return ChanState

        # signed_A : Bool
        signed_A: "bool" = None
        # signed_B : Bool
        signed_B: "bool" = None
        # min_A : Grams
        min_A: "CellSlice" = None
        # min_B : Grams
        min_B: "CellSlice" = None
        # expire_at : uint32
        expire_at: "int" = None
        # A : Grams
        A: "CellSlice" = None
        # B : Grams
        B: "CellSlice" = None

        def __init__(self, signed_A: "bool" = None, signed_B: "bool" = None, min_A: "CellSlice" = None, min_B: "CellSlice" = None, expire_at: "int" = None, A: "CellSlice" = None, B: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.signed_A = signed_A    
            self.field_names.append("signed_A")
            self.signed_B = signed_B    
            self.field_names.append("signed_B")
            self.min_A = min_A    
            self.field_names.append("min_A")
            self.min_B = min_B    
            self.field_names.append("min_B")
            self.expire_at = expire_at    
            self.field_names.append("expire_at")
            self.A = A    
            self.field_names.append("A")
            self.B = B    
            self.field_names.append("B")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 0, 'Cons tag check failed'

                self.signed_A = cs.load_bool()
                self.signed_B = cs.load_bool()
                self.min_A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.min_B = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.expire_at = cs.load_uint(32)
                self.A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.B = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chan_state_close(RecordBase):
        def get_tag_enum(self):
            return ChanState.Tag.chan_state_close

        def get_tag(self):
            return ChanState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanState.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanState.cons_len_exact, list) else ChanState.cons_len_exact

        def get_type_class(self):
            return ChanState

        # signed_A : Bool
        signed_A: "bool" = None
        # signed_B : Bool
        signed_B: "bool" = None
        # promise_A : Grams
        promise_A: "CellSlice" = None
        # promise_B : Grams
        promise_B: "CellSlice" = None
        # expire_at : uint32
        expire_at: "int" = None
        # A : Grams
        A: "CellSlice" = None
        # B : Grams
        B: "CellSlice" = None

        def __init__(self, signed_A: "bool" = None, signed_B: "bool" = None, promise_A: "CellSlice" = None, promise_B: "CellSlice" = None, expire_at: "int" = None, A: "CellSlice" = None, B: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.signed_A = signed_A    
            self.field_names.append("signed_A")
            self.signed_B = signed_B    
            self.field_names.append("signed_B")
            self.promise_A = promise_A    
            self.field_names.append("promise_A")
            self.promise_B = promise_B    
            self.field_names.append("promise_B")
            self.expire_at = expire_at    
            self.field_names.append("expire_at")
            self.A = A    
            self.field_names.append("A")
            self.B = B    
            self.field_names.append("B")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 1, 'Cons tag check failed'

                self.signed_A = cs.load_bool()
                self.signed_B = cs.load_bool()
                self.promise_A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.promise_B = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.expire_at = cs.load_uint(32)
                self.A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.B = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chan_state_payout(RecordBase):
        def get_tag_enum(self):
            return ChanState.Tag.chan_state_payout

        def get_tag(self):
            return ChanState.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanState.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanState.cons_len_exact, list) else ChanState.cons_len_exact

        def get_type_class(self):
            return ChanState

        # A : Grams
        A: "CellSlice" = None
        # B : Grams
        B: "CellSlice" = None

        def __init__(self, A: "CellSlice" = None, B: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.A = A    
            self.field_names.append("A")
            self.B = B    
            self.field_names.append("B")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(3) == 2, 'Cons tag check failed'

                self.A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.B = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanState")


# class for type `ChanPromise`
class ChanPromise(TLBComplex):
    class Tag(Enum):
        chan_promise = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanPromise.Tag.chan_promise: ChanPromise.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ChanPromise.Tag"]:
        return ChanPromise.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ChanPromise.Tag.chan_promise

        def get_tag(self):
            return ChanPromise.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanPromise.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanPromise.cons_len_exact, list) else ChanPromise.cons_len_exact

        def get_type_class(self):
            return ChanPromise

        # channel_id : uint64
        channel_id: "int" = None
        # promise_A : Grams
        promise_A: "CellSlice" = None
        # promise_B : Grams
        promise_B: "CellSlice" = None

        def __init__(self, channel_id: "int" = None, promise_A: "CellSlice" = None, promise_B: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.channel_id = channel_id    
            self.field_names.append("channel_id")
            self.promise_A = promise_A    
            self.field_names.append("promise_A")
            self.promise_B = promise_B    
            self.field_names.append("promise_B")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.channel_id = cs.load_uint(64)
                self.promise_A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.promise_B = TLBComplex.constants["t_Grams"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanPromise")


# class for type `ChanSignedPromise`
class ChanSignedPromise(TLBComplex):
    class Tag(Enum):
        chan_signed_promise = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanSignedPromise.Tag.chan_signed_promise: ChanSignedPromise.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ChanSignedPromise.Tag"]:
        return ChanSignedPromise.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ChanSignedPromise.Tag.chan_signed_promise

        def get_tag(self):
            return ChanSignedPromise.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanSignedPromise.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanSignedPromise.cons_len_exact, list) else ChanSignedPromise.cons_len_exact

        def get_type_class(self):
            return ChanSignedPromise

        # sig : Maybe ^bits512
        sig: "CellSlice" = None
        # promise : ChanPromise
        promise: "CellSlice" = None

        def __init__(self, sig: "CellSlice" = None, promise: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.sig = sig    
            self.field_names.append("sig")
            self.promise = promise    
            self.field_names.append("promise")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.sig = TLBComplex.constants["t_Maybe_Ref_bits512"].fetch(cs) 
                self.promise = TLBComplex.constants["t_ChanPromise"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanSignedPromise")


# class for type `ChanMsg`
class ChanMsg(TLBComplex):
    class Tag(Enum):
        chan_msg_init = 0
        chan_msg_payout = 1
        chan_msg_timeout = 2
        chan_msg_close = 3

    cons_len_exact = 32
    cons_tag = [0x27317822, 0x37fe7810, 0x43278a28, 0xf28ae183]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanMsg.Tag.chan_msg_init: ChanMsg.Record_chan_msg_init, ChanMsg.Tag.chan_msg_close: ChanMsg.Record_chan_msg_close, ChanMsg.Tag.chan_msg_timeout: ChanMsg.Record_chan_msg_timeout, ChanMsg.Tag.chan_msg_payout: ChanMsg.Record_chan_msg_payout}

    def get_tag(self, cs: CellSlice) -> Optional["ChanMsg.Tag"]:
        return ChanMsg.Tag(int(cs.bselect(4, 0x801c)))


    class Record_chan_msg_init(RecordBase):
        def get_tag_enum(self):
            return ChanMsg.Tag.chan_msg_init

        def get_tag(self):
            return ChanMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanMsg.cons_len_exact, list) else ChanMsg.cons_len_exact

        def get_type_class(self):
            return ChanMsg

        # inc_A : Grams
        inc_A: "CellSlice" = None
        # inc_B : Grams
        inc_B: "CellSlice" = None
        # min_A : Grams
        min_A: "CellSlice" = None
        # min_B : Grams
        min_B: "CellSlice" = None
        # channel_id : uint64
        channel_id: "int" = None

        def __init__(self, inc_A: "CellSlice" = None, inc_B: "CellSlice" = None, min_A: "CellSlice" = None, min_B: "CellSlice" = None, channel_id: "int" = None):
            super().__init__()
            self.field_names = []
            self.inc_A = inc_A    
            self.field_names.append("inc_A")
            self.inc_B = inc_B    
            self.field_names.append("inc_B")
            self.min_A = min_A    
            self.field_names.append("min_A")
            self.min_B = min_B    
            self.field_names.append("min_B")
            self.channel_id = channel_id    
            self.field_names.append("channel_id")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x27317822, 'Cons tag check failed'

                self.inc_A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.inc_B = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.min_A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.min_B = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.channel_id = cs.load_uint(64)                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chan_msg_close(RecordBase):
        def get_tag_enum(self):
            return ChanMsg.Tag.chan_msg_close

        def get_tag(self):
            return ChanMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanMsg.cons_len_exact, list) else ChanMsg.cons_len_exact

        def get_type_class(self):
            return ChanMsg

        # extra_A : Grams
        extra_A: "CellSlice" = None
        # extra_B : Grams
        extra_B: "CellSlice" = None
        # promise : ChanSignedPromise
        promise: "CellSlice" = None

        def __init__(self, extra_A: "CellSlice" = None, extra_B: "CellSlice" = None, promise: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.extra_A = extra_A    
            self.field_names.append("extra_A")
            self.extra_B = extra_B    
            self.field_names.append("extra_B")
            self.promise = promise    
            self.field_names.append("promise")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0xf28ae183, 'Cons tag check failed'

                self.extra_A = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.extra_B = TLBComplex.constants["t_Grams"].fetch(cs) 
                self.promise = TLBComplex.constants["t_ChanSignedPromise"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chan_msg_timeout(RecordBase):
        def get_tag_enum(self):
            return ChanMsg.Tag.chan_msg_timeout

        def get_tag(self):
            return ChanMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanMsg.cons_len_exact, list) else ChanMsg.cons_len_exact

        def get_type_class(self):
            return ChanMsg


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x43278a28, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    class Record_chan_msg_payout(RecordBase):
        def get_tag_enum(self):
            return ChanMsg.Tag.chan_msg_payout

        def get_tag(self):
            return ChanMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanMsg.cons_len_exact, list) else ChanMsg.cons_len_exact

        def get_type_class(self):
            return ChanMsg


        def __init__(self):
            super().__init__()
        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x37fe7810, 'Cons tag check failed'
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanMsg")


# class for type `ChanSignedMsg`
class ChanSignedMsg(TLBComplex):
    class Tag(Enum):
        chan_signed_msg = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanSignedMsg.Tag.chan_signed_msg: ChanSignedMsg.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ChanSignedMsg.Tag"]:
        return ChanSignedMsg.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ChanSignedMsg.Tag.chan_signed_msg

        def get_tag(self):
            return ChanSignedMsg.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanSignedMsg.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanSignedMsg.cons_len_exact, list) else ChanSignedMsg.cons_len_exact

        def get_type_class(self):
            return ChanSignedMsg

        # sig_A : Maybe ^bits512
        sig_A: "CellSlice" = None
        # sig_B : Maybe ^bits512
        sig_B: "CellSlice" = None
        # msg : ChanMsg
        msg: "CellSlice" = None

        def __init__(self, sig_A: "CellSlice" = None, sig_B: "CellSlice" = None, msg: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.sig_A = sig_A    
            self.field_names.append("sig_A")
            self.sig_B = sig_B    
            self.field_names.append("sig_B")
            self.msg = msg    
            self.field_names.append("msg")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.sig_A = TLBComplex.constants["t_Maybe_Ref_bits512"].fetch(cs) 
                self.sig_B = TLBComplex.constants["t_Maybe_Ref_bits512"].fetch(cs) 
                self.msg = TLBComplex.constants["t_ChanMsg"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanSignedMsg")


# class for type `ChanOp`
class ChanOp(TLBComplex):
    class Tag(Enum):
        chan_op_cmd = 0

    cons_len_exact = 32
    cons_tag = [0x912838d1]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanOp.Tag.chan_op_cmd: ChanOp.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ChanOp.Tag"]:
        return ChanOp.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ChanOp.Tag.chan_op_cmd

        def get_tag(self):
            return ChanOp.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanOp.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanOp.cons_len_exact, list) else ChanOp.cons_len_exact

        def get_type_class(self):
            return ChanOp

        # msg : ChanSignedMsg
        msg: "CellSlice" = None

        def __init__(self, msg: "CellSlice" = None):
            super().__init__()
            self.field_names = []
            self.msg = msg    
            self.field_names.append("msg")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                assert cs.load_uint(32) == 0x912838d1, 'Cons tag check failed'

                self.msg = TLBComplex.constants["t_ChanSignedMsg"].fetch(cs)                 
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanOp")


# class for type `ChanData`
class ChanData(TLBComplex):
    class Tag(Enum):
        chan_data = 0

    cons_len_exact = 0
    cons_tag = [0]


    def __init__(self):
        super().__init__()

        self.tag_to_class = {ChanData.Tag.chan_data: ChanData.Record}

    def get_tag(self, cs: CellSlice) -> Optional["ChanData.Tag"]:
        return ChanData.Tag(0)


    class Record(RecordBase):
        def get_tag_enum(self):
            return ChanData.Tag.chan_data

        def get_tag(self):
            return ChanData.cons_tag[self.get_tag_enum().value]

        def get_tag_len(self):
            return ChanData.cons_len_exact[self.get_tag_enum().value] if isinstance(ChanData.cons_len_exact, list) else ChanData.cons_len_exact

        def get_type_class(self):
            return ChanData

        # config : ^ChanConfig
        config: "Cell" = None
        # state : ^ChanState
        state: "Cell" = None

        def __init__(self, config: "Cell" = None, state: "Cell" = None):
            super().__init__()
            self.field_names = []
            self.config = config    
            self.field_names.append("config")
            self.state = state    
            self.field_names.append("state")

        def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                self.config = cs.load_ref()
                
                if rec_unpack:
                    self.config = TLBComplex.constants["t_Ref_ChanConfig"].fetch(self.config, True, strict) # at 1
                    assert self.config is not None

                self.state = cs.load_ref()
                
                if rec_unpack:
                    self.state = TLBComplex.constants["t_Ref_ChanState"].fetch(self.state, True, strict) # at 1
                    assert self.state is not None
                
                if strict:
                    for i in self.field_names:
                        if i not in self.conditional_fields:
                            assert getattr(self, i) is not None, f'Field {i} is None'
            except (TabError):
                return False
            return True

        def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = True) -> bool:
            try:
                if cell_ref.is_null():
                    return False
                cs = cell_ref.begin_parse()
                return self.unpack(cs) and cs.empty_ext()

            except (TabError):
                return False
            return True

    def always_special(self):
        return False


tlb_classes.append("ChanData")

# definitions of constants
TLBComplex.constants["t_Unit"] = Unit()
TLBComplex.constants["t_Truet"] = Truet()
TLBComplex.constants["t_Bool"] = Bool()
TLBComplex.constants["t_BoolFalse"] = BoolFalse()
TLBComplex.constants["t_BoolTrue"] = BoolTrue()
TLBComplex.constants["t_Bit"] = Bit()
TLBComplex.constants["t_Unary"] = Unary()
TLBComplex.constants["t_MsgAddressExt"] = MsgAddressExt()
TLBComplex.constants["t_Anycast"] = Anycast()
TLBComplex.constants["t_MsgAddressInt"] = MsgAddressInt()
TLBComplex.constants["t_MsgAddress"] = MsgAddress()
TLBComplex.constants["t_Grams"] = Grams()
TLBComplex.constants["t_Coins"] = Coins()
TLBComplex.constants["t_ExtraCurrencyCollection"] = ExtraCurrencyCollection()
TLBComplex.constants["t_CurrencyCollection"] = CurrencyCollection()
TLBComplex.constants["t_CommonMsgInfo"] = CommonMsgInfo()
TLBComplex.constants["t_CommonMsgInfoRelaxed"] = CommonMsgInfoRelaxed()
TLBComplex.constants["t_TickTock"] = TickTock()
TLBComplex.constants["t_StateInit"] = StateInit()
TLBComplex.constants["t_StateInitWithLibs"] = StateInitWithLibs()
TLBComplex.constants["t_SimpleLib"] = SimpleLib()
TLBComplex.constants["t_MessageAny"] = MessageAny()
TLBComplex.constants["t_IntermediateAddress"] = IntermediateAddress()
TLBComplex.constants["t_MsgEnvelope"] = MsgEnvelope()
TLBComplex.constants["t_InMsg"] = InMsg()
TLBComplex.constants["t_ImportFees"] = ImportFees()
TLBComplex.constants["t_InMsgDescr"] = InMsgDescr()
TLBComplex.constants["t_OutMsg"] = OutMsg()
TLBComplex.constants["t_EnqueuedMsg"] = EnqueuedMsg()
TLBComplex.constants["t_OutMsgDescr"] = OutMsgDescr()
TLBComplex.constants["t_OutMsgQueue"] = OutMsgQueue()
TLBComplex.constants["t_ProcessedUpto"] = ProcessedUpto()
TLBComplex.constants["t_ProcessedInfo"] = ProcessedInfo()
TLBComplex.constants["t_IhrPendingSince"] = IhrPendingSince()
TLBComplex.constants["t_IhrPendingInfo"] = IhrPendingInfo()
TLBComplex.constants["t_OutMsgQueueInfo"] = OutMsgQueueInfo()
TLBComplex.constants["t_StorageUsed"] = StorageUsed()
TLBComplex.constants["t_StorageUsedShort"] = StorageUsedShort()
TLBComplex.constants["t_StorageInfo"] = StorageInfo()
TLBComplex.constants["t_Account"] = Account()
TLBComplex.constants["t_AccountStorage"] = AccountStorage()
TLBComplex.constants["t_AccountState"] = AccountState()
TLBComplex.constants["t_AccountStatus"] = AccountStatus()
TLBComplex.constants["t_ShardAccount"] = ShardAccount()
TLBComplex.constants["t_DepthBalanceInfo"] = DepthBalanceInfo()
TLBComplex.constants["t_ShardAccounts"] = ShardAccounts()
TLBComplex.constants["t_Transaction_aux"] = Transaction_aux()
TLBComplex.constants["t_Transaction"] = Transaction()
TLBComplex.constants["t_AccountBlock"] = AccountBlock()
TLBComplex.constants["t_ShardAccountBlocks"] = ShardAccountBlocks()
TLBComplex.constants["t_TrStoragePhase"] = TrStoragePhase()
TLBComplex.constants["t_AccStatusChange"] = AccStatusChange()
TLBComplex.constants["t_TrCreditPhase"] = TrCreditPhase()
TLBComplex.constants["t_TrComputePhase_aux"] = TrComputePhase_aux()
TLBComplex.constants["t_TrComputePhase"] = TrComputePhase()
TLBComplex.constants["t_ComputeSkipReason"] = ComputeSkipReason()
TLBComplex.constants["t_TrActionPhase"] = TrActionPhase()
TLBComplex.constants["t_TrBouncePhase"] = TrBouncePhase()
TLBComplex.constants["t_SplitMergeInfo"] = SplitMergeInfo()
TLBComplex.constants["t_TransactionDescr"] = TransactionDescr()
TLBComplex.constants["t_SmartContractInfo"] = SmartContractInfo()
TLBComplex.constants["t_LibRef"] = LibRef()
TLBComplex.constants["t_OutAction"] = OutAction()
TLBComplex.constants["t_OutListNode"] = OutListNode()
TLBComplex.constants["t_ShardIdent"] = ShardIdent()
TLBComplex.constants["t_ExtBlkRef"] = ExtBlkRef()
TLBComplex.constants["t_BlockIdExt"] = BlockIdExt()
TLBComplex.constants["t_BlkMasterInfo"] = BlkMasterInfo()
TLBComplex.constants["t_ShardStateUnsplit_aux"] = ShardStateUnsplit_aux()
TLBComplex.constants["t_ShardStateUnsplit"] = ShardStateUnsplit()
TLBComplex.constants["t_ShardState"] = ShardState()
TLBComplex.constants["t_LibDescr"] = LibDescr()
TLBComplex.constants["t_BlockInfo"] = BlockInfo()
TLBComplex.constants["t_Block"] = Block()
TLBComplex.constants["t_BlockExtra"] = BlockExtra()
TLBComplex.constants["t_TYPE_1653"] = TYPE_1653()
TLBComplex.constants["t_TYPE_1654"] = TYPE_1654()
TLBComplex.constants["t_ValueFlow"] = ValueFlow()
TLBComplex.constants["t_FutureSplitMerge"] = FutureSplitMerge()
TLBComplex.constants["t_ShardDescr_aux"] = ShardDescr_aux()
TLBComplex.constants["t_ShardDescr"] = ShardDescr()
TLBComplex.constants["t_ShardHashes"] = ShardHashes()
TLBComplex.constants["t_ShardFeeCreated"] = ShardFeeCreated()
TLBComplex.constants["t_ShardFees"] = ShardFees()
TLBComplex.constants["t_ConfigParams"] = ConfigParams()
TLBComplex.constants["t_ValidatorInfo"] = ValidatorInfo()
TLBComplex.constants["t_ValidatorBaseInfo"] = ValidatorBaseInfo()
TLBComplex.constants["t_KeyMaxLt"] = KeyMaxLt()
TLBComplex.constants["t_KeyExtBlkRef"] = KeyExtBlkRef()
TLBComplex.constants["t_OldMcBlocksInfo"] = OldMcBlocksInfo()
TLBComplex.constants["t_Counters"] = Counters()
TLBComplex.constants["t_CreatorStats"] = CreatorStats()
TLBComplex.constants["t_BlockCreateStats"] = BlockCreateStats()
TLBComplex.constants["t_McStateExtra_aux"] = McStateExtra_aux()
TLBComplex.constants["t_McStateExtra"] = McStateExtra()
TLBComplex.constants["t_SigPubKey"] = SigPubKey()
TLBComplex.constants["t_CryptoSignatureSimple"] = CryptoSignatureSimple()
TLBComplex.constants["t_CryptoSignaturePair"] = CryptoSignaturePair()
TLBComplex.constants["t_Certificate"] = Certificate()
TLBComplex.constants["t_CertificateEnv"] = CertificateEnv()
TLBComplex.constants["t_SignedCertificate"] = SignedCertificate()
TLBComplex.constants["t_CryptoSignature"] = CryptoSignature()
TLBComplex.constants["t_McBlockExtra_aux"] = McBlockExtra_aux()
TLBComplex.constants["t_McBlockExtra"] = McBlockExtra()
TLBComplex.constants["t_ValidatorDescr"] = ValidatorDescr()
TLBComplex.constants["t_ValidatorSet"] = ValidatorSet()
TLBComplex.constants["t_BurningConfig"] = BurningConfig()
TLBComplex.constants["t_GlobalVersion"] = GlobalVersion()
TLBComplex.constants["t_ConfigProposalSetup"] = ConfigProposalSetup()
TLBComplex.constants["t_ConfigVotingSetup"] = ConfigVotingSetup()
TLBComplex.constants["t_ConfigProposal"] = ConfigProposal()
TLBComplex.constants["t_ConfigProposalStatus"] = ConfigProposalStatus()
TLBComplex.constants["t_WcSplitMergeTimings"] = WcSplitMergeTimings()
TLBComplex.constants["t_WorkchainDescr"] = WorkchainDescr()
TLBComplex.constants["t_ComplaintPricing"] = ComplaintPricing()
TLBComplex.constants["t_BlockCreateFees"] = BlockCreateFees()
TLBComplex.constants["t_StoragePrices"] = StoragePrices()
TLBComplex.constants["t_GasLimitsPrices"] = GasLimitsPrices()
TLBComplex.constants["t_ParamLimits"] = ParamLimits()
TLBComplex.constants["t_BlockLimits"] = BlockLimits()
TLBComplex.constants["t_MsgForwardPrices"] = MsgForwardPrices()
TLBComplex.constants["t_CatchainConfig"] = CatchainConfig()
TLBComplex.constants["t_ConsensusConfig"] = ConsensusConfig()
TLBComplex.constants["t_ValidatorTempKey"] = ValidatorTempKey()
TLBComplex.constants["t_ValidatorSignedTempKey"] = ValidatorSignedTempKey()
TLBComplex.constants["t_MisbehaviourPunishmentConfig"] = MisbehaviourPunishmentConfig()
TLBComplex.constants["t_SizeLimitsConfig"] = SizeLimitsConfig()
TLBComplex.constants["t_SuspendedAddressList"] = SuspendedAddressList()
TLBComplex.constants["t_OracleBridgeParams"] = OracleBridgeParams()
TLBComplex.constants["t_JettonBridgePrices"] = JettonBridgePrices()
TLBComplex.constants["t_JettonBridgeParams"] = JettonBridgeParams()
TLBComplex.constants["t_BlockSignaturesPure"] = BlockSignaturesPure()
TLBComplex.constants["t_BlockSignatures"] = BlockSignatures()
TLBComplex.constants["t_BlockProof"] = BlockProof()
TLBComplex.constants["t_TopBlockDescr"] = TopBlockDescr()
TLBComplex.constants["t_TopBlockDescrSet"] = TopBlockDescrSet()
TLBComplex.constants["t_ProducerInfo"] = ProducerInfo()
TLBComplex.constants["t_ComplaintDescr"] = ComplaintDescr()
TLBComplex.constants["t_ValidatorComplaint"] = ValidatorComplaint()
TLBComplex.constants["t_ValidatorComplaintStatus"] = ValidatorComplaintStatus()
TLBComplex.constants["t_VmCellSlice"] = VmCellSlice()
TLBComplex.constants["t_VmStackValue"] = VmStackValue()
TLBComplex.constants["t_VmStack"] = VmStack()
TLBComplex.constants["t_VmSaveList"] = VmSaveList()
TLBComplex.constants["t_VmGasLimits_aux"] = VmGasLimits_aux()
TLBComplex.constants["t_VmGasLimits"] = VmGasLimits()
TLBComplex.constants["t_VmLibraries"] = VmLibraries()
TLBComplex.constants["t_VmControlData"] = VmControlData()
TLBComplex.constants["t_VmCont"] = VmCont()
TLBComplex.constants["t_DNS_RecordSet"] = DNS_RecordSet()
TLBComplex.constants["t_Text"] = Text()
TLBComplex.constants["t_ProtoList"] = ProtoList()
TLBComplex.constants["t_Protocol"] = Protocol()
TLBComplex.constants["t_SmcCapList"] = SmcCapList()
TLBComplex.constants["t_SmcCapability"] = SmcCapability()
TLBComplex.constants["t_DNSRecord"] = DNSRecord()
TLBComplex.constants["t_ChanConfig"] = ChanConfig()
TLBComplex.constants["t_ChanState"] = ChanState()
TLBComplex.constants["t_ChanPromise"] = ChanPromise()
TLBComplex.constants["t_ChanSignedPromise"] = ChanSignedPromise()
TLBComplex.constants["t_ChanMsg"] = ChanMsg()
TLBComplex.constants["t_ChanSignedMsg"] = ChanSignedMsg()
TLBComplex.constants["t_ChanOp"] = ChanOp()
TLBComplex.constants["t_ChanData"] = ChanData()

TLBComplex.constants["t_natwidth_1"] = NatWidth(1)
TLBComplex.constants["t_natwidth_9"] = NatWidth(9)
TLBComplex.constants["t_natleq_30"] = NatLeq(30)
TLBComplex.constants["t_Maybe_Anycast"] = Maybe(TLBComplex.constants["t_Anycast"])
TLBComplex.constants["t_int8"] = Int(8)
TLBComplex.constants["t_bits256"] = Bits(256)
TLBComplex.constants["t_int32"] = Int(32)
TLBComplex.constants["t_VarUInteger_16"] = VarUInteger(16)
TLBComplex.constants["t_VarUInteger_32"] = VarUInteger(32)
TLBComplex.constants["t_HashmapE_32_VarUInteger_32"] = HashmapE(32, TLBComplex.constants["t_VarUInteger_32"])
TLBComplex.constants["t_uint64"] = UInt(64)
TLBComplex.constants["t_uint32"] = UInt(32)
TLBComplex.constants["t_natwidth_5"] = NatWidth(5)
TLBComplex.constants["t_Maybe_natwidth_5"] = Maybe(TLBComplex.constants["t_natwidth_5"])
TLBComplex.constants["t_Maybe_TickTock"] = Maybe(TLBComplex.constants["t_TickTock"])
TLBComplex.constants["t_Maybe_Ref_Cell"] = Maybe(TLBComplex.constants["t_RefCell"])
TLBComplex.constants["t_HashmapE_256_SimpleLib"] = HashmapE(256, TLBComplex.constants["t_SimpleLib"])
TLBComplex.constants["t_Ref_StateInit"] = RefT(TLBComplex.constants["t_StateInit"])
TLBComplex.constants["t_Either_StateInit_Ref_StateInit"] = Either(TLBComplex.constants["t_StateInit"], TLBComplex.constants["t_Ref_StateInit"])
TLBComplex.constants["t_Maybe_Either_StateInit_Ref_StateInit"] = Maybe(TLBComplex.constants["t_Either_StateInit_Ref_StateInit"])
TLBComplex.constants["t_Message_Any"] = Message(TLBComplex.constants["t_Anything"])
TLBComplex.constants["t_natleq_96"] = NatLeq(96)
TLBComplex.constants["t_Ref_Message_Any"] = RefT(TLBComplex.constants["t_Message_Any"])
TLBComplex.constants["t_Ref_Transaction"] = RefT(TLBComplex.constants["t_Transaction"])
TLBComplex.constants["t_Ref_MsgEnvelope"] = RefT(TLBComplex.constants["t_MsgEnvelope"])
TLBComplex.constants["t_HashmapAugE_256_InMsg_ImportFees"] = HashmapAugE(256, TLBComplex.constants["t_InMsg"], TLBComplex.constants["t_ImportFees"])
TLBComplex.constants["t_Ref_InMsg"] = RefT(TLBComplex.constants["t_InMsg"])
TLBComplex.constants["t_uint63"] = UInt(63)
TLBComplex.constants["t_HashmapAugE_256_OutMsg_CurrencyCollection"] = HashmapAugE(256, TLBComplex.constants["t_OutMsg"], TLBComplex.constants["t_CurrencyCollection"])
TLBComplex.constants["t_HashmapAugE_352_EnqueuedMsg_uint64"] = HashmapAugE(352, TLBComplex.constants["t_EnqueuedMsg"], TLBComplex.constants["t_uint64"])
TLBComplex.constants["t_HashmapE_96_ProcessedUpto"] = HashmapE(96, TLBComplex.constants["t_ProcessedUpto"])
TLBComplex.constants["t_HashmapE_320_IhrPendingSince"] = HashmapE(320, TLBComplex.constants["t_IhrPendingSince"])
TLBComplex.constants["t_VarUInteger_7"] = VarUInteger(7)
TLBComplex.constants["t_Maybe_Grams"] = Maybe(TLBComplex.constants["t_Grams"])
TLBComplex.constants["t_Ref_Account"] = RefT(TLBComplex.constants["t_Account"])
TLBComplex.constants["t_HashmapAugE_256_ShardAccount_DepthBalanceInfo"] = HashmapAugE(256, TLBComplex.constants["t_ShardAccount"], TLBComplex.constants["t_DepthBalanceInfo"])
TLBComplex.constants["t_uint15"] = UInt(15)
TLBComplex.constants["t_Maybe_Ref_Message_Any"] = Maybe(TLBComplex.constants["t_Ref_Message_Any"])
TLBComplex.constants["t_HashmapE_15_Ref_Message_Any"] = HashmapE(15, TLBComplex.constants["t_Ref_Message_Any"])
TLBComplex.constants["t_Ref_TYPE_1616"] = RefT(TLBComplex.constants["t_Transaction_aux"])
TLBComplex.constants["t_HASH_UPDATE_Account"] = HASH_UPDATE(TLBComplex.constants["t_Account"])
TLBComplex.constants["t_Ref_HASH_UPDATE_Account"] = RefT(TLBComplex.constants["t_HASH_UPDATE_Account"])
TLBComplex.constants["t_Ref_TransactionDescr"] = RefT(TLBComplex.constants["t_TransactionDescr"])
TLBComplex.constants["t_uint16"] = UInt(16)
TLBComplex.constants["t_HashmapAug_64_Ref_Transaction_CurrencyCollection"] = HashmapAug(64, TLBComplex.constants["t_Ref_Transaction"], TLBComplex.constants["t_CurrencyCollection"])
TLBComplex.constants["t_HashmapAugE_256_AccountBlock_CurrencyCollection"] = HashmapAugE(256, TLBComplex.constants["t_AccountBlock"], TLBComplex.constants["t_CurrencyCollection"])
TLBComplex.constants["t_VarUInteger_3"] = VarUInteger(3)
TLBComplex.constants["t_Maybe_VarUInteger_3"] = Maybe(TLBComplex.constants["t_VarUInteger_3"])
TLBComplex.constants["t_Maybe_int32"] = Maybe(TLBComplex.constants["t_int32"])
TLBComplex.constants["t_Ref_TYPE_1628"] = RefT(TLBComplex.constants["t_TrComputePhase_aux"])
TLBComplex.constants["t_Maybe_TrStoragePhase"] = Maybe(TLBComplex.constants["t_TrStoragePhase"])
TLBComplex.constants["t_Maybe_TrCreditPhase"] = Maybe(TLBComplex.constants["t_TrCreditPhase"])
TLBComplex.constants["t_Ref_TrActionPhase"] = RefT(TLBComplex.constants["t_TrActionPhase"])
TLBComplex.constants["t_Maybe_Ref_TrActionPhase"] = Maybe(TLBComplex.constants["t_Ref_TrActionPhase"])
TLBComplex.constants["t_Maybe_TrBouncePhase"] = Maybe(TLBComplex.constants["t_TrBouncePhase"])
TLBComplex.constants["t_natwidth_6"] = NatWidth(6)
TLBComplex.constants["t_Maybe_Cell"] = Maybe(TLBComplex.constants["t_Anything"])
TLBComplex.constants["t_natwidth_8"] = NatWidth(8)
TLBComplex.constants["t_MessageRelaxed_Any"] = MessageRelaxed(TLBComplex.constants["t_Anything"])
TLBComplex.constants["t_Ref_MessageRelaxed_Any"] = RefT(TLBComplex.constants["t_MessageRelaxed_Any"])
TLBComplex.constants["t_natwidth_7"] = NatWidth(7)
TLBComplex.constants["t_natleq_60"] = NatLeq(60)
TLBComplex.constants["t_Ref_OutMsgQueueInfo"] = RefT(TLBComplex.constants["t_OutMsgQueueInfo"])
TLBComplex.constants["t_Ref_ShardAccounts"] = RefT(TLBComplex.constants["t_ShardAccounts"])
TLBComplex.constants["t_HashmapE_256_LibDescr"] = HashmapE(256, TLBComplex.constants["t_LibDescr"])
TLBComplex.constants["t_Maybe_BlkMasterInfo"] = Maybe(TLBComplex.constants["t_BlkMasterInfo"])
TLBComplex.constants["t_Ref_TYPE_1642"] = RefT(TLBComplex.constants["t_ShardStateUnsplit_aux"])
TLBComplex.constants["t_Ref_McStateExtra"] = RefT(TLBComplex.constants["t_McStateExtra"])
TLBComplex.constants["t_Maybe_Ref_McStateExtra"] = Maybe(TLBComplex.constants["t_Ref_McStateExtra"])
TLBComplex.constants["t_Ref_ShardStateUnsplit"] = RefT(TLBComplex.constants["t_ShardStateUnsplit"])
TLBComplex.constants["t_Hashmap_256_Truet"] = Hashmap(256, TLBComplex.constants["t_Truet"])
TLBComplex.constants["t_Ref_BlkMasterInfo"] = RefT(TLBComplex.constants["t_BlkMasterInfo"])
TLBComplex.constants["t_BlkPrevInfo_0"] = BlkPrevInfo(0)
TLBComplex.constants["t_Ref_BlkPrevInfo_0"] = RefT(TLBComplex.constants["t_BlkPrevInfo_0"])
TLBComplex.constants["t_Ref_ExtBlkRef"] = RefT(TLBComplex.constants["t_ExtBlkRef"])
TLBComplex.constants["t_Ref_BlockInfo"] = RefT(TLBComplex.constants["t_BlockInfo"])
TLBComplex.constants["t_Ref_ValueFlow"] = RefT(TLBComplex.constants["t_ValueFlow"])
TLBComplex.constants["t_MERKLE_UPDATE_ShardState"] = MERKLE_UPDATE(TLBComplex.constants["t_ShardState"])
TLBComplex.constants["t_Ref_MERKLE_UPDATE_ShardState"] = RefT(TLBComplex.constants["t_MERKLE_UPDATE_ShardState"])
TLBComplex.constants["t_Ref_BlockExtra"] = RefT(TLBComplex.constants["t_BlockExtra"])
TLBComplex.constants["t_Ref_InMsgDescr"] = RefT(TLBComplex.constants["t_InMsgDescr"])
TLBComplex.constants["t_Ref_OutMsgDescr"] = RefT(TLBComplex.constants["t_OutMsgDescr"])
TLBComplex.constants["t_Ref_ShardAccountBlocks"] = RefT(TLBComplex.constants["t_ShardAccountBlocks"])
TLBComplex.constants["t_Ref_McBlockExtra"] = RefT(TLBComplex.constants["t_McBlockExtra"])
TLBComplex.constants["t_Maybe_Ref_McBlockExtra"] = Maybe(TLBComplex.constants["t_Ref_McBlockExtra"])
TLBComplex.constants["t_Ref_TYPE_1653"] = RefT(TLBComplex.constants["t_TYPE_1653"])
TLBComplex.constants["t_Ref_TYPE_1654"] = RefT(TLBComplex.constants["t_TYPE_1654"])
TLBComplex.constants["t_natwidth_3"] = NatWidth(3)
TLBComplex.constants["t_Ref_TYPE_1658"] = RefT(TLBComplex.constants["t_ShardDescr_aux"])
TLBComplex.constants["t_BinTree_ShardDescr"] = BinTree(TLBComplex.constants["t_ShardDescr"])
TLBComplex.constants["t_Ref_BinTree_ShardDescr"] = RefT(TLBComplex.constants["t_BinTree_ShardDescr"])
TLBComplex.constants["t_HashmapE_32_Ref_BinTree_ShardDescr"] = HashmapE(32, TLBComplex.constants["t_Ref_BinTree_ShardDescr"])
TLBComplex.constants["t_HashmapAugE_96_ShardFeeCreated_ShardFeeCreated"] = HashmapAugE(96, TLBComplex.constants["t_ShardFeeCreated"], TLBComplex.constants["t_ShardFeeCreated"])
TLBComplex.constants["t_Hashmap_32_Ref_Cell"] = Hashmap(32, TLBComplex.constants["t_RefCell"])
TLBComplex.constants["t_Ref_Hashmap_32_Ref_Cell"] = RefT(TLBComplex.constants["t_Hashmap_32_Ref_Cell"])
TLBComplex.constants["t_HashmapAugE_32_KeyExtBlkRef_KeyMaxLt"] = HashmapAugE(32, TLBComplex.constants["t_KeyExtBlkRef"], TLBComplex.constants["t_KeyMaxLt"])
TLBComplex.constants["t_HashmapE_256_CreatorStats"] = HashmapE(256, TLBComplex.constants["t_CreatorStats"])
TLBComplex.constants["t_HashmapAugE_256_CreatorStats_uint32"] = HashmapAugE(256, TLBComplex.constants["t_CreatorStats"], TLBComplex.constants["t_uint32"])
TLBComplex.constants["t_natwidth_16"] = NatWidth(16)
TLBComplex.constants["t_Maybe_ExtBlkRef"] = Maybe(TLBComplex.constants["t_ExtBlkRef"])
TLBComplex.constants["t_Ref_TYPE_1672"] = RefT(TLBComplex.constants["t_McStateExtra_aux"])
TLBComplex.constants["t_Ref_SignedCertificate"] = RefT(TLBComplex.constants["t_SignedCertificate"])
TLBComplex.constants["t_HashmapE_16_CryptoSignaturePair"] = HashmapE(16, TLBComplex.constants["t_CryptoSignaturePair"])
TLBComplex.constants["t_Maybe_Ref_InMsg"] = Maybe(TLBComplex.constants["t_Ref_InMsg"])
TLBComplex.constants["t_Ref_TYPE_1680"] = RefT(TLBComplex.constants["t_McBlockExtra_aux"])
TLBComplex.constants["t_Hashmap_16_ValidatorDescr"] = Hashmap(16, TLBComplex.constants["t_ValidatorDescr"])
TLBComplex.constants["t_HashmapE_16_ValidatorDescr"] = HashmapE(16, TLBComplex.constants["t_ValidatorDescr"])
TLBComplex.constants["t_Maybe_bits256"] = Maybe(TLBComplex.constants["t_bits256"])
TLBComplex.constants["t_Hashmap_32_Truet"] = Hashmap(32, TLBComplex.constants["t_Truet"])
TLBComplex.constants["t_uint8"] = UInt(8)
TLBComplex.constants["t_Ref_ConfigProposalSetup"] = RefT(TLBComplex.constants["t_ConfigProposalSetup"])
TLBComplex.constants["t_uint256"] = UInt(256)
TLBComplex.constants["t_Maybe_uint256"] = Maybe(TLBComplex.constants["t_uint256"])
TLBComplex.constants["t_Ref_ConfigProposal"] = RefT(TLBComplex.constants["t_ConfigProposal"])
TLBComplex.constants["t_HashmapE_16_Truet"] = HashmapE(16, TLBComplex.constants["t_Truet"])
TLBComplex.constants["t_int64"] = Int(64)
TLBComplex.constants["t_natwidth_12"] = NatWidth(12)
TLBComplex.constants["t_natwidth_32"] = NatWidth(32)
TLBComplex.constants["t_natwidth_13"] = NatWidth(13)
TLBComplex.constants["t_HashmapE_32_WorkchainDescr"] = HashmapE(32, TLBComplex.constants["t_WorkchainDescr"])
TLBComplex.constants["t_Hashmap_32_StoragePrices"] = Hashmap(32, TLBComplex.constants["t_StoragePrices"])
TLBComplex.constants["t_HashmapE_256_Truet"] = HashmapE(256, TLBComplex.constants["t_Truet"])
TLBComplex.constants["t_Ref_ValidatorTempKey"] = RefT(TLBComplex.constants["t_ValidatorTempKey"])
TLBComplex.constants["t_HashmapE_256_ValidatorSignedTempKey"] = HashmapE(256, TLBComplex.constants["t_ValidatorSignedTempKey"])
TLBComplex.constants["t_HashmapE_288_Unit"] = HashmapE(288, TLBComplex.constants["t_Unit"])
TLBComplex.constants["t_HashmapE_256_uint256"] = HashmapE(256, TLBComplex.constants["t_uint256"])
TLBComplex.constants["t_Ref_JettonBridgePrices"] = RefT(TLBComplex.constants["t_JettonBridgePrices"])
TLBComplex.constants["t_Ref_BlockSignatures"] = RefT(TLBComplex.constants["t_BlockSignatures"])
TLBComplex.constants["t_Maybe_Ref_BlockSignatures"] = Maybe(TLBComplex.constants["t_Ref_BlockSignatures"])
TLBComplex.constants["t_Ref_TopBlockDescr"] = RefT(TLBComplex.constants["t_TopBlockDescr"])
TLBComplex.constants["t_HashmapE_96_Ref_TopBlockDescr"] = HashmapE(96, TLBComplex.constants["t_Ref_TopBlockDescr"])
TLBComplex.constants["t_MERKLE_PROOF_Block"] = MERKLE_PROOF(TLBComplex.constants["t_Block"])
TLBComplex.constants["t_Ref_MERKLE_PROOF_Block"] = RefT(TLBComplex.constants["t_MERKLE_PROOF_Block"])
TLBComplex.constants["t_MERKLE_PROOF_ShardState"] = MERKLE_PROOF(TLBComplex.constants["t_ShardState"])
TLBComplex.constants["t_Ref_MERKLE_PROOF_ShardState"] = RefT(TLBComplex.constants["t_MERKLE_PROOF_ShardState"])
TLBComplex.constants["t_Ref_ProducerInfo"] = RefT(TLBComplex.constants["t_ProducerInfo"])
TLBComplex.constants["t_Ref_ComplaintDescr"] = RefT(TLBComplex.constants["t_ComplaintDescr"])
TLBComplex.constants["t_Ref_ValidatorComplaint"] = RefT(TLBComplex.constants["t_ValidatorComplaint"])
TLBComplex.constants["t_int257"] = Int(257)
TLBComplex.constants["t_natwidth_10"] = NatWidth(10)
TLBComplex.constants["t_natleq_4"] = NatLeq(4)
TLBComplex.constants["t_Ref_VmStackValue"] = RefT(TLBComplex.constants["t_VmStackValue"])
TLBComplex.constants["t_natwidth_24"] = NatWidth(24)
TLBComplex.constants["t_HashmapE_4_VmStackValue"] = HashmapE(4, TLBComplex.constants["t_VmStackValue"])
TLBComplex.constants["t_Ref_TYPE_1727"] = RefT(TLBComplex.constants["t_VmGasLimits_aux"])
TLBComplex.constants["t_HashmapE_256_Ref_Cell"] = HashmapE(256, TLBComplex.constants["t_RefCell"])
TLBComplex.constants["t_uint13"] = UInt(13)
TLBComplex.constants["t_Maybe_uint13"] = Maybe(TLBComplex.constants["t_uint13"])
TLBComplex.constants["t_Maybe_VmStack"] = Maybe(TLBComplex.constants["t_VmStack"])
TLBComplex.constants["t_int16"] = Int(16)
TLBComplex.constants["t_Maybe_int16"] = Maybe(TLBComplex.constants["t_int16"])
TLBComplex.constants["t_Ref_VmCont"] = RefT(TLBComplex.constants["t_VmCont"])
TLBComplex.constants["t_Ref_DNSRecord"] = RefT(TLBComplex.constants["t_DNSRecord"])
TLBComplex.constants["t_HashmapE_256_Ref_DNSRecord"] = HashmapE(256, TLBComplex.constants["t_Ref_DNSRecord"])
TLBComplex.constants["t_Ref_MsgAddressInt"] = RefT(TLBComplex.constants["t_MsgAddressInt"])
TLBComplex.constants["t_bits512"] = Bits(512)
TLBComplex.constants["t_Ref_bits512"] = RefT(TLBComplex.constants["t_bits512"])
TLBComplex.constants["t_Maybe_Ref_bits512"] = Maybe(TLBComplex.constants["t_Ref_bits512"])
TLBComplex.constants["t_Ref_ChanConfig"] = RefT(TLBComplex.constants["t_ChanConfig"])
TLBComplex.constants["t_Ref_ChanState"] = RefT(TLBComplex.constants["t_ChanState"])
