import random
array = [i for i in range(0, 10)]
random.shuffle(array)
sister = [None for i in range(0, len(array))]
a = 0


print("Sorting: "+str(array)+".")
print("")

b = len(array)-1
d = len(array)-1
while True:
    if len(array)==0:
        break # we're done here
    print(str(sister)+", "+str(array))
    ma = array[0]
    mi = array[0]
    for c in array:
        if c>ma:
        	ma = c # new max
        if c<mi:
        	mi = c # new min
    if (not mi==array[0]) and (not ma==array[b]):
        random.shuffle(array)
        continue # nothing to see here

    if d-a==0: # there's just one
        sister[d] = array[0]
        break
    elif d-a==1: # just two left
        sister[a] = array[0]
        sister[d] = array[1]
        break
    if mi==array[0]:
        # min is there
        sister[a]=mi
        array.pop(0)
        a += 1
        b -= 1
    if ma==array[b]:
        # max is there
        sister[d]=ma
        array.pop(b)
        b -= 1
        d -= 1
print("")
print("Sorted: "+str(sister)+".")
