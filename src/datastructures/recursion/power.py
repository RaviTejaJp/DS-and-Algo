def power(base_number: int, exponent: int) -> int:
    assert exponent == int(exponent), "Exponent must be a integer"
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / base_number * power(base_number, exponent+1)
    else:
        return base_number * power(base_number, exponent-1)


print(power(2,2))
print(power(2,-2))