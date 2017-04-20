import os
import time


global correctScore
global incorrectScore
correctScore = 0
incorrectScore = 0

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def listTaskWords():
	clearScreen()
	print('BUSINESS MANAGEMENT TASK WORDS')
	print(' ')
	print('Analyse             Identify the main features then examine closely; examine in parts; show how the parts relate to the whole, e.g. analyse the essential components in decision-making or in the problem solving process')
	print('Apply               Use the information provided or knowledge in a particular situation and make links and connections; use theory to help in a practical example')
	print('Compare             Bring together for noting the points of likeness and difference, e.g. compare management theory and practice')
	print('Define              Accurately state or explain the meaning of the term')
	print('Describe            Provide a detailed account of something; give the facts about something and if the question refers to a process, provide a detailed account in sequential order')
	print('Discuss             Examine an issue or response and state arguments or opinions covering both sides of the issue or response covered in the stimulus material')
	print('Distinguish         Recognise or show points of difference; note the distinctive characteristics')
	print('Establish criteria  Determine criteria or measures to conduct an evaluation')
	print('Explain             Make the meaning of something clear and understandable')
	print('Evaluate            Apply a weighted criteria to the relative strengths and weaknesses of the arguments raised in the stimulus material, as well as provide your opinion')
	print('Identify            Determine or establish as being a particular thing, or determine the key characteristics or features')
	print('Illustrate          Provide an example to support your statement or comment')
	print('Label               Describe or designate, e.g. label the organisational chart with the appropriate management levels')
	print('List                Enter in a list with others')
	print('Outline             Provide a brief description of the term or topic')
	print('Justify             Justify your choice or selection')
	print('Recommend           Present and state facts, ideas or feelings appropriate to the issue or response covered in the stimulus material')
	print('Select              Choose one in preference to another')
	print(' ')
	if input('go back? [y/n] ') == 'y':
		mainMenu()
	else:
		listTaskWords()

def mainMenu():
	clearScreen()
	print('BUSINESS MANAGEMENT TASK WORDS')
	menuChoice = input('Would you like to [list] the task words or [play] a game of flash cards? ')
	if menuChoice == 'list':
		listTaskWords()
	elif menuChoice == 'play':
		flashcardGame()
	else:
		print('Please enter a correct option')

def gameQuestion(word, definition):
	global correctScore
	global incorrectScore
	clearScreen()
	print('BUSINESS MANAGEMENT FLASHCARDS | Correct: ' + str(correctScore))
	print(' ')
	print(definition)
	if str(input('Enter task word: ').lower()) == str(word).lower():
		print('Correct!')
		global correctScore
		correctScore = correctScore +1
		time.sleep(1)
	else:
		print('Incorrect! The word was: ' + word)
		time.sleep(1)

def gameQuestion2(word, word2, definition):
	global correctScore
	global incorrectScore
	clearScreen()
	print('BUSINESS MANAGEMENT FLASHCARDS | Correct: ' + str(correctScore))
	print(' ')
	print(definition)
	gameQuestion2Input = str(input('Enter task word: ').lower())
	if gameQuestion2Input == str(word).lower():
		print('Correct!')
		global correctScore
		correctScore = correctScore +1
		time.sleep(1)
	elif gameQuestion2Input == str(word2).lower():
		print('Correct!')
		global correctScore
		correctScore = correctScore +1
		time.sleep(1)
	else:
		print('Incorrect! The word was: ' + word)
		time.sleep(1)

def flashcardGame():
	clearScreen()
	print('BUSINESS MANAGEMENT FLASHCARDS')
	print(' ')
	print('Welcome to the BMM flashcard game!')
	print('A definition will appear on screen and you will have to determine the correct task word for it')
	print(' ')
	gameready = input('Are you ready? (y/n) ')
	if gameready == 'n' or '':
		mainMenu()
	elif gameready == 'y':
		correctScore = 0
		clearScreen()
		gameQuestion('Analyse', 'Identify the main features then examine closely; examine in parts; show how the parts relate to the whole, e.g. analyse the essential components in decision-making or in the problemsolving process')
		gameQuestion('Apply', 'Use the information provided or knowledge in a particular situation and make links and connections; use theory to help in a practical example')
		gameQuestion('Define', 'Accurately state or explain the meaning of the term')
		gameQuestion('Compare', 'Bring together for noting the points of likeness and difference, e.g. compare management theory and practice')
		gameQuestion('Describe', 'Provide a detailed account of something; give the facts about something and if the question refers to a process, provide a detailed account in sequential order')
		gameQuestion('Discuss', 'Examine an issue or response and state arguments or opinions covering both sides of the issue or response covered in the stimulus materia')
		gameQuestion('Distinguish', 'Recognise or show points of difference; note the distinctive characteristics')
		gameQuestion('Establish Criteria', 'Determine criteria or measures to conduct an evaluation')
		gameQuestion('Explain', 'Make the meaning of something clear and understandable')
		gameQuestion('Evaluate', 'Apply a weighted criteria to the relative strengths and weaknesses of the arguments raised in the stimulus material, as well as provide your opinion')
		gameQuestion('Identify', 'Determine or establish as being a particular thing, or determine the key characteristics or features')
		gameQuestion('Illustrate', 'Provide an example to support your statement or comment')
		gameQuestion('Label', 'Describe or designate, e.g. label the organisational chart with the appropriate management levels')
		gameQuestion('List', 'Enter in a list with others')
		gameQuestion('Outline', 'Provide a brief description of the term or topic')
		gameQuestion2('Provide Reasons', 'Justify', 'Justify your choice or selection')
		gameQuestion2('Recommend', 'Suggest', 'Present and state facts, ideas or feelings appropriate to the issue or response covered in the stimulus material')
		gameQuestion('Select', 'Choose one in preference to another')
		clearScreen
		print('BUSINESS MANAGEMENT FLASHCARDS')
		print(' ')
		global correctScore
		if correctScore >= 9:
			print('Congratulations, you got ' + str(correctScore) + ' correct')
			time.sleep(5)
			mainMenu()
		elif correctScore == 0:
			print('YOU GOT THEM ALL WRONG, GO BACK AND STUDY')
			time.sleep(5)
			mainMenu()
		else:
			print('You only got ' + str(correctScore) + ' correct, that\'s less than half, you might want to study more.')
			time.sleep(5)
			mainMenu()


mainMenu()
