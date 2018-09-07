# not familiar
import common as cm

def sorted_insert(head,node):
    if node == None:
        return head

    if head == None or node.val <= head.val : # need to insert head or before head
        node.next = head
        return node

    cur = head
    while cur.next != None:  ## cur
        if cur.next.val >= node.val:
            break
        cur = cur.next

    node.next = cur.next 
    cur.next = node

    return head

def insertion_sort(head):
    if head == None:
        return head

    sortedarr = None
    cur = head
    while cur != None:
        cur_next = cur.next
        sortedarr = sorted_insert(sortedarr,cur)
        cur = cur_next
    return sortedarr

def main():
    li = [2, 3, 5, 99, 6,8, 9]
    llact = cm.ll_action()
    a = llact.create_list_ll(li)
    llact.show(a)
    print("\n")
    b = insertion_sort(a)
    llact.show(b)

if __name__ == "__main__":
    main()