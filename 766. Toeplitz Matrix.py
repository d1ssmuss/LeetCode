def isToeplitzMatrix(matrix):
    # Потом разобрать!!!
    # # end_x, end_y = len(matrix) - 1, len(matrix[0]) - 1\
    end_x, end_y = len(matrix), len(matrix[0]) # 3 4
    start_x, start_y = len(matrix) - 1, 0
    x, y = start_x, start_y
    numbers = []
    # Идём слева направо
    while (x != end_x and y != end_y) and (x >= 0 and y >= 0):
        nums = []
        while x >= 0 and y >= 0:
            nums.append(matrix[x][y])
            x -= 1
            y -= 1
        numbers.append(nums)
        if y != len(matrix[0]) - 1 and start_y + 1 <= end_y - 1:
            x, y = len(matrix) - 1, start_y + 1
            start_y = y
        else:
            x, y = start_x - 1, start_y
            start_x = x
        # print(x,y)
    numbers = numbers[1:len(numbers) - 1]
    for spisok in numbers:
        if len(list(set(spisok))) == 1:
            continue
        else:
            return False
    return True



print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isToeplitzMatrix([[1,2],[2,2]]))