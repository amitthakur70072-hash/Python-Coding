# def outer():
#     x=10
#     def inner():
#      print(x)
#     return inner
# f=outer()
# f()



# def counter():
#    count=0
#    def increment():
#       print(count)
#    return increment
# c=counter()
# c()

# def greet(name):
#     print("hello",end=" ")
#     def greet2():
#         print(name)
#     return greet2
# g= greet("amit")
# g()

# def make_adder(n):
#     def adder(x):
#      return x+n
#     return adder
    
# add5= make_adder(5)
# print(add5(3))


# def store(name):
#    def greet():
#       print("hello", name)
#    return greet
# x=store("amit")
# x()

# def one():
#    def another(x):
#       return x**2
#    return another
# y= one()
# print(y(5))

def counter():
    count = [0]   # list (mutable)

    def increment():
        count[0] += 1
        return count[0]

    return increment


c = counter()
print(c())
print(c())




