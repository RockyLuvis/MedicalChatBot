#my_hash = {'rr': '8.9', 'uu': '9.1', 'ee': '8.7', 'wsd': '7.8', 'oo': '9.0', 'jk': '7.9'}
my_hash = {}
test = []
i=0
while (i < 2):
    try:
        key = input ("Enter key:")
        value = input ("Enter value:")
        i = i+1
        
        my_hash[key] = float(value)
    except Exception as e:
        print (e)
        continue

print (f"my hash: {my_hash}")
#test = sorted(my_hash.values(), reverse=True)
#print (test[0])
       