# try:
#     a= int("aman")
#     print(a)
# except ValueError:
#     print("Value error occurred")
# try:
# #  a=5 / 0 
#  b=int("abc")
# #  print(a)
#  print(b)
# except ZeroDivisionError:
#  print("cannot divide by zero!")
# except ValueError:
#  print("invalid conversion to int!")

# try:
#  input_user=int(input("enter number: "))
#  print("you entered the number")
# except:
#  print("value is not an integer")

# try:
#  a=int(input())
#  b=int(input())
#  print("div=",a/b)
# except ZeroDivisionError:    
#  print("you are entering a zero divident entity")
# except ValueError: 
#  print("invalid entry entered by the user")
# else:
#  print("thanks")


# q3
# try:
#  l=[12,3,4,44,55]
#  print(l[54])
# except IndexError:
#  print("index is not found")
# else:
#  print("thank you")

# 4 Handle KeyError when accessing a missing key in a dictionary.
# try:
#     s={1:"amit",2:"aman"}
#     print(s[3])
# except KeyError:
#     print("value is missing")
# else:
#     print("thanks ")

# 5 Write a program that opens a file and handles FileNotFoundError
# try:
#     f = open("data.txt", "r")   
#     print(f.read())            
#     f.close()
# except FileNotFoundError:
#     print(" File not found")
#
#try:
#  num=int(input("enter a number: "))
#  a=[6,3]
#  print(a[num])
# except ValueError:
#  print("number entered is not an interger")
# except IndexError:
#  print("index error")


# handling a key error''
# try:
#     a=(input("enter a value: "))
#     key={"amit":1,"amir":2}
#     print(key[a])
# except ValueError:
#     print("enter value is not available")

# Write a program that opens a file and handles FileNotFoundError
# try:
#  f=open("data.txt")
#  data=f.read()
#  print(data)
#  f.close()
# except FileNotFoundError:
#  print("no record found")

# Use try-except-else to divide two numbers
# try:
#  a=int(input("enter the number: "))
#  b=int(int(input("enter second nubmer: "))) 
#  if  b==0:
#   print("you are entering a wrong value",ZeroDivisionError)
#  else:
#      print("division of two nubmers is: ", a/b)
# except ValueError:
#   print("please enter a valid integer only")

# # Use try-except-finally and show that finally always runs
# try:
#     a=int(input("enter the number: "))
#     b=int(input("enter the number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("you entered an invalid number")
# except ValueError:
#     print("you enterd invalid value")
# finally:
#     print("thanks")

# Take user input and convert to integer. If invalid, print "Invalid Input"
# try:
#     a=(input("enter something:  "))
#     b= int((a))
#     print(b)
# except ValueError:
#     print("you enter wrong id")

# Handle multiple exceptions in one except block
# try:
#     a=int(input("enter the number: "))
#     b=int(input("enter the number: "))
#     c=a/b
#     print(c)
# except(ZeroDivisionError,ValueError):
#     print("invalid format") 
# finally:
#     print("thank you for your time")

# Write a program that catches any exception using Exception
# try:
#     a=(input("enter a number: "))
#     print(int(a))
# except Exception as e:
#     print("some error occured",e)

# intermediate level
# calcultor program that handle erroe value and zero division
# try:
#     operator=int(input("enter an operator(+,-,*,/,%): "))
#     num1=float(input("Enter the number: "))
#     num2=float(input("enter second number"))
                 









def greet():
    print("hello")
a=greet
a()


def greet():
    print("hello")
def aaa(func):
    func()
aaa(greet)


def greet(name):
    return f"hello,{name}"
say_hello=greet
print(say_hello("principle"))


def square(x):
    return x*x
def operate(func,num):
    return func(num)
print(operate(square,5))


































    
    

