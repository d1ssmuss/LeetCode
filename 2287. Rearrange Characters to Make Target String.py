class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        # I hate myself for this code...
        # Чтобы слово было построено, нужно чтобы все буквы из target были <= по количеству букв из s
        d_s = {i:s.count(i) for i in set(s) if i in target}
        d_t = {i:target.count(i) for i in set(target)}
        print(d_s, d_t)
        for letter in target:
            if target.count(letter) > s.count(letter):
                return 0
        answ = []
        for k,v in d_s.items():
            answ.append(v // d_t[k])
        return min(answ)
        # return 1 if d_s.values() == d_t.values() else min(d_s.values())
