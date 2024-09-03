class Fib:                                        
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                           
        self.a = 0
        self.b = 1
        #it assigns when starting of the iteration then next method take place the process
        # print(self.a,self.b)
        return self

    def __next__(self):
        print(self.a,self.b)
        fib = self.a
        if fib > self.max:
            raise StopIteration                   
        self.a, self.b = self.b, self.a + self.b
        return fib
    

for i in Fib(10):
    print(i,end=" ")
    pass