# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        splited_sentence = s.split()
        
        return " ".join(splited_sentence[:k])