# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [] #onde vou guardar os subsets

        def backtrack(index, path): #index: a partir de qual pos em nums vou olhar | path: subset que esta sendo construido
            result.append(path[:]) #add subset atual ao resultado, path[:] cria uma copia do path atual
            
            for i in range(index, len(nums)): # itera sobre os elementos restantes p/ formar novos subsets
                path.append(nums[i]) # add elemento atual nums[i] ao subset atual
                backtrack(i + 1, path) #chama backtrack com prox index e o subset ''atualizado''
                path.pop() #desfaz ultima adicao (backtrack) para testar outras combinacoes

        
        backtrack(0, []) # iniciando o backtracking com index 0 e um subset vazio
        return result