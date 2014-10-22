
def quick_sort(alist, low, high):
    if low < high:
        key = find_key(alist, low, high)
        quick_sort(alist, low, key-1)
        quick_sort(alist, key+1, high)
        
def find_key(alist, low, high):
    temp = alist[low]
    while low<high:
        while low < high and alist[high] >= temp:
            high = high -1 
        alist[low] = alist[high]
        while low < high and alist[low] <= temp:
            low = low + 1
        alist[high] = alist[low]
        
    alist[low] = temp
    return low
    
if __name__ == "__main__":
    alist = [2,5,3,4,1,9,7]
    quick_sort(alist, 0, len(alist)-1)
    print alist