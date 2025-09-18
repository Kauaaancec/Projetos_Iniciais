a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados formam um triângulo!")
else:
    print("Os lados não formam um triângulo.")
