class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for i in range(len(index)):
            arr = arr[:index[i]] + [nums[i]] + arr[index[i]:]
        return arr
