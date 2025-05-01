Boa noite galerinha do mal

Por hoje seremos direto ao ponto:

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        resp = nums.copy()
        nums.clear()
        print(resp)
        for idx, value in enumerate(resp):
            if value != val:
                nums.append(value)
        
        return len(nums)
        

copio e limpo o array passado, preciso fazer isso pois ao final precisarei do array nums sem os itens removidos. Como remover itens durante o for é delicado optei por gerar uma cópia. Percorro o array copiado e caso o valor nao seja oq to buscando responder eu appendo no array nums. Simples, fácil!! É isso tropinha