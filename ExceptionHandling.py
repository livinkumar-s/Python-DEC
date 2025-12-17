print("Step1")
print("Step2")
print("Step3")

print("Final Step")

# print(8/0)
# try:
#     print(int("Hello"))
#     print("hello"+1234)
# except TypeError:
#     print("invalid type")
# except ValueError:
#     print("invalid conversion")

# print(int("Hello"))

# try:
#     print(9/0)
# except ZeroDivisionError:
#     print("Invalid Expression")

try:
    inp1=int(input("Enter Number1: "))
    inp2=int(input("Enter Number2: "))
    print(inp1/inp2)
except ZeroDivisionError:
    print("Invalid Expression!")
except ValueError:
    print("Invalid value")
finally:
    print("Final Step")


print("Something")

if True:
    print("Hello")