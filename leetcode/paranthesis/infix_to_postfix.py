from __future__ import annotations


def solution(equation: str) -> str:
    map = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '^': 2,
        '(': -1,
    }
    stack: list = []
    result: str = ''
    for item in equation:
        if item in map or item in ')':
            if item == ')':
                popped_item = stack.pop()
                while popped_item != '(':
                    result += popped_item
                    popped_item = stack.pop()
            elif stack:
                if map[stack[-1]] < map[item]:
                    stack.append(item)
                else:
                    while stack and map[stack[-1]] >= map[item]:
                        popped_item = stack.pop()
                        if popped_item != '(':
                            result += popped_item
                    stack.append(item)
            else:
                stack.append(item)
        else:
            result += item

    while stack:
        result += stack.pop()
    print(f' Input : {equation} -- Output : {result}')
    return result


inputs = []
inputs.append('(a+b*c/d^2)+3+a')
inputs.append('(a+b*c/d)+3+a')
inputs.append('a+b*c/d+3+a')
inputs.append('a+b*c/d+3*a')

for input in inputs:
    solution(input)
