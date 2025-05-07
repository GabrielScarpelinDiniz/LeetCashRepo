nums = [1,2,3,4,1,2,3,4]

def remove(nums):
    ocorrencias={}
    total=0
    i=0
    for numero in nums:
        if (numero in ocorrencias):
            ocorrencias[numero] +=1
        else:
            ocorrencias[numero] = 1
    
    for numero in ocorrencias:
        nums[i] = numero
        total+=1
        i+=1
    
    del nums[total:-1]
    return total

print(remove(nums))