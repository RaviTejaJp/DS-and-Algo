def sum_of_digits(number: int) -> int:
    result = 0
    if number < 0:
        number = number * -1
    while number > 0:
        digit = int(number % 10)
        number = number // 10
        result += digit
    return result

def recursive_sum_of_digit(number: int) -> int:
    if number < 0:
        return recursive_sum_of_digit(-1*number)
    if 0 <= number <= 9:
        return int(number)
    else:
        return int(number%10) + recursive_sum_of_digit(number // 10)

print(sum_of_digits(-123.1))
print(recursive_sum_of_digit(-123.1))