
#!/bin/python3

import math
import os
import random
import re
import sys
# Function for birthday cake candles
def birthdayCakeCandles(ar):
    n = len(ar)
    c = 0
    max = ar[0]
    for i in range(n):
        if ar[i] > max:
            max = ar[i]

    for i in range(n):
        if ar[i] == max:
            c += 1
    return c

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))
# Calling the birthdayCakeCandles and storing it's return value on result

result = birthdayCakeCandles(ar)
print(result)
