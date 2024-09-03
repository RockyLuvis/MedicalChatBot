nums = [2,2,2,2,3,2,2,3]
val  = 2

length = len(nums)
print (length)
j = 0
#nums = [i for i in nums if i != val]
i = 0
while i < len(nums):
    if (nums[i] == val):
        nums.remove(val)
        #i = i - 1
    else:
        i = i +1

print (nums)