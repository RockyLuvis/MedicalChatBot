'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

phone_combination = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


digits = input ("Enter digit combination:")
if digits == "":
    print("No combination entered")
    output = "No input"
    print (output)

try:
    if not digits.isdigit():
        raise ValueError ("enter valid combination between 2-9")
    else:    

        #if the combination is only two number
        first = digits[0]
        second = digits[1]

        #look up correspondig letters for first and second
        letters1 = phone_combination[first]
        letters2 = phone_combination[second]
        output = [].r

        for i in range(len(letters1)):
            for j in range(len(letters2)):
                output.append(letters1[i]+letters2[j])
except Exception as e:
    raise Exception ("Input valid combination",e)
print (output)

 