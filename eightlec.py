# tuple ------


 
# tup = ("Hello",)
 
# tp = tuple(("hello",))
 
# ls = list((tup))
 
# ls.append("guru99")
# print(type(ls),ls)
# tup = tuple((ls))
# print(type(tup))
 
 
 
 
 # print(type(tp))
 
 # del tup
 
 # print(tup)
 
 # print(type(tup))
 # print(type(tup))
 # print(tup[1])
 # print(tup[0:-1])
 
 # tup1 = ("tup 1",)
 # tup2 = ("tup 2",)
 
 # tup3 = tup1 + tup2
 # print(tup3)
 
tup1 = ("faisalabad","Jaranwala","Lahore")
tup2 = (1,2,3,4,5,6,7)
tup3 = tup2 + tup1
# print(tup3)
# print(tup3[7:] + tup3[:7])
ls = list(tup3)
ls2 =[]
for i in  ls:
     ls2.insert(0, i)
tup4 = tuple(ls2)
print(type(tup4))
print(ls)
 
 
 
 