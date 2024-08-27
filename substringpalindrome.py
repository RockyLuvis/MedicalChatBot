mystring = "babad"
print (len(mystring))
result = []

i = 0
count = 0
temp = ""

#while ( i< len(mystring) ):
for i in range(len(mystring)):

  if (len(mystring) == 1):
    print("Only one character string ")
    #return
  else:
    # Concatenate next character to temp
    temp = temp + mystring[i]
    print (f"DEBUG: Concatenated sub string = {temp}")
    temp_len = len(temp)
    # now iterate temp_len times taking each time one less character from front.
    # Skip the first iteration
    if temp_len == 1:
      print ("Fetch the next character")
      continue
    else:
      # Perform iterated serach for all characters
      for k in range(temp_len):
        my_sub = temp[k::]
        #reverse my_sub
        print (f"DEBUG: sliced sub string = {my_sub}")
        if (len(my_sub) != 1):
          my_sub1 = my_sub[::-1]
          print (f"DEBUG: Reversed sub string = {my_sub1}")
          if my_sub == my_sub1:
            print ("Palindrome {mysub}")
            result.append(my_sub)
            my_sub = ""

  print (f"Result = {result}")

final_result = max(result, key=len)
print (len(final_result))
print (f"largest substring Palindrome = {final_result}")
