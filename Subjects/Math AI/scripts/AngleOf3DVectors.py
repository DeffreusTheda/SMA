A1 = int(input())
A2 = int(input())
A3 = int(input())
B1 = int(input())
B2 = int(input())
B3 = int(input())

def w(s):
    return f'({s})' if s < 0 else s

print(f'cos^{{-1}} (\\frac{{{A1} ({B1}) + {A2} ({B2}) + {A3} ({B3})}}{{\\sqrt{{{w(A1)}^2 + {w(A2)}^2 + {w(A3)}^2}} \\sqrt{{{w(B1)}^2 + {w(B2)}^2 + {w(B3)}^2}}}})')
