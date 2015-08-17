import time
import sys
import math
xrange = range if sys.version_info.major == 3 else xrange

def is_prime(num):

  if num == 2:
    return True
  if num % 2 == 0: return False

  limit = int(math.ceil(math.sqrt(num)))
  for i in xrange(3, limit + 1, 2):
    if num % i == 0:
      return False
  
  return True

if len(sys.argv) != 2:
  print("Example usage: python is-prime.py 37")
  sys.exit()

num = int(sys.argv[1])
start = time.time()
result = is_prime(num)
end = time.time()

if result:
  print("Prime!")
else:
  print("Not prime :(")
print("time to calc: " + str(end - start))
