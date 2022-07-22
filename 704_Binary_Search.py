class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left pointer points to beginning of array
        #right pointer points to last index in array
        lP = 0
        rP = len(nums)-1
        #while the left pointer is to the left of the right pointer
        while(lP<=rP): 
            #split the array in half
            pivot = lP + (rP-lP//2)
            #if the target is greater or less than the number at the halfway point search the other half
            if nums[pivot]>target:
                rP = pivot-1 
            elif nums[pivot]<target:
                lP = pivot + 1
            else:
                return pivot
        return -1
