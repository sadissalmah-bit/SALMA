# Base class for all formulas
class Formula:
    def calculate(self):
        pass

    def display_formula(self):
        pass


# 1. Pressure = Force / Area
class Pressure(Formula):
    def __init__(self, force, area):
        self.force = force
        self.area = area

    def calculate(self):
        try:
            return self.force / self.area
        except ZeroDivisionError:
            return "Error: Area cannot be zero."

    def display_formula(self):
        return f"Pressure = Force / Area\nSubstituting: Pressure = {self.force} / {self.area}"


# 2. WEIGHT = Mass × Gravity
class WEIGHT(Formula):
    def __init__(self, mass):
        self.mass = mass
        self.gravity = 9.81

    def calculate(self):
        return self.mass * self.gravity

    def display_formula(self):
        return f"WEIGHT = Mass × Gravity\nSubstituting: WEIGHT = {self.mass} × {self.gravity}"


# 3. Work Done = Force × Distance
class WorkDone(Formula):
    def __init__(self, force, distance):
        self.force = force
        self.distance = distance

    def calculate(self):
        return self.force * self.distance

    def display_formula(self):
        return f"Work Done = Force × Distance\nSubstituting: Work Done = {self.force} × {self.distance}"


# 4. Hydrostatic Pressure = Density × Gravity × Height
class HydrostaticPressure(Formula):
    def __init__(self, density, height):
        self.density = density
        self.gravity = 9.81
        self.height = height

    def calculate(self):
        return self.density * self.gravity * self.height

    def display_formula(self):
        return (f"Hydrostatic Pressure = Density × Gravity × Height\n"
                f"Substituting: Hydrostatic Pressure = {self.density} × {self.gravity} × {self.height}")


# 5. Density = Mass / Volume
class Density(Formula):
    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume

    def calculate(self):
        try:
            return self.mass / self.volume
        except ZeroDivisionError:
            return "Error: Volume cannot be zero."

    def display_formula(self):
        return f"Density = Mass / Volume\nSubstituting: Density = {self.mass} / {self.volume}"


# 6. Force = Mass × Acceleration
class Force(Formula):
    def __init__(self, mass, acceleration):
        self.mass = mass
        self.acceleration = acceleration

    def calculate(self):
        return self.mass * self.acceleration

    def display_formula(self):
        return f"Force = Mass × Acceleration\nSubstituting: Force = {self.mass} × {self.acceleration}"


# --------------------------
# Main Program with Menu
# --------------------------
def main():
    while True:
        print("\nPetroleum Engineering Formula Calculator")
        print("1. Pressure = Force / Area")
        print("2. WEIGHT = Mass × Gravity")
        print("3. Work Done = Force × Distance")
        print("4. Hydrostatic Pressure = Density × Gravity × Height")
        print("5. Density = Mass / Volume")
        print("6. Force = Mass × Acceleration")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        try:
            if choice == '1':
                force = float(input("Enter Force (N): "))
                area = float(input("Enter Area (m²): "))
                formula = Pressure(force, area)

            elif choice == '2':
                mass = float(input("Enter Mass (kg): "))
                formula = WEIGHT(mass)

            elif choice == '3':
                force = float(input("Enter Force (N): "))
                distance = float(input("Enter Distance (m): "))
                formula = WorkDone(force, distance)

            elif choice == '4':
                density = float(input("Enter Density (kg/m³): "))
                height = float(input("Enter Height (m): "))
                formula = HydrostaticPressure(density, height)

            elif choice == '5':
                mass = float(input("Enter Mass (kg): "))
                volume = float(input("Enter Volume (m³): "))
                formula = Density(mass, volume)

            elif choice == '6':
                mass = float(input("Enter Mass (kg): "))
                acceleration = float(input("Enter Acceleration (m/s²): "))
                formula = Force(mass, acceleration)

            elif choice == '0':
                print("Thank you for using the calculator!")
                break

            else:
                print("Invalid choice. Please enter a number from 0 to 6.")
                continue

            # Display result
            print("\n" + formula.display_formula())
            print("Answer:", formula.calculate())

        except ValueError:
            print("Invalid input! Please enter numeric values only.")


# Run the program
if __name__ == "__main__":
    main()
