import unittest
import random
from solution import solution, two_pointer

class SolutionTest(unittest.TestCase):
    def test_case(self):
        test_case_count = 10000
        for i in range(test_case_count):
            case_input = [random.randint(1,100) for _ in range(random.randint(0,100))]
            # print(f"{case_input} --- {two_pointer(case_input)}")
            self.assertEqual(solution(case_input), two_pointer(case_input))

if __name__ == '__main__':
    unittest.main()