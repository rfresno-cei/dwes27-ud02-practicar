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
print(f'Underage: {acc_underage}')