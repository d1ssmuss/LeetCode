def reverse(x):
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value
    to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    Если задано 32-разрядное целое число со знаком x, верните x с перевернутыми цифрами.
    Если при изменении x значение выходит за пределы диапазона 32-разрядных целых чисел
    со знаком [-231, 231 - 1], верните 0.

    Предположим, что среда не позволяет вам хранить 64-разрядные целые числа (со знаком или без знака).
    :param x:
    :return:
    """
    if not (-2 ** 31 <= x <= 2 ** 31 - 1):
        return 0
    else:
        if x < 0:
            str_x = str(x)[1:]
            number = int(f"{str(x)[0]}{int(str_x[::-1])}")
            if not (-2 ** 31 <= number <= 2 ** 31 - 1):
                return 0
            else:
                return number
        else:
            if not (-2 ** 31 <= int(str(x)[::-1]) <= 2 ** 31 - 1):
                return 0
            else:
                return int(str(x)[::-1])



a = reverse(int(input())) # -120 -> -21
print(a)
print(reverse(1534236469))