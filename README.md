Intersection of
Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A: a1 → a2
↘
c1 → c2 → c3
↗
B: b1 → b2 → b3
begin to intersect at node c1.
Notes:
• If the two linked lists have no intersection at all, return null.
• The linked lists must retain their original structure after the function returns.
• You may assume there are no cycles anywhere in the entire linked structure.
• Your code should preferably run in O(n) time and use only O(1) memory.



The ListNode class defines a basic structure for a singly linked list node, where each node has a value and a reference to the next node.

The getIntersectionNode function takes two linked lists (headA and headB) as input and returns the node at which they intersect. If there is no intersection, it returns None.

The function calculates the lengths of both linked lists using a helper function getLength.

It then adjusts the starting points of the linked lists so that they have the same length from the intersection point to the end.

Finally, it traverses both linked lists simultaneously until it finds the intersection point. If there is no intersection, it returns None.

The example demonstrates the usage of the code by creating two linked lists (A and B) with an intersection at a specific node (c1) and then finding and printing the intersection node's value.
