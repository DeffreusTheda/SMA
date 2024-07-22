A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

def w(s):
    return f'({s})' if s < 0 else s

print(f'cos^{{-1}} (\\frac{{{A1} ({B1}) + {A2} ({B2})}}{{\\sqrt{{{w(A1)}^2 + {w(A2)}^2}} \\sqrt{{{w(B1)}^2 + {w(B2)}^2}}}})')
