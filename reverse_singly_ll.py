import random

class single_ll:
    def __init__(self):
        self.next = None

class single_node:
    def __init__(self,val):
        self.val = val
        self.next = None

def create_random_ll(value):
    #head_single = single_ll()
    rdnum = random.randint(0,99)
    head = single_node(rdnum)
    for i in xrange(1,value):
        rdnum = random.randint(0,99)
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
def reverse_recursive(head):
    if head.next == None or head == None:
        return head
    print("pre head = %d, head.next = %d" % (head.val, head.next.val))
    reserved = reverse_recursive(head.next)
    print("head = %d, head.next = %d\n" % (head.val,head.next.val))
    head.next.next = head   # link next.next to itself, becuase current is head -1
    head.next = None        # cut next link
                            # recursive would memorize every previsous number

    return reserved

def reverse(head):
    if head.next == None:
        return head
    pt = head
    tmp = head.next      ## note: save before giving value
    pt.next = None
    while tmp != None:
            tmp_next = tmp.next # key: reverse way
            tmp.next = pt
            pt = tmp
            tmp = tmp_next
    return pt 

def main():
    a = create_random_ll(10)
    show(a)
    print('  \n')
    b = reverse_recursive(a)
    show(b)

if __name__ == "__main__":
    main()