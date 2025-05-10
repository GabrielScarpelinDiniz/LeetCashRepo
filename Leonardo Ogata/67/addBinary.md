# Add Binary

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Add binary é receber duas strings contendo numéros binários somar as duas e retorna o valor da soma em binário

&nbsp;&nbsp;&nbsp;&nbsp; Nessa documentação eu venho relatar a triste que passei devido a infeliz linguagem java, primeiramente desenvolvi um algoritmo maluco, mas que funciona e eu estavam muito feliz com ele, pq apesar de ser grande e feio eu podia dizer que era honesto e que eu me diverti e aprendi muito sobre java enquanto fazia, esse foi o algoritmo desenvolvido: 

```java
        public String addBinary(String a, String b) {

        long decA = 0;
        long decB= 0;

        int p = 0;
        for (int i =  a.length() - 1; i >= 0; i--) {
            decA += Character.getNumericValue(a.charAt(i)) * Math.pow(2, p);
            p ++;
        }

        p = 0;
        for (int i =  b.length() - 1; i >= 0; i--)  {
            decB += Character.getNumericValue(b.charAt(i)) * Math.pow(2, p); 
            p++;
        }

        long temp = decA + decB;

        StringBuilder result = new StringBuilder();
        if (temp == 0) {
            result.append("0");
        } else {
            while (temp > 0) {
                result.append(temp % 2);
                temp = temp / 2;
            }
            result.reverse();
        }

        return result.toString();
    }
```

&nbsp;&nbsp;&nbsp;&nbsp; Porém apesar do código funcionar as entradas eram grandes demais até para o tipo long, dai eu pensei que teria que me render a python para facilitar minha vida, mas eu resolvi fazer uma última pesquisa para não me render a essa linguagem que eu tanto evito. E eu encontrei... Eu encontrei um tipo maior que long da biblioteca Math do java, o `BigInteger` e ao começar a ler a API eu não sabia que estava prestes a me deparar com o plot twist mais maléfico da minha vida.

&nbsp;&nbsp;&nbsp;&nbsp; Aparentemente o tipo `BigInteger` possui uma função em que você pode converter um número para qualquer base incluindo binário, fazendo com que meu antigo código cheio de vida, insipiração, loucura e espirito de programador serie D fosse substituido pela seguinte solução:

```java
    public String addBinary(String a, String b) {

    //Recebe string A e converte para binário
    BigInteger numA = new BigInteger(a, 2); 

    //Recebe string A e converte para binário
    BigInteger numB = new BigInteger(b, 2);

    //Soma as duas strings
    BigInteger sum = numA.add(numB);

    //Retorna a soma em formato de string         
    return sum.toString(2); 

    }   

```

## Lógica do Algoritmo triste
- Converte ambas string para binário
- Soma os valores binários
- Retorna o valor como string
    

## Complexidade
- Tempo: O algoritmo possui complexidade de O($n$), onde n é o tamanho da maior string.
- Espaço: O uso de espaço adicional é O($n$), onde n é o tamanho da maior string.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata13.png" alt="luto" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e hoje estou de luto pelo meu código, que todos tenham um bom dia por que hoje pra mim o dia acordou sendo noite.</p>
    </div>
</div>
