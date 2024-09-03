dividend = 10
divisor = -3

# Error check to make sure divisor is not zero
# raise value error if zero
if divisor == 0:
    raise ValueError ("Divisor cannot be zero")

# Error check to make sure divisor is integer
if not isinstance(divisor,int):
    raise TypeError ("Divisor has to be Int")

# Loop through n time and check if sum <= diviend
mysum = 0
count = 0

if (dividend == divisor):
    count = 1

neg_flag = False

if divisor < 0 or dividend < 0:
    neg_flag = True

if divisor < 0 and  dividend < 0:
    neg_flag = False

divisor = abs(divisor)
dividend = abs(dividend)

while(mysum <= dividend):
    print ("Inside while")
    mysum = mysum + divisor
    if mysum <= dividend:   
        print ("sum=", mysum)
        count = count + 1
    else:
        print ("Divident is less than divider")
        break
if neg_flag:
    print ("Division=", -count)
else:
    print ("Division result:",count)
