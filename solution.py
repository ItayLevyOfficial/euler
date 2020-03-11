import sympy
import itertools


def read_primes() -> [int]:
    with open('primes_list.txt', 'r') as file:
        return list(itertools.chain.from_iterable([map(int, line.split()) for line in file]))


def create_primes_set(prime_index: int, primes: [int]) -> {int}:
    prime = primes[prime_index]
    primes_set = set()
    for prime2 in primes:
        if prime2 != primes and \
                sympy.isprime(int(f'{prime}{prime2}')) and sympy.isprime(int(f'{prime2}{prime}')):
            primes_set.add(prime2)
    return primes_set


def main():
    primes = read_primes()
    sets_map = {}
    for prime1_index in range(len(primes)):
        create_pairs_if_needed(prime_index=prime1_index, primes=primes, sets_map=sets_map)
        for prime2_index in range(prime1_index, len(primes)):
            if primes[prime2_index] in sets_map[prime1_index]:
                create_pairs_if_needed(prime_index=prime2_index, primes=primes, sets_map=sets_map)
                for prime3_index in range(prime2_index, len(primes)):
                    prime3 = primes[prime3_index]
                    if prime3 in sets_map[prime2_index] and prime3 in sets_map[prime1_index]:
                        create_pairs_if_needed(prime_index=prime3_index, primes=primes, sets_map=sets_map)
                        for prime4_index in range(prime3_index, len(primes)):
                            prime4 = primes[prime4_index]
                            if prime4 in sets_map[prime2_index] and prime4 in sets_map[prime1_index] and prime4 in sets_map[prime3_index]:
                                create_pairs_if_needed(prime_index=prime4_index, primes=primes, sets_map=sets_map)
                                for prime5_index in range(prime4_index, len(primes)):
                                    prime5 = primes[prime5_index]
                                    if prime5 in sets_map[prime2_index] and prime5 in sets_map[
                                        prime1_index] and prime5 in sets_map[prime3_index] and prime5 in sets_map[prime4_index]:
                                        create_pairs_if_needed(prime_index=prime5_index, primes=primes,
                                                               sets_map=sets_map)
                                        print(primes[prime1_index], primes[prime2_index], prime3, prime4, prime5)


def create_pairs_if_needed(prime_index, primes, sets_map):
    if prime_index not in sets_map:
        sets_map[prime_index] = create_primes_set(prime_index=prime_index, primes=primes)


if __name__ == '__main__':
    main()
