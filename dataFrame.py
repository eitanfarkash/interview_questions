import pandas as pd

# data = {
#     "calories": [420, 380, 420],
#     "duration": [50, 40, 45],
#     "average": [10, 20, 30]
# }
#
# # load data into a DataFrame object:
# df = pd.DataFrame(data)
# df.insert(3, "newCol", [1, 2, 3])
# print(df)

# info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
#         'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}
#
# info = pd.DataFrame(info)
# print(info)
# info['three'] = [20, 40, 60, 70, 80, 90]
# print(info)

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
print(df)
print(df.loc['cobra', 'shield'])
