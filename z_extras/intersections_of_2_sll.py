# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

'''

# Time: O(n+m) and Space: O(n)
# Runtime: 480 ms, faster than 5.07%
# Memory Usage:  30 MB, less than 24.17%
def getIntersectionNode(headA,headB):
    '''
    Travese a and add each node to a hashset
    then traverse b checking the first occurance in the hashset
    '''
    storage = {}
    while headA is not None:
        if headA.val in storage:
            storage[headA] += 1
        else:
            storage[headA] = 1
        headA = headA.next

    while headB is not None:
        if headB in storage:
            return headB
            break
        headB = headB.next
    

# Time: O(n+m) and Space: O(1)
# Runtime: 456 ms, faster than 6.91% 
# Memory Usage:  29.5 MB, less than 69.37%
def getIntersectionNode2(headA,headB):
    '''
    find a way to start from a node that will make both sll have equal distance to the end 
    independent of length actual distance.
    e.g:
    [4,1,8,4,5] starts from 4
    [5,6,1,8,4,5] starts from 6
    '''

    l1,l2 = headA,headB
        
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1

INPUT_LIST= [1,9,1,2,4]
INPUT_LIST2= [3,2,4]
print(getIntersectionNode(INPUT_LIST,INPUT_LIST2)) #output 2 (Intersected at '2') 
print(getIntersectionNode2(INPUT_LIST,INPUT_LIST2)) #output 2 (Intersected at '2') 
