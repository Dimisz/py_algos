def fibonacci(num):
    assert int(num) == num and num >= 0, "Fibonacci Number is calculated for integer greater or equal to 0"
    if num in [0, 1]:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)