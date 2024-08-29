s = input("Enter chracter:")
p = input("input a pattern:")

#remove all leading spaces
s1 = s.strip()
i=0

if s1[0] == '*':
    print("DEBUG: Return cannot start with * Error")

if p[0] == '*':
    print("DEBUG: Return True as matching string starts with *")

#print (s1)
if s1 == p :
    print ("Match")
if '.*' in p:
    print("DEBUG: Return true")
else: #handle abc* match
    for c in p[i::]:
        print (f"printing {c}")
        if c == s1[i]:
            i = i+1
        elif c == "*" and i>1:
            print ("Continue to check for c after c")
            print ("DEBUG: matched as string has few chars of matching pattern and * at the end ")
    
    for m in s1[i-1::]:
        if m == p[i-1] #check to make sure remaining characters after * match with character preceeding *
            match = True
        else:
            match = False
    if (match):
        print("Matched")
'''
#print(int(s1))
i=0
if s1[0] in '+-':
    i = i+1
   

for c in s1[i::]:
    if c.isdigit() :
            i = i+1
    else:
        print(s)
        print(int(s1[0:i:].strip()))

'''