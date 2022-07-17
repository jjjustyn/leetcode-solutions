class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #declare dictionary to hold unique key value pairs of letters from each string
        d = dict()
        #for the entire length of the strings
        for i in range(0, len (s)):
            #check if the current pair is in the dictionary
            if (s[i], t[i]) not in d.items():
                #if either of them are already in the dictionary the strings are not isomorphic
                if s[i] in d.keys() or t[i] in d.values():
                    return False
                else:
                    d[s[i]] = t[i]
        return True
        