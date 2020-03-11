def main():
    sum = 0
    for wire_length in range(start=12, stop=100):
        for long_rib in range(start=wire_length // 3, stop=wire_length // 2):
            if one_legal_combination(wire_length=wire_length, long_rib=long_rib):



if __name__ == '__main__':
    main()
