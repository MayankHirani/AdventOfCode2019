
with open ('day2_data.txt') as f:
	data = f.read().split(',')
	values = [int(x) for x in data]

values[1] = 12;values[2] = 2

for index in range(0, len(values), 4):

	if values[index] == 1:

		values[ values[index + 3] ] = values[ values[index + 1] ] + values[ values[index + 2] ]

	elif values[index] == 2:

		values[ values[index + 3] ] = values[ values[index + 1] ] * values[ values[index + 2] ]

	elif values[index] == 99:

		print(values[0])
		break

	else:

		pass

	print(values)
