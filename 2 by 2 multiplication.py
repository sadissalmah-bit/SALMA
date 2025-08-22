# Base class for multiplication
class Multiplication:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def calculate(self):
		raise NotImplementedError("Subclasses must implement this method.")

# Derived class for 2 by 2 multiplication
class TwoByTwoMultiplication(Multiplication):
	def calculate(self):
		# Method for multiplying two numbers
		return self.a * self.b

# Another derived class for demonstration (e.g., addition)
class TwoByTwoAddition(Multiplication):
	def calculate(self):
		# Method for adding two numbers
		return self.a + self.b

# Function to get user input safely
def get_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid integer.")


def main():
	print("--- 2 by 2 Multiplication Table ---")
	try:
		a = get_int("Enter the first number: ")
		b = get_int("Enter the second number: ")
		print("Choose operation:")
		print("1. Multiplication")
		print("2. Addition")
		choice = input("Enter 1 or 2: ")

		# Polymorphism: use base class reference
		if choice == '1':
			operation = TwoByTwoMultiplication(a, b)
		elif choice == '2':
			operation = TwoByTwoAddition(a, b)
		else:
			print("Invalid choice.")
			return

		try:
			result = operation.calculate()
			print(f"Result: {result}")
		except Exception as error:
			print(f"Calculation error: {error}")

		# Show 2x2 multiplication table
		print("\n2 by 2 Multiplication Table:")
		for i in range(1, 3):
			for j in range(1, 3):
				try:
					table_op = TwoByTwoMultiplication(i, j)
					print(f"{i} x {j} = {table_op.calculate()}")
				except Exception as table_error:
					print(f"Error in table calculation: {table_error}")
	except Exception as main_error:
		print(f"Main error: {main_error}")

if __name__ == "_main_":
	main()