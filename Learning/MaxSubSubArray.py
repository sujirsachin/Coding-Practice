from Learning.AssertionTest import test


def max_sum_subarray(arr, k):
    if not arr or k > len(arr):
        return []
    max_sum = float('-inf')
    result = []

    for i in range(len(arr) - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]

        if current_sum > max_sum:
            max_sum = current_sum
            result = arr[i: i + k]

    return result


def max_sum_subarray2(arr, k):
    max_sum = float('-inf')
    window_sum = 0
    window_start = 0
    result_start_index = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # Once we hit a window of size `k`
        if window_end - window_start + 1 == k:
            if window_sum > max_sum:
                max_sum = window_sum
                result_start_index = window_start

            window_sum -= arr[window_start]
            window_start += 1

    return arr[result_start_index: result_start_index + k]


max_sum_subarray_test_cases = [
    (([2, 1, 5, 1, 3, 2], 3), [5, 1, 3]),
    (([1, 9, 2, 5, 1], 2), [9, 2]),
    (([5, 5, 5, 5], 2), [5, 5]),
    (([1, 2, 3], 3), [1, 2, 3]),
    (([10], 1), [10]),
    (([-4, -2, -1, -5], 2), [-2, -1]),
    (([1, 2, 3, 2, 1], 3), [2, 3, 2]),
    (([5, 1000, -1, 2, 3], 2), [5, 1000]),
    (([1, 3, -1, 2, 4], 4), [3, -1, 2, 4]),
]

for args, expected in max_sum_subarray_test_cases:
    test(max_sum_subarray, expected, *args)

print("***** All test cases passed in max_sum_subarray *****")

for args, expected in max_sum_subarray_test_cases:
    test(max_sum_subarray2, expected, *args)

print("***** All test cases passed in max_sum_subarray2 *****")
