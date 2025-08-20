# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        current_substring = ""

        for char in s:
            while char in current_substring:
                current_substring = current_substring[1:]
            
            current_substring += char
            max_length = max(max_length, len(current_substring))            

        return max_length
    
'''
1- verificamos se a letra ja existe com o loop while, se ja existir, precisamos encolher pela esquerda ate que a duplicata seja removida.

2- encolher a janela: removemos o primeiro caractere da substring atual.
ex: se o substr_atual = "abc" e a nova letra for "a", o loop while vai remover o "a" do inicio, resultando em "bc"
o loop while testa de novo: "a" não está em "bc", então o loop para

3- expandindo a janela: adiciono a nova letra ao final da substring
por ser imutavel, preciso fazer `substr_atual = substr_atual + letra`

4- atualizo o comprimento
comparo o comprimento da nosssa janela atual com o maximo ja registrado
e guardamos o maior valor entre eles, e retornamos o maximo no final
'''