# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open('input.txt') as f:
        number = 0
        line = f.readline()

        while line:
            number = number + int(line)
            line = f.readline()

        print 'number:', number