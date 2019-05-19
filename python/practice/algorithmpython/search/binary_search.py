def binary_search(target, low, high, arrays):
    while high >= low:
        mid = (high + low) // 2
        if target == arrays[mid]:
            return mid
        elif target > arrays[mid]:
            low = mid + 1
        elif target < arrays[mid]:
            high = mid - 1


def binary_search_recur(target, low, high, arrays):
    if low > high:
        return -1
    mid = (low + high) // 2
    if target > arrays[mid]:
        return binary_search_recur(target, mid + 1, high, arrays)
    elif target < arrays[mid]:
        return binary_search_recur(target, low, mid - 1, arrays)
    elif target == arrays[mid]:
        return mid

