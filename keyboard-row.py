class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        resultado = []
        for w in words:
            word_lower = set(w.lower())
           
            if any(word_lower.issubset(r) for r in rows):
                resultado.append(w)
        return resultado