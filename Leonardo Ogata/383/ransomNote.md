# Ransom Note

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Ransom Note é identificar se a string Ransom Note pode ser reescrita com as letras da string magazine

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Cria array para armazenar letras de magazine
    arrM = []

    # Preenche o array com cada palavra
    for i in magazine:
        arrM.append(i)

    # Itera sobre ransomNote
    for j in ransomNote:
        # Se o caractere estiver presente de ransomNote estiver presente no array ele é removido do array
        if j in arrM:
            arrM.pop(arrM.index(j))
        # Se o caractere não estiver presente de ransomNote estiver presente no array é retornado falso
        else:
            return False
    # Caso a palavra inteira rode e não falte nenhuma letra é retornado verdadeiro
    return True
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho de ransomNote.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata62.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
