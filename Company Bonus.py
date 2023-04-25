a ,b =input().split()
a =float(a)
b =int(b)
if b<5:
    print(f"{a:.2f}")
elif b>=5:
    a =(0.05*a)+a
    print(f"{a:.2f}")
