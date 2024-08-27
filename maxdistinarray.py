'''
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
'''

result = []
input_array = [[1,2,8],[4,5],[1,2,3],[5,7,3,2,1]]

def max_dist():
    try:
        if (len(input_array) == 0):
            raise Exception ("Input array cannot be empty")
        i=0
        while i < (len(input_array)-1):

            first = input_array[i].copy()
            f_min = min(first)
            f_max = max(first)
            j = i+1
            while j < len(input_array):

                second = input_array[j].copy()
                s_min = min(second)
                s_max = max(second)
                result.append(abs(f_max - s_min))
                result.append(abs(f_min - s_max))
                j = j+1
          
            #for x in range(len(first)):
            #    for y in range(len(second)):
            #        dist = first[x] - second[y]
            #        result.append(abs(dist))
            
            i=i+1
        print(result)
        m = max (result)
        #result1 = sorted(result, reverse=True)
        print ("m=",m)     
    except Exception as e:
        raise Exception (e)
    
max_dist()