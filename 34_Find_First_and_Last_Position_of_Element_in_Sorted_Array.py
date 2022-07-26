class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            begin = 0
            end = len(nums)-1
            pivot = 0
            while(end>=begin):
                pivot = begin + (end-begin//2)
                if nums[pivot] == target:   
                    if(isFirst):
                        if pivot == begin or nums[pivot-1]!=target:
                            return pivot
                        end = pivot - 1
                    else:
                        if pivot == end or nums[pivot+1]!=target:
                            return pivot
                        begin = pivot + 1
                        
                elif nums[pivot] > target:
                    end = pivot - 1
                    
                else:
                    begin = pivot + 1
                    
            return -1 
        
        return [findBound(True), findBound(False)]
