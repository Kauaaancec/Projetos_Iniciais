print ('=====CÁLCULO SIMPLES DE IMC=====')
altura = float(input('Qual a sua altura? '))
peso = float(input('Seu peso? '))
IMC =  peso / (altura * altura)
print('Seu IMC é: {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Seu IMC está abaixo do peso normal.')
elif IMC <= 25:
    print('Você está em seu peso ideal!')
elif IMC <= 30:
    print('Você está com execesso de peso.')
elif IMC <= 35:
    print('Obesidade classe I')
elif IMC <= 40:
    print('Obesidade classe II')
elif IMC <= 45:
    print('Obesidade classe III')
