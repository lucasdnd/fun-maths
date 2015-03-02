import time
import sys
import math

out = file("result.txt", "w")

def is_prime(num):

  if num == 2:
    out.write(str(num) + "\n")
    return True
  if num % 2 == 0: return False

  limit = int(math.ceil(math.sqrt(num)))
  for i in xrange(3, limit + 1, 2):
    if num % i == 0:
      return False
  
  out.write(str(num) + "\n")
  return True

def find_nth_prime(num):
  primes = 0
  i = 2
  while primes < num:
    if is_prime(i):
      primes = primes + 1
    i = i + 1

if len(sys.argv) != 2:
  print "Example usage: python 7-nth-prime.py 1000"
  sys.exit()

num = int(sys.argv[1])
start = time.time()
find_nth_prime(num)
end = time.time()
out.close()
print "Done in " + str(end - start)
print "Result saved in result.txt"
