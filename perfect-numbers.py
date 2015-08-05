# Perfect Numbers
# Finds the perfect numbers up to the input value
# A perfect number is a number which the sum of its divisors equals the number itself
# Good luck finding the fifth one

import sys
input = input if sys.version_info.major == 3 else raw_input

def isPerfect(num):
  sum = 0
  for i in range(1, num):
    if num % i == 0:
      sum = sum + i

  if sum == num:
    return True
  return False

n = int(input("Print perfect numbers up to: "))
for i in range(1, n):
  if isPerfect(i):
    print(str(i))
