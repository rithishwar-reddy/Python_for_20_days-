age = int(input("Enter your age : "))
if age>=18:
    print("You can vote")
else:
    print("You can't vote")

age = int(input("Enter your age : "))
if age>=50:
    print("Go to ground floor")
else:
    print("Go to first floor")


a = (input())
if a[0]==a[len(a)-1]:
    print("Lucky")                            #Palindrome
else:20 
    print("Super Lucky")20

n = int(input("Enter the amount: "))
if n == 10:
    print("Collect Chips")
elif n == 20:
    m = input("Select among [s,t,f]: ")
    if m == "t":
        print("Collect Thumbsup")
    elif m == "s":                            #Token
        print("Collect Sprite")
    elif m == "f":
        print("Collect Fanta")
    else:
        print("Product is not existed")
else:
    print("Order cannot be accepted!!")
print("Thankyou for visiting")

n = input()
if n == n[::-1]:
    print("Palindrome")                   #Palindrome
else:
    print("Not Palindrome")

n = input()
r_str=" "                                  #Reverse
for i in n:
    r_str= i+r_str
print(r_str)


n= input()
is_palindrome = True
i=0
j=len(n)-1
while(i<=j):                                  #DSA
    if n[i] == n[j]:
        j += 1
        j -= 1
    else:
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not Palindrome")

