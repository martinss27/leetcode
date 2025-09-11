# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_s = "".join(word1)
        word2_s = "".join(word2)

        return word1_s == word2_s