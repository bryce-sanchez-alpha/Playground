def gcd(a:int, b:int) -> int:
    a,b = abs(a),abs(b)
    a,b = max(a,b),min(a,b)
    while b != 0:
        a,b = b,a%b
    return a

print(gcd(12,10))
