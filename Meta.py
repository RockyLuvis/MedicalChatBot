'''
Build a hash like reding 3 files

my_hash = {
    "chicken": ["2", "file1", "file2"],
    "pig": ["3", "file1", "file2", "file3"],
    "goat": ["1", "file1"]
}
'''
import os
import sys
from pathlib import Path
my_hash = {}

files = ["file1", "file2", "file3"]

def getduplicates(files):

    a_count = 1

    for file in files:
        filepath = Path(file)
        with open(filepath, 'r') as f:
            for line in f:
                my_key = line.strip()
                if my_key in my_hash:
                    my_hash[my_key][0] += 1
                    my_hash[my_key].append(file)
                    #print (my_hash)
                else:
                    my_hash[my_key] = [(a_count), file]
                    #print (my_hash)
    
    #Sort only the number in dec order
    #print (my_hash.items())
    sorted_items = sorted(my_hash.items(), key=lambda item: item[1][0])
    print (sorted_items)
    i = 0



    for item in sorted_items:
        my_key = item[i]
        values = item[i+1]

        print ("mykey =",my_key)
        if (values[0] == 1):
            print (f" {my_key} has occured {values[0]} time in file {values[1]}")
        else:
            print (f" {my_key} has occured {values[0]} times in files {values[1:]}")







getduplicates(files)
