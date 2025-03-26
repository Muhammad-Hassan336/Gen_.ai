# 1st Assignment

# # Given data
# bonus = 15000
# percentage = 0.22

# # Calculate the total salary
# total_salary = bonus / percentage
# print("The total salary of the employee is: {total_salary}")


# 2nd Assignment

# edu = int (input("Enter your Education"))
# age = int (input("Enter your age"))
# height = float(input("Enter your height"))

# if(edu <=12 and (age>=18 and age<=32)):
#  print("You are passed")
# elif((age>=18 and age<=32) and height>=5.6):
#   print("you are passed")
# elif(height>=5.6 and edu <=12):
#   print("you are passed")
# else:
#   print("you are not passed")


# 3rd ASSignment

# bonus = 15000

# salary = (bonus/0.22)
# print("salary", salary)

# 4th Assignment

# a = "jaranwala"
# b = "faisalabad"
# c = "lahore"
# print(a[:1].upper()+"aranwala")
# print(b[:1].upper()+"aisalabad")
# print(c[:1].upper()+"ahore")

# 5th assignment

# p = "jaranwala lahore faisalabad"
# print(p[0:1].upper() +p[1:9], p[10:11].upper() + p[11:16], p[17:18].upper() + p[18:] )

# 6th assignment

# j = "jaranwala"
# l = "lahore"
# f = "faisalabad"
# b = j.replace("j","J")
# print(b)
# c = l.replace("l","L")
# print(c)
# d = f.replace("f","F")
# print(d)

# 7th Assignment : Lower the first 

# st = "Jaranwala Faisalabad Lahore Karachi Multan"
# print(st [0].lower() + "aranwala", st[10].lower() +"aisalabad", st[21].lower() + "ahore", st[28].lower() + "arachi", st[36].lower() + "ultan")

# 8th assignment : Capitalize the first word

# ls = ["lahore", "faisalabd","jaranwala"]

# for item in ls:
#   print(item.title())


#   9th asignment : capitalize the firts and last word

# ls = ["lahore", "faisalabad","jaranwala"]
# lp =[]
# for x in ls:
#     p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#     lp.append(p)
# print(p)
# print(lp)

# 10th ASsignment: reverse a word

#   sp =[]
#     for x in ls:
#         p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#         sp.append(p)
#         print(sp)


# ls = ["lahore","karachi","peshawar"]
# lp =[]
# for x in ls:
#     lp.insert(0,x)
#     print(lp)

#  11th Assignment : take a 10 cities and reverse it and do a first and last word in capital

# ls = ["lahore","karachi","peshawar","jaranwala","gujranwala", "sahiwal","faisalabad","quetta","hyderabad","okara"]
# # ls.reverse()
# lp = []
# for x in ls:
#     lp.insert(0,x)
#     print(lp)
#     sp =[]
#     for x in ls:
#         p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#         sp.append(p)
#         print(sp)


# 12 Assignment: take a input from user and print in list

# a = input("input your name :")
# b = input("input your father name :")
# c = [a,b]
# print(c)


# 13 Assignment fictorial

# num = int(input("Enter a number: "))  
# factorial = 1  

# for i in range(1, num + 1):  
#     factorial *= i  

# print("Factorial of", num, "is", factorial)



# 14 Assignment : how many 3 in 100

# count = 0

# for i in range(1, 101):
#     count += str(i).count('3')

# print("Total occurrences of digit 3:", count)


# str = {"item1", "item2"}
# (str1 , str2) = str
# print(str)
# ls = list(str)
# print(ls)
# ls = tuple((str))
# print(ls)


# ls = set(["hello", "world"])
# tup = set(("hello", "item2"))

# nt = ls.intersection(tup)
# un = ls.union(tup)
# df = ls.difference(tup)
# print(nt, un , df)

tup = (1,2,3,4,5,6,7,8,9,10)
(a,b,c,d,e,f,g,h,*i) = tup

print(i)
var = list(i)
st2 = ["menu","main menu"]
lis = var + st2
print(lis)
print(set(lis))











