from __future__ import annotations


def solution(equation: str) -> bool:
    stack: list = []
    map = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for item in str(equation):
        if item in ('(', '{', '['):
            stack.append(item)
        if item in (')', '}', ']'):
            if stack:
                if map[item] == stack.pop():
                    pass
                else:
                    return False
            else:
                return False

    return bool(stack)


inputs = []
inputs.append('(A+B)')
inputs.append('{A+B}')
inputs.append('[A+B]')
inputs.append('(A+B)+{([A+B]+C)}')
inputs.append('{{A+B} + C}')
inputs.append('[A+B]')

for input in inputs:
    print(solution(equation=input))
