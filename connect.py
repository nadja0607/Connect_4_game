'''
CS-UH 1001 Introduction to Computer Science
Fall 2018
Project name: Connect 4 game
Professor: Yasir Zaki
Student: Nadja Fejzic
'''

#imports
import random, os, time

#parameters
numRows=6
numCols=7
numPlayers=2
board=[]
playerNames=['Player 1','Player 2']
checkers=['X','O']
numPlays = numCols*numRows
winNum=4
plays=0
win=False
turn=random.randint(0,numPlayers-1)

#greetings
time.sleep(0.5)
print('HELLO!!!')
time.sleep(0.5)
print('WELCOME TO CONNECT 4!!!')
time.sleep(0.5)
print('TRY TO CONNECT 4 CHECKERS AN WIN!!!')
print('Be careful and check ALL 4 directions')
time.sleep(1)
print('Players get ready....')
time.sleep(1)


#creating the board
for r in range(numRows):
    temp=[]
    for c in range(numCols):
        temp.append('-')
    board.append(temp)


#printing the board
def printBoard():
	os.system('clear')
	for c in range(numCols):
		print(c, end=' ')
	print()
	for r in range(numRows):
		for c in range(numCols):
			print(board[r][c], end=' ')
		print()

#defining inputs
def userInput():
	column=input(playerNames[turn]+', enter the column number: ')

	while not column.isdigit():
		print('Your input is invalid. Please enter an integer withing the table range: ')
		column=input(playerNames[turn]+', enter the column number: ')
	while int(column)>numCols-1 or int(column)<0 or column==' ':
		print('The number you entered is out of range. Enter the valid number: ')
		column=input(playerNames[turn]+', enter the column number: ')



	return (column)

#check win
def checkWin():
	#horizontal
	for a in range(numRows):
		for b in range(numCols - winNum+1):
			count=0
			for i in range (winNum):
				if board[a][b+i]==checkers[turn]:
					count=count+1
				else:
					count=0
			if count==winNum:
				return True

	#vertical
	for d in range(numRows- winNum+1):
		for f in range(numCols):
			count=0
			for i in range(winNum):
				if board[d+i][f]==checkers[turn]:
					count=count+1
				else:
					count=0
			if count==winNum:
				return True

	#1st diagonal
	for g in range(numRows- winNum+1):
		for h in range(numCols- winNum+1):
			count=0
			for m in range(winNum):
				if board[g+m][h+m]==checkers[turn]:
					count=count+1
				else:
					count=0
			if count==winNum:
				return True
				
			
	#2nd diagonal
	for g in range(numRows- winNum+1):
		for h  in range(numCols- winNum+1):
			count=0
			for m in range(winNum):
				if board[g+m][h-m]==checkers[turn]:
					count=count+1
				else:
					count=0
			if count==winNum:
				return True
	else:
		return False


#game loop
while win != True and plays< numPlays :
	printBoard()
	col=int(userInput())
	for r in range(numRows-1,-1,-1):
		if board[r][col]=='-':
			board[r][col]=checkers[turn]
			plays+=1
			print(plays)
			break
			
	
	print(plays)
	win=checkWin()
	turn=(turn+1)%numPlayers
	printBoard()
if plays==numPlays:
	print('IT IS A DRAW... TRY AGAIN...')
elif win==True:
	print('CONGRATULATIONS!!!!!')
	time.sleep(0.5)
	print(playerNames[turn],'YOU ARE THE WINNER!!!!')