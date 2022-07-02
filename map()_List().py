print("Exemplo:")

linguagens = ["Python","Java","JavaScript","C","C#","C++","Swift","Go","Kotlin"]
#linguagens = 'Python Java JavaScript C C# C++ Swift Go Kotlin'.split()  #Opção de Sintaxe

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é: {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é: {nova_lista}")