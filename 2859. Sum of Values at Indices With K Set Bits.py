class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = [i for i in range(len(nums)) if str(bin(i)[2:]).count('1') == k]
        return sum([nums[i] for i in n])
