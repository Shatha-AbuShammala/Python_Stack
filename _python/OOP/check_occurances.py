class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        return len(set(count.values())) == 1