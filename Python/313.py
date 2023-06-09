import queue
import math as m

def main():
    n = int(input())
    ls = [int(x) for x in input().split()]
    res = 0
    num = 0
    sort_ls = sorted(ls)
    k = m.ceil(n / 2)
    print(k)
    # Либо первый на 1 больше либо равен s2
    s1 = queue(sort_ls[:k])
    s2 = queue(sort_ls[k:].reverse())
    print(s1)
    print(s2)
    for i in range(1, n + 1):
        if len(s1) < len(s2):
            s1.append(s2[-1])
            s2.pop_front()
        elif len(s1) > len(s2) + 1:
            s1.append(s2[-1])
            s2.pop()
        num = s1[-1]
        res += num
        del_num = ls.pop()
        if del_num <= num:
            s1.remove(del_num)
        
            
    #     tmp = sorted(ls[:i])
    #     if len(tmp) > 1 and i % 2 == 0:
    #         num = tmp[(len(tmp) // 2) - 1]
    #     elif len(tmp) > 1:
    #         id = (len(tmp) - 1) // 2
    #         num = tmp[id]
    #     elif len(tmp) == 1:
    #         num = tmp[0]
    #     # print(tmp, num)
    #     res += num
    print(res)
    print(s1)

if __name__ == '__main__':
	main()

"""
test №1
5
1 2 3 1 2
answer = 7!!!

"""