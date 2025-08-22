
"""
Simple Permeability Calculator (Beginner Friendly)
Demonstrates: Function, Method, Classes, Inheritance, Polymorphism, Error Handling
"""


# permeability calculation
class PermeabilityCalculator:
	def __init__(self, area, viscosity, pressure_drop, length, flow_rate):
		self.area = area
		self.viscosity = viscosity
		self.pressure_drop = pressure_drop
		self.length = length
		self.flow_rate = flow_rate
	def calculate(self):
		# This method should be overridden by subclasses
		raise NotImplementedError("Use a specific calculation method class.")


# This class uses Darcy's Law
class DarcyCalculator(PermeabilityCalculator):
	def calculate(self):
		# Darcy's Law: k = (Q * mu * L) / (A * ΔP)
		return (self.flow_rate * self.viscosity * self.length) / (self.area * self.pressure_drop)


# This class uses an empirical formula
class EmpiricalCalculator(PermeabilityCalculator):
	def calculate(self):
		#  k = Q / (A * ΔP) * 1000
		return (self.flow_rate / (self.area * self.pressure_drop)) * 1000


# Function to get a number from the user
def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")

# Main function

def main():
	print("--- Permeability Calculator ---")
	area = get_float("Enter area (m^2): ")
	viscosity = get_float("Enter viscosity (cP): ")
	pressure_drop = get_float("Enter pressure drop (Pa): ")
	length = get_float("Enter length (m): ")
	flow_rate = get_float("Enter flow rate (m^3/s): ")

	print("Choose calculation method:")
	print("1. Darcy's Law")
	print("2. Empirical Formula")
	choice = input("Enter 1 or 2: ")

	# Polymorphism: use base class reference
	if choice == '1':
		calculator = DarcyCalculator(area, viscosity, pressure_drop, length, flow_rate)
	elif choice == '2':
		calculator = EmpiricalCalculator(area, viscosity, pressure_drop, length, flow_rate)
	else:
		print("Invalid choice.")
		return

	try:
		result = calculator.calculate()
		print(f"Permeability is: {result:.4e} m^2")
	except Exception as error:
		print(f"Something went wrong: {error}")

if __name__ == "__main__":
	main()
