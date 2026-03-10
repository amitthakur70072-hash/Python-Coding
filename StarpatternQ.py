# q1 \n * * * * * 
# for i in range(1,6):
#     print("*")

# q2  *****
# for i in range(1,6):
#    print("*",end="")


# q3  4 ****  and 4 * down
# for  i in range(1,5):
#     print("*"*4)
   
# q4 right angle triangle
# for i in range(1,6):
#     print("*"*(i))

# q5 trianangle but ulti

# for i in range(5,0,-1):
#  print("*"*i)

# q6  trangle but spacing in between them
# for  i in range(1,5):
#     print("* "*i)

# q7 pyramid pattern
# n=5
# for i in range(1,6):
  
#  print(" "*(n-i) +"*"*(2*i-1))

# Right-aligned increasing triangle
# for i in range(1,6):
#     print(" "*(5-i),"*"*i)


# Right-aligned decreasing triangle
# n=5
# for i in range(n):
#     print(" "*i,"*"*(n-i))

# Right-aligned increasing triangle
# n=5
# for i in range(n):
#     print(" ")
#     for j in range(n-i-1):
#         print(" ",)

# a={"c":"amit","b":"lal"}
# print(a["c"]+" "+a["b"])


# a=[1,2,3,4,5]
# print(sorted(set(a))[-2])


# 6
# 66
# 666
# n=(input("enter your choice: "))
# for i in range(1,4):
#     print((n+" ")*i)



def name(first, last):
    return (f"Hello {first} {last}! You just delved into python.")
x=name("Ross","Taylor")
print(x)