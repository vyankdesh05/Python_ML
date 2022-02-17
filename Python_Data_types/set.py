data = {10,20,30,40}
mylist = [10,20,30,40]

print("Datatype is : ",type(data))
print("Length is : ",len(data))
print("Data from set : ",data)
print("Dats from list : ",mylist)

# print(data[0])

print("Data traversal using loop")
for no in data:
    print(no, end = "  ")

data1 = {10,20,30,40,10}    # duplicate elements are allowed but stored only once

print("New set is :", data1)

data2 = {10,20,30.5,"Hello",True}

print(data2)