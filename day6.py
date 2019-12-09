

f = [x.strip('\n') for x in open('day6_data.txt').readlines()]

direct_orbits = len(f)

planets = set()

orbits = {}

for orbit in f:

	x, y = orbit.split(')')

	planets.add(x); planets.add(y)

	orbits[y] = x

planets = list(planets)

total_orbits = 0

for planet in planets:
	
	if planet in orbits:
		current = orbits[planet]

		total_orbits += 1

		while current in orbits:

			current = orbits[ current ]

			total_orbits += 1


print(total_orbits)

