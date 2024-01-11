result = []
def flatten(arr):
    for item in arr:
        if isinstance(item,list):
            flatten(item)
        else:
            result.append(item)



x = [1, 2, 3, [4, 5],[1, [2, [3, 4], [[5]]]],[[1], [2], [3]]]

flatten(x)
print(result)