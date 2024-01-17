class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # Helper function to get the length of a linked list
    def getLength(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # Get the lengths of both linked lists
    lenA, lenB = getLength(headA), getLength(headB)

    # Move the longer linked list's head to make both lists equal in length
    while lenA > lenB:
        headA = headA.next
        lenA -= 1

    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Traverse both linked lists until an intersection is found
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None

# Example
# Create the linked lists A and B with an intersection at node C1
a1 = ListNode(1)
a2 = ListNode(2)
c1 = ListNode(3)
c2 = ListNode(4)
c3 = ListNode(5)
b1 = ListNode(6)
b2 = ListNode(7)
b3 = ListNode(8)

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3

b1.next = b2
b2.next = b3
b3.next = c1  # Intersection point

result = getIntersectionNode(a1, b1)
if result:
    print("Intersection found at node with value:", result.value)
else:
    print("No intersection found.")
