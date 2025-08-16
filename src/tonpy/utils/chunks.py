# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
