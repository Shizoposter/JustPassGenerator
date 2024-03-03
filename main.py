# First Project. Password Generation.

import string
import random
from tkinter import *

fourthPassword_S = ['lemon', 'bottle', 'notepad', 'teacher', 'matemathics', 'letter', 'window', 'level', 'axe', 'pen']
fourthPassword_P = ['awful', 'ugly', 'warm', 'daily', 'economic', 'glass', 'beautiful', 'huge', 'unhappy', 'impossible']
fourthPassword_G = ['read', 'believe', 'be', 'fall', 'live', 'listen', 'understand', 'wonder', 'write', 'talk']

def mainGenerator():

	if difficultyList.curselection() == (0,):
		passwordEntry.delete(0, END)
		alpha = [','.join(random.sample(string.ascii_letters, 3)), 
			','.join(random.sample(string.digits, 1))
			]
		# random.shuffle возвращает значение None, поэтому сделал по-другому:
		beta = alpha[0] + alpha[1]
		s = ''
		for i in beta:
			if i == ',':
				continue
			else:
				s = s + i
		s1 = ''.join(random.sample(s, k=len(s)))
		passwordEntry.insert(END, s1)

	elif difficultyList.curselection() == (1,):
		passwordEntry.delete(0, END)
		alpha = [','.join(random.sample(string.ascii_letters, 4)), 
			','.join(random.sample(string.digits, 2)),
			random.choice(string.punctuation)
			]
		# random.shuffle возвращает значение None, поэтому сделал по-другому:
		beta = alpha[0] + alpha[1] + alpha[2]
		s = ''
		for i in beta:
			if i != ',':
				s = s + i
			else:
				continue
		s1 = ''.join(random.sample(s, k=len(s)))
		passwordEntry.insert(END, s1)

	elif difficultyList.curselection() == (2,):
		passwordEntry.delete(0, END)
		alpha = [','.join(random.sample(string.ascii_letters, 6)), 
			','.join(random.sample(string.digits, 3)),
			random.choice(string.punctuation)
			]
		# random.shuffle возвращает значение None, поэтому сделал по-другому:
		beta = alpha[0] + alpha[1] + alpha[2]
		s = ''
		for i in beta:
			if i != ',':
				s = s + i
			else:
				continue
		s1 = ''.join(random.sample(s, k=len(s)))
		passwordEntry.insert(END, s1)

	elif difficultyList.curselection() == (3,):
		passwordEntry.delete(0, END)
		alpha = [str(random.randint(2, 99)),
		random.choice(fourthPassword_P),
		random.choice(fourthPassword_S),
		random.choice(fourthPassword_G),
		random.choice(string.punctuation)
		]

		# random.shuffle возвращает значение None, поэтому сделал по-другому:
		beta = alpha[0] + alpha[1] + alpha[2] + alpha[3]
		s = ''
		for i in beta:
			if i != ',':
				s = s + i
			else:
				continue

		passwordEntry.insert(END, s+random.choice(string.punctuation))


def choiceADifficulty():

	rootCanv.destroy()
	startMenu_Label.destroy()
	startMenu_Button.destroy()
	infoLabel.destroy()

	global difficultyList
	difficultyList = Listbox(root, selectmode = SINGLE, height = 4)
	difficultyList.insert(END, 'Simple password', 'Middle password', 'Difficult password', 'Meaning password')
	difficultyList.place(x = 230, y = 120)

	startGenerate_Button = Button(root, width = 15, text = 'Start Generation', fg = '#b1b5b1', bg = '#4b4d4b', font = ('Bauhaus 93', 20), activeforeground = '#b1b5b1', activebackground = '#313331', command = mainGenerator)
	startGenerate_Button.place(x = 203, y = 400)

	global passwordEntry
	passwordEntry = Entry(root, width = 25, bd = 2, bg = '#b1b5b1', font = ('Candara', 20))
	passwordEntry.place(x = 108, y = 300)

root = Tk()
root.title('Password Generation')
root.geometry('600x600')
root.resizable(False, False)
root['bg'] = '#4b4d4b'

rootCanv = Canvas(root, width = 256, height = 256, bg = '#4b4d4b', bd=0, highlightthickness=0)
rootCanv.place(x = 150, y = 135)
logoPath = PhotoImage(file = 'password_icon_184039.gif')
logoPlace = rootCanv.create_image(145, 135, anchor = CENTER, image = logoPath)

startMenu_Label = Label(root, text = 'Password Generation', fg = '#b1b5b1', bg = '#4b4d4b', font = ('Candara', 30))
startMenu_Label.place(x = 120, y = 75)

startMenu_Button = Button(root, width = 15, text = 'Start', fg = '#b1b5b1', bg = '#4b4d4b', font = ('Candara', 20), bd = '3', activeforeground = '#b1b5b1', activebackground = '#313331', command = choiceADifficulty)
startMenu_Button.place(x = 180, y = 450)

infoLabel = Label(root, text = 'Written by Ushakov Kirill - Yota <yotahole850@gmail.com>', fg = '#b1b5b1', bg = '#4b4d4b', font = ('Candara', 15))
infoLabel.place(x = 30, y = 560)



root.mainloop()






