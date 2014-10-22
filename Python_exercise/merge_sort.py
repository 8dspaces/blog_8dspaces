#!/usr/bin/env python

def merge_sort(alist, low, high):
    """docstring for merge_sort"""
    if low < high:
        mid = (low + high) / 2
        merge_sort(alist, low, mid)
        merge_sort(alist, mid+1, high)
        merge(alist, low, mid, high)
        
def merge(alist, low, mid, high):
    left = alist[low:mid+1]
    right = alist[mid+1: high+1]
    for i in range(low, high+1):
        if left and right:
            if left[0] < right[0]:
                alist[i] = left.pop(0)
            else:
                alist[i] = right.pop(0)
        elif left:
            alist[i] = left.pop(0)
        elif right:
            alist[i] = right.pop(0)
            
if __name__ == '__main__':
    alist = range(100, 0, -1)
    merge_sort(alist, 0, len(alist) - 1)
    print alist