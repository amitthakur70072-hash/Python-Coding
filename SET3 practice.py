# a={"kursi":"chair","manja":"bedbox","pankha":"fan"}


# aa= input("enter the name you want to tranaslate: ")
# print (a.get(aa,"no word found"))
# aa=set()
# a= int(input("enter 1st number:"))
# aa.add(a)
# b=int(input("enter 2nd number: "))
# aa.add(b)
# c=int(input("enter 3rd number: "))
# aa.add(c)
# d=int(input("enter 4th number: "))
# aa.add(d)
# print(aa)
  
# a=set()
# a.add(20)
# a.add(20.0)
# a.add("20")
# print(len(a))
# print(a)

a={}
f1=input("enter your name: ")
lang= input("add language: ")
a.update({f1:lang})
f2=input("enter your name: ")
lang= input("add language: ")
a.update({f2:lang})
f3=input("enter your name: ")
lang= input("add language: ")
a.update({f3:lang})
print(a)
print(a.get("amit"))

