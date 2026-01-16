class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                if count >= k:
                    count = 0
                else:
                    return False
        return True
