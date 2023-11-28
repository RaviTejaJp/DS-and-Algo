from __future__ import annotations
inputs = []
inputs.append('/')
inputs.append('/home/')
inputs.append('/home')
inputs.append('/home/../..')
inputs.append('/')
inputs.append('/home/.')
inputs.append('/home')
inputs.append('/home/foo/../../../../.././temp//./')


def simplify_path(path: str) -> str:
    split_path = path.split('/')
    result: list = []
    for directory in split_path:
        if directory == '' or directory == '.':
            pass
        elif directory == '..':
            if result:
                result.pop()
        else:
            result.append(directory)
    return '/' + '/'.join(result)


for input in inputs:
    print(simplify_path(input))
