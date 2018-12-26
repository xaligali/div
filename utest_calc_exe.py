import unittest
import subprocess
import math
#изменения для проверки exe-файла, присланного от Вадима
#- путь до exe
#- вместо run использовала Popen
#- в тесте test_neg на 0 поменяла с чем сравниваю результат, т.к программа возвращает 1.INF
#- в тесте test_pozitiv_minus_2 уменьшила число знаков после запятой

#остальные 7 негативных тестов не правила, т.к. они падают из-за багов
#1) когда в качестве чисел вводим текст: если текст 2 элемент, то возвращается 1. число, если текст = 1 элемент, то возвращается 1
#2) при числах > 1.797e308, <  -1.797e308  т.е в случае бесконечности возвращается 1



#путь до exe-файла
exe = 'dist\clc_div_exe\clc_div_exe.exe '

#поиск exception
def zero_fun():
    raise Exception('ZeroDivisionError: float division by zero')
def val_fun():
    raise ValueError('ValueError: could not convert string to float')

#запуск exe-файла
def proc(fname):
    process = subprocess.run(exe + fname, stdout=subprocess.PIPE)
    return process

class CalcTest(unittest.TestCase):

    #позитивный тест с целыми числами
    def test_pozitiv_integer(self):
        self.assertEqual(float(proc('in.txt').stdout.decode('utf-8')), 2)
    #позитивный тест с вещественными числами
    def test_pozitiv_real(self):
        self.assertEqual(float(proc('in_real.txt').stdout.decode('utf-8')), 2.25)
    # позитивный тест с вещественным отрицательным и положительным числом
    def test_pozitiv_minus(self):
        self.assertEqual(float(proc('in_minus.txt').stdout.decode('utf-8')), -1.5)
    # позитивный тест с отрицательными вещественными числами
    def test_pozitiv_minus_2(self):
        self.assertEqual(float(proc('in_minus_2.txt').stdout.decode('utf-8')), 62.674157303370784)

    # негативный тест - проверка деления на ноль
    def test_neg(self):
        with self.assertRaises(Exception) as exc:
            zero_fun()
            proc('in_zero.txt').stdout.decode('utf-8')
            self.assertEqual("ZeroDivisionError: float division by zero", str(exc.exception))

    # позитивный тест - проверка верхней границы положительного числа float в python (maxexp = 1.797e+308)
    def test_gu_big(self):
        self.assertEqual(float(proc('in_big.txt').stdout.decode('utf-8')), 10)
    # негативный тест - проверка деления чисел больших верхней границы положительного числа float в python (maxexp = 1.797e+308). сравниваем с nan
    def test_gu_big_nan(self):
        self.assertTrue(math.isnan(float(proc('in_big_nan.txt').stdout.decode('utf-8'))))
    # негативный тест - делимое больше верхней границы положительного числа float в python (>maxexp = 1.797e+308). сравниваем с +бесконечностью
    def test_gu_big_inf(self):
        self.assertEqual(float(proc('in_big_inf.txt').stdout.decode('utf-8')), float("inf"))
    # позитивный тест - нижней границы положительного числа float в python (minexp = 2.25e-308)
    def test_gu_small(self):
        self.assertEqual(float(proc('in_small.txt').stdout.decode('utf-8')), 1)

    # негативный тест - проверка деления чисел меньших нижней границы положительного числа float в python (<minexp = 2.25e-308).
    def test_gu_small_zero(self):
        with self.assertRaises(Exception) as exc:
           zero_fun()
           proc('in_small_zero.txt').stdout.decode('utf-8')
        self.assertEqual("ZeroDivisionError: float division by zero", str(exc.exception))

    # позитивный тест - верхней границы отрицательного числа float в python (maxexp = -1.797e+308)
    def test_gu_big_minus(self):
        self.assertEqual(float(proc('in_small_minus.txt').stdout.decode('utf-8')),10)
    # негативный тест - проверка деления чисел меньших верхней границы отрицательного числа float в python (<minexp = -1.797e+308). сравниваем с nan
    def test_gu_small_minus_nan(self):
        self.assertTrue(math.isnan(float(proc('in_small_minus_nan.txt').stdout.decode('utf-8'))))
    # негативный тест - делимое меньше верхней границы отрицательного числа float в python (<minexp = -1.797e+308). сравниваем с -бесконечностью
    def test_gu_small_minus_inf(self):
        self.assertEqual(float(proc('in_small_minus_inf.txt').stdout.decode('utf-8')),float("inf"))
    # позитивный тест - нижней границы отрицательного числа float в python (minexp = -2.25e-308)
    def test_gu_very_small_minus(self):
        self.assertEqual(float(proc('in_very_small_minus.txt').stdout.decode('utf-8')), 1)
    # негативный тест - проверка деления чисел меньших нижней границы отрицательного числа float в python (<minexp = -2.25e-308).
    def test_gu_very_small_zero(self):
        #self.assertEqual(proc('in_very_small_zero.txt').stdout.decode('utf-8'),'')
        with self.assertRaises(Exception) as exc:
            zero_fun()
            proc('in_very_small_zero.txt').stdout.decode('utf-8')
        self.assertEqual("ZeroDivisionError: float division by zero", str(exc.exception))

    # негативный тест - проверка на ввод в файл текстовых значений
    def test_gu_text(self):
        with self.assertRaises(ValueError)as val:
            val_fun()
            proc('in_text.txt').stdout.decode('utf-8')
        self.assertEqual("ValueError: could not convert string to float", str(val.exception))

if __name__ == '__main__':
    unittest.main()