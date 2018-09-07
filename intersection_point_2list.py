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
    while cur1 != None and cur2 != None:
        if count == 0:
            # shift 1
            if dif < 0:
                for i in xrange(0,abs(dif)):
                    cur2 = cur2.next
            else:
                for i in xrange(0,abs(dif)):
                    cur1 = cur1.next
        #check whether it is intersection
        if cur1 == cur2:
            return cur1
        cur1 = cur1.next
        cur2 = cur2.next
        count += 1
    return None

def intersect_sample(head1, head2):
  list1node = None
  list1length = get_length(head1)
  list2node = None
  list2length = get_length(head2)

  length_difference = 0
  if list1length >= list2length :
    length_difference = list1length - list2length
    list1node = head1
    list2node = head2
  else:
    length_difference = list2length - list1length
    list1node = head2
    list2node = head1

  while length_difference > 0:
    list1node = list1node.next
    length_difference-=1

  while list1node != None:
    if list1node == list2node:
      return list1node

    list1node = list1node.next
    list2node = list2node.next
  return None

def get_length(head):
  list_length = 0
  while head != None:
    head = head.next
    list_length+=1
  return list_length



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