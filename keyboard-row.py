# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        resultado = []  # final result
        
        first_row = "qwertyuiop"  # 1st row of keyboard
        second_row = "asdfghjkl"  # 2nd row
        third_row = "zxcvbnm"     # 3rd row

        for w in words:  # runs through each word in the list of words
            word_lower = w.lower()  # converts to lowercase

            if not word_lower:  # if the word is empty, skip it
                continue

            primeira_letra = word_lower[0]  # gets the first letter of the word

            linha_candidata = None  # initialize candidate line
            if primeira_letra in first_row:
                linha_candidata = first_row
            elif primeira_letra in second_row:
                linha_candidata = second_row
            elif primeira_letra in third_row:
                linha_candidata = third_row

            palavra_valida = True  # assume the word is valid until proven otherwise
            for letra in word_lower:  # check each letter in the word
                if letra not in linha_candidata:  # if the letter is not in the candidate line
                    palavra_valida = False
                    break 

            if palavra_valida:  # in case the word is fully valid
                resultado.append(w)  # add to result list

        return resultado  
