from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] != 9:
        digits[-1] +=1
        return digits
    else:
        carry = 1
        i = len(digits) - 1
        while carry >0 and i >=0:
            if digits[i] !=9:
                digits[i] +=1
                carry = 0
                break
            else:
                digits[i] = 0
            i -= 1
        if carry !=0:
            digits.insert(0,1)
        return digits


print(plusOne([9]))