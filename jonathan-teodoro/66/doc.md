class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        i = len(digits) - 1

        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i >= 0:
            digits[i] += 1
        else:
            digits.insert(0, 1)

        return digits

Menos trivial do que eu pensei. Para casos bases é muito facil por exemplo [1,2,3] so ir no ultimo e adicionar +1. O problema ocorre quando adicionamos casos como [9,9,9] que precisamos fazer tratamentos especificos. Ai é dureza. Primeiro crio uma if com early return para caso a situacao for um caso de trivialidade. Se for eu mato logo isso e nao dou chance para validacoes inuteis. Se nao, ai eu valido. um while para checar os 9. Quando para de encontrar noves, adiciona um ao numero ou, caso nao tenha nada antes insere no inicio.
