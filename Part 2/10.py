s = input()
res = ""
for char in reversed(s):
    if char == '(':
        res += ')'
    else:
        res += '('
print(res)
