#https://leetcode.com/explore/interview/card/google/67/sql-2/3044/
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        split_domain_name = lambda x : x.split("@")
        res = [split_domain_name(email)[0].replace(".",'').split("+")[0]+"@"+split_domain_name(email)[1] for email in emails]
        return len(set(res))