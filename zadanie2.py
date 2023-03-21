#zadanie 2

l1 = float(input('liczba 1: '))
l2 = float(input('liczba 2: '))
z = input('znak: ')

if(z == '+'):
    print(l1 + l2)
elif(z == '-'):
    print(l1 - l2)
elif(z == '*'):
    print(l1 * l2)
elif(z == '/'):
    print(l1 / l2)
elif(z == '//'):
    print(l1 // l2)
elif(z == '%'):
    print(l1 % l2)
elif(z == '**'):
    print(l1 ** l2)
else:
    print("zle dane")