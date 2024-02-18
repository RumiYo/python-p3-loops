#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_integers = [ integer * integer for integer in int_list ]
    return squared_integers

def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:   
        if i % 15 == 0:
             print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1    
