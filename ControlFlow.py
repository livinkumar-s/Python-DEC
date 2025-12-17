# print("Step1")
# print("Step2")
# print("Step3")

# inp=int(input("Enter age: "))

# if inp>=18:
#     print("Can vote") #age>=18
# else:
#     print("Cannot vote") #age<18


# Conditional Clause

# a=10
# b=20

# if a>b-15 and a>b:
#     print("Step1")
#     print("Step2")
#     print("Step3")
# else:
#     print("From else Block!")

# print("Final Step")

# num = int(input("Enter a number: "))
# if num & 1 == 0:
#     print(num, "is Even")
# else:
#     print(num, "is Odd")

# a=10

# if a>12:
#     print("From If block!")
# elif a>12:
#     print("From Elif1 block")
# elif a==12:
#     print("From Elif2 block")
# else:
#     print("From Else block")

# mark
# 90-100 --> O
# 80-89--> A+
# 70-79--> A
# 60-69--> B
# 50-59--> C
# 0-49 --> Fail

# mark = int(input("Enter a Number: "))
# if mark>90 and mark <=100:
#           print("O Grade")
# elif mark>80 and mark <=90:
#          print ("A+ grade")
# elif mark>70 and mark <=80:
#          print ("A grade")
# elif mark>60 and mark <=70:
#          print ("B grade")
# elif mark>50 and mark <=60:
#          print ("C grade")
# else:
#         print("Fail")

# a=int(input("Enter a Number: "))

# if a>10:
#     if a>15:
#         print("Very large!")
#     else:
#         print("Large")
# else:
#     if a<5:
#         print("Very small!")
#     else:
#         print("Small")


# Loops 
# x=0

# while x<5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("----------------")
#     x-=1

# iteration count -->1,2,3,4,5
# x --> 0,1,2,3,4,5

# a="Hello guys.. i am from tamilnadu...! welcome to the session"

# print(a[4])
# print(a[4])
# print(len(a))

# a=range(100)
# print(list(a))

# str="helloworld"

# print(len(str))

# for i in range(100):
#     print(i)
#     print("-----------")

# for i in range(1,10):
#     print(i)

# for i in range(5,50,7):
#     print(i)

# for i in range(1000,0,-1):
#     print(i)

# i=0

# while i<10:
#     print(i)
#     if i==7:
#         break
#     i+=1

# print(i)

# for i in range(51):
#     if i==25:
#         continue
#     print(i)

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("guru")
#     elif i%3==0 or i%5==0:
#         continue
#     else:
#         print(i)

# for i in range(100):
#     print("Hello world")

# secret_number=77

# while True:
#     num=int(input("Guess the number: "))
#     if secret_number==num:
#         print("You won!")
#         break
#     else:
#         print("Try again!")



# print("* ")
# print("* * ")
# print("* * * ")
# print("* * * * ")
# print("* * * * * ")

# len=40

# for i in range(len):
#     print("* "*(i+1))

# for i in range(6):
#     for j in range(6):
#         print("*", end=" ")
#     print()

len=50
#10*10

for i in range(1,len+1): #(1,2,3,4,5)
    for j in range(1,len+1):
        if i==1 or i==len or j==1 or j==len:
            print("* ",end="")
        else:
            print("  ",end='')
    print()
    

#i=1
#j=1,2,3,4,5
#i=2
#j=1,2,3,4,5
#i=3
#j=1,2,3,4,5
#i=4
#j=1,2,3,4,5
#i=5
#j=1,2,3,4,5

# print("Hello",end="")
# print("Hello")
# print("Hello")