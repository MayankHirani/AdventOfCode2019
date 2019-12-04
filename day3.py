
import numpy as np

f = open('day3_data.txt').read().split('\n')

wire1 = f[0].split(',')
wire2 = f[2].split(',')

wire1_coords = []
wire2_coords = []

# Use sets and intersection of two sets (Set of values of one, set of values of another)

# FINDING ALL COORDINATES

for values in (wire1, wire2):

	current_coord = [ 0, 0 ]

	for coord in values:

		move_value = int(coord[1:])

		if coord[0] == 'R':

			for x in range(1, move_value + 1):

				c = [ current_coord[0] + x, current_coord[1] ]

				if values is wire1:

					wire1_coords.append(c)

				elif values is wire2:

					wire2_coords.append(c)

			current_coord = [ current_coord[0] + move_value, current_coord[1] ]

		elif coord[0] == 'L':

			for x in range(1, move_value + 1):

				c = [ current_coord[0] - x, current_coord[1] ]

				if values is wire1:

					wire1_coords.append(c)

				elif values is wire2:

					wire2_coords.append(c)

			current_coord = [ current_coord[0] - move_value, current_coord[1] ]

		elif coord[0] == 'U':

			for x in range(1, move_value + 1):

				c = [ current_coord[0], current_coord[1] + x ]

				if values is wire1:

					wire1_coords.append(c)

				elif values is wire2:

					wire2_coords.append(c)

			current_coord = [ current_coord[0], current_coord[1] + move_value ]

		elif coord[0] == 'D':

			for x in range(1, move_value + 1):

				c = [ current_coord[0], current_coord[1] - x ]

				if values is wire1:

					wire1_coords.append(c)

				elif values is wire2:

					wire2_coords.append(c)

			current_coord = [ current_coord[0], current_coord[1] - move_value ]

# FIND INTERSECTIONS

intersections = []

for coord in wire1_coords:

	print(wire1_coords.index(coord), len(wire1_coords))

	if coord in wire2_coords:

		intersections.append(coord)

distances = []

# FINDING THE DISTANCE TO EACH INTERSECTION

def man_distance(point1, point2):

	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

for intersection in intersections:

	distances.append(man_distance([0, 0], intersection))

print(min(distances))
