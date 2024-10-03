palavra = str(input("Digite uma palavra: ")).lower()

quantidadeLetrasA = palavra.count("a") + palavra.count("á") + palavra.count("à") + palavra.count("ã") + palavra.count("â")
if (quantidadeLetrasA > 0):
    print(f"A palavra '{palavra}', possui {quantidadeLetrasA} letra(s) 'A'!")
else:
    print(f"A palavra '{palavra}', NÃO possui nenhuma letra 'A'!")

