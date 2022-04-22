def an(n):
    if n == 0: return 2
    elif n == 1: return 3
    else: return 5 * an(n - 1) - 6 * an(n - 2) + 3 * n + 1

def bn(n):
    return -7 * 2**n + (13/4.0) * 3**n + (1.5) * n + (23.0/4)

for n in range(10):
    print(n, an(n), bn(n))
    
