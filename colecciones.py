# Exercise 1
lista = [1, 2, 3]
print(lista[0])
print(lista[1])
print(lista[2])

# Exercise 2
lista = ['hola', 'haba', 'hola', 'python']
print(lista)
lista[1] = 'javascript'
print(lista)

# Exercise 3
lista = [1, 2, 3]
print(lista[0] + lista[1] + lista[2])

# Exercise 4
lista = [7, 8, 2, 4, 5]
print(sum(lista) / len(lista))

# Exercise 5
lista = ['esternocleidomastoideo', 'desoxirribonucleico', 'otorrinolaringólogo']
mas_larga = ''
if len(lista[0]) >= len(lista[1]) and len(lista[0]) >= len(lista[2]):
    mas_larga = lista[0]
elif len(lista[1]) >= len(lista[0]) and len(lista[1]) >= len(lista[2]):
    mas_larga = lista[1]
else:
    mas_larga = lista[2]
print(mas_larga)
# Alternativa: print(max(lista, key=len))

# Exercise 6
lista = ['dieguito', 'nereíta', 'manolito', 'capicito', 'danielito']
# palabra = input('Introduce una palabra: ')
palabra = 'dieguito'
if palabra in lista:
    print('Sí está')
else:
    print('No está')

# Exercise 7
matriz = [[4.5, 6],
          [8, 10]]
print(matriz[0][0])
print(matriz[0][1])
print(matriz[1][0])
print(matriz[1][1])

# Exercise 8
matriz = [[1, 2, 3],
          [7, 8, 9]]
valores = [elemento for fila in matriz for elemento in fila]
# Alternativa: media = sum(matriz[0] + matriz[1]) / (len(matriz[0]) + len(matriz[1]))
print(sum(valores) / len(valores))

# Exercise 9
lista = ['dieguito', 'nereíta', 'manolito', 'capicito', 'danielito']
print(lista[1])
print(lista[-1])
print(len(lista))

# Exercise 10
lista = [1.3, 4.2, 6.8, 3.6, 7.3]
media = sum(lista) / len(lista)
if media >= 5:
    print('Aprobado')
else:
    print('Suspenso')

# Exercise 11
lista = ['rojo', 'azul', 'verde', 'amarillo', 'rosa']
color = input('Introduce un color: ')
print(color in lista)

# Exercise 12
miset = {'12345678A', '12345678B', '12345678C', '12345678D', '12345678D'}
print(len(miset))
print('12345678B' in miset)

# Exercise 13
miset = {'Pepito', 'Juanito', 'Laurita', 'Jorgito', 'Anita'}
nombre = input('Introduce un nombre: ')
if nombre in miset:
    print('Ya existe')
else:
    miset.add(nombre)
    print(miset)

# Exercise 14
miset1 = {1, 6, 3, 8, 9}
miset2 = {1, 7, 3}
if len(miset1) > len(miset2):
    print('El set 1 es más largo')
elif len(miset2) > len(miset1):
    print('El set 2 es más largo')
else:
    print('Los dos sets tienen el mismo tamaño')

# Exercise 15
diccionario = {
    'Pepito': 20,
    'Juanito': 56,
    'Laurita': 15,
    'Jorgito': 12,
    'Anita': 82
}
nombre = input('Introduce un nombre: ')
if nombre in diccionario:
    print(diccionario[nombre])
    print(f'Mayor de edad: {diccionario[nombre] >= 18}')

# Exercise 16
diccionario = {
    'Pepito': 5.6,
    'Juanito': 2.9,
    'Laurita': 9.6,
    'Jorgito': 6.3,
    'Anita': 7.2
}
nombre = input('Introduce un nombre: ')
if nombre in diccionario:
    print(diccionario[nombre])
    print(f'Aprobado: {diccionario[nombre] >= 5}')

# Exercise 15
diccionario = {
    'Pepito': 'abcd',
    'Juanito': '1234',
    'Laurita': 'a1b2',
    'Jorgito': 'hola',
    'Anita': 'adios'
}
nombre = input('Introduce un nombre: ')
contra = input('Introduce una contraseña: ')
if nombre in diccionario and diccionario[nombre] == contra:
    print('Login correcto')
else:
    print('Usuario y/o contraseña incorrectos')