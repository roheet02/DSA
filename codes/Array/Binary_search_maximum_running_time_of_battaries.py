class Solution:
    def maxRunTime(self, n, batteries):
        total = sum(batteries)  #total energy available
        left, right = 0, total // n #the answer cannot exceed total // n (average time)
        
        while left < right:   #binary search for the maximum feasible time
            mid = (left + right + 1) // 2 
            #calculate how many minutes we can support across all computers
            #if each computer must run for 'mid' minutes
            usable = 0
            for b in batteries:
                usable += min(b, mid)
                #small optimization: if we already have enough, stop early
                if usable >= n * mid:
                    break
            #if sum(min(bi, mid)) >= n * mid, time 'mid' is feasible
            if usable >= n * mid:
                left = mid   # try longer time
            else:
                right = mid - 1  # try shorter time
        return left
        
print(Solution().maxRunTime(3,[3,4,5,6]))