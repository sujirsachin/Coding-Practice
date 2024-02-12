def lengthOfLastWord(s: str) -> int:
    words = s.split(" ")
    words[:] = [x for x in words if x]
    print(len(words[-1]))


print(lengthOfLastWord("   fly me   to   the moon  "))
