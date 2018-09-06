class single_node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_random_ll(li):
    #head_single = single_ll()
    rdnum = li[0]
    value = len(li)
    head = single_node(rdnum)
    for i in xrange(1,value):
        rdnum = li[i]
        a = single_node(rdnum)
        if i == 1:
            head.next = a
        else:
            tmp.next = a
        tmp = a
    return head
def show(ll):
    #ll = ll.next
    while ll != None:
        print(ll.val)
        ll = ll.next
def remove_duplicates_sample(head):
    if head == None:
        return head
    dup_set = set()
    dup_set.add(head.val)
    curr = head
    while curr.next != None: # key: move next value 
        if curr.next.val in dup_set:
            curr.next = curr.next.next # this way can do without previous
            #dont have to move, because it move next next to next
        else:
            dup_set.add(curr.next.val)
            curr= curr.next
    return head
def remove_duplicates(head):
    if head == None:
        return head
    hashtable =set()
    tmp = head.next
    prev = head 
    hashtable.add(head.val)
    while tmp != None:
        tmp_next = tmp.next
        if(tmp.val in hashtable):
            prev.next = tmp.next  #key: how to delete element
            tmp.next = None
        else:
            hashtable.add(tmp.val)
        tmp = tmp_next
    return head
def main():
    li = [2, 3, 5, 5, 6,8, 9]
    a = create_random_ll(li)
    show(a)
    print('  \n')
    b = remove_duplicates(a)
    show(b)

if __name__ == "__main__":
    main()