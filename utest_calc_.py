import unittest
import clc_div_exe
import math

class CalcTest(unittest.TestCase):
    # позитивный тест с целыми числами
    def test_pozitiv_integer(self):
        self.assertEqual(clc_div_exe.div("in.txt"), 2)
    # позитивный тест с вещественными числами
    def test_pozitiv_real(self):
        self.assertEqual(clc_div_exe.div("in_real.txt"), 2.25)
    # позитивный тест с вещественным отрицательным и положительным числом
    def test_pozitiv_minus(self):
        self.assertEqual(clc_div_exe.div("in_minus.txt"), -1.5)
    # позитивный тест с отрицательными вещественными числами
    def test_pozitiv_minus_2(self):
        self.assertEqual(clc_div_exe.div("in_minus_2.txt"), 62.674157303370784)
    # негативный тест - проверка деления на ноль
    def test_neg(self):
        with self.assertRaises(ZeroDivisionError):
            clc_div_exe.div("in_zero.txt")
        # либо так
        #with self.assertRaises(Exception) as exc:
        #    clc_div_exe.div("in_zero.txt")
        #self.assertEqual("float division by zero", str(exc.exception))

    # позитивный тест - проверка верхней границы положительного числа float в python
    def test_gu_big(self):
        self.assertEqual(clc_div_exe.div("in_big.txt"), 10)
    # негативный тест - проверка деления чисел больших верхней границы положительного числа float в python (maxexp = 1.797e+308). сравниваем с nan
    def test_gu_big_nan(self):
        self.assertTrue(math.isnan(clc_div_exe.div("in_big_nan.txt")))
    # негативный тест - делимое больше верхней границы положительного числа float в python (>maxexp = 1.797e+308). сравниваем с +бесконечностью
    def test_gu_big_inf(self):
        self.assertEqual(clc_div_exe.div("in_big_inf.txt"), float("inf"))
    # позитивный тест - нижней границы положительного числа float в python (minexp = 2.25e+308)
    def test_gu_small(self):
        self.assertEqual(clc_div_exe.div("in_small.txt"), 1)
    # негативный тест - проверка деления чисел меньших нижней границы положительного числа float в python (<minexp = 2.25e+308).
    def test_gu_small_zero(self):
        with self.assertRaises(ZeroDivisionError):
            clc_div_exe.div("in_small_zero.txt")
    # позитивный тест - нижней границы положительного числа float в python (minexp = 2.25e+308)
    def test_gu_small_minus(self):
        self.assertEqual(clc_div_exe.div("in_small_minus.txt"),10)
    # негативный тест - проверка деления чисел меньших нижней границы отрицательного числа float в python (<minexp = -1.797e+308). сравниваем с nan
    def test_gu_small_minus_nan(self):
        self.assertTrue(math.isnan(clc_div_exe.div("in_small_minus_nan.txt")))
    # негативный тест - делимое меньше нижней границы отрицательного числа float в python (<minexp = -1.797e+308). сравниваем с -бесконечностью
    def test_gu_small_minus_inf(self):
        self.assertEqual(clc_div_exe.div("in_small_minus_inf.txt"),float("inf"))
    # позитивный тест - нижней границы отрицательного числа float в python (minexp = -2.25e+308)
    def test_gu_very_small_minus(self):
        self.assertEqual(clc_div_exe.div("in_very_small_minus.txt"), 1)
    # негативный тест - проверка деления чисел меньших нижней границы отрицательного числа float в python (<minexp = 2.25e+308).
    def test_gu_very_small_zero(self):
        with self.assertRaises(ZeroDivisionError):
            clc_div_exe.div("in_very_small_zero.txt")
    # негативный тест - проверка на ввод в файл числовых значений
    def test_gu_text(self):
        with self.assertRaises(ValueError):
            clc_div_exe.div("in_text.txt")

if __name__ == '__main__':
    unittest.main()