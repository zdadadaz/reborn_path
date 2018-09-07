import common as cm

def intersect(head1, head2):
    if head1 == None or head2 == None:
        return -1
    #check linked list length
    cur = head1
    len1 = 0
    while cur != None:
        len1 += 1
        cur = cur.next
    cur = head2
    len2 = 0
    while cur != None:
        len2 += 1
        cur = cur.next
    dif = len1 - len2
    count = 0
    cur1 = head1
    cur2 = head2
    # check intersection
    while count < max(len1,len2):
        if count == 0:
            # shift 1
            if dif < 0:
                for i in xrange(0,abs(dif)):
                    cur1 = cur1.next
                cur2 = cur2.next
            else:
                for i in xrange(0,abs(dif)):
                    cur2 = cur2.next
                cur1 = cur1.next
            #check whether it is intersection
            if cur1.val == cur2.val:
                return cur1
        else:
            cur1 = cur1.next
            cur2 = cur2.next
        
        if cur1.val == cur2.val:
            return cur1
        count += 1
    return -1
        

def main():
    llact = cm.ll_action()
    a = llact.create_random_ll(5)
    b = llact.create_random_ll(7)
    node1 = cm.single_node(8)
    node2 = cm.single_node(9)
    llact.insert_at_tail(a, node1)
    llact.insert_at_tail(a, node2)
    llact.insert_at_tail(b, node1)
    llact.show(a)
    print("\n")
    llact.show(b)
    print("\n")
    c = intersect(a,b)
    llact.show(c)

if __name__ == "__main__":
    main()