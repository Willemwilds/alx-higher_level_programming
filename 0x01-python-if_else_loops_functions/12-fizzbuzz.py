#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end="", sep=" ")
        elif num % 3 == 0:
            print("Fizz", end="", sep=" ")
        elif num % 5 == 0:
            print("Buzz", end="", sep=" ")
        else:
            print(num, end="", sep=" ")
