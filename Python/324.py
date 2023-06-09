import sys


def main():
    min_len = min([int(x) for x in input().split()])
    n_costs = [int(x) for x in input().split()]
    m_pays = [int(x) for x in input().split()]
    n_costs.sort()
    m_pays.sort()
    m_pays.reverse()
    i = 0
    res = 0
    while i < min_len and n_costs[i] < m_pays[i]:
        res = res - n_costs[i] + m_pays[i]
        i += 1
    # print(n_costs)
    # print(m_pays)
    print(res)


if __name__ == '__main__':
	main()