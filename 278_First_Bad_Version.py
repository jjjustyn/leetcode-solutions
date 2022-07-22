# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #set left pointer to first version and right pointer to last version
        leftP = 1
        rightP = n
        #while the leftP is less than rightP
        while leftP < rightP:
            #calculate middle of interval
            pivot  = leftP + ((rightP-leftP)//2)
            #if it is a bad version we know we can discard the rest of the versions on the right
            if isBadVersion(pivot):
                rightP = pivot
                #if its not a bad version we know that the first bad version must be past this point
            else:
                leftP = pivot + 1
                
        return leftP
