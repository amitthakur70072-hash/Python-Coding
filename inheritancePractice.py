# Create a class Student with a constructor that initializes name and age and prints them.

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# s1=Student("amit",21)


# Create a class Rectangle with a constructor that takes length and width and prints the area of rectangle.
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print(f"the area of rectangle is {self.length*self.width}")
# s1=Rectangle(12,23)
# s1.area()


# 3. create a class Employee with a constructor that takes name and salary.
# If salary is not provided, it should default to 30000.
# class Employee:
    
#     def __init__(self,name,salary=30000):
#         self.name=name
#         self.salary=salary

#     def Salaries(self):
#         print(f"the employee name is {self.name} and your salary is {self.salary}")
# s1=Employee("amit",250000)
# s2=Employee("amika")
# s2.Salaries()
# s1.Salaries()

# Create a class Addition with a constructor that accepts two numbers and prints their sum.

# class Addition():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.sum=self.a+self.b

#         print(f"addition is {self.sum}")
# a=int(input(" "))
# b=int(input(" "))
# s1=Addition(a,b)


# Create a class NumberCheck with a constructor that takes a number and checks whether it is even or odd

class NumberCheck:
    def __init__(self ,a):
      self.a=a
      if a%2==0:
         print("it is even number")
      else:
         print("number is odd")
a=int(input("enter the number: "))
s1=NumberCheck(a)

    