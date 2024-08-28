#if statement
x=0
if(x==0):
  print("x is zero")

#if..else statement
y=18
if(y<18):
  print("Less than 18")
else:
  print("Greater than 18")

#if..elif..else statement
z=-1
if(x<0):
  print("z is negative")
elif(x>0):
  print("z is poistive")
else:
  print("z is zero")  

#nested if statement
number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

#compact if
number = 10
if number > 0: print('Positive')

#ternary if
grade = 40
result = 'pass' if number >= 50 else 'fail'
print(result)

#Logical operator to add multiple condition
age = 35
salary = 6000

# add two conditions using and operator
if age >= 30 and salary >= 5000:
    print('Eligible for the premium membership.')
else:
    print('Not eligible for the premium membership')