from typing import List

def strictly_increasing_till(case: List[int], start_index: int) -> int:
    for i in range(start_index, len(case)):
        if i != len(case) - 1:
            if case[i] < case[i + 1]:
                pass
            else:
                return i
        else:
            return i

def strictly_decreasing_till(case: List[int], start_index: int) -> int:
    for i in range(start_index, len(case)):
        if i != len(case) - 1:
            if case[i] > case[i + 1]:
                pass
            else:
                return i
        else:
            return i


def solution2(case: List[int]) -> bool:
    result: bool = False
    length: int = len(case)
    if length >= 3:
        index: int = strictly_increasing_till(case=case,start_index=0)
        if index != length-1:
            index: int = strictly_decreasing_till(case=case,start_index=index)
            if index == length-1:
                result = True
            else:
                pass
        else:
            pass
    return result


def solution(case: List[int]) -> bool:
    i: int = 1
    length: int = len(case)
    if length >= 3:
        while(i < length and  case[i] > case[i-1]):
            i += 1
        if i == 1 or i == length:
            print(f"{case} -- result : {False}")
            return False
        while(i < length and case[i] < case[i-1]):
            i += 1
        if i == length:
            print(f"{case} -- result : {True}")
            return True
        else:
            print(f"{case} -- result : {False}")
            return False