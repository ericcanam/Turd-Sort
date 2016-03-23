import random
array = [i for i in range(0, 10)]
random.shuffle(array)
sister = [None for i in range(0, len(array))]
a = 0
print("Would you like to sort the default array, "+str(array)+"?")
print(" (type 'yes' to use it, or 'no' to define your own [in case you don't trust me])")
da = input(" -> ")

while da.lower()!="yes" and da.lower()!="no":
    print("sorry, that prompt was not recognised.")
    print("Would you like to use the array, "+str(array)+"?")
    print(" (type 'yes' to use it, or 'no' to define your own)")
    da = input(" -> ")

if da.lower()=="no":
    array = []
    print("type an integer to add it to the list, or anything else to stop adding to the list")
    while True:
        iv = input(" -> ")
        if (iv.startswith('-') and iv[1:].isdigit()) or (iv.isdigit()):
            array.append(int(iv))
        else:
            break
    print("your new array is: "+str(array)+".")
    sister = [None for i in range(0, len(array))]
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
print("your sorted array is: "+str(sister)+".")

input("press any key to escape");