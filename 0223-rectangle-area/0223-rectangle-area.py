class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total_area=(ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        overlap_area=0
        xoverlap=min(ax2,bx2)-max(ax1,bx1)
        yoverlap=min(ay2,by2)-max(ay1,by1)
        if xoverlap>0 and yoverlap>0:
            overlap_area=xoverlap*yoverlap
        return total_area-overlap_area
        