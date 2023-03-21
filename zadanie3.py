#zadanie 3

p1 = "Jak masz na imię oraz nazwisko?"

a1 = "oglądanie telewizji/filmów/seriali"
b1 = "czytanie książek/czasopism"
c1 = "inne, jakie?"

p2 = "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:"

a2 = "podczas podróży"
b2 = "w czasie wolnym (po pracy, na urlopie)"
c2 = "inne, jakie?"

p3 = "W jakich okolicznościach czytasz książki najczęściej?"

a3 = "chęć poszerzenia wiedzy"
b3 = "czytanie mnie relaksuje/odpręża"
c3 = "inny, jaki?"

o1 = input(f'{p1}\n'
           f'a) {a1}\n'
           f'b) {b1}\n'
           f'c) {c1}\n')

if o1.lower() == 'a':
    o1 = a1
elif o1.lower() == 'b':
    o1 = b1
elif o1.lower() == 'c':
    o1 = input('podaj odp: ')
else:
    print('???')

o2 = input(f'{p2}\n'
           f'a) {a2}\n'
           f'b) {b2}\n'
           f'c) {c2}\n')

if o2.lower() == 'a':
    o2 = a2
elif o2.lower() == 'b':
    o2 = b2
elif o2.lower() == 'c':
    o2 = input('podaj odp: ')
else:
    print('???')

o3 = input(f'{p3}\n'
           f'a) {a3}\n'
           f'b) {b3}\n'
           f'c) {c3}\n')

if o3.lower() == 'a':
    o3 = a3
elif o3.lower() == 'b':
    o3 = b3
elif o3.lower() == 'c':
    o3 = input('podaj odp: ')
else:
    print('???')

print('-----------------')

print(p1 + '\n' + o1 + '\n')
print(p2 + '\n' + o2 + '\n')
print(p3 + '\n' + o3 + '\n')