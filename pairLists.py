import random


l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['A', 'B', 'C', 'D', 'E', 'F']
result = []

for i in range (max(len(l1), len(l2))):
    try:
        result.append(f"{l1[i]}{l2[i]}")
    except:
        if len(l1) > len(l2):
            item = random.choice(l2)
            result.append(f"{l1[i]}{item}")
        else:
            item = random.choice(l1)
            result.append(f"{item}{l2[i]}")
print(f"the result list = {result}")
