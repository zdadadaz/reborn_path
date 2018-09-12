import common as cm

def merge_sorted(head1, head2):
    if head1 == None and head2 == None:
        return head1
    elif head1 == None:
        return head2
    elif head2 == None:
        return head1
    
    # init
    m_tail = None
    m_head = None
    cur1 = head1
    cur2 = head2
    if (cur1.val < cur2.val):
        m_head = cur1
        cur1 = cur1.next
    else:
        m_head = cur2
        cur2 = cur2.next
    m_tail = m_head
    # check the following list
    while cur1 != None and cur2 != None:
        if (cur1.val < cur2.val):
            m_tail.next = cur1 
            cur1 = cur1.next
        else:
            m_tail.next = cur2
            cur2 = cur2.next
        m_tail = m_tail.next

    # check the last few list after one list is finish
    if cur1 == None and cur2 != None:
        tmp = cur2 
        cur2 = cur1
        cur1 = tmp
    #cm.ll_action().show(m_head)
    #print("\n")
    if cur1 != None:
        m_tail.next = cur1 
        
    return m_head
def main():
    llact = cm.ll_action()
    li1 = [3,9, 14, 59, 90, 100]
    li2 = [6,10,15, 33, 56, 99]
    a = llact.create_list_ll(li1)
    b = llact.create_list_ll(li2)

    llact.show(a)
    print("\n")
    llact.show(b)
    print("\n")
    c = merge_sorted(a,b)
    print("\n")
    llact.show(c)

if __name__ == "__main__":
    main()