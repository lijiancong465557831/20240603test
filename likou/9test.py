def length_of_longest_substring(s):
    if not s:
        return 0
    # 初始化窗口的左右边界和用于存储字符的字典
    left, right = 0, 0
    char_dict = {}
    max_length = 0
    while right < len(s):
        if s[right] in char_dict and char_dict[s[right]] >= left:
            # 如果当前字符已经在字典中，并且其位置大于等于左边界，那么更新左边界
            left = char_dict[s[right]] + 1
        # 将当前字符的位置存入字典
        char_dict[s[right]] = right
        # 更新最大长度
        max_length = max(max_length, right - left + 1)
        # 移动右边界
        right += 1
    return max_length
if __name__ == '__main__':
    length_of_longest_substring("abcaaa")