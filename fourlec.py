#  multiline in string

a = """whta is your
name"""
print(a)

# concetination in string

a = "hello "
b = "world "
print(a  +  b , a+" "+b )

# concetination in string us typecasting for integer

a = 42
b = 23
print(str(a) + str(b))

# Format in string and integer/float

age = 23
marks = 45
total = "{} your total marks is 100  and you got {}"
obt = total.format(age,marks)    # for multiple value we use , comma
print(obt)

# Slicing in string

a ="Hello AI Class"
print(a[0:1])
print(a[1:2])
print(a[2:3])
print(a[0:]) # these are all method of slicing


# Split in string

a = "Hello AI Class"
b = a.split(",")  # comma is used to combine value in array
c = a.split(" ")  # these space is used to sperate the array value 
print(b,c)

# Upper case And Lower case

str = "hello world"
up = str.upper()
lo = str.lower()
print(up , lo , str.capitalize() , str.title() ,str.replace("e","E"))
