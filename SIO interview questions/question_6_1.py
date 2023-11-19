"""
Question 6.1:
    In question 5, the function "evaluate" was implemented.
    In this question the task is to add code to support the operations which appear below.

    You can use the function "evaluate" from question 5.
    You can assume that all input is legal.
"""

my_calc = MyCalc()
my_calc.store("A = - 10 + 5 + 5 + 10")
my_calc.store("B = A + 5")
my_calc.store("C = A + B + 5")
print("A = {}".format(my_calc.get("A")))
print("B = {}".format(my_calc.get("B")))
print("C = {}".format(my_calc.get("C")))
print(my_calc.check("A = C - B"))
print(my_calc.check("A + B + 5 = C"))
print(my_calc.check("A > B"))
print(my_calc.check("A < B"))
