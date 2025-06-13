# Cada vez mais perto do dia 50

Oii Gente! Hoje eu resolvi o exercício 1603 do LeetCash, esse exercício instancia uma classe ParkingSystem, na qual tem o construtor que determina a quantidade de carros que podemos ter no estacionamento de acordo com o tipo de carro, podendo ser big, medium e small. Além disso, ela possui um método que para adicionar carro, mas para adicionar um carro, ele tem que ver o limite de carros daquele tipo disponíveis. Para isso, eu segui os seguintes passos:

1. No Construtor, crio um atributo `veículos`, que recebe a quantidade de veículos big, medium e small;

2. No método addCar, que tem como parâmetro `carType`, eu:

    2.1. If para verificar o tipo de carro, se `carType == 1`:
    
    2.2.1. E se `veículo[0] > 1`, eu diminuo um carro de veículo[0] e retorno `True`

    2.12. If para verificar o tipo de carro, se `carType == 2`:
    
    2.2.1. E se `veículo[1] > 1`, eu diminuo um carro de veículo[1] e retorno `True`

    2.1. If para verificar o tipo de carro, se `carType == 3`:
    
    2.2.1. E se `veículo[2] > 1`, eu diminuo um carro de veículo[2] e retorno `True`

3. Se não, eu retorno `False`

Pronto! Mais um exercício resolvido!!!