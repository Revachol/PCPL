import unittest
from rk2_refactoring import *

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.microprocessors = [
            Microprocessor(1, 'Intel Core i7'),
            Microprocessor(2, 'AMD Ryzen 5'),
            Microprocessor(3, 'Intel Xeon'),
        ]
        self.computers = [
            Computer(1, 'Персональный компьютер', 120000, 1),
            Computer(2, 'Серверный компьютер', 150000, 1),
            Computer(3, 'Рабочая станция', 80000, 2),
        ]
        self.comp_micros = [
            CompMicro(1, 1),
            CompMicro(2, 1),
            CompMicro(3, 2),
        ]

    def test_task_A1(self):
        result = task_A1(self.computers, self.microprocessors)
        expected = {
            'Intel Core i7': ['Персональный компьютер', 'Серверный компьютер'],
            'AMD Ryzen 5': ['Рабочая станция'],
        }
        self.assertEqual(result, expected)

    def test_task_A2(self):
        result = task_A2(self.computers, self.microprocessors, self.comp_micros)
        expected = [
            ('Intel Core i7', 270000),
            ('AMD Ryzen 5', 80000),
            ('Intel Xeon', 0),
        ]
        self.assertEqual(result, expected)

    def test_task_A3(self):
        result = task_A3(self.computers, self.microprocessors, self.comp_micros, 'Intel')
        expected = {
            'Intel Core i7': ['Персональный компьютер', 'Серверный компьютер'],
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
