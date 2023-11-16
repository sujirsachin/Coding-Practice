from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    result = ""
    smallest = min(len(string) for string in strs)
    for i in range(smallest):
        for string in strs:
            if string[i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result

a = ["flower", "flow", "flight"]
print(longestCommonPrefix(a))