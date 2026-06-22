class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i in bracket_map:
                poplist = stack.pop() if stack else '#'

                if bracket_map[i] != poplist:
                    return False
            else:
                stack.append(i)
        
        return not stack
