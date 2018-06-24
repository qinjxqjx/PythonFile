def check(a):
   return a[0][0] == a[2][2] and a[0][1] == a[2][1] and a[0][2] == a[2][0] and a[1][0] == a[1][2]
while True:
    a = []
    for i in range(3):
        s = raw_input()
        if not s: break
        a.append(s)
    if not a: break
    if check(a):
        print 'YES'
    else:
        print 'NO'


