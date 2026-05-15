class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = set(nums.count(i) for i in nums)
        d = {i:[] for i in frequency}
        d = dict(sorted(d.items()))
        for j in nums:
            d[nums.count(j)].append(j)
        answ = []
        # print(d)
        for v in d.values():
            for i in sorted(v, reverse=True):
                answ.append(i)
        return answ
