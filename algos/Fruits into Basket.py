#https://leetcode.com/explore/interview/card/google/67/sql-2/3046/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        max_picked = 0
        n = len(fruits)
        for i in range(0,n):
            basket = set()
            for j in range(i, n):
                basket.add(fruits[j])
                if len(basket) <= 2:
                    max_picked = max(max_picked, j-i+1)
                elif len(basket) == 2:
                    break

        return max_picked



