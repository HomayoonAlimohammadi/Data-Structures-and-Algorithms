def GCD(a, b, gcd=None):
    
    if gcd is None:
        gcd = min(a,b)

    if a % gcd == 0 and b % gcd == 0:
        return gcd

    return GCD(a, b, gcd-1) 


print(GCD(28, 24))

