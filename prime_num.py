# !/usr/bin/env python3
import math


def checker(int_num):
    if (int_num < 2):
        return False
    elif (int_num in [2, 3, 5, 7]):
        return True
    elif (int_num % 2 == 0):
        return False
    else:
        i = 3
        while i <= int_num // 2:
            if math.gcd(int_num, i) != 1:
                return False
            else:
                i += 2
    return True


def num_list(int_a, int_b):
    if int_a == int_b:
        if checker(int_a):
            return [int_a]
        else:
            return [None]
    else:
        maxnum = max(int_a, int_b)
        minnum = min(int_a, int_b)
        if maxnum < 2:
            return [None]
        elif maxnum == 2:
            return [2]
        elif minnum <= 2:
            minnum = 3
            result = [2]
            while minnum <= maxnum:
                for p in result:
                    if math.gcd(minnum, p) == 1:
                        if p == result[-1]:
                            result.append(minnum)
                        else:
                            continue
                    else:
                        minnum += 1
                        break
            return result
        else:
            prelist = num_list(2, minnum - 1)
            result = []
            while minnum <= maxnum:
                for p in prelist:
                    if math.gcd(minnum, p) == 1:
                        if p == prelist[-1]:
                            prelist.append(minnum)
                            result.append(minnum)
                        else:
                            continue
                    else:
                        minnum += 1
                        break
            return result


a = input('请输入区间：')
b = a.split(' ')
print(num_list(int(b[0]), int(b[1])))
input()
exit()
