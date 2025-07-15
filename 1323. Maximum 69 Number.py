def maximum69Number(num):
    """
    :type num: int
    :rtype: int
    """
    num = str(num).replace("6", "9", 1)
    return int(num)


a = maximum69Number(int(input()))
print(a)