# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词
def new_list(l):
    dic = {}
    for i in l:
        sorted_list = "".join(sorted(i))
        if sorted_list in dic.keys():
            dic[sorted_list].append(i)
        else:
            dic[i] = [i]
    return dic.values()


# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题
def lianxu(nums):
    countlist = []
    count = 0
    for i in nums:

        countlist[count] = 0
        for j in i:
            if j + 1 == i[nums.index(i) + 1]:
                countlist[count] = countlist[count] + 1
            else:
                break;
    count+=1
    print(max(countlist))
    print(nums[max(countlist)])


if __name__ == '__main__':
    # l = ["cw", "abe", "eba", "bea", "wc", "gfd"]
    # print(new_list(l))
    b = ["1234", "5423", "3", "453", "123456"]
    lianxu(b)
