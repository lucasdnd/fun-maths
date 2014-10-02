# Kaprekar's Constant
# 6174 is the Kaprekar's Constant. Here's why it's so special:
# 1. Take any four-digit number that is not made of only 1 number (can't be 1111, 2222, ...., or 9999)
# 2. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary
# 3. Subtract the smaller number from the bigger number
# 4. Go back to step 2
# For any 4 digit number that matches the rule described in #1, you'll end up reaching 6174.

# This is the string version of "kaprepars-constant.py"

import sys
input = input if sys.version_info.major == 3 else raw_input

const = 6174

def getDigits(num):
  digits = []
  numStr = str(num)
  digits.append(numStr[0])
  digits.append(numStr[1])
  digits.append(numStr[2])
  digits.append(numStr[3])
  digits.sort()
  return digits

def getAscending(num):
  digits = getDigits(num)
  return int(digits[0] + digits[1] + digits[2] + digits[3])

def getDescending(num):
  digits = getDigits(num)
  return int(digits[3] + digits[2] + digits[1] + digits[0])

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

