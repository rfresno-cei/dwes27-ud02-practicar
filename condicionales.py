# Exercise 1
nota = int(input('Introduce una nota: '))
if nota >= 9 and nota <= 10:
    print('Sobresaliente')
elif nota >= 7:
    print('Notable')
elif nota > 5:
    print('Bien')
elif nota == 5:
    print('Suficiente')
else:
    print('Insuficiente')

# Exercise 2
num1 = int(input('Introduce un número: '))
num2 = int(input('Introduce otro número: '))
simbolo = input('Introduce un símbolo: ')
if simbolo == '+':
    print(num1 + num2)
elif simbolo == '-':
    print(num1 - num2)
elif simbolo == '*':
    print(num1 * num2)
elif simbolo == '/':
    print(num1 / num2)
else:
    print('Símbolo no reconocido')

# Exercise 3
num1 = int(input('Introduce un número: '))
num2 = int(input('Introduce otro número: '))
num3 = int(input('Introduce otro número: '))
if num1 == num2 and num2 == num3:
    print('Todos iguales')
elif num1 >= num2 and num1 >= num3:
    print(f'{num1} es mayor')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} es mayor')
else:
    print(f'{num3} es mayor')

# Exercise 4
num1 = int(input('Introduce un número: '))
num2 = int(input('Introduce otro número: '))
num3 = int(input('Introduce otro número: '))
if num1 == num2 and num1 == num3:
    print('Equilátero')
elif num1 == num2 or num1 == num3 or num2 == num3:
    print('Isósceles')
else:
    print('Escaleno')

# Exercise 5
num1 = int(input('Introduce un número: '))
if num1 >= 100 and num1 <= 200:
    print('Está en el rango')
else:
    print('No está en el rango')

# Exercise 6
num1 = int(input('Introduce un valor en metros: '))
unidad = input('Introduce una unidad diferente: ')
if unidad == 'km':
    print(num1 / 1000)
elif unidad == 'cm':
    print(num1 * 100)
elif unidad == 'mm':
    print(num1 * 1000)
else:
    print('Unidad no reconocida')

# Exercise 7
num1 = int(input('Introduce una edad: '))
fin_semana = bool(input('Introduce si es fin de semana: '))
precio = 0
if num1 < 12:
    precio = 5
elif num1 < 17:
    precio = 7
else:
    precio = 10
if fin_semana:
    precio += 2
print(f'{precio} €')

# Exercise 8
num1 = int(input('Introduce un número de mes: '))
if num1 == 1:
    print('Enero')
elif num1 == 2:
    print('Febrero')
elif num1 == 3:
    print('Marzo')
elif num1 == 4:
    print('Abril')
elif num1 == 5:
    print('Mayo')
elif num1 == 6:
    print('Junio')
elif num1 == 7:
    print('Julio')
elif num1 == 8:
    print('Agosto')
elif num1 == 9:
    print('Septiembre')
elif num1 == 10:
    print('Octubre')
elif num1 == 11:
    print('Noviembre')
elif num1 == 12:
    print('Diciembre')
else:
    print('El mes no existe')

# Exercise 9
num1 = int(input('Introduce un número: '))
if num1 % 3 == 0:
    print('Es múltiplo de 3')
if num1 % 5 == 0:
    print('Es múltiplo de 5')
if num1 % 7 == 0:
    print('Es múltiplo de 7')

# Exercise 10
num1 = int(input('Introduce una temperatura: '))
if num1 < 10:
    print('Hace frío')
elif num1 < 30:
    print('Templado')
else:
    print('Hace calor')