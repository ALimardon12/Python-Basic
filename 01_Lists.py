# Lists: ordered, mutable, allows duplicate elements
alist = [1, 2, 3.12, "hello", True]
print(list)
print(type(list))
a = ["apple", "kiwi", "grape", "nut", "mango", "apricot"]
print(a[0])  # 0 index
print(a[:])  # full element
print(a[2:])  # from 2 index to finish
print(a[:4])  # from start to 3 index: ["apple", "kiwi", "grape", "nut"]
print(a[-1])  # apricot
print(a[::2])  # ["apple", "grape", "mango"]
print(a[::-1])  # ["apricot", "mango", "nut", "grape", "kiwi", "apple"]
b = a[3]
print(b)  # nut
print(len(a))  # length of list
"""-----------------------------------------------------------------------------------"""

for i in a:
    print(i)
"""results: 
apple
kiwi
grape
nut
mango
apricot
"""

"""--------------------------------------------------------------------------------"""
if "mango" in a:
    print("yes")
else:
    print("not found")
"""---------------------------------------------------------------------------------"""
# add element to list
f = [1, 2, 3, 4, 5, 12]
b = f.append(13)
print(b)

f.insert(0, "Alimardon")
print(f)

f = [1, 2, 3]
g = ["Alimardon", "Prince12", "Infin1ty.uz"]
f.extend(g)
print(f)
g.extend(f)
print(g)
"""--------------------------------------------------------------------------------"""
# remove element from list
# 1
q = ["hello", "apple", "kiwi", "movie"]
q.pop()
print(q)
# 2
q.remove("apple")
print(q)
# 3
q.clear()
print(q)
# 4
del q
print(q)  # q not found

"""--------------------------------------------------------------------------------"""
# sort list
t = [12, 232, 1, -98, 34]
t.sort()
print(t)  # [-98, 1, 12, 34, 232]

t.reverse()
print(t)  # [232, 34, 12, 1, -98]

t.sort(reverse=False)
print(t)  # [-98, 1, 12, 34, 232]

t.sort(reverse=True)
print(t)  # [232, 34, 12, 1, -98]

k = sorted(t)
print(k)  # [-98, 1, 12, 34, 232]

"""----------------------------------------------------------------------------"""

ab = [12] * 5
print(ab)  # [12, 12, 12, 12, 12]
p12 = [1, 2, 3, 4, 5]
a12 = ab + p12
print(a12)  # [12, 12, 12, 12, 12, 1, 2, 3, 4, 5]

"""------------------------------------------------------------------------------"""
# list copy
# 1
v = [1, 2, 3, 4, 5]
i = v
print("i: ", i)
print("v: ", v)
i.append(123)
print("i: ", i)
print("v: ", v)
# 2
r = [1, 2, 3, 4, 5]
j = r.copy()
print("j: ", j)
print("r: ", r)
j.append(123)
print("r: ", r)
print("j: ", j)
# 3
s = [1, 2, 3, 4, 5]
l = list(s)
print("s: ", s)
print("l: ", l)
l.append("salom")
print("s: ", s)
print("l: ", l)

"""---------------------------------------------------------------------------"""

mylist = [1, 2, 3, 4, 5]
h = [x*x for x in mylist]
print(mylist)  # result: [1,2,3,4,5]
print(h)  # result: [1, 4, 9, 16, 25]
