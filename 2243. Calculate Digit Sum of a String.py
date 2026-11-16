class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        while True:
            new_s = ''
            for i in range(0, len(s), k):
                new_s += str(sum([int(i) for i in s[i:i + k]]))
            s = new_s
            if len(new_s) <= k:
                break
        return new_s




print(Solution().digitSum(s = "11111222223", k = 3))
print(Solution().digitSum(s = "233", k = 3))
