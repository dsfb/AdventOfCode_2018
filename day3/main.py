# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('input.txt') as f:
        dic = dict()

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

    summer = 0
    for t in dic:
        if dic[t] > 1:
            summer = summer + 1

    print 'summer:', summer
