# def add(x,y):
#     return(x+y)
# a = int(input("Enter first number: "))                  # add using def function
# b= int(input("Enter second number: "))
# c= add(a,b)
# print(c)


# def fact(n):
#     if n <= 1:
#         return 1                              # factorial using Recursion 
#     return n*fact(n-1)                        # by giving return 1 it can be also done for negative
# n=int(input("Enter a number : "))
# print(fact(n))


# def fibb(n):
#     if n <= 0:
#         return 0
#     if n == 1:                                  # fibonacci series recursion
#         return 1
#     return fibb(n-1)+fibb(n-2)
# n=int(input("Enter the number : "))
# for i in range(n):
#     print(fibb(i),end" ")


'''                         "OOPS Concept in Python"                  '''
# class Iphone:
#     def icloud(self):
#         print("free 5gb space")
#     def call(self,number):
#         print("calling...",number)                        #Class
# iphone16pro = Iphone() #obj creation
# number_1 = int(input("Enter number : "))
# print(type(iphone16pro))
# iphone16pro.call(number_1)


# class AmazonService:
#     def __init__(self,Agentname,agentId,custId):
#         self.custId=custId
#         self.Agentname=Agentname
#         self.agentId=agentId
# agentName = "sam"
# AgentId=1
# complaint=input("Enter your issue : ")
# customerId=int(input("Enter cust id : "))
# while complaint:
#     Agent1 = AmazonService(agentName,AgentId,customerId)
#     complaint = False
# print("Agent",Agent1.agentId,"is handling customer :",Agent1.custId)