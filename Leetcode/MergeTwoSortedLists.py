from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    end = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[end] = nums1[m - 1]
            m -= 1
        else:
            nums1[end] = nums2[n - 1]
            n -= 1
        end -= 1
    while n > 0:
        nums1[end] = nums2[n - 1]
        n -= 1
        end -= 1
    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))
