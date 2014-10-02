# Kaprekar's Constant
# 6174 is the Kaprekar's Constant. Here's why it's so special:
# 1. Take any four-digit number that is not made of only 1 number (can't be 1111, 2222, ...., or 9999)
# 2. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary
# 3. Subtract the smaller number from the bigger number
# 4. Go back to step 2
# For any 4 digit number that matches the rule described in #1, you'll end up reaching 6174.

import sys
input = input if sys.version_info.major == 3 else raw_input

const = 6174

def getDigits(num):
  digits = []
  digits.append(num / 1000)
  digits.append((num % 1000) / 100)
  digits.append((num % 100) / 10)
  digits.append(num % 10)
  return digits

def getAscending(num):
  digits = getDigits(num)
  digits.sort()
  return (digits[0] * 1000) + (digits[1] * 100) + (digits[2] * 10) + digits[3]

def getDescending(num):
  digits = getDigits(num)
  digits.sort()
  return (digits[3] * 1000) + (digits[2] * 100) + (digits[1] * 10) + digits[0]

def kaprekar(num, steps):

  desc = getDescending(num)
  asc = getAscending(num)
  result = desc - asc

  steps += 1
  print "[" + str(steps) + "] -> " + str(desc) + " - " + str(asc) + " = " + str(result)

  return kaprekar(result, steps) if result != const else 1

print "Enter a 4 digit number that is not made of the same numbers"
num = int(input("(can't be 1111, 2222, ...., or 9999): "))
steps = 0
kaprekar(num, steps)

