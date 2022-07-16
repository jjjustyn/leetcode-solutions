class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #the length of each string serve as the bounds of the pointers
        S_LENGTH, T_LENGTH = len(s), len(t)
        
        sP = tP = 0
        
        while sp < S_LENGTH and tP < T_LENGTH:
            #moves both pointers right if they are pointing to the same letter
            if s[sP] == t[tP]:
                sP+=1
                tP+=1
            #moves only the t pointer right to see if the next letter in t will also be in s
            else:
                tP+=1
        #if the string s is a subsequence its pointer will have pointed past its last index  
        return sP == s_LENGTH