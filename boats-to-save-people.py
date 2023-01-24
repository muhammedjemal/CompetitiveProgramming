class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i= 0
        n=len(people) - 1
        while i <= n:
            if people[i] + people[n] <= limit: 
                n -= 1
            i += 1
        return i
