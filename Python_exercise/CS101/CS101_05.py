def get_hash(keywords, size = 99):
    
    sum = 0
    for char in keywords:
        sum = (sum + ord(char)) % size 
    return sum
    
#    li = [] 
#    while sum > size:
#        li.append(str(sum % size))
#        sum = sum/size 
#    return "".join(li[::-1])
    
#print get_hash("mick")
#print get_hash("shdishid")

def make_large_index(size):
    index = []
    letters = ['a' for _ in range(8)]
    while len(index) < size:
        word = ''.join(letters)
        index.append(word)
        for i in range(len(letters)-1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i])+1)
                break
            else:
                letters[i] = 'a'        
        
    return index
    
def make_large_index_2(size):
    index = []
    letters = ['a' for _ in range(8)]
    i = len(letters)-1
    while size > 0:
        word = ''.join(letters)
        index.append(word)
        
        letters[i] = chr(ord(letters[i])+1)
        while letters[i] > 'z':
            letters[i] = 'a'
            i = i-1
            letters[i] = chr(ord(letters[i])+1)    
        i = len(letters)-1               
        size = size -1
    return index    
    
print make_large_index(100)