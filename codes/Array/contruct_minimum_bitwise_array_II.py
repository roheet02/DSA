class Solution:
    def minBitwiseArray(self, nums):
        ans=[]
        for n in nums:
            if n!=2:
                ans.append(n-((n+1)&(-n-1))//2)
            else:
                ans.append(-1)
        return ans        
print(Solution().minBitwiseArray([2,3,5,7]))