from collections import deque

def find_max_sliding_window(arr, window_size):
	window = deque()
	arrlen = len(arr)
	result = []
	#left head, right tail
	#popleft/appendleft, pop/popleft
	# first window
	for i in xrange(window_size): 
		if i < arrlen:
			#print(len(window))
			while len(window) != 0 and arr[i]>arr[window[0]]:
				window.pop()
			window.append(i)
			#print(window[0])
	#print(arr[window[-1]])
	result.append(arr[window[-1]])
	if window_size>arrlen:
		return arr[window[-1]]

	#sliding window
	for i in xrange(window_size,arrlen): 
		while len(window) != 0 and arr[i]>arr[window[0]]:
			window.pop()
		#print('i = %d' % (i))
		window.append(i)
		#print(window[-1])

		#popleft
		while len(window) != 0 and window[-1]<=i-window_size: ## be careful the conition
			window.popleft()
		#print(arr[window[0]])
		result.append(arr[window[-1]])
	
	return result



def main():
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	qq = find_max_sliding_window(a,4)
	print(qq)


if __name__ == "__main__":
    main()
  