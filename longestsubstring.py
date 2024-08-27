mystr = "ababab"

strlen = len(mystr)
result = []
#cstr = ""
#result.append(mystr[0])

for i in range(strlen):

    #Check if substr1 is same as result
    substr = mystr[i]
    if (len(result) == 0):
        result.append(substr)
        continue
    else:
            #Push the one character subtstring.
            print ("substring =", substr)
            result.append(substr)
            #Get the previous substrings from Result list for concetenation
            # Get i positions strings from result to concatenae and push to result
            #Also make substring2 is not in one of those ith behind position strings in result array
            k = i
            print("k,i=",k,i)
            tracker = k+1
            resultlen = len(result)
            print ("tracker=",tracker)
            for j in range (k):
                print("j=",j)
                print ("resultlen=", resultlen)
                substr_temp = result [resultlen - tracker]
                tracker = tracker - 1
                if ( substr not in substr_temp):
                    cstr =  substr_temp + substr
                    result.append(cstr)
                #Also concatenate with last contenated result
            print("Result=",result)
                # and push substr2, cstr and last concatenated result
                #resultlen = len(result)
                #lcstr = result[resultlen] + substr2
                #result.append(substr2)
                #result.append(cstr)
                #result.append(lstr)
l_len = max(result, key=len)
print("largest len=", len(l_len))
            

        


