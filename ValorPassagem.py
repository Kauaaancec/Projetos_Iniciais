distancia = float(input("Digite a distância da viagem em km: "))
if distancia <= 200:
    preco_por_km = 50
else:
    preco_por_km = 45

preco_total = distancia * preco_por_km

print(f"O preço da passagem para {distancia} km é R$ {preco_total:.2f}")