# Collatz Conjecture
# Start with a number n > 1. Find the number of steps it takes to reach one using
# the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

import sys
input = input if sys.version_info.major == 3 else raw_input

num = int(input("Enter a number: "))
steps = 0

while num != 1:
  if num % 2 == 0:
    num //= 2
  else:
    num *= 3
    num += 1

  steps += 1
  print("[" + str(steps) + "] = " + str(int(num)))
