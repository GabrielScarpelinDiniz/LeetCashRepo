# Outro dia de LeetCash

Fala galera (Para um bom entendedor, duas palavras bastam)! Passando aqui pra mostrar mais um exercício resolvido no modo a lá CC. O escolhido da vez foi o 198 - House Robber, aquele clássico de escolher as casas pra roubar sem chamar a polícia.

A ideia é simples: você tem uma lista de casas com dinheiro, mas não pode roubar duas seguidas. Então a gente usa programação dinâmica pra ir guardando o melhor valor acumulado até cada casa.

No código, começo tratando os casos em que tem 0 ou 1 casa. Depois, crio a lista `dp` pra armazenar o máximo acumulado. As duas primeiras posições são preenchidas direto, e a partir da terceira é só aplicar a fórmula:

```python
dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
```

No final, `dp[-1]` tem o resultado que a gente quer.

Então é isso, exercício resolvido! Um beijo para vocês e bom domingo.