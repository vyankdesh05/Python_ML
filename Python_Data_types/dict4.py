data = {"Even" : [2,4,6,8], "Odd" : [1,3,5,7], "Other" : [11.5,21.5,51.5]}

print(data["Even"][0])

for keys in data:
    print(keys)
    for i in data[keys]:
        print(i)

print("Data by new for loop")

for keys in data:
    print(keys, end = "")
    for i in range(len(data[keys])):
        print(data[keys][i], end = " ")
    print(" ")