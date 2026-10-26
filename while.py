import random

# Exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2
i = 10
while i >= 1:
    print(i)
    i -= 1

# Exercise 3
i = 1
acc = 0
while i <= 10:
    acc += i
    i += 1
print(acc)

# Exercise 4
i = 1
while i <= 20:
    print(i)
    i += 2

# Exercise 5
i = 1
acc = 1
while i <= 8:
    acc *= i
    i += 1
print(acc)

# Exercise 6
aleatorio = random.randint(1, 10)
acertado = False
while not acertado:
    num1 = int(input('Introduce un número: '))
    if num1 == aleatorio:
        print('Acertaste')
        acertado = True
    else:
        print('Incorrecto')

# Exercise 7
i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i += 1

# Exercise 8
usuario = 'pepito'
contrasena = '1234'
login = False
while not login:
    usu_intr = input('Introduce usuario: ')
    pwd_intr = input('Introduce contraseña: ')
    if usu_intr == usuario and pwd_intr == contrasena:
        print('Login correcto')
        login = True
    else:
        print('Login incorrecto')

# Exercise 9
usuario = 'pepito'
contrasena = '1234'
login = False
intentos = 0
while not login:
    usu_intr = input('Introduce usuario: ')
    pwd_intr = input('Introduce contraseña: ')
    if usu_intr == usuario and pwd_intr == contrasena:
        print('Login correcto')
        login = True
    else:
        print('Login incorrecto')
        intentos += 1
        if intentos == 3:
            print('Demasiados intentos')
            break