def is_armstrong_number(number):
    number_of_digits = 0
    sum = 0
    temp = number
    while temp > 0:
        temp //= 10
        number_of_digits += 1

    temp = number
    while  temp > 0:
        remainder = temp % 10
        sum += remainder ** number_of_digits
        temp //= 10
    return sum == number