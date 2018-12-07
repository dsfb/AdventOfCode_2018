# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline()

        count2 = 0
        count3 = 0
        while line:
            dic = {}
            for c in line:
                dic[c] = dic.get(c, 0) + 1

            vals = set(dic.values())

            if 2 in vals:
                count2 = count2 + 1

            if 3 in vals:
                count3 = count3 + 1

            line = f.readline()

    print 'result:', count2 * count3
