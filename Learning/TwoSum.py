from Learning.AssertionTest import test


def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            return True
    return False

test_cases = [
    (([1, 2, 4, 9], 8), False),
    (([1, 2, 3], 10), False),
    (([], 5), False),
    (([2, 2, 2, 2], 4), True),
    (([1, 2, 3, 4, 6], 7), True),
]
for args, expected in test_cases:
    test(has_pair_with_sum, expected, *args)
