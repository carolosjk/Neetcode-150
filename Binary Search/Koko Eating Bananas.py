class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        i,j = 1, max(piles)
        rate = j

        while i <= j:
            m = (j+i) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)

            if hours > h:
                i = m+1
            else:
                j = m-1
                rate = m

        return rate
