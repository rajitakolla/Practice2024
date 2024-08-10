class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        numberOfCharacters = len(s)
        count = {}
        result = 0
        start = 0
        for i in range(numberOfCharacters):

            if s[i] in count:
                start = max(count[s[i]], start)


            result = max(result, i-start+1)
            count[s[i]] = i+1

        return result
