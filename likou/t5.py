class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        window = Counter()
        t_dict = Counter(t)
        min_str = s

        left = right = 0
        while right < len(s):
            c = s[right]  # 不是right+1，而是right. 因为此时window里面没有元素。
            window[c] += 1
            right += 1

            # debug
            print(f"window: [{left}, {right})", window)

            while (left < right and window > t_dict):
                # 收缩窗口前更新min_str
                if right - left < len(min_str):
                    min_str = s[left:right]
                    print(f"min_str: {min_str}")
                d = s[left]
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
                left += 1
                # 收缩窗口后更新min_str

            # print(f"min_str: {min_str}")

        return min_str


if __name__ == '__main__':
    s = Solution()
    s.minWindow("adsabdsa", "ads")
