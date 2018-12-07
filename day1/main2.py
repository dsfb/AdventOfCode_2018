# -*- coding: utf-8 -*-

if __name__ == "__main__":
    frequencies = list()
    with open('input.txt') as f:
        line = f.readline()

        while line:
            frequencies.append(line)
            line = f.readline()

        conj = set()
        number = 0
        twice = None
        conj.add(number)

        while True:
            for line in frequencies:
                number = number + int(line)
                if number in conj:
                    twice = number
                    print 'twice:', number
                    break

                conj.add(number)

            if twice is not None:
                break


