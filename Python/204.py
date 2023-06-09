import sys


def main():
    n = int(input())
    nums = []
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        nums.append(a * b)
    gen_sum = sum(nums)
    k = 100 / gen_sum
    for num in nums:
        res = (num * k) / 100
        print(round(res, 12))


if __name__ == '__main__':
	main()