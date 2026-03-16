# def add():
#     return 5+3
# result=add()
# # print(result)

# def add(a,b):
#     return a+b
# print(add(10,20))

# def calculation(a,b):
#     return a+b,a-b,a*b
# x,y,z=calculation(10,5)
# print(x)
# print(y)
# print(z)


# def example():
#     print("hello")
#     return
#     print("world")
# example()

# def simple_interset(p,r,t):
#     si=(p*r*t)/100
#     print(si)
#     return si
# simple_interset(20000,12,2)

# def func(a="amit"):
#     print("hello",a)
# func("aman")

# def fun(a,b):
#     print(a+b)
# fun(12,34)

# keyword argument
# def student(name,age):
#     print(name,age)
# student(age=18,name="amit")

# def add(*numbers):
#     print(sum(numbers))
# add(5,10,56,47)

# def student (**details):
#     print(details)
# student(name="amit", age=21,city="Delhi")
# def f(a,b):
#     print(a*b)
# f(3,10).........positional argument

# 2. reate a function student(name, course) and call it by passing values in correct order.
# def student(name, course):
#     print(name,course)
# student(21,"amit")
# Write a function area(length, breadth) and calculate the area of a rectangle.
# def area(lenght,breadth):
#   print(lenght*breadth)
# area(12,23)

# printing the * pattern
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     print("*"*i)

# n=3
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1))
# ***
# * *
# ***
# n=3
# for i in range(1,n+1):
#     if(i==1 or i==3):
#         print("*"*n)
#     else:
#         print("*"+" "*(n-2)+"*")


n=int(input("enter the number: "))
for i in range(10,0,-1):
 print(f"{n}X{i}={n*i}")