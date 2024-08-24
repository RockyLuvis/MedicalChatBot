

input_list = [8,8,3,3,6,9,2,3,1]

#Detect duplicates and seperate non duplicates
test_list = []

count = 0

for i in range(len(input_list)):
    for j in range(len(input_list)):

        if (input_list[i] == input_list[j]):
            count = count + 1
        else:
            pass
    print ("DEBUG:count =",count)
    if (count > 1):
        #skip as number occurs more than once
        count = 0
        continue
    else:
        test_list.append(input_list[i])
        count = 0
test_list = sorted(test_list, reverse=True)
print ("test_list:", test_list[0])
#Sort the non_dupliates list and return top of 