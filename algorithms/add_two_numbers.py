"""
given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
dd the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 80

> assume n1 and n2 has the same number of digits
"""

from typing import Optional

class ListNode:
    def __init__(self,val=0, next=None):
        self.value = val
        self.next = next
    
    def __str__(self):
        head=self
        s = "["
        while head != None:
            s+=str(head.value) + ','
            head=head.next
        return s[:-1]+']'


def add_two_numbers(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    resultHead = ListNode()
    n3_ptr= resultHead
    n3_pptr = n3_ptr
    while head1 is not None or head2 is not None:
        d2 = head2.value if head2 != None else 0
        d1 = head1.value if head1 != None else 0
        n3_ptr.value += d1 + d2
        head1 = head1.next if head1 != None else None
        head2 = head2.next if head2 != None else None

        n3_ptr.next = ListNode()
        
        if n3_ptr.value > 9:
            n3_ptr.value = n3_ptr.value -10
            n3_ptr.next.value = 1
        n3_pptr = n3_ptr
        n3_ptr = n3_ptr.next
    if n3_ptr.value == 0:
        n3_pptr.next=None
    return resultHead

l1=ListNode(2, ListNode(4,ListNode(3)))
l2=ListNode(5, ListNode(6,ListNode(4)))

r = add_two_numbers(l1,l2)
print(r)
assert str(r) == "[7,0,8]"
r = add_two_numbers(ListNode(0),ListNode(0))
print(r)
assert str(r) == "[0]"
# assert add_two_numbers(l1,l2) == [7,0,8]
l1=ListNode(9, ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9, ListNode(9)))))))
l2=ListNode(9, ListNode(9,ListNode(9,ListNode(9))))
r = add_two_numbers(l1,l2)
print(r)
assert str(r) == "[8,9,9,9,0,0,0,1]"
r = add_two_numbers(l2,l1)
print(r)
assert str(r) == "[8,9,9,9,0,0,0,1]"

