# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
# 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
def a(nums):
    oklist = []
    for i in nums:
        for j in nums:
            for k in nums:
                if (i != j and j != k and i != k) and (i + j + k == 0):
                    o = []
                    o.append(i), o.append(j), o.append(k)
                    o.sort()
                    if o not in oklist:
                        oklist.append(o)
    return oklist


if __name__ == '__main__':
    print(a([-1, 3, -2, 9, -8]))
