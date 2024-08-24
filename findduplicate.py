
import os
from pathlib import Path
import hashlib

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    # Create a hash object using the specified algorithm
    hash_func = hashlib.new(hash_algorithm)

    # Open the file in binary mode and read it in chunks
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)

    # Return the hex digest of the hash
    return hash_func.hexdigest()



def findDuplicateFiles():
    # From the base path get a list of all paths for the filename
    file_path = []
    for root, dirs, files in os.walk ("."):
        for name in files:
            if name == 'a.txt':
                file_path.append(os.path.join (root, name))

    print (file_path)

    Duplicate_file_list = {}
    #from the list of file_path hash for each file
    for file in file_path:
        #print (f'processing file: {file}')
        hash_value = calculate_file_hash(file)

        if (hash_value in Duplicate_file_list ):
            print ("step2 -> adding file to hash")
            Duplicate_file_list[hash_value].append(file)
        elif(len(Duplicate_file_list) == 0 or hash_value not in Duplicate_file_list):
            print ("step1 -> adding file to empty hash")
            Duplicate_file_list[hash_value] = [file]
        else:
            continue

            
    print (Duplicate_file_list.items())


    #Compare the hash, if <hash> in list
    # If hash are equal then append only those matching paths into a seperate list
    # Now prompt the user of matching path and ask if which to delete
    for hashvalue, path in Duplicate_file_list.items():
        if (len (path) > 1):
            for file in path:
                print ('Duplicate file path: ', file)

findDuplicateFiles()