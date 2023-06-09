import math

def part_nod(num, nod):
	res = set()
	if nod == 1:
		res.add(nod)
	else:
		res.add(num)
		delimeter = nod
		k = nod
		while (delimeter < num):
			if (num % delimeter == 0):
				res.add(delimeter)
			delimeter += 1
	return res

def find_nod(num_1, num_2, nod):
	set_1 = part_nod(num_1, nod)
	set_2 = part_nod(num_2, nod)
	# if num_1 == 5 or num_1 == 640:
	# 	print("set_1", set_1, num_1)
	# 	print("set_2", set_2, num_2)
	set_res = set.intersection(set_1, set_2)
	if len(set_res) == 0:
		return 0
	else:
		return max(set_res)

def find_x_y(num, nod):
	sqrt_num = math.ceil(math.sqrt(num))
	set_1 = set()
	delimiter = nod
	k = nod
	prev = 0
	while (delimiter <= sqrt_num):
		if (num % delimiter == 0):
			if (prev + k < delimiter):
				k += k
			set_1.add(delimiter)
			print(delimiter, k)
			prev = delimiter
		delimiter += k
		# print(delimiter, sqrt_num)
	return set_1

# def simple_delimiter(num):
# 	set_1 = set()
# 	d = {}
# 	delimiter = 2
# 	while (delimiter <= num):
# 		if (num % delimiter == 0):
# 			set_1.add(delimiter)
# 			d.update({delimiter : d.get(delimiter, 0) + 1})
# 			num = num // delimiter
# 		else:
# 			delimiter += 1
# 		# print(delimiter, sqrt_num)
# 	return set_1, d

def count_answer(nok, nod, nums):
	count_nums = 0
	dk = nod * nok
	for num in nums:
		num_1 = num
		num_2 = dk // num
		new_nod = find_nod(num_1, num_2, nod)
		# print("nod:", nod, "new_nod:", new_nod, "> nums:", num_1, num_2)
		if (new_nod == nod):
			if (num_1 == num_2):
				count_nums += 1
			else:
				count_nums += 2
	print(count_nums)


def main():
	nums = [int(i) for i in input().split()]
	nod = nums[0]
	nok = nums[1]
	if (nok == 1 and nod == 1):
		print(1)
	else:
		# print(simple_delimiter(nok * nod))
		dividers = find_x_y(nok * nod, nod)
		print(dividers, len(dividers))
		count_answer(nok, nod, dividers)
		

if __name__ == '__main__':
	main()

	# 1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 64, 80,  128,  160,  320,  640
	# 1, 5, 25,  125,  625, 3 125
	# 3 90
	# 6 6
	# 2 1000000000000