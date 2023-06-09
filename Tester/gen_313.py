import random
import string
from random import randrange

writer = open('input.txt', 'w')
s = ""
n = 10
writer.write(str(n) + "\n") #100
for i in range(0, n):
    s += str(randrange(n)) + " "
writer.write(s)
writer.close()

# 1000000000
# 200000