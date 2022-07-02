texto = "Deveras, o rato roeu a roupa estampada com o logo do Python escrito 'python é demais!' do rei de roma"

print(f"\nO Tamanho do Texto é: {len(texto)} caracteres")
print(f"\nPython in Texto: {'Python' in texto}")
print(f"\nQuantidade de Y no texto: {texto.count('y')}")
print(f"\nAs 5 primeiras letras do texto são: {texto[0:5]}")
print(f"\nQuantidade de Python no texto: {texto.count('python')}\n\n")

print(f"Texto = {texto}\n\n")

palavras=texto.split()
print(f"Palavras = {palavras}\n")
print(f"Quantidade de Palavras = {len(palavras)}")