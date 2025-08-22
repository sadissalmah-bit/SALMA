
"""
Simple Hydrostatic Pressure Calculator (Beginner Friendly)
Demonstrates: Function, Method, Classes, Inheritance, Polymorphism, Error Handling
"""


# This is the base class for pressure calculation
class HydrostaticPressureCalculator:
	def __init__(self, density, depth, gravity=9.81):
		self.density = density
		self.depth = depth
		self.gravity = gravity
	def calculate(self):
		# This method should be overridden by subclasses
		raise NotImplementedError("Use a specific fluid type class.")


# This class is for fresh water
class FreshWaterPressureCalculator(HydrostaticPressureCalculator):
	def calculate(self):
		# Hydrostatic pressure formula: P = density * gravity * depth
		return self.density * self.gravity * self.depth


# This class is for brine (salt water)
class BrinePressureCalculator(HydrostaticPressureCalculator):
	def calculate(self):
		# Brine is a bit heavier, so we multiply by 1.02
		return self.density * self.gravity * self.depth * 1.02


# Function to get a number from the user
def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")

# Main function

def main():
	print("--- Hydrostatic Pressure Calculator ---")
	density = get_float("Enter fluid density (kg/m^3): ")
	depth = get_float("Enter depth (m): ")
	gravity = get_float("Enter gravity (m/s^2, default 9.81): ")
	if gravity == 0:
		gravity = 9.81

	print("Choose fluid type:")
	print("1. Fresh Water")
	print("2. Brine (Salt Water)")
	choice = input("Enter 1 or 2: ")

	# Polymorphism: use base class reference
	if choice == '1':
		calculator = FreshWaterPressureCalculator(density, depth, gravity)
	elif choice == '2':
		calculator = BrinePressureCalculator(density, depth, gravity)
	else:
		print("Invalid choice.")
		return

	try:
		result = calculator.calculate()
		print(f"Hydrostatic pressure is: {result:.2f} Pa")
	except Exception as error:
		print(f"Something went wrong: {error}")

if __name__ == "__main__":
	main()
    