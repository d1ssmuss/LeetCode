class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        count = 0
        curr_h, curr_m = map(int, current.split(":"))
        corr_h, corr_m = map(int, correct.split(':'))
        curr_minutes = curr_h * 60 + curr_m
        corr_minutes = corr_h * 60 + corr_m
        delta = corr_minutes - curr_minutes
        while delta != 0:
            if delta >= 60:
                delta -= 60
            elif 15 <= delta <= 60:
                delta -= 15
            elif  5 <= delta < 15:
                delta -= 5
            else:
                delta -= 1
            count += 1
        return count



a = Solution().convertTime('02:30', '04:35')
print(a)
print(Solution().convertTime('11:00', '11:01'))