from typing import Any, Dict, Iterable, Optional

supported_types = [
    'Int8',
    'Int16',
    'Int32',
    'Int64',
    'Int128',
    'Int256',
    'UInt8',
    'UInt16',
    'UInt32',
    'UInt64',
    'UInt128',
    'UInt256',
    'String',
    'FixedString(64)',
    'Address',
    'Boolean',
    'Datetime'
]


def parse_tlb_spec(
    struct_dump: Optional[Dict[str, Any]],
    tlb: Dict[str, Any],
    *,
    prefix: str = "",
    name_prefix: str = "",
    columns_only: bool = False,  # False: return values; True: return types (dton_type)
) -> Dict[str, Any]:
    def _walk_path(obj: Any, parts: Iterable[str]) -> Any:
        cur = obj
        for p in parts:
            if not isinstance(cur, dict):
                return None
            cur = cur.get(p)
            if cur is None:
                return None
        return cur

    def _normalize(val: Any, dtype: Optional[str]) -> Any:
        if dtype == "FixedString(64)" and isinstance(val, int):
            return hex(val).upper()[2:].zfill(64)
        return val

    out: Dict[str, Any] = {}

    parse_items = tlb.get("parse")
    if not parse_items:
        return out
    assert isinstance(parse_items, list), "tlb['parse'] must be a list"

    with_types = bool(tlb.get("dump_with_types"))
    type_col = f"{prefix}{name_prefix}type"

    if with_types:
        if columns_only:
            out[type_col] = "String"
        else:
            if isinstance(struct_dump, dict) and "type" in struct_dump:
                out[type_col] = struct_dump.get("type")

    seen_last_names = set()

    for item in parse_items:
        labels = item.get("labels", {}) or {}
        if labels.get("skipParse", False):
            continue

        path = item.get("path")
        assert path, "Missing path in TLB 'parse' item"
        parts = path.split(".")
        last = parts[-1]

        # Checking duplicates by last
        if last in seen_last_names:
            raise ValueError(f"Duplicate path {last}")
        seen_last_names.add(last)

        dtype = labels.get("dton_type")
        assert dtype is not None, f"Missing dton_type for path '{path}'"
        if supported_types is not None:
            assert dtype in supported_types, f"Unsupported ABI type {dtype}"

        name = labels.get("name", last)
        key = f"{prefix}{name_prefix}{name}"

        if columns_only:
            out[key] = dtype
            continue

        if struct_dump is None:
            continue

        root = struct_dump.get(parts[0])
        val = _walk_path(root, parts[1:]) if len(parts) > 1 else root
        if val is None:
            continue

        out[key] = _normalize(val, dtype)

    return out
