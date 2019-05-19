import re

# t = int(input())
# for i in range(t):
#     input_digit = input()
#     if input_digit.isnumeric():
#         print(bool(re.search(r"^[-+]\d*\.\d+", input_digit)))


m = re.search(r"([a-z0-9])\1+", input())
print(m.group())
print(m.group(1) if m else -1)