

with open('day5_data.txt') as f:

	data = f.read().split(',')

	values = [int(x) for x in data]


class IntcodeReader():

	def __init__(self, intcode):

		self.intcode = intcode

		self.current_opcode_index = 0

		self.instruction = ''

		self.value1 = 0
		self.value2 = 0

	def run_program(self):

		# Move through intcode until 

		while True:

			self.instruction = str(f"{ self.intcode[self.current_opcode_index] :05d}")

			if self.instruction[3:] == '99':

				break

			elif self.instruction[3:] in ('01', '02'):

				self.operation()

			elif self.instruction[3:] in ('03', '04'):

				self.new_instructions()

			print(self.current_opcode_index)

			self.move()


	def operation(self):

		# Set the right values

		if self.instruction[2:3] == '0':

			self.value1 = self.intcode[ self.intcode[self.current_opcode_index + 1] ]

		else:

			self.value1 = self.intcode[self.current_opcode_index + 1]

		if self.instruction[1:2] == '0':

			self.value2 = self.intcode[ self.intcode[self.current_opcode_index + 2] ]

		else:

			self.value2 = self.intcode[self.current_opcode_index + 2]

		# Add / Multiply

		if self.instruction[3:] == '01':

			self.intcode[ self.intcode[self.current_opcode_index+3] ] = self.value1 + self.value2

		elif self.instruction[3:] == '02':

			self.intcode[ self.intcode[self.current_opcode_index+3] ] = self.value1 * self.value2


	def new_instructions(self):

		self.value1 = self.intcode[self.current_opcode_index+1]

		if self.instruction[3:] == '03':

			user_input = int(input("Enter the user input: "))

			self.intcode[self.value1] = user_input

		elif self.instruction[3:] == '04':

			print(self.intcode[self.value1])



	def move(self):

		if self.instruction[3:] in ('01', '02'):

			self.current_opcode_index += 4

		elif self.instruction[3:] in ('03', '04'):

			self.current_opcode_index += 2


int_read = IntcodeReader(values)
int_read.run_program()

