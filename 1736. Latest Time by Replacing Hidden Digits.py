class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        h1, h2, _, m1, m2 = t
        if h1 == '?':
            h1 = '2' if h2 == '?' or int(h2) <= 3 else '1'
        if h2 == '?':
            h2 = '9' if int(h1) <= 1 else '3'
        if m1 == '?':
            m1 = '5'
        if m2 == '?':
            m2 = '9'
        return f"{h1}{h2}:{m1}{m2}"
        
