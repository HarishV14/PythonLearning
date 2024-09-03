import re
#parsing phone number 
phonePattern=re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

print(phonePattern.search('300-390-1232'))
print(phonePattern.search('300-390-1232').groups()) #it groups the value and return as tuple using group if doesnot match then it will return error
print(phonePattern.search('800 555 1212')) #- is compulsory


print("--------------------------------------------------1")
phonePattern=re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$') #\d+ mention one or more digits can be there
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('800-555-1212-12349090090').groups())
print("--------------------------------------------------2")

phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$') #/D+ non (0-9) can be present in that division of the words
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('800 555 12122 1234'))

print("--------------------------------------------------3")

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
