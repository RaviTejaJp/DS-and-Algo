# Problem
""" 
Given the height of walls find the container with more water return area



"""


def solution(heights: list) -> int:
    max_area = 0
    for index,height in enumerate(heights):
        width = 0
        for mover in heights[index+1:]:
            width = width + 1
            area = (min(height,mover)*width)
            if max_area < area:
                max_area = area
    return max_area

def two_pointer(heights: list) -> int:
    left = 0
    max_area = 0
    right = len(heights) - 1
    width = len(heights) - 1
    
    while width > 0:
        max_area = max(max_area, min(heights[left],heights[right]) * width)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left = left + 1
        width -= 1
    return max_area
