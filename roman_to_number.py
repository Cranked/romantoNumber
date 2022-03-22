def romanToInt(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    current_value = ""
    for x in s:
        if current_value != "":
            if romans.get(current_value) < romans.get(x):
                result -= 2*romans.get(current_value)
        if (x == "I"):
            current_value = "I"
            result += 1
        elif x == "V":
            current_value = "V"
            result += 5
        elif x == "X":
            current_value = "X"
            result += 10
        elif x=="L":
            current_value = "L"
            result += 50
        elif x == "C":
            current_value = "C"
            result += 100
        elif x == "D":
            current_value = "D"
            result += 500
        elif x == "M":
            current_value = "M"
            result += 1000

    return result
if "__main__":
    string="MCMXCIV"
    result=romanToInt(string)
    print(result)
