#https://leetcode.com/explore/interview/card/google/67/sql-2/472/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.replace("-",'').upper()
        counter = k
        res = ""
        for i in range(len(s)-1,-1,-1):
            if counter != 0:
                res = s[i]+res
                counter -=1
            else:
                res = s[i]+'-'+res
                counter = k-1

        return res