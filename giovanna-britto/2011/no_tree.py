class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cont = 0
        for op in operations:
            if "+" in op:
                cont += 1
            else:
                cont -= 1
        return cont 