import time 

def fib(n):
    if 0 < n <=2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib1(n):
    x, y = 0, 1
    li = []
    i = 1
    while i <= n:
        li.append(x)
        x, y = y, x+y
        i += 1
    return li
    
def fib2():
    x, y = 0,1
    while True:
        yield x
        x, y = y,x+y
        
        
if __name__ == "__main__":
    import itertools 
    
    start_time = time.time()
    list(itertools.islice(fib2(), 30))
    end_time = time.time()
    print end_time - start_time  # 0.007

    start_time = time.time()
    li = fib1(30)
    end_time = time.time()
    print end_time - start_time  # 0.007
    
    start_time = time.time()
    [fib(i) for i in range(1,30)]
    end_time = time.time()
    print end_time - start_time  #  0.554