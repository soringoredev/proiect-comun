'''


DARIANA!!!!

CReeaza un exercitiu nou in care s aavem doua variabile
username si password..
Utilizatorul trebuie s apoatya sa le introduca de la tastatura.

si tu sa le afisezi la ecran

'''
username = input('Introdu userul:')
password = input('Introdu parola:')
# print(username)
# print(password)

if len(username) < 3:
    print('Username too short.')
else:
    print('Login system ready.')