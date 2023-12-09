def is_armstrong(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit)**order for digit in str(num))
    return num == sum_of_digits
