# not familiar
def partition(a,s,e):
    i = s
    j = e
    pivot = a[s]
    while i<j:
        while i<=e and a[i]<= pivot:
            i = i+1
        while j>=s and a[j]> pivot:
            j = j-1
        if(i<j):
            a[i],a[j] = a[j],a[i]
    a[s] = a[j]
    a[j]= pivot

    return j
def quick_sort_rec(a, s, e):
    if s<e:
        pivot = partition(a,s,e)
        quick_sort_rec(a, s, pivot-1)
        quick_sort_rec(a, pivot+1,e)
        
def quick_sort(a):
  quick_sort_rec(a, 0, len(a) - 1)

def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [55,23,26,2,18,78,23,8,2,3]
    qq = quick_sort(b)
    print(b)

if __name__ == "__main__":
    main()