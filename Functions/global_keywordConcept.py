# global variable
c = 1 

def add():

     # increment c by 2
    
    # c = c + 2

    print(c)

add()


# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3 