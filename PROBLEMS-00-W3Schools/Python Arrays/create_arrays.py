from array import *
vals = array('i', [5,6,4,7,2,-5])

print("List : ", vals, "which is ", type(vals))


print(vals)
print(vals[2])

for loop in vals:
    print("From For : ", loop)

for loop in range(4):
    print("Range : ", loop)