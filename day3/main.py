# -*- coding: utf-8 -*-

if __name__ == '__main__':
     with open('input.txt') as f:
        line = f.readline()

        tokens = line.split(" ")
        distances = tokens[2].split(",")
        x_dist = int(distances[0])
        y_dist = int(distances[1])
        
        print(tokens)