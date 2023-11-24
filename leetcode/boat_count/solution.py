from typing import List
import math


def my_solution(weights: List[float], boat_limit: int) -> int:
    weights.sort()
    left = 0
    right = len(weights) - 1
    boat_needed = 0
    while left <= right:
        if left == right and weights[left] <= boat_limit:
            boat_needed += 1
            left = left + 1
            right = right - 1
        else:
            if boat_limit == weights[right]:
                boat_needed += 1
                right = right - 1
            elif weights[right] + weights[left] <= boat_limit:
                boat_needed += 1
                left = left + 1
                right = right - 1
            elif weights[right] + weights[left] > boat_limit:
                boat_needed += 1
                right = right - 1
    return boat_needed


def course_solution(
    weights: List[float], boat_limit: int, boat_occupancy_limit: int
) -> int:
    boat_needed: int = 0
    weights.sort()
    if weights[0] <= 0 or weights[-1] > boat_limit:
        pass
    else:
        left = 0
        right = len(weights) - 1
        print(f"Weights : {weights}")
        while left <= right:
            current_iteration_weight = 0
            count = 0
            while left <= right and count < boat_occupancy_limit and current_iteration_weight < boat_limit:
                current_iteration_weight += weights[right]
                if current_iteration_weight > boat_limit:
                    current_iteration_weight -= weights[right]
                    break
                else:
                    print(f"Person from {right} is in boat {boat_needed+1}")
                    right = right - 1
                    count = count + 1
            while left <= right and count < boat_occupancy_limit and current_iteration_weight < boat_limit:
                current_iteration_weight += weights[left]
                if current_iteration_weight > boat_limit:
                    current_iteration_weight -= weights[left]
                    break
                else:
                    print(f"Person from {left} is in boat {boat_needed+1}")
                    left = left + 1
                    count = count + 1
            boat_needed += 1
            if boat_needed > len(weights):
                break
            print("="*100)
            print(f"Boat : {boat_needed}")
            print(f"Current Iteration weight is : {current_iteration_weight}")
            print(f"Current boat occupance count is : {count}")
            print(f"Current pointers for left : {left} and right : {right}")
            print("="*100)
            
    max_boat_needed = len(weights)
    min_boat_needed = math.ceil(len(weights) / boat_occupancy_limit)
    if (boat_needed > max_boat_needed) or (
        boat_needed < min_boat_needed):
        print("Something looks wrong")
    else:
        return boat_needed
