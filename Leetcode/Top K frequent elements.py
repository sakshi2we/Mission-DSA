from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = Counter(nums)
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        l = []
        for i in range(k):
            l.append(sorted_items[i][0])
        
        return l