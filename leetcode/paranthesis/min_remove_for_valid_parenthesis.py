from __future__ import annotations


def solution(equation: str) -> str:
    stack: list = []
    remove_index: list = [0]*len(equation)
    for index, char in enumerate(equation):
        if char == ')':
            if stack:
                stack.pop()
            else:
                remove_index[index] = 1
        elif char == '(':
            stack.append(index)
        else:
            pass
    for item in stack:
        remove_index[item] = 1

    result: str = ''
    for index, char in enumerate(equation):
        if remove_index[index]:
            pass
        else:
            result += char
    print(f'Modified Equation : {result}')
    print(f'Equation : {equation}')
    print(f'Remove Index : {remove_index}')
    print('*'*100)


inputs = []
inputs.append(')a+b')
inputs.append('(a+b')
inputs.append('((a+b')
inputs.append('((a+b)')
inputs.append('((a+b))')
inputs.append('((a+b)))')
inputs.append(')a+b+(c)')
inputs.append('(a+b+(c)')
inputs.append('((a+b+(c)')
inputs.append('((a+b)+c')
inputs.append('((a+b))+c')
inputs.append('((a+b)))+c')

for input in inputs:
    solution(input)
