def game():

	name = input("Hello Player! Share your name...\n")

	def odd_even():

		num = int(input("What number are you thinking of?\n"))

		if num % 2 == 0:
			print(f"You thought of {num}. That's an even number!")
			response = input("Have Another?\n(Type Yes/No)\n").lower()

		else:
			print(f"You thought of {num}. That's an odd number! Have another?")
			response = input("Have Another?\n(Type Yes/No)\n").lower()

		if response == "yes":
			odd_even()

		else:
			print(f"Thanks for playing {name[0].upper() + name[1:].lower()}!")

	odd_even()

game()