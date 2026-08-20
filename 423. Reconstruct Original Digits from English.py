from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        d = Counter(s)
        # print(d)
        nums = ''
        digits = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        even = {'z':'zero', 'w':'two', 'u':'four', 'x':'six', 'g':'eight'}
        odd = {'o':'one', 'r':'three', 'f':'five', 's':'seven', 'i':'nine'}
        for letter in even.keys():
            if letter in d.keys(): # буква цифры есть в строке (z, w, u, x, g)
                nums += digits[even[letter]] * d[letter] # записываем цифры
                # print(letter, even[letter])
                k = d[letter]
                for j in even[letter]: # проходим по буквам цифры (z e r o)
                    d[j] -= k
                    if d[j] == 0:
                        del d[j]
            # print(d, nums)
        # print(d, nums)
        for letter in odd.keys(): # o r f s n
            if letter in d.keys():
                nums += digits[odd[letter]] * d[letter]
                # print(letter, odd[letter])
                k = d[letter]
                for j in odd[letter]:
                    # d[j] -= k
                    if j == 'n':
                        d[j] //= 2
                    else:
                        d[j] -= k
                    if d[j] == 0:
                        del d[j]
            # print(d, nums)
        # print(d, nums)
        return ''.join(sorted(nums))
