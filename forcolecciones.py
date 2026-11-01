# Exercise 1
lista = ['hola', 'adios', 'buenas', 'tardes', 'noches']
for i in lista:
    print(i)

# Exercise 2
lista = [1, 5, 3, 6, 3]
acc = 0
for i in lista:
    acc += i
print(acc)

# Exercise 3
lista = [5.7, 7.4, 8.3, 9.6, 2.4]
acc = 0
for i in lista:
    acc += i
print(acc / len(lista))

# Exercise 4
lista = [4, 5, 8, 3, 2]
pares = 0
impares = 0
for i in lista:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Pares: {pares}')
print(f'Impares: {impares}')

# Exercise 5
lista = ['Pepito', 'Juanito', 'Laurita', 'Jorgito', 'Anita']
nombre = input('Introduce un nombre: ')
encontrado = False
for i in lista:
    if nombre == i:
        print('Está en la lista')
        encontrado = True
        break
if not encontrado:
    print('No está en la lista')

# Exercise 6
lista = ['hola', 'adios', 'buenas', 'tardes', 'noches']
for i in range(len(lista)):
    print(f'Cadena {i+1}: {lista[i]}')

# Exercise 7
miset = ('hola', 'adios', 'buenas', 'tardecitas', 'noches')
mas_larga = None
mayor = 0
for i in miset:
    if len(i) >= mayor:
        mas_larga = i
        mayor = len(i)
print(mas_larga)

# Exercise 8
dict = {
    'Pepito': 6.5,
    'Juanito': 7.8,
    'Laurita': 5.7,
    'Jorgito': 9.6,
    'Anita': 9.2
}
mas_alta = None
mayor = 0
mas_baja = None
menor = 10
acc = 0
for nombre in dict:
    acc += dict[nombre]
    if dict[nombre] >= mayor:
        mas_alta = nombre
        mayor = dict[nombre]
    if dict[nombre] <= menor:
        mas_baja = nombre
        menor = dict[nombre]
print(f'Más alta: {mas_alta}')
print(f'Más baja: {mas_baja}')
print(f'Media: {acc / len(dict)}')

# Exercise 9
dict = {
    'Teclado': 6.5,
    'Ratón': 7.8,
    'Monitor': 5.7,
    'Altavoces': 9.6,
    'Cámara': 9.2
}
for prod in dict:
    print(f'{prod}: {dict[prod]*1.21}')

# Exercise 10
dict = {
    'Julián': 2001,
    'Manué': 2015,
    'Er Dani': 1993,
    'Er Otro Dani': 1999,
    'Terry': 2006
}

acc_adult = 0
acc_underage = 0
for name in dict:
    if 2026 - dict[name] >= 18:
        acc_adult += 1
    else:
        acc_underage += 1
print(f'Adults: {acc_adult}')
print(f'Underages: {acc_underage}')