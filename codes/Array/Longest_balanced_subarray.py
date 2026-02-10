class Solution:
    def longestBalanced(self, nums):
        n=len(nums)
        length=0
        for i in range(n-1):
            even=set()
            odd=set()
            for j in range(i,n):
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(even)==len(odd):
                    length = max(length,(j-i)+1)
        return length
print(Solution().longestBalanced([2,2,1,3]))