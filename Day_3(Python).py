# list_1 = [3,6,4,5,6,3]        
# first_sum = sum(list_1)       
# second_sum = sum(set(list_1))*2                     #List 
# res = second_sum-first_sum
# print(res)

# n = int(input("Enter input : "))
# fact = 1
# for i in range(n,1,-1):                              #Factorial
#     fact *= i        #(fact = fact*i)
# print(fact)

# n = 5
# fact = 0
# for i in range(1,11):                                  #Sum of factorial of 1st 10 of input
#     fact = n*i + fact
# print(fact)

# list_1 = [1,7,9,7,4,6,2]
# target = 7
# for i in range(len(list_1)):                          #Linear search
#     if target==list_1[i]:
#         print(i)
#         break

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# target = int(input("Enter the Target : "))
# start = 0
# end = len(list_1)-1
# index = -1                                             #Binary search
# while(start<=end):
#     middle = (start+end)//2
#     if list_1[middle]==target:
#         index = (middle)
#         break
#     elif list_1[middle]>target:
#         end = middle-1
#     elif list_1[middle]>target:
#         start = middle+1
# if index != -1:
#     print(index)
# else:
#     print("Not found")


# n = int(input("Enter number of stars : " ))
# for i in range(1,n+1):                                   #Star Pattern
#     print("* "*i)
    
# n = int(input("Enter no of stars : " ))
# for i in range(n,0,-1):                                     #Inverted Star Pattern
#     print("* "*i)

# n = int(input("Enter number: " ))
# for i in range(1,n+1):                                    #Number Pattern
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# n = int(input("Enter number: " ))
# for i in range(1,n+1):                                       #Number Pattern
#     str1=""
#     for j in range(1,i+1):
#         str1+=str(j)+" "
#     print(str1)


# n = int(input("Enter number of stars: " ))
# for i in range(1,n+1):                                      #Pyramid Pattern
#     for stars in range(1,n-i+1):
#         print(" ",end=" ")
#     for star in range(1,2*i):
#         print("*",end=" ")
#     print()

# n = int(input("Enter number of stars: " ))
# for i in range(1,n+1):                                       #Pyramid Pattern in shortcut
#     print(" "*(n-i)+"* "*i)

# n = int(input("Enter number of stars: "))
# for i in range(1,n+1):
#     if i == 1 or i == n:                                       #Hollow Triangle
#         print("* "*i)
#     else:
#         print("*"+" "*(2*i-3)+"*")

# n = int(input("Enter number of stars : " ))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")                                        #Hollow Pyramid
#     for h in range(1,i+1):
#         if h ==1 or h ==i or i ==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
        