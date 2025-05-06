nums = [2, 2, 3, 1, 3, 4, 4]

def achar(nums):
    ocorrencias = {}

    for numero in nums:
        if (numero in ocorrencias):
            ocorrencias[numero]+=1
        else:
            ocorrencias[numero]=1

    for numero in nums:
        if (ocorrencias[numero]==1):
            return numero
    return None
print(achar(nums))