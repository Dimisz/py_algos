def first_method():
    second_method()
    print("I am the first method calling the second")

def second_method():
    third_method()
    print("I am the second method calling the third...")

def third_method():
    fourth_method()
    print("I am the third method calling the fourth...")

def fourth_method():
    print("I am the fourth method")

first_method()