class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split('-')
        year, month, day = int(date[0]), int(date[1]), int(date[2])
        days = 0
        for m in range(1, 13):
            if m == month:
                days += day
                break
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                days += 31
            elif m == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days += 29
                else:
                    days += 28
            else:
                days += 30
            print(days)
        return days
