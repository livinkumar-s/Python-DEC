# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")

# printSteps()
# printSteps()

# def addVal(a,b):
#     print(a+b)

# addVal(8,9)
# addVal(90,80)

# print(10)

# def greaterOne(a,b):
#     if a>b:
#         print("a")
#     else:
#         print("b")

# greaterOne(100,101)
# greaterOne(b=70,a=100)


# def mulVal(a,b=20):
#     print(a*b)

# mulVal(10,60)

# def steps():
#     print("Started")
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     return 67
#     print("Step4")
#     print("Step5")
#     print("Final Step")


# print(steps())

# def multiply(a,b):
#     return a*b


# print(432)

# a=input("Enter a number: ")
# print(a)

# check ---> num ---> odd, even 

# def check(num):
#     if num % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
# check(86)
 

# def sumNum(*a): # a--> variable length parameter
#     print(sum(a))


# sumNum(546,43,546,2,6,546,3)

# def collectData(**data):
#     print(data)

# collectData(name="Vijay",age=51,noOfMovies=68)


# Scopes

# a=10

# def func1():
#     a=15
#     print("The value of a from inside func1 is: ",a)


# func1()
# print("The value of a is: ",a)

def outer():

    print("Outer function")

    def inner():
        print("Inner function")
    inner()
    

outer()