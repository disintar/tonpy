from tonpy.libs.python_ton import PyCellBuilder
from tonpy.types.cell import Cell
from tonpy.types.cellslice import CellSlice


# py::class_<PyCellBuilder>(m, "PyCellBuilder")
#     .def(py::init<>())
#     .def("store_uint_str", &PyCellBuilder::store_uint_str, py::arg("str") = "", py::arg("bits") = "",
#          py::return_value_policy::reference_internal)
#     .def("store_int_str", &PyCellBuilder::store_int_str, py::arg("str") = "", py::arg("bits") = "",
#          py::return_value_policy::reference_internal)
#     .def("store_builder", &PyCellBuilder::store_builder, py::arg("cb"), py::return_value_policy::reference_internal)
#     .def("store_zeroes", &PyCellBuilder::store_zeroes, py::arg("bits"), py::return_value_policy::reference_internal)
#     .def("store_ones", &PyCellBuilder::store_ones, py::arg("bits"), py::return_value_policy::reference_internal)
#     .def("store_address", &PyCellBuilder::store_address, py::arg("addr"), py::return_value_policy::reference_internal)
#     .def("store_bitstring", &PyCellBuilder::store_bitstring, py::arg("bs"),
#          py::return_value_policy::reference_internal)
#     .def("store_slice", &PyCellBuilder::store_slice, py::arg("cs"), py::return_value_policy::reference_internal)
#     .def("store_grams_str", &PyCellBuilder::store_grams_str, py::arg("grams"),
#          py::return_value_policy::reference_internal)
#     .def("store_var_integer", &PyCellBuilder::store_var_integer, py::arg("int"), py::arg("bit_len"), py::arg("sgnd"),
#          py::return_value_policy::reference_internal)
#     .def("get_cell", &PyCellBuilder::get_cell)
#     .def("store_ref", &PyCellBuilder::store_ref)
#     .def("dump", &PyCellBuilder::dump)
#     .def("get_hash", &PyCellBuilder::get_hash)
#     .def("dump_as_tlb", &PyCellBuilder::dump_as_tlb, py::arg("tlb_type"))
#     .def("to_boc", &PyCellBuilder::to_boc)
#     .def("__repr__", &PyCellBuilder::toString);

class CellBuilder:
    def __init__(self):
        self.builder = PyCellBuilder()

    def store_ref(self, cell: Cell) -> PyCellBuilder:
        """
        Take cell and store it to next reference in current builder

        :param cell: Cell to be stored as reference to current builder
        :return: updated (self) builder with new reference to cell
        """
        self.builder.store_ref(cell.cell)
        return self

    def store_grams(self, n) -> PyCellBuilder:
        self.builder.store_grams_str(str(n))
        return self

    def to_boc(self) -> str:
        return self.builder.to_boc()

    def store_slice(self, cell_slice):
        self.builder.store_slice(cell_slice.cell_slice)
        return self

    def store_builder(self, b):
        self.builder.store_builder(b.builder)
        return self

    def store_uint(self, a, b):
        self.store_uint_str(str(a), b)
        return self

    def store_int(self, a, b):
        self.store_int_str(str(a), b)
        return self

    def store_addr(slef, a):
        self.builder.store_address(a)
        return self

    def store_var_uint(self, a, b):
        self.builder.store_var_integer(str(a), b, False)
        return self

    def store_var_int(self, a, b):
        self.builder.store_var_integer(str(a), b, True)
        return self

    def store_var_integer(self, a, b, c=False):
        self.builder.store_var_integer(str(a), b, c)
        return self

    def end_cell(self):
        return Cell(self.builder.get_cell())

    def dump(self):
        return self.builder.dump()

    def dump_as_tlb(self, a):
        return self.builder.dump_as_tlb(a)

    def __repr__(self):
        return self.builder.__repr__()
