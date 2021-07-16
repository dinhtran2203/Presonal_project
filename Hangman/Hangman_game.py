

import random
import string
def get_random_word():
	word = random.choice(open("word.txt").readlines())

	"""
	word.rstrip() is remove the last character in the string. 
	the word in txt file is ***/n
	"""
	return word.rstrip().upper()

def hang_man():

	word = get_random_word()

	# define unique words
	hidden_word = set(word)

	# alphabet character
	alphabet = set(string.ascii_uppercase)

	used_letters = set()
	lives = 5
	while len(hidden_word) > 0 and lives > 0:

		print()
		# letter used
		print("You have " ,lives, " life left and You have used: " , " ".join(used_letters))

		# what current word is (ie w-s-d)
		currentword = [letter if letter in used_letters else '-' for letter in word]
		print("current word: ", " ".join(currentword))

		userinput = input("Guess a letter: ").upper()
		if userinput in alphabet - used_letters:
			used_letters.add(userinput)
			if userinput in hidden_word:
				hidden_word.remove(userinput)
			lives-=1
		elif userinput in used_letters:
			print("you have used that character. Please try again")
		else:
			print("Invalid character. Please try again")
	if lives > 0:
		print("---------------------------------")
		print("Congratulation you found the word")
		print("The word is: ", word)
	print("---------------------------------")
	print("You lose the game. The word is: " , word)
hang_man()



