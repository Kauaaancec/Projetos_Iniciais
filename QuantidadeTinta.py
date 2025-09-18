largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
area = largura * altura
area = area / 2
print('Para uma parede com a largura de {}m e altura de {}m será necessario {} litros de tinta'.format(largura, altura, area))