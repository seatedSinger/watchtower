'''
1. Find middle of LL
2. Rev from middle
3. Compare LL from start and from mid
4. With LL need > proper head references
'''
def isPlaindrome(head):
    cur = head
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
#* Reversal
    node = None
    while slow:
        slow.next, node, slow = node, slow, slow.next
        # tmp = slow.next
        # slow.next = node 
        # node = slow
        # slow = tmp
    while node:
        if node.val != cur.val:
            return False
        node = node.next
        cur = cur.next
    return True

'''
def reverseLL(head):
    prev = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    # head = head.next #* Nope
    return prev


def revLLinplace(head):
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
'''
