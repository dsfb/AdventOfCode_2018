# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dic = dict()

    with open('input.txt') as f:
        for line in f:
            tokens = line.split(" ")
            distances = tokens[2].split(",")
            x_dist = int(distances[0])
            y_dist = int(distances[1][:-1])
            wid_hei = tokens[3].split('x')
            width = int(wid_hei[0])
            try:
                height = int(wid_hei[1][:-1])
            except ValueError:
                height = int(wid_hei[1])

            for i in range(width):
                for j in range(height):
                    t = (x_dist + i, y_dist + j)
                    dic[t] = dic.get(t, 0) + 1

    indexer = 1

    with open('input.txt') as f:
        for line in f:
            tokens = line.split(" ")
            distances = tokens[2].split(",")
            x_dist = int(distances[0])
            y_dist = int(distances[1][:-1])
            wid_hei = tokens[3].split('x')
            width = int(wid_hei[0])
            try:
                height = int(wid_hei[1][:-1])
            except ValueError:
                height = int(wid_hei[1])

            condition = True
            for i in range(width):
                if not condition:
                    break

                for j in range(height):
                    t = (x_dist + i, y_dist + j)
                    if dic[t] > 1:
                        condition = False
                        break

            if condition:
                print 'indexer:', indexer
                break

            indexer = indexer + 1
