import random as r
p = int(input("Simple Random Sampling!\nPopulation Size: "))
k = int(input("Sample Size: "))
o = [i+1 for i in range(p)]
t = []
while len(t) < k:
    t.append(o.pop(r.randint(0, len(o)-1)))
for x in range(len(t)):
    print(str(t[x]) + (', ' if x+1!=len(t) else ''), end='')
print()

