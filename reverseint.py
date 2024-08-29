x = -123
result = []
digit = 0
if x < 0:
    negative = True

x = abs(x)
while (x > 0):
    # Get numbers from the interger via %
    digit = int(str(digit) + str(x % 10))
    #now remove the last number from x
    newx = x//10
    x = newx
    print ("x=",x)
print (digit)

if negative:
    digit = '-' + str(digit)
print ("negative digit=", digit)