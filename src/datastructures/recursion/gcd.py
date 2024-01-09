def euclidean_gcd(number1: int, number2: int) -> int:
    assert number1 == int(number1), f"{number1} is not integer"
    assert number2 == int(number2), f"{number2} is not integer"
    
    if number1 == 0 or number2 == 0:
        return number1 or number2
    else:
        return euclidean_gcd(max(number1, number2) % min(number1, number2), min(number1, number2))

print(euclidean_gcd(121212,363636))