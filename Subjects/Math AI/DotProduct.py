A1 = int(input())
A2 = int(input())
A3 = int(input())
B1 = int(input())
B2 = int(input())
B3 = int(input())

print(f'{A2} ({B3}) - {B2} ({A3})')
print(f'{A3} ({B1}) - {B3} ({A1})')
print(f'{A1} ({B2}) - {B1} ({A2})')

print()

print(A2 * B3 - B2 * A3, end=' ')
print(A3 * B1 - B3 * A1, end=' ')
print(A1 * B2 - B1 * A2)
