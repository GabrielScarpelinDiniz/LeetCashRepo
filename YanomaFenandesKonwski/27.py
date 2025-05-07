nums = [0,4,4,0,4,4,4,0,2]
def remove(nums, numero):
    contador = 0
    for numeros in nums:
        if (numeros == numero):
            contador +=1
    i=0
    while i<contador:
        nums.remove(numero)
        i+=1
    return nums

print(remove(nums,4))

