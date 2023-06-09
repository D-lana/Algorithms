import random
import string
from random import randrange

writer = open('input.txt', 'w')
s = ""
n = 10
for i in range(0, n):
    s += random.choice(string.ascii_lowercase)
writer.write(str(s) + '\n')
writer.close()

# 1000000000
# 200000