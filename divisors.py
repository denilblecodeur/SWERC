def divisors(n):
    primeFactors = getPrimeFactors(n)
    res = []
 
    pw = 1
    for factor in primeFactors:
        pw *= primeFactors[factor] + 1
    
    for i in range(pw):
        divisor = 1
        for factor in primeFactors:
            divisor *= factor ** (i % (primeFactors[factor] + 1))
            i //= primeFactors[factor] + 1
        res.append(divisor)
    
    return res