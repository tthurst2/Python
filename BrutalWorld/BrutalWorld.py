from __future__ import print_function
import random, time, sys


if sys.argv[1:]:
    target_array = []
    for x in sys.argv[1:]:
        target_array += x + " "
else:
    target_array = list("Hello, World!")
string_array = [""] * len(target_array)
i = 0
while i < len(target_array):
    string_array[i] = chr(random.randint(32, 126))
    if string_array[i] == target_array[i]:
        i += 1
    print("".join(string_array), end="\r")
    time.sleep(.004)