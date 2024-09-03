
#n! = n * n-1 * .. * 1
from itertools import permutations

words = [] #: 3! = 6
s = "barfoofoobarthefoobarman"

def substringpermutation(words, s):

    if words is None:
        raise ValueError ("words cannot be empty")
    
    if not isinstance(words, str) or not isinstance(s, str):
        raise TypeError ("words and str have to be string")

    #word_count = words.count
    perm_list = []
    perm = permutations(words)
    for p in perm:
        #print("".join(p))
        my_p = "".join(p)
        perm_list.append(my_p)

    print(perm_list)

    for n in perm_list:
        if n in s:
            print(f"permutation {n} is at index {s.index(n)}")
