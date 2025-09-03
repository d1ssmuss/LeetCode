def majorityElement(nums):
    _set = set(nums) # O(1)
    for i in _set:
        if nums.count(i) > len(nums) / 2:
            return i


# print(majorityElement([2,2,1,1,1,2,2]))
