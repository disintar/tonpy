from tonpy.types.cellslice import CellSlice
from tonpy.types.cell import Cell
from tonpy.autogen.block import Transaction, MessageAny


class CustomSubscription:
    def __init__(self):
        pass

    def check(self, tx: CellSlice) -> bool:
        raise NotImplementedError


class TransactionSubscription(CustomSubscription):
    def __init__(self, op_code: int = None, text: str = None):
        super().__init__()

        if text and not (op_code == 0 or op_code is None):
            raise ValueError("Text supported only for 0 OP code")

        self.op_code = op_code if text is None else 0
        self.text = text

        assert self.op_code is not None or self.text is not None

    def check(self, tx: CellSlice) -> bool:
        t = Transaction()
        tt = t.fetch(tx)

        if hasattr(tt.r1.in_msg, 'value'):
            in_msg_body = tt.r1.in_msg.value.body.value
            if isinstance(in_msg_body, Cell):
                in_msg_body = in_msg_body.begin_parse()

            if self.op_code is not None:
                if in_msg_body.bits < 32 or in_msg_body.load_uint(32) != self.op_code:
                    return False

                if self.text is not None:
                    try:
                        in_msg_text = in_msg_body.load_string(strict=False)
                        return self.text in in_msg_text
                    except Exception as e:
                        print(e)
                        return False

        else:
            return False
