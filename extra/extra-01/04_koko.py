import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # min k where sum(ceil(piles[i]/k)) <= h is also fills
        # sum(piles[i])/h <= k <= max(piles)/floor(h/n)

        lower_limit = math.ceil(sum(piles) / h)  # O(n)
        upper_limit = math.ceil(max(piles) / (h // len(piles)))  # O(n)

        # binary search
        def binary(left, right) -> int:  # O(log n)
            while left < right:
                mid = (left + right) // 2
                if sum([math.ceil(pile / mid) for pile in piles]) <= h:  # O(n)
                    # mid can be the minimum number to satisfy the condition
                    right = mid
                else:
                    # mid is too small to satisfy the conditions
                    left = mid + 1
            return left

        return binary(lower_limit, upper_limit)  # O(n log n)