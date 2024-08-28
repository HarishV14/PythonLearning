def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
# print(message)

# declare global variable
message = 'Next Hello'

def greet():
    # declare local variable
    message="wel"
    print('Local', message)

greet()
print('Global', message)


# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()