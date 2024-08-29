numbers = [1, 2, 3, 4]

# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

print("--------------------------------------------")

# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]

print("--------------------------------------------")
numbers = [1, 2, 3, 4, 5, 6]

# find even and odd numbers
even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]

print(even_odd_list)

print("--------------------------------------------")
multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]

print(multiplication)