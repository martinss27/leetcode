# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        resultado = []
        
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        for w in words:
            word_lower = w.lower()

            if not word_lower:
                continue

            primeira_letra = word_lower[0]

            linha_candidata = None 
            if primeira_letra in first_row:
                linha_candidata = first_row
            elif primeira_letra in second_row:
                linha_candidata = second_row
            elif primeira_letra in third_row:
                linha_candidata = third_row

            palavra_valida = True 
            for letra in word_lower:
                
                if letra not in linha_candidata:
                    palavra_valida = False
                    break 

            if palavra_valida:
                resultado.append(w)

        return resultado 
