from tkinter import *
import random


#creating window
window = Tk()
window.title('Tic Tac Toe')
window.geometry('500x600')

#creating a frame
frame = Frame(window)
frame.pack()

#setting up players
players = ['x', 'o' ]
player = random.choice(players)

#setting up colors
w_color = 'lightgreen'
t_color = 'lightblue'

#this function switches turns between the 2 players and checks for wins/ties
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == '' and handle_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if handle_winner() is False:
                player = players[1]
                label.config(text=(players[1] + ' turn'))
            elif handle_winner() is True:
                label.config(text=(players[0] + ' wins'))
            elif handle_winner() is 'Tie':
                label.config(text=('Tie'))

        else:
            buttons[row][column]['text'] = player
            if handle_winner() is False:
                player = players[0]
                label.config(text=(players[0] + ' turn'))
            elif handle_winner() is True:
                label.config(text=(players[1] + ' wins'))
            elif handle_winner() is 'Tie':
                label.config(text=('Tie'))

#this function checks if any of the possible wins have the same simbol (x or o)
def handle_winner():
    #rows
    for row in range(3): 
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg=w_color)
            buttons[row][1].config(bg=w_color)
            buttons[row][2].config(bg=w_color)
            return True
    #columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg=w_color)
            buttons[1][column].config(bg=w_color)
            buttons[2][column].config(bg=w_color)
            return True
    #diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
            buttons[0][0].config(bg=w_color)
            buttons[1][1].config(bg=w_color)
            buttons[2][2].config(bg=w_color)
            return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
            buttons[0][2].config(bg=w_color)
            buttons[1][1].config(bg=w_color)
            buttons[2][0].config(bg=w_color)
            return True
    #tie
    elif handle_empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg=t_color)
        return 'Tie'
    else:
        return False

#this function checks if the game can still be played or if there are no more spaces left
def handle_empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1 
    if spaces == 0:
        return False
    else:
        return True

#this function is used to reset the game
def handle_new_game():
    global player

    player = random.choice(players)
    label.config(text= player + ' turn')

    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ''
            buttons[row][column].config(bg='white')

#setting up buttons
buttons = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]]

#setting up label
label = Label(text= player + ' turn', font=('arial', 40)) 
label.pack(side='top')

#setting up reset button
reset_btn = Button(text='reset', font=('arial', 20), command=handle_new_game)
reset_btn.pack(side='top')


#using button arr to display buttons
for row in range(3):
    for column in range(3):

        buttons[row][column] = Button(frame, text='', font=('arial', 40),
        width=5, height=2, command= lambda row=row, column=column: next_turn(row, column))

        buttons[row][column].grid(row=row, column=column)












window.mainloop()