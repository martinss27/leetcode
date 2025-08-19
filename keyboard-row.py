class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # using sets to represent each row O(1)
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        resultado = []
        for w in words:
            word_lower = set(w.lower())
            
            # check if the word's letters are a subset of any row
           
            if any(word_lower.issubset(r) for r in rows):
                resultado.append(w)
        return resultado