import sys


def main():
    s = input()
    c = input()
    res = len(s)
    i = 0
    j = 0
    id = 0
    d = {}
    flag = 0
    # s_1 = [0, 0]
    while id < len(s):
        while id < len(s) and s[id] in c:
            j = id
            d.update({s[id] : d.get(s[id], 0) + 1})
            if len(d) == len(c):
                flag = 1
                while i < len(s) and d[s[i]] > 1:
                    d[s[i]] -= 1
                    i += 1
                if res > j - i:
                    res = j - i
                    # s_1[0], s_1[1] = i, j + 1
            id += 1
        while id < len(s) and s[id] not in c:
            id += 1
        i = id
        d.clear()
    # print(s[s_1[0] : s_1[1]])
    if flag == 1:
        print(res + 1)
    else:
       print(0) 


if __name__ == '__main__':
	main()
    