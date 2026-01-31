class Solution:
    def nextGreatestLetter(self, letters, target):
        left,right = 0,len(letters)-1
        while left<=right:
            mid=(left+right)//2
            if letters[mid]>target:
                right= mid-1
            else:
                left=mid+1
        return letters[left%len(letters)]
        
print(Solution().nextGreatestLetter(["c","f","j"],"a"))