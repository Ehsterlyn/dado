'''
Coding-Ehsterlyn video 8
Mi año como personaje de Rol
'''

'''
Debemos tirar 4 dados y quedarnos con la suma de los 3 mejores
'''

import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)

suma=dado1+dado2+dado3+dado4
menor=min(dado1,dado2,dado3,dado4)
res=suma-menor

print("Fuerza %i"% res)

dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)

suma=dado1+dado2+dado3+dado4
menor=min(dado1,dado2,dado3,dado4)
res=suma-menor

print("Destreza %i"% res)

dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)

suma=dado1+dado2+dado3+dado4
menor=min(dado1,dado2,dado3,dado4)
res=suma-menor

print("Constitución %i"% res)

dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)

suma=dado1+dado2+dado3+dado4
menor=min(dado1,dado2,dado3,dado4)
res=suma-menor

print("Inteligencia %i"% res)

dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)

suma=dado1+dado2+dado3+dado4
menor=min(dado1,dado2,dado3,dado4)
res=suma-menor

print("Sabiduria %i"% res)

dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)

suma=dado1+dado2+dado3+dado4
menor=min(dado1,dado2,dado3,dado4)
res=suma-menor

print("Carisma %i"% res)
