class FakeModule:
    def __init__(self):
        pass

    class RGBMatrix(object):
        def __init__(self, rows, chains = 1, parallel = 1):
            print("ok")

        def CreateFrameCanvas(self):
            return 0

        def SwapOnVSync(self, c):
            return 0


import unittest
import sys

sys.modules['rgbmatrix'] = FakeModule
from rgbmatrix import RGBMatrix
import matrixled.matrix_main


class Test(unittest.TestCase):
    def test_alwaysfails(self):
        self.assertTrue(5 > 3, "5 is not bigger than 3")

    def test_trypry(self):
        self.m = RGBMatrix(32)
        self.assertEqual(0, self.m.CreateFrameCanvas())

    def test_main(self):
        pass

if __name__ == '__main__':
    unittest.main()
