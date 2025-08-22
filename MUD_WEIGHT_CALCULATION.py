# Base class for mud weight calculation
class MudWeightCalculator:
	def __init__(self, density):
		self.density = density
	def calculate(self):
		raise NotImplementedError("Subclasses must implement this method.")

# Derived class for calculation in ppg (pounds per gallon)
class MudWeightPPG(MudWeightCalculator):
	def calculate(self):
		return self.density * 0.008345404

# Derived class for calculation in SG (specific gravity)
class MudWeightSG(MudWeightCalculator):
	def calculate(self):
		return self.density / 1000

# Function to get user input safely
def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")

def main():
	print("--- Mud Weight Calculation ---")
	density = get_float("Enter mud density (kg/m^3): ")
	print("Choose calculation method:")
	print("1. Pounds per gallon (ppg)")
	print("2. Specific gravity (SG)")
	choice = input("Enter 1 or 2: ")

	# Polymorphism: use base class reference
	if choice == '1':
		calculator = MudWeightPPG(density)
	elif choice == '2':
		calculator = MudWeightSG(density)
	else:
		print("Invalid choice.")
		return

	try:
		result = calculator.calculate()
		if choice == '1':
			print(f"Mud weight: {result:.2f} ppg")
		else:
			print(f"Mud weight: {result:.3f} SG")
	except Exception as error:
		print(f"Something went wrong: {error}")

if __name__ == "__main__":
	main()
