# 给你一个整数数组 nums 和一个整数 k ，12345
# 请你统计并返回 该数组中和为 k 的子数组的个数 。
def count_subarrays(nums, k):
    count = 0  # 初始化计数器为 0
    current_sum = 0  # 初始化当前子数组的和为 0
    subarray_sums = {}  # 创建一个字典，用于存储子数组和及其出现次数
    for num in nums:  # 遍历数组 nums
        current_sum += num  # 更新当前子数组的和
        if current_sum == k:  # 如果当前子数组的和等于 k，则计数器加 1
            count += 1
        # 计算以当前位置结尾的子数组的和与 k 的差值
        diff = current_sum - k
        # 如果差值在之前出现过，则将其出现次数加到计数器中
        if diff in subarray_sums:
            count += subarray_sums[diff]
        # 更新当前子数组的和及其出现次数
        subarray_sums[current_sum] = subarray_sums.get(current_sum, 0) + 1
    return count  # 返回结果


if __name__ == '__main__':
    print(count_subarrays([1, 2, 3, 4, 5], 8))
