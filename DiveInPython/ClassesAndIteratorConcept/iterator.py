import re
#finds the all the number in the string
print(re.findall('[0-9]+', '16 2-by-4s in rows of 8'))

#find the alphates in the string captial letters
print(re.findall('[A-Z]+', 'SEND + MORE == MONEY sss'))

#without + then it will seperate by single character
print(re.findall('[A-Z]', 'SEND + MORE == MONEY sss'))

#it include the small letter also
print(re.findall('[A-Za-z]', 'SEND + MORE == MONEY sss'))

#Start with space and continue with s and starting letter of the string is also should be s 
print(re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick. seek s"))

a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
print(set(a_list)) #keeps unique element

a_string = 'EAST IS EAST'
print(set(a_string)) #return uniqe character in the string and return as the set

words = ['SEND', 'MORE', 'MONEY']
print(''.join(words))
print(set(''.join(words)))


# assert 1+1==3,"if true it will not do nothing if this will displayed in the assertion error"

unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
gen = (ord(c) for c in unique_characters) #it is generator expression sotores as the generator

# print(next(gen))
print(next(gen),"using next")
print(next(gen),"using next")
print(next(gen),"using next")
print(next(gen),"using next")
print(next(gen),"using next")
# print(next(gen))

#once printed using next another time cannot remaing after the next
#once iterared next time u can't only one time is iterable gnereator
for i in gen:
    print(i,end=" ")

