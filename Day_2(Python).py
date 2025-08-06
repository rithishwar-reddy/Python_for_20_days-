str1 = (input("Enter Any Sentence : ").title())
print(str1)                                       #For capitalizing every starting of words

for i in range(len(str1)):
    if str[i]==" " and str[i+1]!=" ":
        str1 = str[:i+1]


string = "All silver tea cups".title()
new_list=string.split(" ")                            # pascal = "AllSilverTeaCups"
str2="".join(new_list)
print(str2)

string = "All silver tea cups".lower()
new_list=string.split(" ")                            # snake = "all_silver_tea_cups"
str2="_".join(new_list)
print(str2)

string = "All silver tea cups".title()
new_list=string.split(" ")                             # string2 = "All-Silver-Tea-Cups"
str2="-".join(new_list)
print(str2)

string = "All silver tea cups".title()
string1= string[0].lower()+string[1:]                  # Camel = "allSilverTeaCups"
new_list= string1.split(" ")
str2= "".join(new_list)
print(str2)

vowels = input().lower()
count = 0                                              # vowels count
for i in vowels:
    if i in "aeiou":
        count+=1
print(count)

li = [2,1]
li.sort()                                              # sort method
li2 = [3]
res = li+li2+["ttr"]+[True,565.99]
print(res)

list = input().split()                                  #sorted method
list2 = sorted(list)
print(list) 

l2 = list(map(int,input().split()))
l2.sort()                                                 #sorting using map
print(l2)   
i= len(l2)-1                                             
highest = l2[i]
print(highest)

list = [3,6,7,8,9,5]
highest = list[0]
for i in range(len(list)):                                 #finding highest no. using traversing
    if list[i]>highest:
        highest = list[i]
print(highest)

 