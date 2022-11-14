def sum_digits(num):
    assert num >= 0 and int(num) == num, "Please use a positive integer"

    if num < 10:
        return num
    else:
        return num % 10 + sum_digits(num // 10)