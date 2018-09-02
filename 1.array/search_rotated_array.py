def binarysearch(arr, key, st, end):
    if(st>end):
        return -1
    
    mid = (st+end)/2
    if arr[mid] == key:
        return mid

    #first two are for key in the sorted half array
    if arr[st] <= arr[mid] and arr[mid] > key and arr[st] <= key:
        return binarysearch(arr, key, st, mid-1)
    elif arr[mid] <= arr[end] and key > arr[mid] and arr[end] >= key:
        return binarysearch(arr, key, mid+1, end)
    elif arr[st] >=  arr[mid]:  ## when key in unsorted half,
        return binarysearch(arr, key, st, mid-1)
    elif arr[end] <=  arr[mid]:
        return binarysearch(arr, key, mid+1, end)

def binarysearch_main(arr, key):
    return binarysearch(arr, key,0, len(arr)-1)

def main():
	a = [4,5,6,1,2,3 ]
	qq = binarysearch_main(a,6)
	print(qq)


if __name__ == "__main__":
    main()