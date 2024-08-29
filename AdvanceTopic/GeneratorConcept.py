def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)


print("---------------------------------------------------------------------")

# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)

print("------------------------------------")
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
# for i in all_even():
#     print(i)

print("------------------------------------------")
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        c=x+y
        x=y
        y=c
        print(c,"fibo")
        yield x # it return s every single time to square

def square(nums):
    for num in nums:
        # print(num,"square")
        yield num**2 #it returns the value to the sum

print(sum(square(fibonacci_numbers(10))))

# Output: 4895

def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print(item)


def some_function():
    for i in range(4):
        yield i

for i in some_function():
    print(i,end='\t')

class my_range:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = self.n
        self.n += 1
        return result
    
print(type(my_range))
generator = my_range(20)
print(next(generator),"hwl")  # 0
print(next(generator))  # 1
print(next(generator))  # 2


