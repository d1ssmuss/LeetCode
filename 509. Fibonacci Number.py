class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = []
        for i in range(n + 1):
            if i <= 1:
                f.append(i)
            else:
                f.append(f[i - 1] + f[i - 2])
        return f[n]
