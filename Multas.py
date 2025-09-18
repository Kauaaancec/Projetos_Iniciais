n1 = float(input('Qual foi a velocidade maxima do carro? '))
if n1 > 80:
    n1 = (n1 - 80) * 7
    print('O carro está acima do limite da via e será multando em R${}'.format(n1))
    