# PUBLIC ATTRIBUTE where attributes can be accesed outside the function
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("amit")
# print(s1.name)

# private attribute
# class Account:
#     def __init__(self,account_num,account_pass):
#         self.account_num=account_num
#         self.__account_pass=account_pass
#     def reset_pass(self):
#         print(self.__account_pass)

# acc1=Account("12345","abcde")

# print(acc1.account_num)
# print(acc1.reset_pass())

# class Person:
#     __name="anonymous"

#     def __hello(self):
#         print("hello boy")
#     def welcome(self):
#        self.__hello()
#        return self.__name


# p1= Person()
# print(p1.welcome())

