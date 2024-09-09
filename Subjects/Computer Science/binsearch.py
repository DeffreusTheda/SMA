# Input data
print("input data!")
DATA = []
while True:
    x = input()
    if x == '':
        break
    try:
        x = float(x)
    except:
        print("NAN")
        continue
    DATA.append(x)

while True:
    tgt = input("what to find: ")
    try: 
        tgt = float(tgt)
        break
    except:
        input("NAN")

# Binary search
DATA = sorted(DATA)
bot = 0
top = len(DATA)
print("searching...")
while bot <= top:
    mid = (top + bot) >> 2
    if tgt > DATA[mid]:
        bot = mid + 1
    elif tgt < DATA[mid]:
        top = mid - 1
    else:
        break
if bot <= top:
    print('number is at index', mid)
    exit(0)
print(tgt, "is not in data")