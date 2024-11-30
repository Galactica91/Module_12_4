import logging
import unittest

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s - %(message)s")

class Runner:
    def __init__(self, name, speed=7):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def walk(self, distance):
        self.distance += distance * self.speed

    def run(self, distance):
        self.distance += distance * self.speed

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Усэйн", -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для объекта - test_walk: %s", e)

    def test_run(self):
        try:
            runner = Runner(123, 5)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта - test_run: %s", e)


    def test_challenge(self):
        runner1 = Runner("Андрей", 10)
        runner2 = Runner("Ник", 5)
        runner1.run(10)
        runner2.walk(10)
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()

