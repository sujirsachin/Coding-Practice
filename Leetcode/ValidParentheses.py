def isValid(s: str) -> bool:
    lookUp = {
        ')': '(',
        '}': '{',
        ']': '['}
    list = []
    for i in range(len(s)):
        if s[i] in lookUp.values():
            list.append(s[i])
        else:
            if len(list) != 0 and list[len(list) - 1]== lookUp[s[i]]:
                list.pop()
            else:
                return False
    if not list:
        return True
    else:
        return False


print(isValid("()[]{}"))