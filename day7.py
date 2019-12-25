
# Itertools for permutations
import itertools

# Prepare import from day 5
from importlib import reload
import day5_part2
reload(day5_part2)

# Get the big boy intcode program from day 5
from day5_part2 import IntcodeReader

# Get the latest intcode program
intcode = [ int(x) for x in open('day7_data.txt').read().split(',') ]


class IntcodeReaderUpdated(IntcodeReader):

	def __init__(self, intcode):

		IntcodeReader.__init__(self, intcode)

		self.original_intcode = intcode.copy()
		self.intcode = intcode
		self.input_signal = 0
		self.final_outputs = []

	def run_program(self, phase_settings):

		self.phase_settings = phase_settings

		# Reset the input signal for each permutation
		self.input_signal = 0

		# Looping through the settings in a combination
		for self.phase_index, self.amplifier in enumerate(self.phase_settings):


			# Reset the intcode to the original for every phase setting
			self.current_opcode_index = 0
			self.intcode = self.original_intcode.copy()
			self.first_input = True

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

			


	def input_output(self):

		self.par1 = self.intcode[self.current_opcode_index+1]

		if self.instruction[3:] == '03':

			# FIRST INPUT
			if self.first_input == True:

				self.intcode[self.par1] = self.phase_settings[self.phase_index]

				self.first_input = False

			# Set it to the input signal if its the second time
			else:

				self.intcode[self.par1] = self.input_signal


		elif self.instruction[3:] == '04':

			self.input_signal = self.intcode[self.par1]

			# Final output from the last amplifier
			if self.phase_index == 4:

				self.final_outputs.append(self.input_signal)


intcode_computer = IntcodeReaderUpdated(intcode)



for combination in itertools.permutations(range(5), 5):

	intcode_computer.run_program( list(combination) )


print(max(intcode_computer.final_outputs))


