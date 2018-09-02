
def find_low_index(arr,key):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low+high)/2           
        if key <= arr[mid]:
            high = mid-1
        else:
            low = mid+1
    if arr[low] == key:  ## not mid,it is low
        return low
    else:
        return -1

def find_high_index(arr,key):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low+high)/2    
        if key >= arr[mid]:
            low = mid+1
        else:
            high = mid-1
    if arr[high] == key:   ## not mid,it is high
        return high
    else:
        return -1

def main():
    a = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,15,15]
    b = [1,2,3,4,5,6,6,6]
    key = 6
    qql = find_low_index(b,key)
    qqh = find_high_index(b,key)
    print('low %d, high %d' % (qql,qqh))


if __name__ == "__main__":
    main()