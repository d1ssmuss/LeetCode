class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1_left, y1_bottom, x1_right, y1_top = rec1
        x2_left, y2_bottom, x2_right, y2_top = rec2
        x1_max = max(x1_left, x2_left)
        y1_max = max(y1_bottom, y2_bottom)
        x2_min = min(x1_right, x2_right)
        y2_min = min(y1_top, y2_top)
        return True if (x1_max <= x2_min and y1_max <= y2_min) and (x1_max - x2_min != 0 and y1_max - y2_min != 0) else False
