# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Test:
    """Test"""

    def __init__(self, a: int, b: str):
        """Constructor method"""
        self.a = a
        self.b = b

    def sum(self, test: int = None) -> int:
        """
        :param uuids: A list of string service UUIDs to be discovered,
            defaults to None
        """
        self.a += test
        return self.a


def print_hi(name: str):
    """Just HI str function"""
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
