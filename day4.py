
password_count = 0

for password in range(353096, 843212 + 1):

	adjacent_bool = False

	increasing_bool = True

	print(password)

	for index, num in enumerate(str(password)[:-1]):

		if num == str(password)[index+1]:

			adjacent_bool = True

		if int(num) > int(str(password)[index+1]):

			increasing_bool = False

	if adjacent_bool == True and increasing_bool == True:

		password_count += 1

		print("One added")

	

print(password_count)