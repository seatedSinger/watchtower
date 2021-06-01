# Fast | slow
def swapNodes(head, k):
    slow, fast = head, head 
    for _ in range(k-1):
        fast = fast.next 
    first = fast

    while fast.next:
        slow, fast = slow.next, fast.next
    first.val, slow.val = slow.val, first.val
    return head

head = [1,2,3,4,5]
k = 2

def solution2(head, k):
    n = 0
    beg = head
    while beg:
        if n == k:
            l = beg
            beg = beg.next
            n += 1
    r = head
    for i in range(n-k):
        r = r.next
    l.val, r.val = r.val, l.val
    return head

def solution3(head, k):
    first = last = head
    for i in range(1, k):
        first = first.next
    null_checker = first
    while null_checker.next:
        last = last.next
        null_checker = null_checker.next
    first.val, last.val = last.val, first.val
    return head
