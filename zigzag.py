'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

'''

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    result = [""] * numRows
    row = 0
    step = 1

    for char in s:
        result[row] += char
        
        print ("added char in row =",char,result)

        # Change direction when reaching the top or bottom row
        if row == 0:
            step = 1  # Move downwards
            #print ("Print step after adding 1 =",step)
        elif row == numRows - 1:
            step = -1  # Move upwards
            #print ("Print step after adding -1 =",step)

        row += step
        print ("Print row after adding =",row)

    print("result=", result)
    return "".join(result)

# Example usage
s = "PAYPALISHIRING"
numRows = 4
output = convert(s, numRows)
print(output)  # Output should be "PINALSIGYAHRPI"
