#  For Loop & while Loop & List Comprension --

# for loop -----

# ls = ["Ali", "Hassan", "Shahzad" , "Zubair"]
# for x in range(len(ls)):
#     print(ls[x],x+1)
# # print(ls[x],x)

# while loop -----

# ls = ["Ali", "Hassan", "Shahzad" , "Zubair"]
# i = 0 
# while i < len(ls):
#     print(ls[i],i)
#     i = i + 1

# range  ---- 

# for x in range(0,101,2):  # starting ending gaping
#     print(x)

# list comprension --- 

# ls = [ x for x in range(2,10,2)]
# print(ls)

# ls = ["ali" , "hassan", "birds"]
# ls2 =[]
# for x in ls:               # first method
#  if "a"in x:
#   ls2.append(x)
# print(ls2)                      

# ls = ["ali" , "hassan", "birds"] 
# ls2 =[x for x in ls if "s"in x]       # 2 method
# print(ls2)                                                                                                                

# remove the value of list ---

# ls = ["ali" , "hassan", "birds"] 
# ls2 =[x for x in ls if x != "hassan"]     # remove hassan for list
# print(ls2)

# ls = ["ali" , "hassan", "birds"] 
# ls2 =[x.capitalize() for x in ls ]     # first word capital
# print(ls2)

# ls = ["ali" , "hassan", "birds"] 
# ls2 =[x[0].upper() + x[1:-1].lower() + x[-1].upper() for x in ls]     # first and last word capital
# print(ls2)