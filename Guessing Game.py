# class for guessing game
class GuessingGame:
	def __init__(self, lower, upper):
		self.lower = lower
		self.upper = upper
	def play(self):
		raise NotImplementedError("Subclasses must implement this method.")

# Derived class for number guessing
import random
class NumberGuessingGame(GuessingGame):
	def play(self):
		number = random.randint(self.lower, self.upper)
		tries = 0
		print(f"I'm thinking of a number between {self.lower} and {self.upper}.")
		while True:
			guess = input("Enter your guess: ")
			try:
				guess = int(guess)
			except ValueError:
				print("Please enter a valid number.")
				continue
			tries += 1
			if guess == number:
				print(f"Congratulations! You guessed the number in {tries} tries.")
				break
			elif guess < number:
				print("Too low. Try again.")
			else:
				print("Too high. Try again.")

# Another derived class for demonstration (e.g., guessing a word)
class WordGuessingGame(GuessingGame):
	def __init__(self, word_list):
		super().__init__(1, len(word_list))
		self.word_list = word_list
	def play(self):
		import random
		word = random.choice(self.word_list)
		print("Guess the secret word!")
		while True:
			guess = input("Enter your guess: ")
			if guess.lower() == word.lower():
				print(f"Correct! The word was '{word}'.")
				break
			else:
				print("Wrong word. Try again.")

def main():
	print("--- Guessing Game ---")
	print("Choose game type:")
	print("1. Number Guessing Game")
	print("2. Word Guessing Game")
	choice = input("Enter 1 or 2: ")

	# Polymorphism: use base class reference
	if choice == '1':
		game = NumberGuessingGame(1, 10)
	elif choice == '2':
		words = ["apple", "banana", "orange", "grape", "melon"]
		game = WordGuessingGame(words)
	else:
		print("Invalid choice.")
		return

	try:
		game.play()
	except Exception as error:
		print(f"Something went wrong: {error}")

if __name__ == "__main__":
	main()


