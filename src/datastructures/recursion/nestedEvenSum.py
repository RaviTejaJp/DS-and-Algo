#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# nestedEvenSum Solution

obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {"superInner": 2, "notANumber": True, "alsoNotANumber": "yup"},
    },
}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"},
}


def nestedEvenSum(obj, sum=0):
    for item in obj:
        if isinstance(obj[item], dict):
            sum = sum + nestedEvenSum(obj[item], 0)
        elif isinstance(obj[item], int):
            if obj[item] % 2 == 0:
                sum = sum + obj[item]
        else:
            pass
    return sum

print(nestedEvenSum(obj=obj2, sum=0))
