from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False  # Fixed indentation issue

# Sample input to test the hasCycle method
def create_cycle_list():
    # Create nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    # Link nodes to form a cycle
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle

    return node1  # Return the head of the list

# Test the hasCycle method
solution = Solution()
head = create_cycle_list()
print(solution.hasCycle(head))  # Should print True since there is a cycle
