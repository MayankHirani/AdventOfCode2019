
with open('day1_data.txt') as f:
	numbers = [int(line.strip('\n')) for line in f.readlines()]

sum = 0

for num in numbers:

	sum += int(num / 3) - 2

print(sum)