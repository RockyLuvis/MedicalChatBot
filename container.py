'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''
height = [6,8,1,9,5,2,7,3,4]
# have two trackers, front and rear
front = 0
rear = len(height)-1
print ("rear =", rear)
largest_vol = 0
for _ in range(len(height)):
# get the distance between the two , which is len(height)
    dist = abs(rear - front)
# Now use the formula , min(height[front],height[rear]) * dist to calculate area
    vol = min( height[front], height[rear]) * dist
    
# Store area for comparision
    if largest_vol < vol:
        largest_vol = vol
# Determine which among height[front], height[rear] is smaller
    if height[front] <= height[rear]:
        front = front + 1
    else:
        rear = rear - 1
# move the pointer pointing to rear inwards
# repeat the process 
# Finally print/return the largest area
print("largest_vol = ",largest_vol)

