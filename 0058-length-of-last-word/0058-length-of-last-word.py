class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(s):
            if i != " ":
                count+=1
            elif count > 0:
                return count
        return count # ---> this extra return function is to prevent other testcases such as "moon"