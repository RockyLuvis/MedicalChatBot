'''
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100


'''


tasks = ["a", "a", "a", "b", "b", "b"] 
wait_time = 6

result_list = []
temp_list = []

#Save the Scheduling order (may not be needed we will see later)
temp_list = tasks

tracker = 0
counter = 0
i = 0

while (tasks):

    #Get the count of, number of times cpu task occurs in the list for ex a :3 b:3 c:2 etc
    print (f"DEBUG: i= {i}")
    cpu_task = tasks[0]
    print (f"DEBUG: cpu task {cpu_task}")
    count = tasks.count(cpu_task)
    print (f"DEBUG: count = {count}")
    
    #Allocate memory upfront to handle tasks[i]
    if (tracker == 0):
        for i in range(2 * (wait_time + 1) + 1):
            result_list.append(None)
    else:
        result_list.append(None)

    counter = tracker
    j = 0
    
    while (j < count):
        #Populate the Result list
        #If list is empty then populate the initial scheduling map
        
        if not result_list:
            result_list[j] = cpu_task

        elif (result_list[counter-1] != cpu_task and result_list[counter] is None):
            result_list[counter] = cpu_task
        # Dont schedule anything till the wait time
            
        counter = counter + wait_time + 1

        j = j+1
   
    # Now I have to remove all occurances of tasks[i] from the tasks array
    # so that we handle only other CPU tasks
    for _ in range (count):
        tasks.remove(cpu_task)
    
    #initialize i to start of the list
    tracker = tracker + 1 
    print (f"tasks array: {tasks}")
    print (f"result list array: {result_list}")
    temp_list = result_list.copy()

print ("Output",len(result_list))

    













