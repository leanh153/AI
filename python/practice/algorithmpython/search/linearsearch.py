def linear_search(target, start_index, end_index, array):
    for i in range(start_index, end_index):
        if target == array[i]:
            return i
    return -1


def linear_search1(target, array):
    for i in range(0, len(array)-1):
        if target == array[i]:
            return i
    return -1


arr = [x for x in range(1000)]
print(len(arr))
print(linear_search(999, 0, len(arr), arr))
