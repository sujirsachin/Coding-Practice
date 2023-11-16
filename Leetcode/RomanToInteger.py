def romanToInt(s: str) -> int:
        look_up = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        result = look_up[s[len(s)-1]]
        i = len(s)-2
        while(i >= 0):
            if(look_up[s[i]] < look_up[s[i+1]]):
                result -= look_up[s[i]]
            else:
                result += look_up[s[i]]
            i = i-1
        return result

print(romanToInt("MCMXCIV"))