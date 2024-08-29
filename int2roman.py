'''
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
'''
lookuptable = {
    "1":	"I",
    "4":    "IV"
    "5":	"V",
    "9":    "IX"
    "10":	"X",
    "40":   "XL",
    "50":	"L",
    "90":   "XC",
    "100":	"C",
    "400":  "CD",
    "500":	 "D",
    "1000":	 "M"
}

num = (input("Enter a number:"))

result = ""

while (num > 0):
    
    if len(num) == 4:
        divider = 1000
    elif (len(num) == 3):
        divider = 100
    elif len(num) == 2:
        divider = 10
    
    if num >= 1000: 
        
        #Determine how many 1000s are there and put that many M's in the final result
        #For the remaining number process as below
        # get % of number
        modval = num % divider
        #lookup and get the roman value for divider
        roman = lookuptable[divider]

        for _ in range(modval):
            result = result + roman
    
        num = num // divider

        #look up hash table and get the corresponding value for the key
        #Before appending check if num > 500

    elif num >= 500 and num < 1000:
        num1 = num - 500
            #process the reminaing number 
        pass
    elif num >=  400 and num < 500:
        # Get the Roman for 400 and process the remaining
        pass 
    elif num >= 100 and num < 400:  
        # Get the Roman corresponding to 100
        # determine how many 100s are there using % and //
        # process the number
        pass

    elif num >= 50 and num < 100:
        #Get the Roman corresponding to 50 
        # process the number
        pass

    elif num >= 40 and num < 50:
        pass

    elif num >=10 and num < 40:
        pass

    elif num>=5 and num < 10:
        pass

    elif num == 4:
        # get roman = IV
        pass

    elif num >=1 and num < 4:
        #Get Roman for 1, I
        #process number of 1s and introduce that many I

    else:
        print("Enter a valid number")

       

