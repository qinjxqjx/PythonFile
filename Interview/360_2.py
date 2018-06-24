def count(n):
    if len(n) == 1:
        if n[0] == "0":
            return 1
        else:
            return 2
    if n[0] == '0': return count(n[1:])
    if n[0] == '1': return count(n[1:]) + (1 << (len(n)-1))
    return 1 << len(n)
while True:
    n = raw_input()
    if not n: break
    n.strip()
    n = str(int(n))
    
    print count(n)-1
