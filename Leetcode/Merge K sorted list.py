# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):  # Fixed __init__
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        newList = ListNode(0)
        temporary_list = newList

        def getSmallestNode():
            min_index = -1
            for i in range(len(lists)):
                if lists[i] is not None:
                    if min_index == -1 or lists[i].val < lists[min_index].val:
                        min_index = i
            if min_index == -1:
                return None
            smallest_node = lists[min_index]
            lists[min_index] = lists[min_index].next
            return smallest_node

        while True:
            node = getSmallestNode()
            if node is None:
                break
            temporary_list.next = node
            temporary_list = temporary_list.next
        
        return newList.next
