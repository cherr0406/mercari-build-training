class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Actual speed and simplicity
        # Time complexity: O(n)
        # Space complexity: O(n) for creating sets
        return set(range(1, len(nums) + 1)) - set(nums)  # O(n)

    def findDisappearedNumbers2(self, nums: list[int]) -> list[int]:
        # Time complexity: O(n)
        # Space complexity: O(1) except for answer
        for num in nums:  #  O(n)
            # index of nums <- store if the number(index+1) exist
            # assign not -1 but its negative bc nums is used to the condition of this loop
            # using abs() allows duplication
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

    def findDisappearedNumbers3(self, nums: list[int]) -> list[int]:
        # simple list
        # Time complexity: O(n)
        # Space complexity: O(n) for creating sets
        appeared = [False] * len(nums)
        for n in nums:
            appeared[n - 1] = True
        return [i + 1 for i in range(len(nums)) if not appeared[i]]  # O(n)
