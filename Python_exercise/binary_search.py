def binary_search(lis, n):
    low = 0
    high = len(lis)
    
    while low <= high:
        mid = (low + high) / 2 
        if lis[mid] == n:
            return mid
        elif lis[mid] < n:
            low = mid + 1
        else:
            high = mid -1
    return None 

def binary_search_2(alist, n, low, high):
    
    if low <= high:
        mid = (low+ high) / 2
        if alist[mid] == n:
            return mid
        elif alist[mid] < n:
            return binary_search_2(alist, n, mid+1, high)
        else:
            return binary_search_2(alist, n, low, mid-1)
    return None 
    
if __name__ == "__main__":
    
    alist = [7, 8, 29,33,24,12,5,9,20]
    alist = sorted(alist)
    print alist 
    print binary_search(alist, 20)
    print binary_search_2(alist, 20, 0, len(alist))