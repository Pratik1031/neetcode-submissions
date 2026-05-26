class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else :
            count = {}
            for i in s :
                count[i] = count.get(i,0) +1
            for i in t :
                count[i] = count.get(i,0) -1
            return all(val == 0 for val in count.values())