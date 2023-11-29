from __future__ import annotations


def solution(equation: str) -> str:
    stack: list = []
    result: int = 0
    for index, char in enumerate(equation):
        if char == ')':
            if stack:
                pair_index = stack.pop()
                result = max((index - pair_index), result)
            else:
                pass
        elif char == '(':
            stack.append(index)
        else:
            pass
    print(result)


inputs = []
inputs.append('((a+b+c)+d+(e+f))')
inputs.append('(a+b+c)+d+(e+f)')
inputs.append('(a+b+c)+(d+(e+f)')
inputs.append('(a)+(d+(e+f)')


for input in inputs:
    solution(input)
