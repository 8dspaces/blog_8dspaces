# coding: utf-8
def josef_circle(count, feed, start = 1):
    
    li = range(1, count+1)
    li_out = []
    
    i = start -1
    while len(li) > 1:
        
        for _ in range(feed-1):
            if i >= len(li)-1:
                i = i - len(li) +1
            else:
                i = i+1
                
        li_out.append(li.pop(i))
    
    
    print "winner is %s" % li.pop()
    print li_out

# Use list as a queue
def josef_circle_2(count, feed, start = 1):
    
    li = range(1, count+1)
    li_out = []
    # handle the start point
    # make sure start point on first 
    i = start -1
    while i > 0:
        li.insert(len(li), li[i])
        i -= 1
    while len(li) > 1:
        
        #计数，数字内的加入到“队尾”，到数字的被pop出来
        for _ in range(feed-1):
            # for the 
            li.insert(len(li), li.pop(0))
                
        li_out.append(li.pop(0))
    
    
    print "winner is %s" % li.pop()
    print li_out
# Use Queue to solve the josef circle more easily 
class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def Josephus(name_list, num):
    name_queue = Queue()
    for name in name_list:
        name_queue.enqueue(name)
    #算法大概这样，一边出来，一边进入，每次数到那个数时，只出来，不进去
    while name_queue.size() > 1:
        for i in range(num-1):
            name_queue.enqueue(name_queue.dequeue())
        name_queue.dequeue()

    return name_queue.dequeue()


#print Josephus(range(1,101), 9)
    
#josef_circle(100, 9)
josef_circle_2(100, 9)