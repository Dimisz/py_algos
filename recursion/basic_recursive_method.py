def recursive_method(n):
    if n < 1:
        print("n is less than 1")
    else:
        print(f"over method call n is: {n}")
        recursive_method(n-1)
        print(n)
recursive_method(5)