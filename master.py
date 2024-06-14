import random
import os

class TicTacToe:
    def __init__(self):
        self.resets_game()
    
    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def resets_game(self):
        self.board = [[" "," ", " "],[" ", " ", " "],[" ", " ", " "]]
        self.done = False

    def checks_win_or_draw(self):
        
        dict_win = {"X": False, "O": False}

        for i in ["X", "O"]:
            #horizontal
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i) or dict_win[i]
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            #vertical
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            #diagonal
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = True
            print("X wins")
            return
        
        elif dict_win["O"]:
            self.done = True
            print("O wins")
            return
        
        if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            self.done = True
            print("It is a draw")
            return

    def gets_players_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print("Type the row of your next move: ")
                x = int(input())

                print("Type the column of your next move: ")
                y = int(input())

                if 0 <= x <= 2 and 0 <= y <= 2 and self.board[x][y] == " ":
                    self.board[x][y] = "X"
                    invalid_move = False
                else:
                    print("Invalid coordinates. Type again.")
            except Exception as e:
                print(e)

    def makes_a_move(self):
        list_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]

        if list_moves:
            x, y = random.choice(list_moves)
            self.board[x][y] = "O"

tic_tac_toe = TicTacToe()

#main game loop
while True: 
    os.system("cls" if os.name == "nt" else "clear")  #crossplatform screen cleaner
    tic_tac_toe.print_board()
    
    if tic_tac_toe.done:
        print("Type 'q' to quit the game or any other button to play again")
        next_move = input()
        if next_move == 'q':
            break
        else:
            tic_tac_toe.resets_game()
    else:
        tic_tac_toe.gets_players_move()
        tic_tac_toe.checks_win_or_draw()
        if not tic_tac_toe.done:
            tic_tac_toe.makes_a_move()
            tic_tac_toe.checks_win_or_draw()