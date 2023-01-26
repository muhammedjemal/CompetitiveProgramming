class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for first, last, seat in bookings:
            res[first - 1] += seat
            if last < n:
                res[last] -= seat
        return accumulate(res)
