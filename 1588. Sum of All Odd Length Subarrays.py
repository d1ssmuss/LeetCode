class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # n = len(arr) - 1 if len(arr) % 2 == 0 else len(arr) - это шаг?
        # n = len(arr)
        # s = 0
        # for step in range(1, n + 1, 2):
        #     # print(step)
        #     for j in range(0, n - step + 1):
        #         print(arr[j:j + step])
        #         s += sum(arr[j:j + step])
        # return s
        n = len(arr)
        s = 0
        for i in range(0, n):
            for j in range(i, n):
                if (i + j) % 2 == 0:
                    print(arr[i:j + 1])
                    s += sum(arr[i:j + 1])
        return s
