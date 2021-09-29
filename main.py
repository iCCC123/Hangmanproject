import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

ended = False
list = ["toyota", "nissan", "cadillac", "ford", "chevrolet", "bentley", "honda", "fiat", "citroen", "borgward", "porsche", "dodge"]
compword = random.choice(list)
wlength = len(compword)

tries = 6

display = []
for i in range(wlength):
	display += "_"
print(display)

while not ended:
	userguess = input("guess a letter: ").lower()

	for q in range(wlength):
		letter = compword[q]
		if letter == userguess:
			display[q] = letter

	if userguess not in compword:
		tries -= 1
		if tries == 0:
			ended = True
			print("you lose.")

	print(f"{' '.join(display)}")

	if "_" not in display:
		ended = True
		print("you win!")

	print(stages[tries])
