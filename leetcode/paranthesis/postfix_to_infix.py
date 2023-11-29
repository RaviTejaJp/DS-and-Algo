from __future__ import annotations


def solution(equation: str) -> str:
    stack: list = []
    for i in equation:
        if i in '+-*/^':
            second_operand = stack.pop()
            first_operand = stack.pop()
            temp = f'({first_operand} {i} {second_operand})'
            stack.append(temp)
        else:
            stack.append(i)
    return stack.pop()


inputs = []
inputs.append('abc*d2^/+3+a+')
inputs.append('abc*d/+3+a+')
inputs.append('abc*d/+3+a+')
inputs.append('abc*d/+3a*+')

for input in inputs:
    print(solution(input))
