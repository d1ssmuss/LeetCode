from collections import Counter


class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x4, x^2, x]
        # k - неотрицательная степень 2-ки
        count_one = nums.count(1)
        mx = 0
        d = Counter(nums)
        del d[1]
        for k in d.keys():
            subset = 0
            while k in d.keys():
                if d[k] >= 2:
                    subset += 2
                    if (k * k) not in d:
                        subset -= 1
                        break
                    k *= k
                else:
                    subset += 1
                    break
            mx = max(mx, subset)
        return max(mx, count_one) if count_one % 2 != 0 or count_one == 0 else max(mx, count_one - 1)






print(Solution().maximumLength([5, 4, 1, 2, 2])) # 3
print(Solution().maximumLength([1, 3, 2, 4])) # 1
print(Solution().maximumLength([4,123, 234, 123, 23, 556])) # 1
print(Solution().maximumLength([4,36,9,16,1,1,4,121,64,4])) # 3
print(Solution().maximumLength([65025,312481,107584,148996,322624,194481,570025,15376,123904,848241,88804,47961,117649,66564,295936,271441,16900,474721,27556,285156,11236,175561,917764,968256,16,38025,312481,426409,354025,8464,522729,60516,210681,378225,638401,101124,697225,427716,262144,940900,988036,324900,151321,309136,178929,168921,189225,4,301401,659344,786769,964324,15625,302500,56644,61504,31684,369664,345744,19321,59049,5041,40000,147456,372100,708964,171396,214369,707281,484,49729,82944,100489,103684,58564,208849,946729,84100,4,600625,334084,683929,9604,245025,97969,147456,160801,434281,223729,294849,166464,432964,518400,376996,17424,315844,256,737881,10000,632025])) # 3
print(Solution().maximumLength([1,16,49,16,121])) # 1
print(Solution().maximumLength([1,1,1,1,1,1,1,1,1,1,2,4,8,16,32,64,128,256,512,1024])) # 9
print(Solution().maximumLength([14,14,196,196,38416,38416])) # 5
