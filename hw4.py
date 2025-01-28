def find_index_equals_value(A, left=0, right=None):
    if right is None:
        right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == mid:
            return mid
        elif A[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1


