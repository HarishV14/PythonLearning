def make_counter(x):
     print('entering make_counter')
     while True:
         yield x 
         print('incrementing x')
         x = x + 1

counter = make_counter(2) 
next(counter)
next(counter)
next(counter)
next(counter)