class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -=1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -=1

            nums[i], nums[j] = nums[j], nums[i]

        v1 = i+1
        v2 = len(nums) - 1

        while v1<v2:
            nums[v1], nums[v2] = nums[v2], nums[v1]
            v1 = v1+1
            v2 = v2-1