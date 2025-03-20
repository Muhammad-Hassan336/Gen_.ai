# Assignment # 1  : --bonus = 15000

# salary =( bonus / 0.22) 
# print("salary", salary)

# Assignment # 2 : --- percentage
# mark = 85 
# totalmarks = 150
# percentage =(mark/totalmarks)*100
# print("persentage is : " ,percentage, "%")

# Assignment # 3 : ---  using replace method ---

# p = "Jaranwala Lahore Multan Fasilabad Pindi"
# print(p)
# #  dont use slice only use replace method to change first letter in small;
# print(p.replace("J","j") .replace( "L","l") .replace( "M","m") .replace( "F","f") .replace( "P","p"))

# Assignment # 4 : ---- first method

# ls = ["lahore","multan","karachi"]

# for item in ls:
#     print(item.title()  .replace("e","E") .replace("n","N") .replace("i","I"))

#  Second method 

# ls = ["lahore","multan","karachi"]
# # lp = []
# for x in ls:
#     p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper() 
#     # lp.append(p)
#     print(p)
# # print(lp)

# 2nd word capital and 2ndlast

# ls = ["lahore","multan","karachi"]
# # lp = []
# for x in ls:
#     p = x[0:1].lower() + x[1:2].upper() + x[2:-2].lower() + x[-2:-1].upper() + x[-1:].lower()  
#     # lp.append(p)
#     print(p)
# # print(lp)


pakistan_cities = ["Karachi", "Lahore", "Islamabad", "Rawalpindi",]
for x in pakistan_cities:
    pakistan_cities.insert(2,x)
    print(pakistan_cities)