 # dictionaries 

# dic = {"name": "Hassan"}
# dic = dict({"name": "Hassan", "age": 22})                    #  dictionaries method as constructor
# print(type(dic),dic, len(dic))


# dic = {"name": "Hassan","age": 22}
# print(dic["age"])                                            # 1 method  
# print(dic.get("name"))                                       # 2 method
# dic["name"]="ahsan"                      
# dic["color"] = "green"                                       # add data in dictionary if data is not found in dictionary using this method
# dic.update({"color": "blue","alpha":"1.09"})                 # update method in dictionary 
# dic.pop("alpha")                                             # remove alpha # in dictionary using pop any value del dont last value
# dic.popitem()                                                # this  method remove last value
# print(dic.keys())                                            # to find keys in dictionary
# print(dic.values())                                          # to find values in dictionary
# print(dic.items())                                           # to find items in dictionary
# del dic["name"]                                              # to delete the key and value
# dic.clear()                                                  # clear the dictionary
# del dic 
# print(dic)

                   # new topic

# MIT Question for interview 
# pass by reference / pass by value
# How to sure which method is use pass by value / pass by reference 


# a = 10
# b = a                                                        # pass by value
# a = 20                                                       # primitives data type
# print(a, b)


# dic1 = { "nama":"hassan" , "age":22}
# dic2 = dic1                                                  # pass by reference
# dic1["name"] = "ali"                                         # Non primitive data type name
# print(dic1,dic2)
 
# copy dictionry


dic1 = {"name":"hassan" , "age":22}
# dic2 = dic1.copy()                                                  # pass by reference
# dic2 = {"name":"hassan" , "age":22}
dic2 = dict(dic1)
dic1["name"] = "zubair"
print(dic1,dic2)
