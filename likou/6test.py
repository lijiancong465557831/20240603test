def length_of_longest_substring(s: str) -> int:
    max_length = 0  # 记录最大长度
    left = 0  # 滑动窗口的左边界
    char_set = set()  # 存储窗口内的字符集合

    for right in range(len(s)):
        # 如果右指针指向的字符已经在窗口内，则移动左指针直到窗口内不再包含重复字符
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # 将当前字符加入窗口内
        char_set.add(s[right])
        # 更新最大长度
        max_length = max(max_length, right - left + 1)

    return max_length


# 测试示例
print(length_of_longest_substring("abbcabcbb"))  # 输出 3
