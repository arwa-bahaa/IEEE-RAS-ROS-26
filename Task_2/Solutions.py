# Problem 1
largest = None
smallest = None

while True:
    num = int(input("Enter number (-1 to stop): "))

    if num == -1:
        break

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Largest number is:", largest)
print("Smallest number is:", smallest)


# Problem 2
n = int(input("Enter a number: "))
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even = sum_even + i

print("Sum of even numbers is:", sum_even)

# Problem 6
sentence = input("Enter a sentence: ")

words = sentence.split()   
words.reverse()          
new_sentence = " ".join(words)  
print(new_sentence)   


# Problem 3
import cmath

z = complex(input())

print(abs(z))
print(cmath.phase(z))


# Problem 4
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
      

# Problem 5
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")


  
