def contar_a(string):
    count = string.lower().count('a')
    
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

texto = input("Informe uma string: ")
print(contar_a(texto))
