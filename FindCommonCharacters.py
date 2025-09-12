# https://leetcode.com/problems/find-common-characters/description/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        set1 = set(words[0]) # b e l a | c o l | 
        set2 = set(words[1]) # l a b e | l o c k
        set3 = set(words[2]) # r o l e | c o k

        intersection = set1 & set2 & set3
        intersection_list = list(intersection)

        result = []

        for candidate_char in intersection_list:
            count_in_word1 = words[0].count(candidate_char) # c1, o2, l1 | b1, a2, l2
            count_in_word2 = words[1].count(candidate_char) # l1, o1, c1, k1 | l2, a1, b1, e1
            count_in_word3 = words[2].count(candidate_char) # c1, o2, k1 | r1, o1, l2, e1, r1

            minimum_frequency = min(count_in_word1, count_in_word2, count_in_word3)

            for i in range(minimum_frequency):  # loop running 3 times
                result.append(candidate_char)
                
        return result
    
'''
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''