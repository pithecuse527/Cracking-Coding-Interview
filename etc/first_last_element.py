class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                runner1 = mid
                while runner1 >= 0 and target == nums[runner1]:
                    runner1 -= 1
                runner2 = mid
                while runner2 <= len(nums)-1 and target == nums[runner2]:
                    runner2 += 1
                return [runner1+1, runner2-1]
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]
                
s = Solution()
print(s.searchRange([1], 1))