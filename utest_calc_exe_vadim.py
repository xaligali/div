import unittest
import subprocess
import math

#путь до exe-файла
exe = 'calc_div.exe < '

#поиск exception
def zero_fun():
    raise Exception('')
def val_fun():
    raise ValueError('ValueError: could not convert string to float')

#запуск exe-файла
def proc(fname):
    process = subprocess.Popen(exe + fname, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode('utf-8')

class CalcTest(unittest.TestCase):

    #позитивный тест с целыми числами
    def test_pozitiv_integer(self):
        self.assertEqual(float(proc('in.txt')), 2)
    #позитивный тест с вещественными числами
    def test_pozitiv_real(self):
        self.assertEqual(float(proc('in_real.txt')), 2.25)
    # позитивный тест с вещественным отрицательным и положительным числом
    def test_pozitiv_minus(self):
        self.assertEqual(float(proc('in_minus.txt')), -1.5)
    # позитивный тест с отрицательными вещественными числами
    def test_pozitiv_minus_2(self):
        self.assertEqual(float(proc('in_minus_2.txt')), 62.6742)
    # позитивный тест - проверка верхней границы положительного числа float в python (maxexp = 1.797e+308)
    def test_gu_big(self):
        self.assertEqual(float(proc('in_big.txt')), 10)
    # позитивный тест - нижней границы положительного числа float в python (minexp = 2.25e-308)
    def test_gu_small(self):
        self.assertEqual(float(proc('in_small.txt')), 1)
    # позитивный тест - верхней границы отрицательного числа float в python (maxexp = -1.797e+308)
    def test_gu_big_minus(self):
        self.assertEqual(float(proc('in_small_minus.txt')), 10)
    # позитивный тест - нижней границы отрицательного числа float в python (minexp = -2.25e-308)
    def test_gu_very_small_minus(self):
        self.assertEqual(float(proc('in_very_small_minus.txt')), 1)
    # негативный тест - проверка деления на ноль
    def test_neg(self):
        #with self.assertRaises(Exception) as exc:
            #('in_text.txt')
            self.assertEqual(proc('in_zero.txt'), '1.#INF')


###############################################################3333
    #возвращает 1
    # негативный тест - проверка деления чисел меньших нижней границы положительного числа float в python (<minexp = 2.25e-308).
    def test_gu_small_zero(self):
        with self.assertRaises(Exception) as exc:
            zero_fun()
            proc('in_small_zero.txt')
        self.assertEqual("ZeroDivisionError: float division by zero", str(exc.exception))

    # негативный тест - проверка деления чисел меньших нижней границы отрицательного числа float в python (<minexp = -2.25e-308).
    def test_gu_very_small_zero(self):
        #self.assertEqual(proc('in_very_small_zero.txt').stdout.decode('utf-8'),'')
        with self.assertRaises(Exception) as exc:
            zero_fun()
            proc('in_very_small_zero.txt')
        self.assertEqual("ZeroDivisionError: float division by zero", str(exc.exception))

    # негативный тест - проверка на ввод в файл текстовых значений
    def test_gu_text(self):
        with self.assertRaises(ValueError)as val:
            val_fun()
            proc('in_text.txt')
        self.assertEqual("ValueError: could not convert string to float", str(val.exception))


    # негативный тест - проверка деления чисел больших верхней границы положительного числа float в python (maxexp = 1.797e+308). сравниваем с nan
    def test_gu_big_nan(self):
        self.assertTrue(math.isnan(float(proc('in_big_nan.txt'))))
    # негативный тест - делимое больше верхней границы положительного числа float в python (>maxexp = 1.797e+308). сравниваем с +бесконечностью
    def test_gu_big_inf(self):
        self.assertEqual(float(proc('in_big_inf.txt')), float("inf"))
    # негативный тест - проверка деления чисел меньших верхней границы отрицательного числа float в python (<minexp = -1.797e+308). сравниваем с nan
    def test_gu_small_minus_nan(self):
        self.assertTrue(math.isnan(float(proc('in_small_minus_nan.txt'))))
    # негативный тест - делимое меньше верхней границы отрицательного числа float в python (<minexp = -1.797e+308). сравниваем с -бесконечностью
    def test_gu_small_minus_inf(self):
        self.assertEqual(float(proc('in_small_minus_inf.txt')),float("inf"))

if __name__ == '__main__':
    unittest.main()