class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        teste = ""
        for i in s:
            if i in alphabet:
                teste += i
        print(teste)
        l = 0
        r = len(teste)-1

        while l<=r:
            print(teste[l], teste[r])
            if teste[l] == teste[r]:
                l +=1
                r -= 1
                continue
            else:
                return False
            l +=1
            r -= 1
        
        return True


Fiz uma logica de merda, com certeza existem formas melhores. Vou tentar explicar minha linha de racicionio: Queria primeiro remover os espaços e caracteres que nao fossem do alfabeto. Depois converter para loweCase para padronizar. Decidi adicionar em um novo array para quando eu percorrer nao ter problema com bug de index no for. Feito isso eu tinha o array preparado. Feito isso, so aplicar two pointer nos dois extremos, certo? Errado. Até passei nos primeiros casos, mas cai em um erro que era com a string "0P", nao tinha levado em consideração numeros. Na primeira versão a gente descartava o 0 e fica só p, que é palindromo. O que tive que fazer, incluir os numeros na brincadeira, e se a string tiver numero, ela tem que ter outro numero na posicao oposta.