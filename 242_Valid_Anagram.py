class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        #if the strings are the same length it wouldn't be possible for them to be anagrams, return false
        if len(s) != len(t):
            return False
        #insert all characters from string s into dict with corresponding value being their frequency
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
        #check if string t matches the keys and frequencies of s, if not return false
        for j in range(len(t)):
            if t[j] in d and d.get(t[j]) > 0:
                d[t[j]] = d.get(t[j]) - 1
            else:
                return False
        
        #this problem can also be done in nlogn time by sorting, but that is a more obvious solution
        
        return True
