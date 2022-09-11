class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n

        for first,last,seats in bookings:
            res[first-1]+=seats
            if last<n:
                res[last]-=seats
        
        for i in range(1,n):
            res[i]+=res[i-1]
        return res