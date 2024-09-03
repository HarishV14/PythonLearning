mess="hello world!"

print(mess[2],mess[-2])

message="""
Working on the messeage
welcome
"""

print(message)

val="program"
print('am' in val)

print(val.upper())
print(val.lower())

print(val.replace("am","er")) #it not affect in that string it returns in another string
#we can also give the index that will match after that index

print(val.find("am")) # it returns the index  if not present it returns -1
print(val.index("am")) # it returns the index but it returns the error

num="123"
print(num.isnumeric())  #if the string contain any word it returns the false

m="hello we are, welcome"
print(m.split(" ")) #it split by the space
print(m.split(",")) #it split by the particular character

print(m.startswith("h"))

print(m.partition(" ")) #it returns tuple and split the value in equal way with given character
print(f'There is two string {m} and {mess}')

print('hello \\ with \n new line and with \t tab and qoutes \' and \"')

print(m[0:3])  #it mention substring in python using the slice operator



query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&') 
print(a_list)
print("-------------------------------------------------------------")
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v] 
print(a_list_of_lists)

print("-------------------------------------------------------------")
a_dic=dict(a_list_of_lists)
print(a_dic)

print("-------------------------------------------------------------")

by=b'abcd\x65'
print(by)
print(type(by))
by+b'\x66'
print(by)
print(by[0])

print("------------------------------------------------------------")
a_string = '深入 Python' 
by = a_string.encode('utf-8')  #here we can mentiont the encoding type like utf-16...32 etc and big5 

print(by,type(by))

