class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = []
        for m in range(1, n + 1):
            for v in range(m, n + 1):
                if m != v:
                    d = nod(m, v)
                    eq = f"{m // d}/{v // d}"
                    if eq not in nums:
                        nums.append(eq)
        return nums

def nod(n, k):
    while n - k != 0:
        if n > k:
            n -= k
        else:
            k -= n
    return n

print(nod(25, 100))
print(nod(2, 4))
print(Solution().simplifiedFractions(2))
print(Solution().simplifiedFractions(4))
print(Solution().simplifiedFractions(3))
