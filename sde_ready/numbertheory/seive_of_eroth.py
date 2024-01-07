def sieve_of_eratosthenes(prime_till: int) -> None:
    memory = { item: False for item in range(2,prime_till+1)}
    
    for item in memory:
        if memory[item]:
            pass
        else:
            for var in range(item, prime_till+1):
                temp = var*item
                if temp > prime_till:
                    break
                else:
                    memory[temp] = True
    for item in memory:
        if not memory[item]:
            print(item)

sieve_of_eratosthenes(100)