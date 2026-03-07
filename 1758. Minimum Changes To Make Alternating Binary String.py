class Solution:
    def minOperations(self, s: str) -> int:
        count_1 = 0
        count_2 = 0
        n = len(s)
        for i in range(n):
            if i % 2 == 0:
                if s[i] == '0':
                    count_1 += 1
                else:
                    count_2 += 1
            else:
                if s[i] == '1':
                    count_1 += 1
                else:
                    count_2 += 1
        return count_1, count_2, min(count_1, count_2)



print(Solution().minOperations("1111")) # 2
print(Solution().minOperations("10")) # 0
print(Solution().minOperations("0100")) # 1
print(Solution().minOperations("110010")) # 2
print(Solution().minOperations("10010100")) # 3