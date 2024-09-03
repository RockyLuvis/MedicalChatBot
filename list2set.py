
import sys

def removeDuplicates(nums):

    try:
        if not all ( isinstance (x, int) for x in nums) :
            raise TypeError ("Input array has to int")
        if len(nums) <= 0:
            raise ValueError ("Input array cannot be empty") 
        ##################
        #solution1
        #myset = set(nums)

        #setlen = len(myset)
        #print ("length=",setlen)
        #mylist = list(myset)
        #print(mylist)
        ####################

        # Go through the loop using i an j

        k = 0
        for i in range(1,len(nums)):

            if nums[i] != nums[k]:

                nums[k] = nums[i]
                k = k+1

    except Exception as e:
        print (e)
        raise Exception (e, sys)
    return k, nums
    #return list(myset), setlen

nums = [0,0,1,1,1,2,2,3,3,4]
explist, length = removeDuplicates(nums)
print ("explist, length :", explist, length)