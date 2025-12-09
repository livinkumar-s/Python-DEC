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

a=int(input("Enter a Number: "))

if a>10:
    if a>15:
        print("Very large!")
    else:
        print("Large")
else:
    if a<5:
        print("Very small!")
    else:
        print("Small")