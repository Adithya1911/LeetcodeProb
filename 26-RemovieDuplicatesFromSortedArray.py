class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=len(nums)
        while i<j-1:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
                j-=1
            else:
                i+=1
        return j