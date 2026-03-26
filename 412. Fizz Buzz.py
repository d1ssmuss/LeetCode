class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answ = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answ.append('FizzBuzz')
            elif i % 3 == 0:
                answ.append('Fizz')
            elif i % 5 == 0:
                answ.append('Buzz')
            else:
                answ.append(str(i))
        return answ
