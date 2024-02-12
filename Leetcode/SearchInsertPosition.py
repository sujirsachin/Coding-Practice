from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        half = nums[len(nums)//2]
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        if target > half:
            print(nums.index(half), len(nums))
            for i in range(nums.index(half), len(nums)):
                if nums[i] < target < nums[i + 1]:
                    return i+1
        else:
            for i in range(0, len(nums[0:half])):
                if nums[i] < target < nums[i+1]:
                    return i+1

#Solution 2: Binary Search
def searchInsert2(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


nums = [1,3,5]
print(searchInsert2(nums,target=4))