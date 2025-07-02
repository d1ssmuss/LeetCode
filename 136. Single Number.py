def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] *= -1
        return sum(nums) * -1

# print(singleNumber([4,1,2,1,2]))
# print(singleNumber([1]))