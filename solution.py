import sympy
import itertools


def read_primes() -> [int]:
    with open('primes_list.txt', 'r') as file:
        return list(itertools.chain.from_iterable([map(int, line.split()) for line in file]))


def create_primes_set(prime: int, primes: [int]) -> {int}:
    primes_set = set()
    for prime2 in primes:
        if sympy.isprime(int(f'{prime}{prime2}')) and sympy.isprime(int(f'{prime2}{prime}')):
            primes_set.add(prime2)
    return primes_set


def main():
    primes = read_primes()
    sets_map = {}
    for prime1 in primes:
        create_pairs_if_needed(prime1, primes, sets_map)
        for prime2 in primes:
            if prime2 != prime1 and prime2 in sets_map[prime1]:


def create_pairs_if_needed(prime, primes, sets_map):
    if prime not in sets_map:
        sets_map[prime] = create_primes_set(prime=prime, primes=primes)


if __name__ == '__main__':
    main()
