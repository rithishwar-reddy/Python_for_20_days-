# n = int(input("Enter the value : "))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         str1=""
#         for j in range(1,i+1):                               # 1
#             str1+=str(j)+" "                                # 1 2
#         print(" "*(n-i)+str1)                              # 1   3
#     else:                                                 # 1     4
#         str2=""                                          # 1 2 3 4 5
#         for k in range(1,i+1):
#             if k==1 or k==i:
#                 str2+=str(k)+" "
#             else:
#                 str2+=" "+" "
#         print(" "*(n-i)+str2)

# def greet(arg1,arg2):
#     print("Hello",arg1,"you are",arg2,"years old")           #Functions(Named arguments)
# name = input("Enter name : ")
# age = int(input("Enter age : "))
# greet(arg2 = age,arg1 = name)

# a = int(input())
# b = int(input())
# o = input()
# def add(a,b):
#     print(a+b)
# def sub(a,b):                                               #Calculator
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# if o == '+':
#     add(a,b)
# elif o == '-':
#     sub(a,b)
# elif o == '*':
#     mul(a,b)
# else:
#     div(a,b)

# n = str(input("Enter number : "))
# s = 0
# power = len(n)
# for i in n:                                                  #Amstrong
#     s+= int(i)**power
# if s==int(n):
#     print("is amstrong")
# else:
#     print("not amstrong")

# n = int(input("Enter number : "))
# count = 0
# for i in range(1,n):
#     if n%i==0:                                                 #Prime
#         count+=1
#     elif count == 2:
#         print("The given number is not a prime")
#     else:
#         print("The given number is a prime")

# def is_prime(m):
#     is_prime= True
#     if m <= 1:
#         is_prime=False                                         #Prime Range
#     else:
#         for i in range(2,int(m**0.5)+1):
#             if m%i==0:
#                 is_prime = False
#                 break
#     if is_prime:
#         print(m,"is a prime")
# m=int(input())
# for i in range(1,m+1):
#     is_prime(i)
