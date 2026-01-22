class Solution:
    def minimumPairRemoval(self, nums):
        operations = 0
        # Function to check if array is non-decreasing
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        # Keep performing operations until array becomes non-decreasing
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            index = 0
            # Find the adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i
            # Merge the selected pair
            nums = nums[:index] + [min_sum] + nums[index + 2:]
            operations += 1
        return operations
print(Solution().minimumPairRemoval([5,2,3,1]))
print(Solution().minimumPairRemoval([1,2,2]))