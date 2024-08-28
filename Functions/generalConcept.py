# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)


#With return statement

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)

#this will pass mentioned as placeholder it kept for the feature use
def future_function():
    pass

# this will execute without any action or error
future_function()  


# *args we handle no of argument

# function to sum any number of arguments
def add_all(*numbers):
    return sum(numbers)

# pass any number of arguments
print(add_all(1, 2, 3, 4))  


#*kwargs in accept of any number of keyword arguments

# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")