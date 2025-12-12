# a="Hello world"
# a[4]='h'

# print(a[-3])

# print(a[-4:])
# print(a[:6]) --> 0,1,2,3,4,5
# print(a[2:9]) --> 2,3,4,5,6,7,8
# print(a[::-1])

# List 

# a=[1,2,-3,-4,"five","six","seven",True,False]

# print(a[:6]) #-->0,1,2,3,4,5
# print(a[2:]) #--> 2,3,....final

# a[4]=5

# print(a)


# lis1.append(100)
# lis1.append(101)

# lis1.extend(range(51))
# lis1.insert(4,"Fuzz")

# lis1.pop(3)
# lis1.pop()
# lis1.pop()
# lis1.pop()

# lis1=[43,546,43,56,4,76,45,87,8,87,99]

# print(lis1[::-1])
# lis1.reverse()
# print(lis1)

# lis1.remove(87)
# lis1.sort()
# lis1.reverse()

# print(lis1)

# print(lis1.count(7))

# print(lis1.index(4))

# Tuple

tup1=(1,2,3,4,5,6,7,8,7,6,5,4,3)

# print(tup1[0])

# tup1[1]=100

# print(tup1.count(3))
# print(tup1.index(3))

person1=("Kelly",32)

# name=person1[0]
# age=person1[1]

name,age=person1
print(name)
print(age)

# Set 

set1={1,2,3,4,5,6,5,4,3,2,1}
set2={6,7,8,9,10,11,12,13}
# set1.add(99)
# set1.remove(6)

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))

# Dict 

# print(person1["name"])

# person1["age"]=43

# person1["Mother name"]="Prafulla Shetty"

# print(person1)



# print(person1.keys())
# print(person1.values())
# print(person1.items())

# person1.pop("age")
# person1.clear()
# print(person1)

# a={56,65,78,89}
# b=list(a)
# print(b[2])

# a=[23,24,43,546,76,54,43,546,76,4,54,56,4,3,2,3,4,5]
# b= list(set(a))
# print (b)

# person1={"name":"Anushka shetty", "age":44, "isMarried":False}
 
# for i in person1:
#     print(person1[i])

lis1=[1,
      2,
      3,
      [4,
       5,
       6,
       ["seven",
        "eight",
        ["nine",
         "ten"]]]
      ]
# print(lis1[3][3][2][1])
print(lis1[-1][-1][-1][-1][-1])