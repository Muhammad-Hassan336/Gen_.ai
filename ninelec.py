#  sets -----
#  set  is unordered
#  in set we dont use index and range

# st = {"hello","world","!"}       # 1 method
# print(type(st))                # output {'world', 'hello', '!'} , so it is unordered
# print(st)

# st = set(("hello","world","!"))       # 2 method
# print(type(st))                      # output {'world', 'hello', '!'} , so it is unordered
# print(st)


# st = set(("hello","world","!"))        # add methods
# st.add("menu")                         # only single value add otherwise error
# print(st)

# st = set(("hello","world","!"))        # update
# st2 = (("menu","main menu"))           # multi value update create new variable
# st.update(st2)
# print(st)

# st = set(("hello","world","!"))          # pop method
# st.pop()                                 # delete  random value
# print(st)

# st = set(("hello","world","!", "hello"))          # no repeated values show
# # st.pop()                                 
# print(st)

# st = set(("hello","world","!", "hello"))          # type casting as a list
# ls = list(st)                                 
# print(type(ls))

# st = set((False,"hello","Yes","world","!","no", "hello",True, 0,1 ))          # boolean                                  
# print(st)

# st = set(("hello","world","!", "hello world"))     # remove method in set and Discard method
# st.remove("hello")                                   # if to time use remove show key error
# st.discard("hello")                             
# print(st)

# st = set(("hello","world","!", "hello world"))     # clear method in set
# st.clear()                                                                
# print(st)

# st = set(("hello","world","!", "hello world"))     # del method in set
# del st                                                               
# print(st)

# st1 = {"hello","world","!"}
# st2 = {"menu", "food", "world"}

# # st3 = st1 + st2                             # +  don't allow
# # st3 = st1 | st2                               # 1 method
# # st3 = st1.union(st2)                          # 2 methods  

# # st3 = st1 & st2                               # 1 method 
# # st3 = st1.intersection(st2)                   # 2 methods

# st3 = st1 - st2                                 # - method 
# # st3 = st1.difference(st2) 

# print(st3)

