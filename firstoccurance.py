haystack = "sadbutsad"
needle = "sadi"

nums = haystack.count(needle)
print ("nums=",nums)

try:
    if nums == 0:
        raise ValueError (f" {needle} is not in Haystack")
    else:
        ind = haystack.index(needle)
except Exception as e:
    print (e) 
    ind = -1

print ("ind=",ind)
