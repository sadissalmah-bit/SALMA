"""
Flow Rate Calculation Program for Petroleum Course
Demonstrates: Function, Method, Classes, Inheritance, Polymorphism, Error Handling
"""

# Base class
class FlowRateCalculator:
	def __init__(self, area, velocity):
		self.area = area
		self.velocity = velocity

	def calculate(self):
		raise NotImplementedError("Subclasses must implement this method.")

# Derived class for linear flow
class LinearFlowCalculator(FlowRateCalculator):
	def calculate(self):
		try:
			# Q = A * v
			flow_rate = self.area * self.velocity
			return flow_rate
		except Exception as e:
			print(f"Error in LinearFlowCalculator: {e}")
			return None

# Derived class for turbulent flow (example adjustment)
class TurbulentFlowCalculator(FlowRateCalculator):
	def calculate(self):
		try:
			
			flow_rate = self.area * self.velocity * 0.95
			return flow_rate
		except Exception as e:
			print(f"Error in TurbulentFlowCalculator: {e}")
			return None

# Function to get user input safely
def get_float(prompt):
	while True:
		try:
			value = float(input(prompt))
			return value
		except ValueError:
			print("Invalid input. Please enter a numeric value.")

# Main function
def main():
	print("--- Flow Rate Calculation ---")
	area = get_float("Enter cross-sectional area (m^2): ")
	velocity = get_float("Enter fluid velocity (m/s): ")

	print("Choose flow type:")
	print("1. Linear Flow")
	print("2. Turbulent Flow")
	method = input("Enter 1 or 2: ")

	# Polymorphism:
	if method == '1':
		calculator = LinearFlowCalculator(area, velocity)
	elif method == '2':
		calculator = TurbulentFlowCalculator(area, velocity)
	else:
		print("Invalid flow type selected.")
		return

	try:
		flow_rate = calculator.calculate()
		if flow_rate is not None:
			print(f"Calculated flow rate: {flow_rate:.4f} m^3/s")
		else:
			print("Calculation failed due to error.")
	except Exception as e:
		print(f"Unexpected error: {e}")

if __name__ == "__main__":
	main()
