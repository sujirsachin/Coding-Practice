def mySqrt(x: int) -> int:
    count=0
    subtract= 1
    while x > 0:
        x -= subtract
        subtract += 2
        if x >=0:
            count += 1

    return count

# Solution 2 Binary Search
def mySqrt2(x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid-1
        else:
            left = mid+1
    return right
print(mySqrt2(16))
