import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('test-walk')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('test_walk')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        challenger = Runner('test1')
        challenge2 = Runner('test2')

        for _ in range(10):
            challenger.run()
            challenge2.walk()
        self.assertNotEqual(challenger.distance, challenge2.distance)


if __name__ == '__main__':
    unittest.main()
