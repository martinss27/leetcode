# leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        nova_matriz = []

        for coluna_atual in range(len(matrix)):
            linha_rotacionada = []
            for linha_atual in range(n-1, -1, -1):
                valor = matrix[linha_atual][coluna_atual]
                linha_rotacionada.append(valor)
            
            nova_matriz.append(linha_rotacionada)

        for i in range(n):
            matrix[i] = nova_matriz[i]