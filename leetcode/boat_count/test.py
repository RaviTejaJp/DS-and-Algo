import unittest
from solution import course_solution
import random
from typing import List

class TestBoatCount(unittest.TestCase):
    def test_course_solution(self):
        weights: List[int] = [6,2,2,2]
        boat_limit:int = 6
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit, boat_occupancy_limit=2), 3)

        weights: List[int] = [6,4,2,2]
        boat_limit:int = 8
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit, boat_occupancy_limit=2), 2)

        weights: List[int] = [1,2]
        boat_limit:int = 3
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 1)

        weights: List[int] = [1]
        boat_limit:int = 3
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 1)
        
        weights: List[int] = [2,2]
        boat_limit:int = 3
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 2)
        
        weights: List[int] = [1,2,2]
        boat_limit:int = 3
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 2)

        weights: List[int] = [2,2,2]
        boat_limit:int = 3
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 3)

        weights: List[int] = [2,2,2]
        boat_limit:int = 4
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 2)

        weights: List[int] = [2,2,2]
        boat_limit:int = 6
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 2)

        weights: List[int] = [2,2,2,6]
        boat_limit:int = 6
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 3)

        weights: List[int] = [6,2,2,2]
        boat_limit:int = 6
        self.assertEqual(course_solution(weights=weights,boat_limit=boat_limit,boat_occupancy_limit=2), 3)

if __name__ == '__main__':
    unittest.main()