def isHappy(n):
    
    seen = set()
    
    while n!=1:
        if n in seen:
            return False

        seen.add(n)
        sum = 0

        for i in str(n):
            square = int(i)*int(i)
            sum += square
        n = sum
    
    return True

print(isHappy(0))

dados_sem_duplicados = df.drop_duplicates(subset="title") 
quantidade_sem_titulos_duplicados = dados_sem_duplicados["type"].value_counts()