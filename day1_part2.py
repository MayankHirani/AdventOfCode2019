
num_list = [int(num) for num in open('day1_data.txt').read().splitlines()]


def find_fuel(num):

	total = 0
	
	if int(num/3)-2 <= 0:

		return 0

	else:

		total += find_fuel(int(num / 3) - 2) + (int(num/3)-2)

		return total

a = sum([find_fuel(num) for num in num_list])

print(a)