class Solution:
    def longestPalindrome(self, s: str) -> int:
        #create dictionary to contain all unique letters in string
        letter_set = dict()
        #iterate through string, counting the amount of times each letter appears
        for i in range(0, len(s)):
            letter_set[s[i]] = letter_set.get(s[i], 0) + 1
        
        pal_len = 0
        #iterate through the values counted, for each pairing of letters count two as well as one unique middle character
        for val in letter_set.values():
            pal_len += val // 2 *2
            
            if pal_len % 2 == 0 and val % 2 == 1:
                pal_len += 1
        
        return pal_len
