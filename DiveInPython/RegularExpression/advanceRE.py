import re

def plural(noun):          
    if re.search('[sxz]$', noun):             
        return re.sub('$', 'es', noun)        
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)       
    elif re.search('[^aeiou]y$', noun):      
        return re.sub('y$', 'ies', noun)     
    else:
        return noun + 's'

print(plural("harish"))
print("------------------------------------------------1")
print(re.search('[abc]', 'Mark')) #it matches the a value

print(re.sub('[abc]',"o",'Markb')) # anything matches in the string []inside this then it will sub

print("------------------------------------------------2")
#the last character followed by Y should not be aeiou and it should end with the Y
print(re.search('[^aeiou]y$', 'vacancy')) 
print(re.search('[^aeiou]y$', 'boy')) #in this o is vowel so it returns the none

print("------------------------------------------------3")
#replace the last letter when it is y when there is y then only replace the word
print(re.sub('y$', 'ies', 'agency'))
print(re.sub('y$', 'ies', 'agenc'))
print("------------------------------------------------4")
print("------------------------------------------------5")
