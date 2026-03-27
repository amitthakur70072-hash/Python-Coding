# class Parent:
#     def animals(self):
#         print("you spaek ")
# class Child(Parent):
#     def bark(self):
#         print("thank you")
# s1=Child()
# s1.animals()
# s1.bark()





# multi
# class student:
#     def st(self):
#         print("hello students")
# class stu2:
#     def stu(self):
#         print("how are you")
# class Child(student,stu2):
#     def ch(self):
#         print("ok bye!")
# s1=Child()
# s1.stu()
# s1.st()


# mutilevel

# class Grandparent:
#     def gr(self):
#         print("hi son")
# class Father(Grandparent):
#     def fat(self):
#         print("hello son")
# class son(Father):
#     def s(self):
#      print("hi dad")
# s1=son()
# s1.s()
# s1.fat()
# s1.gr()





# hierarical:grand by father and son both
# class Grandfather:
#     def g(self):
#         print("hello")
# class Father(Grandfather):
#     def f(self):
#         print("namastey")
# class Son(Grandfather):
#     def s(self):
#         print("ok bye,..... ")
# s1=Son()
# s2=Father()
# s2.f()
# s2.g()
# s1.g()
# s1.s()


# multiple inheritance"
# class Parent1:
#     def __init__(self):
#         print("hi parent 1")
# class Parant2:
#     def __init__(self):
#       print("this is parent 2")
# class child(Parent1,Parant2):
#     def __init__(self):
#         Parent1.__init__(self)
#         Parant2.__init__(self)
#         print("this is the boy")
# s1=child()


# 2 multiple inheritance
# class multiple:
#     def a(self):
#         print("class 1")

# class multiple2:
#     def b(self):
#         print("2nd class")

# class multiple3(multiple,multiple2):
#     def c(self):
#         print("this is the third class")

# s1 = multiple3()

# s1.a()
# s1.b()
# s1.c()


# class Employee:
#     pass
# class programmer(Employee):
#     pass
# class employe(programmer):
#     pass
# s1=Employee()



