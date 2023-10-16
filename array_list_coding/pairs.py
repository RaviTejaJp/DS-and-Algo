def pair_sum(myList, sum):
    seen_compliment = {}
    result = []
    for index, item in enumerate(myList):
        compliment = sum - item
        if item in seen_compliment:
            seen_compliment[item].append(index)
        else:
            seen_compliment[item] = [index]
        if compliment in seen_compliment:
            for index in seen_compliment[compliment]:
                result.append(f'{item}+{compliment}')
    return result

def pair_sum2(myList, sum):
    result = []
    for index, item in enumerate(myList):
        compliment = sum - item
        temp = myList[index+1:]
        count = temp.count(compliment)
        for i in range(count):
            result.append(f'{item}+{compliment}')
    return result



result = pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
print(result)
result = pair_sum2([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
print(result)