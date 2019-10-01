def isprime(n): # 10
    if n == 2:
        return True
    for val in range(2,(n//2)+1): # 2 3 4 5
        if n % val == 0:
            return False
        return True
        