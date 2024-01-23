#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 if number < 0 else number % 10
str_num = f"-{last_digit}" if number < 0 and last_digit != 0 else last_digit
text = f"Last digit of {number} is {str_num} and is"

if last_digit == 0:
    print(f"{text} 0")
elif last_digit > 5 and number > 0:
    print(f"{text} greater than 5")
else:
    print(f"{text} less than 6 and not 0")
