class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        '''
        Вам предоставлена матрица из m x n символов boxGrid, представляющая вид поля сбоку. Каждая ячейка поля является одной из следующих:
        Камень "#"
        Неподвижное препятствие "*"
        Пустое ".'
        Ящик поворачивается на 90 градусов по часовой стрелке, 
        в результате чего некоторые камни падают под действием силы тяжести. 
        Каждый камень падает вниз, пока не наткнется на препятствие, другой камень или дно ящика.
        Сила тяжести не влияет на расположение препятствий, 
        а инерция от вращения ящика не влияет на горизонтальное положение камней.
        
        Гарантируется, что каждый камень в boxGrid будет лежать на препятствии, другом камне или дне коробки.
        
        Верните матрицу n x m, представляющую коробку, после вращения, описанного выше.
        '''
        # Пробуем транспанировать матрицу
        # rotated = [list(row) for row in zip(*boxGrid[::-1])] # Нужно потом разобраться как это работает
        m = len(boxGrid) # строки, длина строки
        n = len(boxGrid[0]) # столбцы, длина столбца
        rotatedBox = [['.' for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                rotatedBox[i][j] = boxGrid[m - 1 - i][j]
                # rotatedBox[j][m - 1 - i] = boxGrid[i][i]
        # for i in range(n):
        #     for j in range(m):
        #         rotatedBox[j][i] = boxGrid[m - 1 - j][i]
        # print(rotatedBox)

        for i in range(m):
            empty_cell = n - 1
            for j in range(n - 1, -1, -1): # иду с конца
                '''
                Начните повторение с нижней части поля 
                и для каждой пустой ячейки проверьте, 
                есть ли над ней какой-нибудь камень без препятствий между ними.
                '''
                if rotatedBox[i][j] == '*':
                    empty_cell = j - 1
                else:
                    if rotatedBox[i][j] == '#':
                        # rotatedBox[i][j] = '#'
                        rotatedBox[i][j] = '.'
                        rotatedBox[i][empty_cell] = '#'
                        empty_cell -= 1
        # print(rotatedBox)
        return [[rotatedBox[i][j] for i in range(len(rotatedBox))] for j in range(len(rotatedBox[0]))]


# print(Solution().rotateTheBox([["#",".","#"]]))
# print(Solution().rotateTheBox([["#",".","*","."], ["#","#","*","."]]))
print(Solution().rotateTheBox([["#","#","*",".","*","."], ["#","#","#","*",".","."], ["#","#","#",".","#","."]]))