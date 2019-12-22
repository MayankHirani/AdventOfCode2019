

f = [x.strip('\n') for x in open('day6_data.txt').readlines()]

direct_orbits = len(f)

planets = set()

orbits = {}

for orbit in f:

	x, y = orbit.split(')')

	planets.add(x); planets.add(y)

	orbits[y] = x

you_line = []

santa_line = []

for obj in ('YOU', 'SAN'):

	current = orbits[obj]

	while current in orbits:

		current = orbits[ current ]

		if obj=='YOU': you_line.append(current)
		else: santa_line.append(current)

you_line = list(reversed(you_line)); santa_line = list(reversed(santa_line))

for index, i in enumerate(you_line):

	if i not in santa_line:

		print( len(you_line[index-1:]) + len(santa_line[index-1:]) )
		break
