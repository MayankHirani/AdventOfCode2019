


with open('day5_data.txt') as f:

	data = f.read().split(',')

	values = [int(x) for x in data]

#values = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


class IntcodeReader():

	def __init__(self, intcode):

		self.intcode = intcode

		self.current_opcode_index = 0

		self.instruction = ''

		self.par1 = 0
		self.par2 = 0

	def run_program(self):

		# Move through intcode until 

		while True:

			self.instruction = str(f"{ self.intcode[self.current_opcode_index] :05d}")

			if self.instruction[3:] == '99':

				break

			elif self.instruction[3:] in ('01', '02'):

				self.operation()

				self.move()

			elif self.instruction[3:] in ('03', '04'):

				self.input_output()

				self.move()

			elif self.instruction[3:] in ('05', '06'):

				self.jump()

			elif self.instruction[3:] in ('07', '08'):

				self.pointer_instructions()

				self.move()

	def set_parameters(self):

		# Save the actual number of the parameter for the jump function

		# Set the right parameters based on immediate or not

		if self.instruction[2:3] == '0':

			self.par1 = self.intcode[ self.intcode[self.current_opcode_index + 1] ]

		elif self.instruction[2:3] == '1':

			self.par1 = self.intcode[self.current_opcode_index + 1]

		if self.instruction[1:2] == '0':

			self.par2 = self.intcode[ self.intcode[self.current_opcode_index + 2] ]

		elif self.instruction[1:2] == '1':

			self.par2 = self.intcode[self.current_opcode_index + 2]


	def operation(self):

		# Set the right values

		self.set_parameters()

		# Add / Multiply

		if self.instruction[3:] == '01':

			self.intcode[ self.intcode[self.current_opcode_index+3] ] = self.par1 + self.par2

		elif self.instruction[3:] == '02':

			self.intcode[ self.intcode[self.current_opcode_index+3] ] = self.par1 * self.par2


	def input_output(self):

		self.par1 = self.intcode[self.current_opcode_index+1]

		if self.instruction[3:] == '03':

			user_input = int(input("Enter the user input: "))

			self.intcode[self.par1] = user_input

		elif self.instruction[3:] == '04':

			print(self.intcode[self.par1])


	def jump(self):

		self.set_parameters()

		if self.instruction[3:] == '05':

			if self.par1 != 0:

				self.current_opcode_index = self.par2

			else:

				self.move()

		elif self.instruction[3:] == '06':

			if self.par1 == 0:

				self.current_opcode_index = self.par2

			else:

				self.move()


	def pointer_instructions(self):

		self.set_parameters()

		if self.instruction[3:] == '07':

			if self.par1 < self.par2:

				self.intcode[ self.intcode[ self.current_opcode_index + 3] ] = 1

			else:

				self.intcode[ self.intcode[ self.current_opcode_index + 3] ] = 0

		elif self.instruction[3:] == '08':

			if self.par1 == self.par2:

				self.intcode[ self.intcode[ self.current_opcode_index + 3] ] = 1

			else:

				self.intcode[ self.intcode[ self.current_opcode_index + 3] ] = 0

	def move(self):

		if self.instruction[3:] in ('01', '02'):

			self.current_opcode_index += 4

		elif self.instruction[3:] in ('03', '04'):

			self.current_opcode_index += 2

		elif self.instruction[3:] in ('05', '06'):

			self.current_opcode_index += 3

		elif self.instruction[3:] in ('07', '08'):

			self.current_opcode_index += 4


int_read = IntcodeReader(values)
int_read.run_program()

