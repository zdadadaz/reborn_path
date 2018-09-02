def move_zeros_to_left(A):
    #TODO: Write - Your - Code
    read = len(A)-1
    write = read
    while write>=0:
        if read < 0:
            A[write] = 0
            write = write -1
        elif(A[read] != 0):
            A[write] = A[read]
            write = write -1
        if read >= 0:  ## corner case has to be careful
            read = read-1   
    return A





def main():
    a = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,15,15]
    b = [1,2,3,4,0,5,6,0,6,0,6]
    key = 6
    qql = move_zeros_to_left(b)
    print(qql)
    #print('low %d, high %d' % (qql,qqh))


if __name__ == "__main__":
    main()