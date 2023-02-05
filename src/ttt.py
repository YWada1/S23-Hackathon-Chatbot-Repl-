import random

class TicTacToe:

  def playttt(self):
    board = [
        "", "", "",
        "", "", "",
        "", "", ""
    ]
    
    winner = ""
    full_board = False
    
    
    def verify_winner(board):
    
        if board[0] == board[1] == board[2] != "":
            return board[0]
        if board[3] == board[4] == board[5] != "":
            return board[3]
        if board[6] == board[7] == board[8] != "":
            return board[6]
    
        if board[0] == board[3] == board[6] != "":
            return board[0]
        if board[1] == board[4] == board[7] != "":
            return board[1]
        if board[2] == board[5] == board[8] != "":
            return board[2]
    
        if board[0] == board[4] == board[8] != "":
            return board[0]
        if board[2] == board[4] == board[6] != "":
            return board[2]
    
    
    def check_full_board(self):
        counter = 0
    
        for box in board:
            if box:
                counter += 1
        if counter == 9:
            return True
        return False
    
    
    def draw_board(self, board):
    
        for index, box in enumerate(board):
    
            if index // 3 != (index - 1) // 3:
                print("+---+---+---+")
    
            if box:
                print("| " + box + " ", end="")
    
            else:
                print("|   ", end="")
    
            if index % 3 == 2:
                print("|")
            if index == 8:
                print("+---+---+---+")
    
    
    while not winner or full_board:
    
        draw_board(self, board)
    
        box_number = -1
        valid_input = False
        while not valid_input:
            box_number = int(input("Choose a box "))
    
            if box_number < 1 or box_number > 9:
                print("Please choose a box between 1 and 9")
    
            elif board[box_number - 1]:
                print("Please choose an empty box")
    
            else:
                board[box_number - 1] = "X"
                valid_input = True
    
        winner = verify_winner(board)
    
        if winner:
            break
    
        computer_play = -1
        while board[computer_play - 1] or computer_play == -1:
            computer_play = random.randint(1, 9)
    
        board[computer_play - 1] = "O"
        print("Computer played box " + str(computer_play))
    
        winner = verify_winner(board)
    
        if full_board:
            break
    
    
    if winner:
        draw_board(self, board)
        print("Winner is "+winner)
    else:
        print("We tied")