#!/usr/bin/env python

try:
    number = int(input("Enter a number: "))
except:
    print("That's silly")
    exit()

potential_divisors = list(range(1, int(number/2 + 1)))
potential_divisors.append(number)

divisors = []
for div in potential_divisors:
    if number % div == 0:
        divisors.append(str(div))

print("The factors of " + str(number) + " are " + ", ".join(divisors) + ".")

