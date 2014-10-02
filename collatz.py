# Collatz Conjecture
# Start with a number n > 1. Find the number of steps it takes to reach one using
# the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

import sys
input = input if sys.version_info.major == 3 else raw_input

def collatz(num, steps):

  if num % 2 == 0:
    num /= 2
  else:
    num *= 3
    num += 1

  steps += 1
  print "[" + str(steps) + "] = " + str(num)

  return collatz(num, steps) if num != 1 else 1

num = int(input("Enter a number: "))
steps = 0
collatz(num, steps)
