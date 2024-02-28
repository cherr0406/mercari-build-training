class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_idx_dict = {}  # {a: 0, b: 1, ...} -> {a: 3, b: 4, ...}
        max_length = 0
        idx_left = 0

        for idx in range(len(s)):
            if s[idx] in c_idx_dict.keys():  # O(len(c_idx_dict))
                # c has appeared in the current substring
                max_length = max(
                    max_length, idx - max(idx_left - 1, c_idx_dict[s[idx]])
                )
                idx_left = max(c_idx_dict[s[idx]] + 1, idx_left)
                c_idx_dict[s[idx]] = idx
            else:
                # c has not appeared in the current substring
                c_idx_dict[s[idx]] = idx
                max_length = max(max_length, idx - idx_left + 1)

        return max_length


# test
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("abcbacbed"))
    print(s.lengthOfLongestSubstring("dvda"))
    print(s.lengthOfLongestSubstring("abba"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))
