import unittest
from backend import Calculations

calculate = Calculations


class TestMethods(unittest.TestCase):

    def test_reynolds(self):
        self.assertAlmostEqual(calculate.calculate_reynolds(self,0.998,1,0.5,0.00102),489.215686,6)

    def test_mach(self):
        self.assertAlmostEqual(calculate.calculate_mach(self,550.27,340.3),1.617014,6)

    def test_prandtl(self):
        self.assertAlmostEqual(calculate.calculate_prandtl(self,0.00543,0.0043),1.2627906,6)

    def test_nusselt(self):
        self.assertAlmostEqual(calculate.calculate_nusselt(self,20,0.15,0.75),4,6)

    def test_rayleigh(self):
        self.assertAlmostEqual(calculate.calculate_rayleigh(self,9.81,0.11,303.15,273.15,0.25,0.0043,0.242),486.0927589,6)

    def test_peclet(self):
        self.assertAlmostEqual(calculate.calculatePeclet(self,0.52,0.335,0.887),0.1963923,6)

    def test_grasof(self):
        self.assertAlmostEqual(calculate.calculateGrashof(self,9.81,0.5778,373,353,0.35,0.0079843),76244.2295629,6)

    def test_fourier(self):
        self.assertAlmostEqual(calculate.calculateFourier(self,0.98554,0.05,0.12),3.4220138,6)

    def test_biot(self):
        self.assertAlmostEqual(calculate.calculateBiot(self,20,0.15,0.75),4,6)

    def test_stokes(self):
        self.assertAlmostEqual(calculate.calculateStokes(self,0.35,5.78,0.19),10.647368,6)


if __name__ == '__main__':
    unittest.main()