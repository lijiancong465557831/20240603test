def length_of_longest_substring(s):
    n = len(s)
    max_length = 0
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            if len(set(s[i:j])) == j - i:
                max_length = max(max_length, j - i)
    return max_length


# print(length_of_longest_substring("aabcdeef"))
i = "1234"
print(i[1:11])
