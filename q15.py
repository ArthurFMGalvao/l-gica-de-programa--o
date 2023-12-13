def grito_de_natal(n):
    # A string base do grito de natal
    grito_base = "Feliz Natal!!"
    
    # Substitui o 'a' em 'Natal' por 'a' repetido n vezes
    grito_animado = grito_base.replace("a", "a" * n)
    
    return grito_animado

print(grito_de_natal(3))  # Saída: “Feliz Nataaal!!”
print(grito_de_natal(5))  # Saída: “Feliz Nataaaaal!!”
print(grito_de_natal(12))  # Saída: “Feliz Nataaaaaaaaaaaal!!”