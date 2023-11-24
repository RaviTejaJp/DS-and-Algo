import unittest
from solution import solution

class SolutionTest(unittest.TestCase):
    def test_input(self):
        x = [i for i in range(10)]
        y = [i for i in range(10,0,-1)]
        case_input = x + y
        self.assertTrue(solution(case_input))
        case_input = x + [2] + y
        self.assertFalse(solution(case_input))
        case_input = x + y + [2]
        self.assertFalse(solution(case_input))
        case_input = [2] + x + y
        self.assertFalse(solution(case_input))
        case_input = x
        self.assertFalse(solution(case_input))
        case_input = x + [9]
        self.assertFalse(solution(case_input))
        case_input = [9] + x
        self.assertFalse(solution(case_input))

if __name__ == '__main__':
    unittest.main()