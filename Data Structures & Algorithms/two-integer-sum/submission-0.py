class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            p=nums[i]
            n=target-p
            if n in a:
                return [a[n],i]
            a[p]=i