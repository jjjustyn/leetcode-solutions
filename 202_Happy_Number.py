class Solution:
    def isHappy(self, n: int) -> bool:
        #function adds the sum of the squares of the given numbers digits
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum+=digit**2
            return total_sum
        #create hash set because we will checking if there is a cycle often
        seen = set()
        #while n isnt 1 and there hasn't been a cycle, keep the process going
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
