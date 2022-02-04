class Solution:
    def findStart(self, nums, target):
        left = 0
        right = len(nums)-1
        if nums[left] == target:
            return left

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid] and target != nums[mid-1]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1
    
    def findEnd(self, nums, target):
        left = 0
        right = len(nums)-1
        if nums[right] == target:
            return right

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid] and target != nums[mid+1]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1

    def searchRange(self, nums, target):
        # base case
        if len(nums) == 0:
            return [-1, -1]

        # find the starting point
        start = self.findStart(nums, target)

        # find the end point
        end = self.findEnd(nums, target)

        return [start, end]
                
s = Solution()
print(s.searchRange([1], 1))