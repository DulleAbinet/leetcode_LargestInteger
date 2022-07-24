class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        
        for i in range(1,len(nums)):
            j=i
            while nums[j-1] + nums[j] < nums[j] + nums[j-1] and j >0:
                nums[j-1] , nums[j] = nums[j] , nums[j-1]
                j -= 1
                
        return str(int("".join(nums)))
