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
