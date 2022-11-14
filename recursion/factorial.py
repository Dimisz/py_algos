def factorial(num):
    assert num >= 0  and int(num) == num, "The number must be positive integer only"
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)