def decimal_to_base(number: int, base: int) -> str:
    if number == 0:
        return '0'
    else:
        return decimal_to_base(int(number//base),base) + str(number % base)

print(decimal_to_base(number=11,base=8))