def sum(s):
    if not s:
        return 0
    #初始化左边框右边框
    left = 0;
    right = 0
    #定义空字典
    dict_char = {}
    max_light = 0
    while right < len(s):
        if s[right] in dict_char and dict_char[s[right]] >= left:
            left = dict_char[s[right]] + 1
        dict_char[s[right]] = right
        max_light = max(max_light, right - left + 1)
        right += 1
    return max_light


if __name__ == '__main__':
    print(sum("abcddasdasczcqetyu"))
