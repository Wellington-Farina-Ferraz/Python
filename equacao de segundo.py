import math


a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
 
delta = b * b - 4 * a * c 

if delta < 0:
    print("esta equação não possui raízes reais")
    
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print("a raiz dupla desta equação é",raiz)
    
else:
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
    
    if (raiz1<raiz2):
        print("as raízes da equação são",raiz1,"e",raiz2)
    else:
        print("as raízes da equação são",raiz2,"e",raiz1)