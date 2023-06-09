#tic-tac-toe game

    #column
#row[0,0] [0,1] [0,2]  row and column index to aid check winner function
#   [1,0] [1,1] [1,2]
#   [2,0] [2,1] [2,2]

from tkinter import*
import random 

def next_turn(row, column):
    global player 
    if game_buttons[row][column]['text'] == "" and check_winner() is False: #if the text on each button on row/column is empty and there is no winner
        if player == players[0]:   #then if player is equal to X
            game_buttons[row][column]['text'] = player #then the empty button's text is == X

            if check_winner() is False: #if there is no winner
                player = players[1] #then if player is equal to "0" - we switched players here
                player_label.config(text=(player + " turn")) #display O's turn

            elif check_winner() is True: #if there's a winner
                player_label.config(text=(player + " wins!")) #display X wins (since O played last)

            elif check_winner() == "Tie":  #if there's a tie
                player_label.config(text=("Tie!")) #display tie on the label
    
            
        else:   

            game_buttons[row][column]['text'] = player
        
            if check_winner() is False: #if there is no winner
                player = players[0] #if player equal X
                player_label.config(text=(player + " turn")) #display X's turn on the label
    
            elif check_winner() is True: #if there's a winner 
                player_label.config(text=(player + " wins!")) #display O wins 
    
            elif check_winner() == "Tie":  #if there's a tie
                player_label.config(text=("Tie!")) #display tie on the label
 
def check_winner(): #function checks for a winner by four ways (vertically, horizontally, diagonally and reverse diagonally)
    for row in range(3):
       if game_buttons[row][0]['text'] == game_buttons[row][1]['text'] == game_buttons[row][2]['text'] !="": #for a vertical win, if the buttons text on 
          #the same row on either of the indexes but different columns are equal to each other and aren't empty
          game_buttons[row][0].config(bg="green") #creates a green background for vertical wins
          game_buttons[row][1].config(bg="green")
          game_buttons[row][2].config(bg="green")
          return True #return true means there's a winner
       
    for column in range(3):
        if game_buttons[0][column]['text'] == game_buttons[1][column]['text'] == game_buttons[2][column]['text'] !="":#for a horizontal win, if the buttons text on 
          #the same column on either of the indexes but different rows are equal to each other and aren't empty
            game_buttons[0][column].config(bg="green") #creates a green background for horizontal wins
            game_buttons[1][column].config(bg="green")
            game_buttons[2][column].config(bg="green")
            return True #there's a winner

        if game_buttons[0][0]['text'] == game_buttons[1][1]['text'] == game_buttons[2][2]['text'] !="":#for a diagonal win, if the buttons text on 
            game_buttons[0][0].config(bg="green") #creates a green background for diagonal wins
            game_buttons[1][1].config(bg="green")
            game_buttons[2][2].config(bg="green")
          #different diagonal rows and columnsare equal to each other and aren't empty
            return True #there's a winner
    
        elif game_buttons[0][2]['text'] == game_buttons[1][1]['text'] == game_buttons[2][0]['text'] !="": #for a reverse diagonal win, if the buttons text on 
        #different reverse diagonal rows and columns are equal to each other aren't empty
            game_buttons[0][2].config(bg="green") #creates a green background for reverse diagonal wins
            game_buttons[1][1].config(bg="green")
            game_buttons[2][0].config(bg="green")
            return True #return there's a winner
    
        elif empty_spaces() is False: #if there are no empty spaces
            return "Tie"
        
    return False #no winner or tie
    
def empty_spaces():
    spaces = 9 #number of spaces on the board
    for row in range(3):
        for column in range(3):
            if game_buttons[row][column]['text'] != "": #if no button a row/column is not empty, that is, it has text on it
                spaces -= 1 #reduce the number of spaces by 1 / so the number of spaces reduces after each play till there is none

    if spaces == 0: #return false when they are no spaces left
        return False #there is a tie
    else:
        return True   

def new_game():
    global player #refers to the global players varaible
    player = random.choice(players) #assigns a random player to a new game first
    player_label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            game_buttons[row][column].config(text="",bg="#F0F0F0")

window = Tk() #instantiates the instance of window
score = 0
players = ["X", "O"]
player = random.choice(players)

game_buttons = [[0,0,0], #each square on the board is represented by 0 (total of 6 sides)
                [0,0,0],
                [0,0,0]]

player_label = Label(window, text= player + " turn", font=('Consolas', 40)) #creates a label to display player's turn
player_label.pack(side="top") #packs the label to the top

restart_button = Button(window, text='Restart', font=('Consolas', 40), command=new_game)
restart_button.pack(side="top")

#creating a frame to hold the buttons
frame = Frame(window)
frame.pack()

#adding the buttons to the frame with a for nested loop instead of creating six buttons manually using grid
for row in range(3):
    for column in range(3):
        game_buttons[row][column] = Button(frame, text="", font=('Consolas', 40), width=5, height=2,
                                command= lambda row=row, column=column : next_turn(row, column))
        #for loop turning each sqaure on the board to a button using row and column
        game_buttons[row][column].grid(row=row,column=column) #this adds the buttons to the window using grid geometry manager

window.title("Tic-Tac-Toe")
window.mainloop() #displays a window on the screen