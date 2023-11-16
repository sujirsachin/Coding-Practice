from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    maximum = float('-inf')
    start = 0
    window = 0
    for end in range(len(nums)):
        window += nums[end]
        if (end+1-start) == k:
            maximum = max(maximum, window)
            window-= nums[start]
            start += 1
    return maximum/k

def findMaxAverage2(nums: List[int], k:int) -> float:
    maximum = float('-inf')
    start = 0
    range1 = len(nums) -k +1
    for end in range(range1):
        window = sum(nums[start:start+k])
        start += 1
        maximum = max(maximum,window)
    return maximum/k
print(findMaxAverage([1,12,-5,-6,50,3],4))
nums=[1,2,3,4]
print(findMaxAverage2([1,12,-5,-6,50,3],4))
