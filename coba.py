import re
# # string = "12WB12W3B24WB"
# # # a = re.findall(r'\d+\w|\w',string)
# # for m in re.findall(r'\d+\w|\w', string):
# #     print(m)
# # # print(a)

# string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
# # a = [m.group(0) for m in re.finditer(r"(.)\1*", string)]
# a = re.findall(r"(.*)\1", string)
# print(a)
