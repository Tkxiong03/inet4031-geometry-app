import unittest
import sphere
import math

class sphereTest(unittest.TestCase):

    def test_volume1(self):
        result = sphere.volume(1)
        self.assertAlmostEqual(result, (4/3) * math.pi * 1**3, places=2)

    def test_volume2(self):
        result = sphere.volume(2)
        self.assertAlmostEqual(result, (4/3) * math.pi * 2**3, places=2)

    def test_volume3(self):
        result = sphere.volume(3)
        self.assertAlmostEqual(result, (4/3) * math.pi * 3**3, places=2)


if __name__ == '__main__':
    unittest.main()