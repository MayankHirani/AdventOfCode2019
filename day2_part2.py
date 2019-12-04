
with open ('day2_data.txt') as f:
	data = f.read().split(',')
	original_values = [int(x) for x in data]

def find_output(values):

	for index in range(0, len(values), 4):

		if values[index] == 1:

			values[ values[index + 3] ] = values[ values[index + 1] ] + values[ values[index + 2] ]

		elif values[index] == 2:

			values[ values[index + 3] ] = values[ values[index + 1] ] * values[ values[index + 2] ]

		elif values[index] == 99:

			break

	return values[0]

output_data = {}

for x in range(0, 100):

	for y in range(0, 100):

		values = [value for value in original_values]

		values[1] = x; values[2]=y

		output_data[find_output(values)] = [x, y]

for output in output_data:

	if output == 19690720:

		print(100 * output_data[output][0] + output_data[output][1])

print(output_data)

