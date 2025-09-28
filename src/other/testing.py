import unittest
from ..api.api import HEAPI


class HouseEscapeTest(unittest.TestCase):

    def testApi(self):
        test1 = HouseEscapeTest.assertIsNone(HEAPI)


def main() -> None:
    het = HouseEscapeTest()
    het.testApi()


if __name__ == "__main__":
    main()


# pytest