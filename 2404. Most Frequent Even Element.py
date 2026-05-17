class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        d = {i:nums.count(i) for i in nums if i % 2 == 0}
        print(d)
        for k,v in d.items():
            if v == max(d.values()):
                return k
        else:
            return -1
