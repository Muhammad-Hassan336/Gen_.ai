# p = "jaranwala"
# a = "fasilabad"
# l = "lahore"
# print(p[:1].upper()+"aranwala",l[:1].upper()+"ahore",a[:1].upper()+"asilabad")

# p = "jananwala lahore faisalabad"
# print(p[0:1].upper() + p[1:9] , p[10:11].upper() + p[11:17] , p[17:18].upper() + p[18:])

p = "jananwala lahore faisalabad"
print(p[0:1].replace("j","J") + p[1:9].upper() , p[10:11] + p[11:17].upper() , p[17:18] + p[18:].upper())

# replace assignment
j = "jananwala" 
l = "lahore" 
f = "faisalabad"
# b = p.replace("j","J")
print(j.replace("j","J") , l.replace("l","L") , f.replace("f","F") )