# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        num_elementos = len(nums)  # número de elementos do input (nums).
        total_subconjuntos = 2**num_elementos  # o número total de subconjuntos é 2^n (ex: 2^3=8(total de subsets)).
        result = []  # lista final c/ todos subsets.

        # itera de 0 a (2^n - 1), onde cada número é uma máscara de bits única para um subconjunto.
        for mask_number in range(total_subconjuntos):
            
            subset_atual = []  # Inicia o subconjunto para a máscara atual.
            
            # itera sob cada elemento para ver se pertence a esse subset.
            for element_index in range(num_elementos):
                
                # verifica se o bit na posição 'element_index' da máscara está ligado (igual a 1).
                if (mask_number >> element_index) & 1:
                    
                    # se o bit estiver ligado, add o elemento correspondente ao subset.
                    subset_atual.append(nums[element_index])
            
            # Adiciona o subset recém-formado à lista de resultados.
            result.append(subset_atual)
            
        return result