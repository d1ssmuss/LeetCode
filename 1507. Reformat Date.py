class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = str(months.index(date[1]) + 1)
        if len(month) == 1:
            month = '0' + month
        day = ''.join([i for i in date[0] if i.isdigit()])
        if len(day) == 1:
            day = '0' + day
        return f"{date[2]}-{month}-{day}"
