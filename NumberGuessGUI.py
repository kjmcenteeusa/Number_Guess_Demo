"""
Program: NumberGuessGUI.py
Chapter 8 (Page 251)
1/22/2024

**NOTE: The module breezypythongui.py
MUST be in the same directory as this
file for the app to run correctly.

Template code for any GUI-based application in Chapter 9

GUI for Number Guessing Game.

"""
from breezypythongui import EasyFrame
import random
# Other imports go here.

# Class header (class name will change from project to project.)
class NumberGuessGUI(EasyFrame):
	#Definition of our classes' constructor method
	def __init__(self):
		# Call to the EasyFrame class constructor.
		EasyFrame.__init__(self, title = "Guessing Game GUI", width = 260, height = 180)

		# Initialize the instance variable for the class.
		self.magicNumber = random.randint(1,100)
		self.count = 0

		# Create and add widgets to the window.
		self.hintLabel = self.addLabel(text = "Guess a number between 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addLabel(text = "Your guess", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)

	# Defintion of the nextGuess() function
	def nextGuess(self):
		""" Processes the user's next guess."""
		
		self.count += 1
		
		""" Collect the user input from the integer field."""
		
		guess = self.guessField.getNumber()
		
		""" Logic that determines the game's outcome."""

		if guess == self.magicNumber:
			self.hintLabel["text"] = "Horray! You got it in " + str(self.count) + " attempts!"
			self.nextButton["state"] = "disabled"
		elif guess < self.magicNumber:
			self.hintLabel["text"] = "Sorry, your guess was too low."
		else:
			self.hintLabel["text"] = "Sorry, your guess was too high."
	
	# Definition of newGame() funtion.

	def newGame(self):
		""" Resets the data and GUI to their original states."""
		self.magicNumber = random.randint(1,10)
		self.count = 0
		self.hintLabel = self.addLabel(text = "Guess a number between 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"

		# Global definition of the main() method.
def main():
	# Instantiate an object from the class into mainLoop()
	NumberGuessGUI().mainloop()
	self.count = 0

# Global call to main() for program entry.
if __name__ == '__main__':
	main()

