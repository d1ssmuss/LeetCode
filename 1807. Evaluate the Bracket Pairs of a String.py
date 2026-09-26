import re
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        keys = re.findall(r'\(([^)]*)\)', s) # <-- ?
        d = {i[0]:i[1] for i in knowledge}
        for i in keys:
            if i in d.keys():
                s = s.replace(f"({i})", d[i])
            else:
                s = s.replace(f"({i})", '?')
        return s
