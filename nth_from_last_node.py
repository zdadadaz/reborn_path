import common as cm
def find_nth_from_last(head, n):
    if head.val == None or n < 1: # n <1 is none
        return None
    count = n

    tail = head
    while count >0: # tail need not none
        count -= 1
        if(tail == None):
            return None
        tail = tail.next
    # Check out-of-bounds, 
    if n != 0:
        return None
    cur = head
    while tail != None:
        cur = cur.next
        tail = tail.next
    return cur


def main():
    llact = cm.ll_action()
    a = llact.create_random_ll(8)
    llact.show(a)
    print("\n")
    key = 4
    c = find_nth_from_last(a,key)
    llact.show(c)

if __name__ == "__main__":
    main()