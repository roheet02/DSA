class Solution:
    def minBitwiseArray(self, nums):
        ans=[]
        for p in nums:
            found=-1
            for x in range(p+1):
                if (x|(x+1))==p:
                    found=x
                    break
            ans.append(found)
        return ans
print(Solution().minBitwiseArray([11,13,31]))