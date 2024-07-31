from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        # This is necessary for the heap to compare ListNode objects
        return self.val < other.val

def mergeKLists(lists):
    min_heap = []
    
    # Insert the head of each list into the min-heap
    for l in lists:
        if l:
            heappush(min_heap, l)
    
    # Dummy node to start the merged list
    dummy = ListNode(0)
    current = dummy
    
    # Extract the smallest node and add to the merged list
    while min_heap:
        smallest_node = heappop(min_heap)
        current.next = smallest_node
        current = current.next
        if smallest_node.next:
            heappush(min_heap, smallest_node.next)
    
    return dummy.next

# Example usage:
# Constructing the lists:
# list1: 1 -> 4 -> 5
# list2: 1 -> 3 -> 4
# list3: 2 -> 6
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
merged_list = mergeKLists(lists)

# Print merged list:
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> 
