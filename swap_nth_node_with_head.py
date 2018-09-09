import common as cm

def swap_nth_node(head, n):
    if head == None:
        return None
    elif n<2:
        return head

    pre = None
    cur = head
    while n > 1: 
        if cur == None:
            return None
        pre = cur
        cur = cur.next
        n -= 1

    pre.next = head
    tmp = head.next
    head.next = cur.next
    cur.next = tmp

    return cur

def main():
    llact = cm.ll_action()
    a = llact.create_random_ll(8)
    llact.show(a)
    print("\n")
    key = 4
    c = swap_nth_node(a,key)
    print("\n")
    llact.show(c)

if __name__ == "__main__":
    main()