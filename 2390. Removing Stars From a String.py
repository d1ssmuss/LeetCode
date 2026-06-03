class Solution:
    def removeStars(self, s: str) -> str:
        stack = ''
        for i in s:
            if i != '*':
                stack += i
            else:
                stack = stack[0:len(stack) - 1]
        return stack
