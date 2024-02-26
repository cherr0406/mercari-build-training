class Solution:
    # Tried to minimize space complexity and actually time
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time complexity: O(n^2) where n=len(pattern), strictly O(n^n + m) where m=len(s)
        # Space complexity: O(n), strictly O(n) where n = the number of pattern, [1,n]
        p_dict = {}  # use dict to store correspondence of a pattern and a word
        idx = 0  # scan s from the head
        s += " "
        for c in pattern:  # O(n)
            if c in p_dict.keys():
                # if c is the known pattern, check if the same word
                if not (
                    p_dict[c] == s[idx : idx + len(p_dict[c])]
                    and s[idx + len(p_dict[c])] == " "
                ):
                    return False
                else:
                    idx = idx + len(p_dict[c]) + 1
            else:
                # if not, check the word is new and store it in p_dict
                tmp_i = s.find(
                    " ", idx
                )  # O(m) but overall, this turns to be scan the entire s only once
                if s[idx:tmp_i] in p_dict.values():  # O(n)
                    return False
                p_dict[c] = s[idx:tmp_i]
                idx = tmp_i + 1
        # check pattern and s is the same numbers
        if idx == len(s):
            return True
        return False

    # Tried to minimize theoretical time complexity
    def wordPattern2(self, pattern: str, s: str) -> bool:
        # Time complexity: O(n) where n=len(pattern), strictly O(n + m) where m=len(s)
        # Space complexity: O(n)
        p_dict = {}
        words = s.split()  # O(m)
        p_set, w_set = set(pattern), set(words)  # O(n), O(n)

        if not len(p_set) == len(w_set) or not len(pattern) == len(words):  # O(1)
            return False

        for i in range(len(pattern)):  # O(n)
            if pattern[i] in p_dict.keys():  # O(1)
                if not p_dict[pattern[i]] == words[i]:
                    return False
            else:
                p_dict[pattern[i]] = words[i]

        return True
