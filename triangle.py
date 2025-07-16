class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        row = len(triangle)
        bottom = triangle[-1]

        for linha_atual in range(len(triangle) - 2, -1, -1): #percorrendo as linhas de baixo p cima
            for indice_coluna in range(len(triangle[linha_atual])): # percorrendo cada numero de cada linha
                
                linha_abaixo = triangle[linha_atual + 1]

                valor_reto = linha_abaixo[indice_coluna]
                valor_diagonal = linha_abaixo[indice_coluna + 1]

                menor_valor = min(valor_reto, valor_diagonal)

                soma = triangle[linha_atual][indice_coluna] + menor_valor

                triangle[linha_atual][indice_coluna] = soma

        return triangle[0][0]