class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([i for i in patterns if i in word])


print(Solution().numOfStrings(['a', 'abc', 'bc', 'd'], 'abc'))
