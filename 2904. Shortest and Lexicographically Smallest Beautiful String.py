class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if set(s) == {'0'}:
            return ''
        else:
            n = len(s)
            arr = {}
            for i in range(n):
                for j in range(i, n):
                    # print(s[i:j + 1])
                    if s[i:j + 1].count('1') == k:
                        arr[s[i:j + 1]] = len(s[i:j + 1])
            mn = []
            print(arr)
            for key,v in arr.items():
                if v == min(arr.values()):
                    mn.append(key)
            return min(mn) if len(mn) != 0 else ''
