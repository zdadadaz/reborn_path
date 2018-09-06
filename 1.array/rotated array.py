#unfinish
def rotateArray(arr,n):
	arr.reverse()
	arr1 = arr[0:n-1]
	#print(arr[1:2])
	#print(arr)
	arr1.reverse()
	arr[-(n-1):-1] = arr1
	arr1 = arr[0:-(n+1)]
	arr1.reverse()
	arr[0:-(n+1)] = arr1
	return arr



def main():
	a = [4,5,6,1,2,3]
	#print(a[0:1])
	qq = rotateArray(a,2)
	print(qq)


if __name__ == "__main__":
    main()