import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # else:
        #     x = math.log(n, 4)
        #     if x - int(x) != 0:
        #         return False
        #     else:
        #         return True
        
        # переводим в СС = 4
        # и ищем паттерн 1000000000..0
        if n <= 0:
            return False
        else:
            n_4 = ''
            while n != 0:
                n_4 += str(n % 4)
                n //= 4
            n_4 = n_4[::-1]
            if n_4[0] == '1' and n_4[1:] == '0' * (len(n_4) - 1):
                return True
            else:
                return False
