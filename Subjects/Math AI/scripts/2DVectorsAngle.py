D = int(input('Dimension (2/3): '))
if D != 2 and D != 3:
    exit(1)

C = int(input('Vector count: '))
if C < 2 or C > 3:
    exit(1)

V = [0 for j in range(D) for i in range(C)]
for I in range(C):
    for J in range(D):
        V[I][J] = int(input(f'{chr(I+65)}{J+1}: '))
        # print(V[I][J])

def meh(S):
    return f'({S})' if int(S) < 0 else S

def num():
    S = ''
    for I in range(C):
        S = S+" + " if S != '' else S
        P = ''
        for J in range(D):
            P = P+" * " if P != '' else P
            P = f'{P}{V[I][J]}'

print(num())

# print(f'cos^{{1}} (\\frac{{{num()}}}{{{den()}})')
