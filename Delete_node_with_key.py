import common as cm

def delete_node(head, key):
    if head == None:
        return head
    prev = None
    cur = head
    while cur.next != None:
        if key == cur.val:
            if prev == None:
                cur_next = cur.next
                cur.next = None
                cur = cur_next      # 2. 
                head = cur          # 1. purpose 
            else:
                prev.next = cur.next
                prev = cur
                curr = cur.next
        else:
            prev = cur
            cur = cur.next
            
    return head
def main():
    li = [2, 3, 5, 99, 6,8, 9]
    llact = cm.ll_action()
    a = llact.create_list_ll(li)
    llact.show(a)
    print("\n")
    key = 2
    b = delete_node(a,key)
    llact.show(b)

if __name__ == "__main__":
    main()

    
