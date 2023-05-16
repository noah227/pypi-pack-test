class TestClass:
    def __init__(self, title="hello"):
        self.title = title

    @staticmethod
    def staticDo():
        print(999)

    @classmethod
    def classDo(cls, *args, **kwargs):
        print(cls, *args, **kwargs)


def testFn(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == "__main__":
    pass
