# Last digits of powers of 2
# I noticed a pattern on the powers of 2: the last digits repeat: 6, 2, 4 and 8.
#
# Example:
#
#     [2]     [4]     [8]    1[6]
#    3[2]    6[4]   12[8]   25[6]
#   51[2]  102[4]  204[8]  409[6]
#  819[2] 1638[4] 3276[8] 6553[6]
#
# In this script, we test this thing.
#

for i in range(1, 16384):

  it_works = True
  result = pow(2, i)
  print (result)

  if i % 4 == 0:
    if result % 10 != 6:
      it_works = False
      break
  elif i % 4 == 1:
    if result % 10 != 2:
      it_works = False
      break
  elif i % 4 == 2:
    if result % 10 != 4:
      it_works = False
      break
  else:
    if result % 10 != 8:
      it_works = False
      break

print ("does it work? " + str(it_works))
