_, *a = map(int, open(0).read().split())
h = max(a)
for i in range(h):
    print(''.join('#.'[h-i > x]for x in a))
