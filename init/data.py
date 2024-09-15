# List
# myList=["apple", "house","formula", "house"] #ordered, changeable, duplicate values
# myList.append("Monalisa")
# print(len(myList))
# print(type(myList))
# print(myList.sort())

# myList[1:3]=["garlic", "watermelon"]
# print(myList)
# # myList.remove("house")
# # myList.remove("Monalisa")
# print(myList)
# # newlist=[]
# # for x in myList:
# #     if "a" in x:
# #         newlist.append(x)
# # print(newlist)

# newlist=[x for x in myList if "a" in x]
# newList= [x.upper() for x in myList if x != "garlic"]
# print(newList)

# listNum=[x for x in range (10)]
# print(listNum)
# listNum.sort(reverse=True)
# print(listNum)

# thirdList= myList.extend(listNum)
# print(thirdList)



# myList.pop(1)
# del myList
# print(myList)


# for x in myList:
#     print(x)
#     if x == "formula":
#         continue
#     print(x)

# for num in range(10):
#     for number in range(10):
#         print(num, number)

# for x in myList:
#     pass
    
# Tuples
myTuple=("apple", "house", "formula", "House", "doctor") #ordered, unchangeable, duplicate values
# print(myTuple)
# print(len(myTuple))

# newTuple=("apple",)
# print(myTuple[1:5])

# tupleList=list(myTuple)
# print(tupleList)
# tupleList[1]="berry"
# newTuple=tuple(tupleList)
# print(newTuple)

# mulTuple=newTuple * 2
# print(mulTuple)
# print(myTuple.index("house"))
# (u,v,w,x,y)=myTuple
# print(u)
# print(v)
# print(w)
# print(x)
# print(y)


# #Set
# mySet={"apples", "house", "cherry", "house", "cherry"} #unordered, unchangeable(remove and add), unindexed
# newSet={"Pine", "corn", "troops", "cherry"}
# # print(mySet)

# for x in mySet:
#     print(x)

# print("house" in mySet)

# mySet.add("Mercedes")

# # mySet.update(myTuple)
# # print(mySet)
# set3= mySet - newSet
# print(set3)





# mySet.remove("Mercedes")
# print(mySet)
# x =mySet.pop()
# print(x)

# #Dictionary
myDict={
    "brand1": {
   "name":"nivea",
    "category": "colonge",
   "year": 1950
    },
    "brand2": {
   "name":"Zito",
    "category": "Puppy soap",
   "year": 1960
    },

     "brand3": {
   "name":"paracetamol",
    "category": "medicine",
   "year": 1990
    },
  } #ordered, changeable and don't duplicate values

print(myDict["brand3"]["name"])

for val, obj in myDict.items():
    print(val)

    for item in obj:
        print(item + ' : ', obj[item])