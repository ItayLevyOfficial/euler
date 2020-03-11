def main():
    long_ribs = {}
    for wire_length in range(start=12,stop=1_500_000):
        for long_rib in range(start=wire_length // 3, stop=wire_length // 2):
            if long_rib in long_ribs:
                if (remain_ribs := wire_length - long_rib) in long_ribs[long_rib] and \
                    long_ribs[long_rib][remain_ribs]:



if __name__ == '__main__':
    main()