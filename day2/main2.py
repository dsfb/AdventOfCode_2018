# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline()

        dic = dict()
        print(len(line))
        while line:
            if line[0] not in dic:
                dic[line[0]] = list()
            
            dic[line[0]].append(line)        

            line = f.readline()

        result = False
        for lista in dic.values():            
            if result:
                break

            for v in lista:
                if result:
                    break

                for k in lista:
                    if result:
                        break

                    if v != k:
                        diffs = 0
                        index = 0
                        locs = []
                        cur_index = 0
                        for cv, ck in zip(v, k):
                            if cv != ck:
                                diffs = diffs + 1
                                locs.append(cv)
                                cur_index = index
                                if diffs > 1:
                                    break
                            index = index + 1

                        if diffs == 1:
                            s = v[:cur_index] + v[cur_index + 1:]
                            print('resultado:', s)
                            print(len(s))
                            result = True
                            break


            break

        print('fim')