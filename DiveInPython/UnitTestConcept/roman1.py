class OutOfRangeError(ValueError):  pass
class nonIntergerError(ValueError): pass

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))                 

def to_roman(n):
    '''convert integer to Roman numeral'''

    print(f"Checking value: {n}")  
    if n <=0 or n > 782:
        raise OutOfRangeError('number out of range (must be 1..782)')
    
    if not isinstance(n,int):
        raise nonIntergerError('number should be only int')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result


print("hello")
# print(to_roman(1012))