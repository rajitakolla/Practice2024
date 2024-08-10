#https://leetcode.com/explore/interview/card/google/67/sql-2/3045/
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        cmb = sorted([(i, x) for i, x in enumerate(arr)], key=lambda x:x[1])  # sort by value and keep index order
        nxt = [[None, None] for _ in range(len(arr))]   # [[odd_nxt, even_nxt]]
        S = []
        for i, _ in cmb:
            while len(S)>0 and S[-1]<=i:
                nxt[S.pop()][0] = i
            S.append(i)
        cmb.sort(key=lambda x:x[1], reverse=True)   # sort by value and keep index order
        S = []
        for i, _ in cmb:
            while len(S)>0 and S[-1]<=i:
                nxt[S.pop()][1] = i
            S.append(i)

        @cache
        def DP(i, is_even):
            if i == len(arr)-1: return True
            if nxt[i][is_even] is None: return False
            return DP(nxt[i][is_even], ~is_even)

        count = 0
        for i in range(len(arr)):
            if DP(i, 0) is True: count += 1

        return count