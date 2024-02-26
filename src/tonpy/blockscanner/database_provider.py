class BaseDatabaseProvider:
    """
    Please note that `BaseDatabaseProvider` must be design like DB connector, because it'll be pickle
    and moved to other process in Pool
    """

    def __init__(self):
        pass


class DummyDatabaseProvider(BaseDatabaseProvider):
    def __init__(self):
        super().__init__()
