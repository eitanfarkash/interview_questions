"""
Question 2:
    create a list which contains all letters from 'a' to 'z'
    Clues:
        i = ord('a')
        c = chr(i)
"""

# your code goes here
letters = []
for i in range(ord('a'), ord('z')+1):
    letters.append(chr(i))

print(f"letters list = {letters}")
# print(f"ord(a)={ord('Z')} and ord('z')={ord('a')}")
