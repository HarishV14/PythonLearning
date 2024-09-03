import re

def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):                             
    return re.search('[^aeiou]y$', noun)
        
def apply_y(noun):                             
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

rules = ((match_sxz, apply_sxz),               
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )
'''It is rules is the tuple contain matches function and apply function
matches function contain searching the condition true return object else none
apply function replaces by the given condtion making plural'''

'''In the plural function the rules tuple will iterates if the matches rule call then contion
equalent apply rule in the tuple will be called
it is the list of funtions'''

def plural(noun):           
    for matches_rule, apply_rule in rules:       
        if matches_rule(noun):
            return apply_rule(noun)
        
print(plural("harish"))
print(plural("deepak"))

print("-------------------------------------------------------------")
'''Additional abstraction is confusing this qualent to the same thing above done in the simple way'''
def plural2(noun):
    if match_sxz(noun):
        return apply_sxz(noun)
    if match_h(noun):
        return apply_h(noun)
    if match_y(noun):
        return apply_y(noun)
    if match_default(noun):
        return apply_default(noun)
    
print(plural2("harish"))
print(plural2("veera"))

print("-------------------------------------------------------------")
'''this is to iterate the function we can match using patter because match contain
 re.search and apply contain re.sub so that can be maked common we pattern is changing
 so that can be maked as the tuple with pattern , search , replace that can be build using 
 build written function'''
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):                                     
        return re.search(pattern, word)
    def apply_rule(word):                                       
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)   

patterns =(
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')                                 
  )

rules = [build_match_and_apply_functions(pattern, search, replace)  
         for (pattern, search, replace) in patterns]

def plural3(noun):
    for matches_rule, apply_rule in rules:  
        if matches_rule(noun):
            return apply_rule(noun)

print(plural3("harish"))
print(plural3("deepan"))

print("-------------------------------------------------------------")

'''It is using file that pattern is stored in the file and using build written function 
using same above build written func '''
import os
os.chdir("C:\\Users\\LENOVO\\Documents\\PythonConcepts\\PythonLearning\\DiveInPython\\Closure")
rules2 = []
with open('pattern.txt', encoding='utf-8') as pattern_file:  
    for line in pattern_file:
        # print(line)                                      
        pattern, search, replace = line.split(None, 3)             
        rules2.append(build_match_and_apply_functions(              
                pattern, search, replace))
# print(rules2)
def plural4(noun):
    for matches_rule, apply_rule in rules2:  
        if matches_rule(noun):
            return apply_rule(noun)
print(plural4("harish"))

print("-----------------------------------------------------------------------")

'''Example of closures nested function that helps in acess the outer function 
variable even after the outer function is closed'''
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())