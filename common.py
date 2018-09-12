import random as rd
class single_node:
    def __init__(self, val):
        self.val = val
        self.next = None
class ll_action:
    def create_random_ll(self,value):
        rdnum = rd.randint(0,99)
        head = single_node(rdnum)
        for i in range(1,value):
            rdnum = rd.randint(0,99)
            a = single_node(rdnum)
            if i == 1:
                head.next = a
            else:
                tmp.next = a
            tmp = a
        return head
    def create_list_ll(self,li):
        #head_single = single_ll()
        rdnum = li[0]
        value = len(li)
        head = single_node(rdnum)
        for i in range(1,value):
            rdnum = li[i]
            a = single_node(rdnum)
            if i == 1:
                head.next = a
            else:
                tmp.next = a
            tmp = a
        return head
    def show(self,ll):
        while ll != None:
            print(ll.val)
            ll = ll.next
    def insert_at_tail(self, listinput, node):
        cur = listinput
        while cur.next != None:
            cur = cur.next
        cur.next = node
        

