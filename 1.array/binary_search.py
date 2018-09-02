#a is sorted list
def binary_search_recursive(a, key,start, end):
	if start>end:
		return -1
	mid = (start+end)/2
	if a[mid] == key:
		return mid
	if a[mid]<key:
		start = mid+1
	else:
		end = mid-1
	return binary_search_recursive(a, key,start, end)

def binary_search_recursive_main(a,key):
	return binary_search_recursive(a,key,0,len(a)-1)

def binary_search(a, key):
  	#TODO: Write - Your - Code
  	low = 0
  	high = len(a)-1
  	mid = high
  	while low <= high:   ## corner case 0 and last one
  		mid = (low + high)/2
  		#print(mid)
		if a[mid]==key:
  			return mid
		elif a[mid]<key:
  			low = mid+1  ## mid is not the value, so add 1 is necessary
  		else:
			high = mid-1
	return -1



def main():
	a = [1, 40, 60, 80, 100, 200, 444, 9999]
	key = 1
	qq = binary_search(a,key)
	qq2 = binary_search_recursive_main(a,key)
	print(qq)
	print(qq2)
	# my code here

if __name__ == "__main__":
    main()
  