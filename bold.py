
'''
This world comprises of small world where world world world is smaller,, 
bold world,, then out put is This <b>world</b> comprises of small <b>world</b> 
where <b>world world</b> is smaller

This world comprises of small world where world world world is smaller,, 
bold world,, then out put is This <b>world</b> comprises of small <b>world</b> 
where <b>world world</b> is smaller --- 
'''
import os
import sys
import numpy as np
#Read the contents into an array


def bolding (string_arr, substring):
    try:
        stop_tracking = False
        tracking = 0
        stoptracking = False
        new_head = None

        for i in range(len(string_arr)):
            if substring in string_arr[i] :
                #start tracking indexes
                tracking = i
                if (new_head):
                  tracking = new_head

                for j in range(tracking+1, len(string_arr)):
                    if substring in string_arr[j]:
                        print (f"Debug1::String {string_arr[j]} matched")
                        test = '<b>'+substring+'</b>'
                        print (f"Debug_test:: {test} ")
                        continue
                    else:
                        #print ("From else j=",j)
                        print (f"Debug2::String {string_arr[j]} ")
                        stop_tracking = j-1
                        if ( j - tracking == 1):
                            string_arr[tracking] = '<b>'+substring+'</b>'
                            print (f" Replaced string1: {string_arr[tracking]}")
                        else:
                            print ("Inside mass bolding")
                            string_arr[tracking] = '<b>'+substring 
                            string_arr[stop_tracking] =  substring+'</b>'
                            new_head = stop_tracking + 1
                            #print (f" Replaced string2: {string_arr[tracking]}")
                            #print (f" Replaced string2: {string_arr[stop_tracking]}")
                       
                          #stoptracking = True
                        #stop tracking and exit from this internal loop
                        break
                
                #if (stoptracking):
                    # Bold <b> from i to j
                    #print (f"tracking, stop_tracking == {tracking}, {stop_tracking}")

                    #if (tracking == stop_tracking):
                        #string_arr[tracking] = '<b>'+substring+'</b>'
                        #print (f" Replaced string1: {string_arr[tracking]}")

                    #else:
                        #print ("Inside mass bolding")
                        #string_arr[tracking] = '<b>'+substring 
                        #string_arr[stop_tracking] =  substring+'</b>'
                        #new_head = stop_tracking + 1
                        #print (f" Replaced string2: {string_arr[tracking]}")
                        #print (f" Replaced string2: {string_arr[stop_tracking]}")
            else:
                print(f"String didnt match main else {string_arr[i]}")
                continue



        print (f" Replaced string: {string_arr}")

    except Exception as e:
        raise Exception (e,sys)

string_arr = []
string_input = input ("Enter the string and sub string:")
string_arr = np.array (string_input.split())
print (len(string_arr))
#Process the array and start searching the string match

# Do string match with array element with string, 
# if there is a match set a flag - Keep track of the starting index value continue the loop
# Check the next array element 
# If next element is different then replace the words starting from tracking index and upto the stop tracking index-1 with <b> and </b>
substring = 'world'
bolding(string_arr , substring)