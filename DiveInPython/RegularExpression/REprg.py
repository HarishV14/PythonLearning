s="100 North main road"
print(s.replace("road","re"))
s1="100 North Broad road"
print("--------------------------------------------------1")
print(s1.replace("road","re"))

print("--------------------------------------------------2")
#I only want to replace last road
#It is difficult way
print(s1[:-4]+s1[-4:].replace("road","re"))

print("--------------------------------------------------3")
#using regular expression
import re
#$ mention end of the string
#^ mention start of the string
print(re.sub("road$","re",s1))
print("--------------------------------------------------4")
print(re.sub("^road","re",s1))
print("--------------------------------------------------5")

print(re.sub('\\bROAD$', 'RD.', s1))
print("--------------------------------------------------6")

print(re.sub(r'\broad\b', 'RD.', s1))   
print("--------------------------------------------------7")


pattern='^M?M?M?$'
print(re.search(pattern,"M"))
print(re.search(pattern,"MM"))
print(re.search(pattern,"MMM"))
print(re.search(pattern,"MMMM")) # it exceed the m because there only given threee m
print(re.search(pattern,"")) # m is given optional so it is matching the string

print("--------------------------------------------------8")
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print(re.search(pattern,"MCM"))
print(re.search(pattern,"MD"))
print(re.search(pattern,"MMMCCC"))
print(re.search(pattern,"MCMC")) #because there should m and cmc not matching that optional
print(re.search(pattern,""))

print("--------------------------------------------------9")

pattern='^M{0,3}$'
print(re.search(pattern,"M"))
print(re.search(pattern,"MM"))
print(re.search(pattern,"MMM"))
print(re.search(pattern,"MMMM")) # it exceed the m because there only given threee m
print(re.search(pattern,"")) # m is given optional so it is matching the string

print("--------------------------------------------------10")

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$' 
'''M is optional if there should only 3 not more than that
In bracket CM or CD or D or C any one should must there but not more than one D and Three C's
In bracker Same before bracket XC or XL or L or X must one should be there but not more 
one given optional can used how many that is given'''
print(re.search(pattern, 'MCMXL'))
print(re.search(pattern, 'MCX'))
print(re.search(pattern, 'CDXL'))
print(re.search(pattern, 'MCMDX'))
print(re.search(pattern, 'CMLXXX'))
print(re.search(pattern, 'CMLXXXX'))

print("--------------------------------------------------11")
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(re.search(pattern, 'MDLV'))
print(re.search(pattern, 'MMDCLXVI'))
print(re.search(pattern, 'MMMDCCCLXXXVIII'))
print(re.search(pattern, 'I'))  
'''The last search I is matched string? how
It choose M as optional in second bracker D as optional and third that matches with I so that 
is matched string'''
print("--------------------------------------------------12")
pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''

print(re.search(pattern, 'M', re.VERBOSE))
print(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))
print(re.search(pattern, 'M')) #does not match because it is not mentioned as VERBOSE
print("--------------------------------------------------13")
