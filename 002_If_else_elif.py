a = int(input())
if a > 0:
    print(a, "big form zero")
elif a == 0:
    print(a, "equal with zero")
else:
    print(a, "small from zero")

b = str(input())
if "Hello" in b:
    print(b)
else:
    print("'Hello' not found")

c = int(input())
d = int(input())
if c >= d:
    print(c, "big from ", d)
elif c <= d:
    print(d, "big from ", c)
elif c == d:
    print(c, " and ", d, "equal")
else:
    print("ERROR")

# > - left is big
# >= -left big or equal
# < - right is big
# <= - right big or equal
# == - equal
# != - not equal
# and
# or
# not
"""Alimardon Boqijonov"""
