import random
print(random.randrange(1,9))
a=2+3j
txt = "My name is Ståle"
x=txt.encode()
print(x)
txt = ",,,,,rrttgg.....banana....rrr"
x=txt.strip(",rt.gan")
print(x)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
del mylist[1]
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
del mylist[1]
print(thislist)

thislist=list({a:"b"})
print(thislist)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
print(y)



