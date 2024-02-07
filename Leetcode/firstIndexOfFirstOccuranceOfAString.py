
def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        for i in range(0,len(haystack)):
            if haystack[i:i+len(needle)] in needle:
                return i
    return -1

#Solution 2
def strStr2(haystack: str, needle: str) -> int:
    if needle in haystack:
        index = haystack.index(needle)
        return index
    else:
        return -1

print(strStr("sadbutsad", "sad"))
print(strStr2("leetcode", "code"))
