import sympy
import itertools


def read_primes():
    with open('primes_list.txt', 'r') as file:
        return list(itertools.chain.from_iterable([map(int, line.split()) for line in file]))


def main():
    primes = read_primes()
    print(primes)


if __name__ == '__main__':
    main()
