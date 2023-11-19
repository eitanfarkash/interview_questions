"""
Question 1:
    1.1 create a list 'l1' which contains the first 10 powers of 2
    1.2 create a list 'l2' which contains the strings: "a1", "a2", "a3",... "a100"
    1.3 create a list 'l3' which contains only the first 10 items from 'l2'
    1.4 create a list 'l4' which contains only the last 15 items from 'l2'
    1.5 create a list 'l5' which is a copy of 'l2'
"""

# your code goes here
l1 = [2 ** i for i in range(11)]
print(f"L1 = {l1}")

l2 = ["a" + str(i) for i in range(101)]
print(f"L2 = {l2}")
l22 = [f"a{str(i)}" for i in range(11)]
print(f"l22 = {l22}")

l3 = l2[:10]
print(f"L3 = {l3}")

l4 = l2[-15:]
print(f"L4 = {l4}")

l5 = l2[:]
l2.insert(0, "A")
print(f"L5 = {l5}")
print(f"L2 first item is - {l2[0]}")
