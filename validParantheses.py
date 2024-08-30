
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
from collections import deque

expected = {
    "(": ")",
    "{": "}",
    "[": "]"
}


mystr = "a + ( b * { c-d} * [ d - (e*f)])"

strlen = len(mystr)
print ("strlen=", strlen)
myheap = deque()

#print ("myheap len=", len(myheap))
i=0

for c in mystr:
    
    print (f"DEBUG : got character {c}")
    if ( myheap is None and c == ")" and c == "}" and c == "["):
        print (f" String cannot start with {c} closed paranthesis")
    
    #elif(c == "(" or c == "{" or c == "["):
    elif c in expected:
        #Push to FIFO
        myheap.append(c)      
        print(f"Pushed : printing FIFO {myheap}")

    #elif ( c == ")" or c == "}" or c == "]"):
    elif c in expected.values():
        # Get the top of the FIFO
        top_fifo = myheap.pop()
        print(f"Poped : {top_fifo}")
        #Get the expected paranthesis from the hash for myhead[tracker]
        #check if tracking paranthesis is a match else fail
        e_paran = expected[top_fifo]
        #print ("DEBUG: e_paran", e_paran)
        if (c == e_paran):
            print (f"Pass: Found expected paranthesis {c} for {top_fifo} ")
            print (f"left in LIFO {myheap}")
        else:
            print (f"Fail: Incorrect paranthesis {c} received when {top_fifo} expected")

if (myheap):
    print (f"Still waiting for {myheap}")
else:
    print ("Found all closing paranthesis")


    
    
        