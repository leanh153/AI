shopping_list = ["apple", "banana", "orange", "eggs"]
nums = [0, 2, 3, 234, 23, 34, 34, 3554, 3, 6]

print("enumerate function ===============")
for index, item in enumerate(shopping_list, 1):
    print("Item: {} : {}".format(index, item))

print("all, any function ===============")
all_result = all(i > 0 for i in nums)
any_result = any(i > 0 for i in nums)

print("list [0, 2, 3, 234, 23, 34, 34, 3554, 3, 6] check greater than 0")
print("all result: ", all_result)
print("any result: ", any_result)

