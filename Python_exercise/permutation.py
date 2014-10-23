# 第一种方法 递归 

def perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
for item in list(perms([1, 2, 3,4])):
    print item
    
    
    
# 第二种方法 itertools

import itertools
print list(itertools.permutations([1, 2, 3,4],3))



#-------------------

#生成全排列
def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p
 
#生成组合
def comb(items, n=None):
    if n is None:
        n = len(items)    
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in comb(rest, n-1):
                yield v + c
 
a = perm('abc')
for b in a:
    print b
    break
print '-'*20
for b in a:
    print b 
