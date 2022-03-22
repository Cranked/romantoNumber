from functools import reduce

romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
def different_solving(s):
    return reduce(lambda value, i: value +(romans[s[i]] if romans[s[i]]>romans[s[i+1]] else -1*romans[s[i]]),reversed(range(len(s)-1)),romans[s[-1]])

def romanToInt(s):
    result=0
    for i in range(len(s)):
        if romans[s[i]] > romans[s[i-1]]:
            result +=romans[s[i]]-2*romans[s[i-1]]
        else:
            result+=romans[s[i]]

        # if (x == "I"):
        #     current_value = "I"
        #     result += 1
        # elif x == "V":
        #     current_value = "V"
        #     result += 5
        # elif x == "X":
        #     current_value = "X"
        #     result += 10
        # elif x=="L":
        #     current_value = "L"
        #     result += 50
        # elif x == "C":
        #     current_value = "C"
        #     result += 100
        # elif x == "D":
        #     current_value = "D"
        #     result += 500
        # elif x == "M":
        #     current_value = "M"
        #     result += 1000

    return result
if "__main__":
    string="MCMXCIV"
    result=romanToInt(string)
    print(result)
    print(different_solving(string))

