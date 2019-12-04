
password_count = 0

for password in range(353096, 843212 + 1):

	pair = False

	increasing_bool = True

	print(password)

	for index, num in enumerate(str(password)[:-1]):


		# Only check a pair if it is not part of group
		if num == str(password)[index+1]:

			if index != 0 and index <= len(str(password))-3:

				if num != str(password)[index-1] and num != str(password)[index + 2]:

					pair = True

			if index == 0:

				if num != str(password)[index+2]:

					pair = True

			elif index > len(str(password))-3 and num != str(password)[index-1]:

				pair = True

		# Increase check
		if int(num) > int(str(password)[index+1]):

			increasing_bool = False

	if pair == True and increasing_bool == True:

		password_count += 1

		print("One added")

	

print(password_count)