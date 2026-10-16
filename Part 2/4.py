s = input()
if '.' in s:
    p = s.split('.')
    rub = p[0]
    kop = p[1]

    if len(kop) == 1:
        kop += '0'
else:
    rub = s
    kop = '0'
print(f"{rub} rub {kop} kop")
