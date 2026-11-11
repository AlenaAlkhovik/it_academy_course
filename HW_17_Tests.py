import unittest

import HW_17_Calculator

class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(HW_17_Calculator.add(45, 27), 72)

    def test_add_negative(self):
        self.assertEqual(HW_17_Calculator.add(-10, -20), -30)

    def test_add_neg_with_pos_1(self):
        self.assertEqual(HW_17_Calculator.add(-7, 17), 10)

    def test_add_neg_with_pos_2(self):
        self.assertEqual(HW_17_Calculator.add(7, -26), -19)

    def test_add_float(self):
        self.assertAlmostEqual(HW_17_Calculator.add(2.16, 17.986), 20.146)

    def test_add_with_zeroes(self):
        self.assertEqual(HW_17_Calculator.add(0, 0), 0)

    def test_subtract_positive(self):
        self.assertEqual(HW_17_Calculator.subtract(108, 29), 79)

    def test_subtract_negative(self):
        self.assertEqual(HW_17_Calculator.subtract(-10, -20), 10)

    def test_subtract_neg_with_pos_1(self):
        self.assertEqual(HW_17_Calculator.subtract(-4, 15), -19)

    def test_subtract_neg_with_pos_2(self):
        self.assertEqual(HW_17_Calculator.subtract(7, -26), 33)

    def test_subtract_float(self):
        self.assertAlmostEqual(HW_17_Calculator.subtract(159.156, 17.986), 141.17)

    def test_subtract_with_zeroes(self):
        self.assertEqual(HW_17_Calculator.subtract(0, 0), 0)

    def test_subtract_with_first_zero(self):
        self.assertEqual(HW_17_Calculator.subtract(0, 24), -24)

    def test_multiply_positive(self):
        self.assertEqual(HW_17_Calculator.multiply(4, 17), 68)

    def test_multiply_negative(self):
        self.assertEqual(HW_17_Calculator.multiply(-5, -46), 230)

    def test_multiply_neg_with_pos_1(self):
        self.assertEqual(HW_17_Calculator.multiply(-4, 15), -60)

    def test_multiply_neg_with_pos_2(self):
        self.assertEqual(HW_17_Calculator.multiply(7, -100), -700)

    def test_multiply_float(self):
        self.assertAlmostEqual(HW_17_Calculator.multiply(15.156, 17.986), 272.595816)

    def test_multiply_with_zeroes(self):
        self.assertEqual(HW_17_Calculator.multiply(0, 0), 0)

    def test_multiply_with_first_zero(self):
        self.assertEqual(HW_17_Calculator.multiply(0, 24), 0)

    def test_divide_positive(self):
        self.assertEqual(HW_17_Calculator.divide(27, 3), 9)

    def test_divide_float_result(self):
        self.assertAlmostEqual(HW_17_Calculator.divide(5, 27), 0.185185185)

    def test_divide_negative(self):
        self.assertEqual(HW_17_Calculator.divide(-136, -8), 17)

    def test_divide_neg_with_pos_1(self):
        self.assertAlmostEqual(HW_17_Calculator.divide(-4, 15), -0.266666666)

    def test_divide_neg_with_pos_2(self):
        self.assertEqual(HW_17_Calculator.divide(100, -25), -4)

    def test_divide_float(self):
        self.assertAlmostEqual(HW_17_Calculator.divide(27.156, 17.986), 1.50984099)

    def test_divide_with_first_zero(self):
        self.assertEqual(HW_17_Calculator.divide(0, 15), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            HW_17_Calculator.divide(5, 0)

    def test_power_positive(self):
        self.assertEqual(HW_17_Calculator.power(4, 2), 16)

    def test_power_negative(self):
        self.assertEqual(HW_17_Calculator.power(-2, -5), -0.03125)

    def test_power_neg_with_pos_1(self):
        self.assertEqual(HW_17_Calculator.power(-4, 7), -16384)

    def test_power_neg_with_pos_2(self):
        self.assertAlmostEqual(HW_17_Calculator.power(7, -2), 0.0204081632653061)

    def test_power_float(self):
        self.assertAlmostEqual(HW_17_Calculator.power(15.156, 3.986), 50793.741223842)

    def test_power_with_first_zero(self):
        self.assertEqual(HW_17_Calculator.power(0, 24), 0)

    def test_power_with_second_zero(self):
        self.assertEqual(HW_17_Calculator.power(1563456, 0), 1)

    def test_power_with_zeroes(self):
        self.assertEqual(HW_17_Calculator.power(0, 0), 1)

    def test_power_with_float_zeroes(self):
        self.assertEqual(HW_17_Calculator.power(0.0, 0.0), 1.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)