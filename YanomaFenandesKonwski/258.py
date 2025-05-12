num = 37

def somar_digitos_ate_um_digito(num):
    while num >= 10:
        soma = 0
        while num > 0:
            soma += num % 10
            num //= 10
        num = soma
    return num
print(somar_digitos_ate_um_digito(num))

