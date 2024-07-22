A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
C1 = int(input())
C2 = int(input())

def w(s):
    return f'({s})' if s < 0 else s

AB = [B1-A1, B2-A2]
AC = [C1-A1, C2-A2]
BA = [A1-B1, A2-B2]
BC = [C1-B1, C2-B2]

print(f'a = cos^{{-1}} (\\frac{{{AB[0]} ({AC[0]}) + {AB[1]} ({AC[1]})}}{{\\sqrt{{{w(AB[0])}^2 + {w(AB[1])}^2}} \\sqrt{{{w(AC[0])}^2 + {w(AC[1])}^2}}}})')
print(f'b = cos^{{-1}} (\\frac{{{BA[0]} ({BC[0]}) + {BA[1]} ({BC[1]})}}{{\\sqrt{{{w(BA[0])}^2 + {w(BA[1])}^2}} \\sqrt{{{w(BC[0])}^2 + {w(BC[1])}^2}}}})')
print(f'c = 180 - a - b')
