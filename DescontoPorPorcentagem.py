def calcular_desconto(valor,desconto=0): #O Parâmetro desconto possui zero valor default
  valor_com_desconto = valor - (valor * desconto)
  return valor_com_desconto

valor1 = calcular_desconto(100) #Não se aplica nenhum desconto
valor2 = calcular_desconto(100,0.25) #Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

continuar=True

while continuar is True:
  val=float(input(f"\nInsira o primeiro valor a ser pago: "))
  desc=float(input(f"\nAgora informe a porcentagem de desconto: "))

  result = calcular_desconto(val,desc)

  print(f"\nO Valor a ser pago com desconto é de {result}")

  bora=input(f"\nDeseja continuar? \nDigite S ou N: ")

  if bora == ("s") or bora ==("S"):
    continuar=True
    print("\n----------------------------------------------------")
  elif bora == ("n") or bora ==("N"):
    continuar=False
  else:
    bora=input(f"\nValor invalido. \nPor favor, informe apenas as letras 'S' para Sim ou 'N' para Não: ")