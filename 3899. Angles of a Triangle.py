import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        a, b, c = sides[0], sides[1], sides[2]
        if a + b > c and a + c > b and b + c > a:
            return [math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180 / math.pi, math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * 180 / math.pi, math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * b * a)) * 180 / math.pi]
        else:
            return []
