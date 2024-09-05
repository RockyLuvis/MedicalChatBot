'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
from itertools import permutations
from itertools import combinations
#Every permutation of t has to be checked in the string s
s = "ADOBECODEBANC"
t = "ABC"
#perm_list = []

#perm = permutations("ABC")


#for i in perm:
#    i1 = "".join(i)
#    perm_list.append(i1)
#print (perm_list)
substr_list = []

for k in range(len(s)):
    substr = ""
    j = k
    found = 3
    for i in range(len(t)): 
        #print (f"i {i} and t[i] {t[i]}")
        while(found):
            #print (f" s[j] = {s[j]} and t[i] = {t[i]}")
            if j >= len(s):  # Avoid index out of range
                print (f"Breaking from {j}>= {len(s)}")
                break
            if (s[j] in t):
                found = found - 1
                #print (f"Found {t[i]}")
                #substr = substr + s[j]
                #break
            #else:
                #substr = substr + s[j]
            j = j + 1
            #print ("substr=",substr)
                   
    if found == 0:
        substr = s[k:j:]
        print ("k, j=",k, j)
        substr_list.append(substr)
    

print ("substr_list", substr_list)

'''
s = "a"
t = "a"

substr_list = []

# Iterate over all starting points in s
for k in range(len(s)):
    substr = ""
    j = k
    found = len(t)
    # Iterate over all characters in t
    for i in range(len(t)): 
        while found:
            if j >= len(s):  # Avoid index out of range
                break
            if s[j] in t:
                found -= 1
            j += 1
        if found == 0:
            substr = s[k:j]
            substr_list.append(substr)
            break  # Move to the next starting point

print("substr_list", substr_list)
substr_list.sort(key=len)

print ("substr_list =", substr_list[0])
'''



