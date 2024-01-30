# Tabuada sucinta 2

print('TABUADA')
z = int(input('Digite um número: '))
for a in range(z, z+1):
    print('--'*5)
    for b in range(1, 11):
        print('{}X{} = {}'.format(a, b, (a*b)))
print('--'*5)
