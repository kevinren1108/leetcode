def countPrimes(n: int) -> int:
    isPrime = [False] * n
    for i in range(2,n):
        isPrime[i] = True
    
    for i in range(n):  
        if isPrime[i] == False:
            continue
        else:
            for j in range(i,n):
                if isPrime[j] != True:
                    continue
                elif j % i == 0 and j != i:
                    isPrime[j] = False


countPrimes(10)                             
                    
                