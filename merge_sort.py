import common as cm
def merge_two_ll(ll1, ll2):
    if ll1 == None and ll2 == None:
        return None
    elif ll1 == None:
        return ll2
    elif ll2 ==None:
        return ll1

    # merge first node
    cur1 = ll1
    cur2 = ll2
    if ll1.val < ll2.val:
        sortedhead = ll1
        ll1= ll1.next
    else:
        sortedhead = ll2
        ll2 = ll2.next
    sorted = sortedhead
    # merge two sorted array
    cur1 = ll1
    cur2 = ll2
    while cur1 != None and cur2 != None:
        if cur1.val < cur2.val:
            temp = cur1
            cur1 = cur1.next
        else:
            temp = cur2
            cur2 = cur2.next
        sorted.next = temp
        sorted = temp
    # check if different length
    if cur1 == None and cur2 != None:
        sorted.next = cur2
    if  cur2 == None and cur1 != None:
        sorted.next = cur1
    
    return sortedhead

def split_arr(head, leftright):
    if head == None:
        temp = (None,None)
        leftright = temp

    if head.next == None:
        temp = (head, None)
        leftright = temp
    
    else:
        # fast, low, two pointer to find the middle point
        slow = head
        fast = head.next
        while fast != None: 
            fast = fast.next
            if fast != None: # all fast
                slow = slow.next
                fast = fast.next
        tmp = (head, slow.next) # slow.next 
        slow.next = None # terminate first linked list, why?
        leftright = tmp
    return leftright

def merge_sort(head):
    if (head == None or head.next == None): # stop condition should be careful
        return head
    first_second = (None,None)
    first_second = split_arr(head, first_second) # use two list to record left and right linked list
    temp = (merge_sort(first_second[0]), merge_sort(first_second[1])) # for right
    first_second = temp

    return merge_two_ll(first_second[0],first_second[1])

def main():
    llact = cm.ll_action()
    a = llact.create_random_ll(10)
    llact.show(a)
    print("\n")
    c = merge_sort(a)
    print("\n")
    llact.show(c)

if __name__ == "__main__":
    main()