def find_last(str, target):
    
    begin = len(target) - len(str)
    span = len(str)
    
    while begin > 0:
        if target[begin: begin + span] == str:
            return begin 
        begin -= 1
    return -1

def find_last_2(str, target):

    r = -1
    begin = target.find(str)
    while begin > 0:
        r = begin 
        begin = target.find(str, begin+1)

    return r

def multi_table(n):
    i =1
    while i <= n:
        j = 1
        while j <= n:
            print "%d x %d = %d \t" % (i, j, i*j),
            j += 1
        print 
        i += 1
multi_table(4)
#target =  "athisisdssdsisthissds"
#print find_last_2("this", target)