#Merege 2 arrays and return median of the final array

list1 = [1,4,5,6]
list2 = [1,8,7,9]

list4 = list1 + list2
s_l = sorted(list4)
print(list4)

mid = len(s_l)//2
print ("mid", mid)

if ((len(s_l) % 2) == 0):
   print ("Median =", (s_l[mid]))
else:
   print ("Median =", (s_l[mid] + s_l[mid+1]) // 2)


#Partion algorithm
# use i and j counters
# Determine smallest of the two lists
# Start working on the smallest list 
# i = 0 and j = m+n+1/2-i, where m is len(list1) and n is len(list2)
# and compare now the i is partion index of l1 and j is partion index of l2
# if (l1[i-1] <= l2[j] and l2[j-1] <= l1[i]) then change partiion increment i and calculate j, repeat the same comparison
#
# until len(l1) and return max(l1) as median

list1 = [1,4,5,6]
list2 = [1,8,7,9]

if len(list1) > len(list2):
    print("DEBUG: Ensure list1 is smaller")
    list1, list2 = list2, list1

# no one list1 is smallest
# m is length of list1
m = len(list1)
n = len(list2)

for i in range (m):
    i = (m + i)//2
    j = (m + n + 1)//2 - i

    print ("DEBUG: i and j",i,j)

    if (list1 [i-1] <= list2[j]):

        

    elif ( list2[j-1] <= list1[i] ):
        #Return max(list1) as median
        #print("Found Median")
        break
    else:
        continue
        
    



