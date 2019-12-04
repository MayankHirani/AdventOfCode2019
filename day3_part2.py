
import numpy as np

f = open('day3_data.txt').read().split('\n')

wire1 = f[0].split(',')
wire2 = f[2].split(',')

wire1_coords = []
wire2_coords = []

wire1_set = set()
wire2_set = set()

# Use sets and intersection of two sets (Set of values of one, set of values of another)

# FINDING ALL COORDINATES

for values in (wire1, wire2):

	current_coord = [ 0, 0 ]

	for coord in values:

		move_value = int(coord[1:])

		if coord[0] == 'R':

			for x in range(1, move_value + 1):

				c = ( current_coord[0] + x, current_coord[1] )

				if values is wire1:

					wire1_coords.append(c)

					wire1_set.add(c)

				elif values is wire2:

					wire2_coords.append(c)

					wire2_set.add(c)

			current_coord = [ current_coord[0] + move_value, current_coord[1] ]

		elif coord[0] == 'L':

			for x in range(1, move_value + 1):

				c = ( current_coord[0] - x, current_coord[1] )

				if values is wire1:

					wire1_coords.append(c)

					wire1_set.add(c)

				elif values is wire2:

					wire2_coords.append(c)

					wire2_set.add(c)

			current_coord = [ current_coord[0] - move_value, current_coord[1] ]

		elif coord[0] == 'U':

			for x in range(1, move_value + 1):

				c = ( current_coord[0], current_coord[1] + x )

				if values is wire1:

					wire1_coords.append(c)

					wire1_set.add(c)

				elif values is wire2:

					wire2_coords.append(c)

					wire2_set.add(c)

			current_coord = [ current_coord[0], current_coord[1] + move_value ]

		elif coord[0] == 'D':

			for x in range(1, move_value + 1):

				c = ( current_coord[0], current_coord[1] - x )

				if values is wire1:

					wire1_coords.append(c)

					wire1_set.add(c)

				elif values is wire2:

					wire2_coords.append(c)

					wire2_set.add(c)

			current_coord = [ current_coord[0], current_coord[1] - move_value ]

# FIND INTERSECTIONS

intersections = wire1_set.intersection(wire2_set)

intersections = list(intersections)

total_moves = []

for intersection in intersections:

	print(intersection)

	total_moves.append(wire1_coords.index(intersection)+1 + wire2_coords.index(intersection)+1)

print(total_moves)
print(min(total_moves))

