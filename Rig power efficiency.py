
"""
Simple Rig Power System Calculator (Beginner Friendly)
Demonstrates: Function, Method, Classes, Inheritance, Polymorphism, Error Handling
"""

# Base class
class RigPowerSystem:
    def __init__(self, voltage, current):
        self.voltage = voltage
        self.current = current
    def calculate(self):
        # This method should be overridden
        raise NotImplementedError("Use a specific power system class.")

# Derived class for AC power system (inherits from RigPowerSystem)
class ACPowerSystem(RigPowerSystem):
    def __init__(self, voltage, current, power_factor):
        super().__init__(voltage, current)
        self.power_factor = power_factor
    def calculate(self):
        # Method for AC power calculation
        if not (0 < self.power_factor <= 1):
            print("Error: Power factor must be between 0 and 1.")
            return None
        return self.voltage * self.current * self.power_factor

# Derived class for DC power system (inherits from RigPowerSystem)
class DCPowerSystem(RigPowerSystem):
    def calculate(self):
        # Method for DC power calculation
        return self.voltage * self.current

# Function to get user input safely
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("--- Rig Power System Calculator ---")
    voltage = get_float("Enter voltage (V): ")
    current = get_float("Enter current (A): ")
    print("Select power system type:")
    print("1. AC Power System")
    print("2. DC Power System")
    choice = input("Enter 1 or 2: ")

    # Polymorphism:
    if choice == '1':
        power_factor = get_float("Enter power factor (0 < pf <= 1): ")
        calculator = ACPowerSystem(voltage, current, power_factor)
    elif choice == '2':
        calculator = DCPowerSystem(voltage, current)
    else:
        print("Invalid choice.")
        return

    try:
        input_power = calculator.calculate()
        if input_power is not None:
            print(f"Input power: {input_power:.2f} Watts")
            output_power = get_float("Enter output power (Watts): ")
            if output_power > input_power:
                print("Warning: Output power cannot be greater than input power.")
            efficiency = (output_power / input_power) * 100 if input_power > 0 else 0
            print(f"Efficiency of rig power system: {efficiency:.2f}%")
        else:
            print("Calculation failed due to error.")
    except Exception as error:
        print(f"Unexpected error: {error}")

if __name__ == "__main__":
    main()
