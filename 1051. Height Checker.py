class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        """
        Школа пытается ежегодно фотографировать всех учеников.
        Учеников просят встать в шеренгу в неубывающей последовательности по росту. 
        Пусть этот порядок будет представлен целочисленным массивом expected, где expected[i] - ожидаемый рост i-го ученика в очереди.

        Вам будет предоставлен целочисленный массив heights, представляющий текущий порядок расположения учеников.
        Каждый рост [i] равен росту i-го ученика в очереди (с индексом 0).

        Возвращает количество индексов, где heights[i] != expected[i].
        """
        count = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count




print(Solution().heightChecker([1,1,4,2,1,3]))
print(Solution().heightChecker([5,1,2,3,4]))
print(Solution().heightChecker([1,2,3,4,5]))
