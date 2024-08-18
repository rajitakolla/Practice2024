#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3049/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        visited = {}

        for i,val in enumerate(nums):
            print(i,val)
            if val not in dups:
                dups.add(val)
                for j,val1 in enumerate(nums[i+1:]):
                    difference = -val - val1
                    if difference in visited and visited[difference] == i:
                        res.add(tuple(sorted((val, val1, difference))))

                    visited[val1] = i
        return res