from Learning.AssertionTest import test


def move_zeroes(arr):
    left = 0
    right = 1
    while right < len(arr):
        if arr[left] == 0 and arr[right] != 0:
            arr[left] = arr[right]
            arr[right] = 0
            right += 1
            left += 1
        elif arr[left] == 0 and arr[right] == 0:
            right += 1
        else:
            right += 1
            left += 1

    return arr


def move_zeroes2(arr):
    insert_position = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i != insert_position:
                arr[insert_position] = arr[i]
                arr[i] = 0
            insert_position += 1
    return arr


move_zeroes_test_cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 0], [0, 0, 0]),
    ([], []),
    ([0], [0]),
    ([1], [1]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
    ([4, 0, 5, 0, 0, 6], [4, 5, 6, 0, 0, 0]),
    ([0, 1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0, 0]),
]

for args, expected in move_zeroes_test_cases:
    test(move_zeroes, expected, args)

print("All tests passed for move_zeroes")

for args, expected in move_zeroes_test_cases:
    test(move_zeroes2, expected, args)

print("All tests passed for move_zeroes2")
