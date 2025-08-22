# Base class for drilling pipe calculation
class DrillingPipe:
	def __init__(self, length, outer_diameter, inner_diameter):
		self.length = length
		self.outer_diameter = outer_diameter
		self.inner_diameter = inner_diameter

	def calculate(self):
		raise NotImplementedError("Subclasses must implement this method.")

	# Method to convert diameter from inches to meters
	def diameter_in_meters(self, diameter_in_inches):
		return diameter_in_inches * 0.0254

	# Method to display pipe info
	def display_info(self):
		print(f"Pipe length: {self.length} m")
		print(f"Outer diameter: {self.outer_diameter} m")
		print(f"Inner diameter: {self.inner_diameter} m")

# Derived class for pipe volume calculation
class PipeVolume(DrillingPipe):
	def calculate(self):
		# Calculate volume of pipe (cylindrical shell)
		import math
		outer_radius = self.outer_diameter / 2
		inner_radius = self.inner_diameter / 2
		volume = math.pi * self.length * (outer_radius**2 - inner_radius**2)
		return volume

	# Method to display volume
	def display_volume(self):
		print(f"Pipe volume: {self.calculate():.4f} m^3")

# Derived class for pipe weight calculation
class PipeWeight(DrillingPipe):
	def __init__(self, length, outer_diameter, inner_diameter, density):
		super().__init__(length, outer_diameter, inner_diameter)
		self.density = density

	def calculate(self):
		# Calculate weight using volume and density
		import math
		outer_radius = self.outer_diameter / 2
		inner_radius = self.inner_diameter / 2
		volume = math.pi * self.length * (outer_radius**2 - inner_radius**2)
		weight = volume * self.density
		return weight

	# Method to display weight
	def display_weight(self):
		print(f"Pipe weight: {self.calculate():.2f} kg")

# Function to get user input safely
def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")

def main():
	print("--- Drilling Pipe Calculation ---")
	length = get_float("Enter pipe length (m): ")
	outer_diameter = get_float("Enter outer diameter (m): ")
	inner_diameter = get_float("Enter inner diameter (m): ")
	print("Choose calculation:")
	print("1. Pipe Volume")
	print("2. Pipe Weight")
	choice = input("Enter 1 or 2: ")

	# Polymorphism: use base class reference
	if choice == '1':
		calculator = PipeVolume(length, outer_diameter, inner_diameter)
		calculator.display_info()
		calculator.display_volume()
	elif choice == '2':
		density = get_float("Enter pipe material density (kg/m^3): ")
		calculator = PipeWeight(length, outer_diameter, inner_diameter, density)
		calculator.display_info()
		calculator.display_weight()
	else:
		print("Invalid choice.")
		return

	# Example of using diameter conversion method
	try:
		diameter_in_inches = get_float("Enter a diameter in inches to convert to meters (optional, or press Enter to skip): ")
		print(f"{diameter_in_inches} inches = {calculator.diameter_in_meters(diameter_in_inches):.4f} meters")
	except Exception:
		pass

if __name__ == "__main__":
	main()
