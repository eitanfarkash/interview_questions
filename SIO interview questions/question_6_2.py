"""
Question 6.2:
    Implement Python class "MyCalc" to support the operations which appear below.

    You can use the function "evaluate" from question 5.
    You can assume that all input is legal.
"""


class MyCalc(object):
    def __init__(self):
        self.my_dict = dict()

    def store(self, s):
        left, right = s.split("=")
        left = left.strip()
        self.my_dict[left] = self.evaluate(right)

    def get(self, s):
        return self.my_dict[s]

    def check(self, s):
        if "=" in s:
            left, right = s.split("=")
            return self.evaluate(left) == self.evaluate(right)
        elif "<" in s:
            left, right = s.split("<")
            return self.evaluate(left) < self.evaluate(right)
        elif ">" in s:
            left, right = s.split(">")
            return self.evaluate(left) > self.evaluate(right)

    def evaluate(self, my_string: str) -> int:
        my_list = my_string.split()
        sign = 1
        my_sum = 0
        for c in my_list:
            if c == "-":
                sign = -1
            elif c == "+":
                sign = 1
            elif c.isalpha():
                my_sum += int(self.my_dict[c]) * sign
            else:
                my_sum += int(c) * sign
        return my_sum
 

my_calc = MyCalc()
my_calc.store("A = - 10 + 5 + 5 + 10")
my_calc.store("B = A + 5")
my_calc.store("C = A + B + 5")
print(f"A = {my_calc.get('A')}")
print(f"B = {my_calc.get('B')}")
print(f"C = {my_calc.get('C')}")
print(f"A = C - B is : {my_calc.check('A = C - B')}")
print(f"A + B + 5 = C is : {my_calc.check('A + B + 5 = C')}")
print(f"A > B is : {my_calc.check('A > B')}")
print(f"A < B is : {my_calc.check('A < B')}")

# class MyCalc(object):
#     def __init__(self):
#         self.d = dict()
#
#     def evaluate(self, my_string: str) -> int:
#         my_list = my_string.split()
#         sign = 1
#         my_sum = 0
#         for c in my_list:
#             if c == "-":
#                 sign = -1
#             elif c == "+":
#                 sign = 1
#             elif c.isdigit():
#                 my_sum += int(c) * sign
#             else:
#                 my_sum += int(self.d[c]) * sign
#         return my_sum
#
#     def store(self, s):
#         left, right = s.split('=')
#         left = left.strip()
#         self.d[left] = self.evaluate(right)
#
#     def get(self, s):
#         return self.evaluate(s)
#
#     def check(self, s):
#         if '=' in s:
#             left, right = s.split('=')
#             return self.evaluate(left) == self.evaluate(right)
#         elif '>' in s:
#             left, right = s.split('>')
#             return self.evaluate(left) > self.evaluate(right)
#         elif '<' in s:
#             left, right = s.split('<')
#             return self.evaluate(left) < self.evaluate(right)
