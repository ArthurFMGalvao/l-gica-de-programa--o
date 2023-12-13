def area_quadrado(lado, exibir=False):
    area = lado ** 2
    if exibir:
        print(f"A área do quadrado é {area}")
    return area

print(area_quadrado (4), True)
print(area_quadrado(9), True)

def area_triangulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"A área do triângulo é {area}")
    return area

print(area_triangulo (6, 9), True)
print(area_triangulo(5, 8), True)
