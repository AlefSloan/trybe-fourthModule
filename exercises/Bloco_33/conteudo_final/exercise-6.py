def triangle_check(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        print("Não é um triangulo")
    elif a == b == c:
        print("Triângulo Equilátero: três lados iguais;")
    elif a == b or b == c or a == c:
        print("Triângulo Isósceles: quaisquer dois lados iguais;")
    else:
        print("Triângulo Escaleno: três lados diferentes.")


triangle_check(5, 10, 20)
