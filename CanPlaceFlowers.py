'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

fb = [0,0,0,0,1]
n = 2

EMPTY = 0
NOT_EMPTY = 1  
# iterate over the array 
# maintain 3 states, a[n-1], a[n] and a[n+1]
# if a[0]  is Allowed then consider consider only a[1] should be empty
# simliarly if a[lenth of array] is allowed then only a[n-1] should be empty

# Keep another copy of the fb for reference and update.
fb_ref = fb
FB_ALLOWED = False
l = len(fb)

while (n > 0):
    i_ref = 0
    i = 0
    for i in range(len(fb)):
        if fb[i] == EMPTY:
            # if array index is 0 then check only current_index+1 and n value to determine Allowed or not. 
            if (i == 0 and fb[i +1] == EMPTY) or (i == l-1 and fb[i-1] == EMPTY):
                FB_ALLOWED = True
                fb_ref[i] = NOT_EMPTY
                print (f"Updated after checking first and last New Plot {fb_ref}") 
            elif ( fb[i+1] == EMPTY and fb[i-1] == EMPTY) :
                FB_ALLOWED = True
                fb_ref[i] = NOT_EMPTY
                print (f"Updated fb for i+1 {fb_ref}") 
                # else check i-1, i and i+1 th element and n value to determine allowed or not.
                # if allowed update the reference copy with new information. 
            #elif fb[i] == NOT_EMPTY:
            #    pass
        i_ref = i_ref + 1
    n = n-1

print (f"New Plot {fb_ref}")
if (FB_ALLOWED):
    print (f"New Plot {fb}")