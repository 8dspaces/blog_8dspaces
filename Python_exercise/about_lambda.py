g = lambda x,y:(x**2 + y**2)
a1 = [g(x,y) for x in range(1,5) for y in range(1,5)]

a2 = [(x**2 + y**2) for x in range(1,5) for y in range(1,5)]

print a1 
print a2

# lambda 多和map, reduce 函数一起使用
# map( lambda, alist)
# reduce(lambda, alist)