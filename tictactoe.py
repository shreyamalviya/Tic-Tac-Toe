class GameUI:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.row = "\t     |     |     "
        self.row_divider = "\t_____|_____|_____"
        print("\n\nLet's play Tic-Tac-Toe!")
        print("\t* To quit the game, press `ctrl d`.")
        print("\t* Refer to the following figure for positions.\n")
        self.draw_board()
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        GameLogic(self)

    def draw_board(self):
        for row in range(9):
            if row == 8:
                    print(self.row)
            elif row in [2, 5]:
                print(self.row_divider)
            elif row in [1, 4, 7]:
                temp_row = self.row
                if row == 1:
                    temp_row = "\t  {}  |  {}  |  {}  ".format(self.board[0][0], self.board[0][1], self.board[0][2])
                elif row == 4:
                    temp_row = "\t  {}  |  {}  |  {}  ".format(self.board[1][0], self.board[1][1], self.board[1][2])
                else:
                    temp_row = "\t  {}  |  {}  |  {}  ".format(self.board[2][0], self.board[2][1], self.board[2][2])
                print(temp_row)
            else:
                print(self.row)


class GameLogic:
    def __init__(self, ui):
        self.ui = ui
        self.played_positions = []
        self.char = ['O', 'X']
        self.main()

    def main(self):
        ch = 'O'
        while not self.game_over():
            if len(self.played_positions) == 9:
                print("\nIt's a draw!")
                break
            ch = self.next_move(ch)
            self.ui.draw_board()

        if self.game_over():
            index = self.char.index(ch)
            ch = self.char[(index+1)%2]
            print("\nCongratulations, {}! You win.".format(ch))

    def next_move(self, char):
        print("\n[{}] Enter position: ".format(char))
        pos = -1
        while pos == -1:
            try:
                pos = input()
                pos = int(pos)
            except EOFError:
                quit()
            except ValueError:
                continue
        if self.check_valid(pos):
            row = (pos-1)//3
            col = pos-1-(3*row)
            self.ui.board[row][col] = char
            self.played_positions.append(pos)
            index = self.char.index(char)
            return self.char[(index+1)%2]
        else:
            print("Invalid input. Try again.")
            index = self.char.index(char)
            return char
        
    def game_over(self):
        for row in range(0, 3):
            if (self.ui.board[row][0] == self.ui.board[row][1] == self.ui.board[row][2]) or\
               (self.ui.board[0][row] == self.ui.board[1][row] == self.ui.board[2][row]):
                if self.ui.board[row][0] != " " and\
                   self.ui.board[0][row] != " ":
                    return True
        if (self.ui.board[0][0] == self.ui.board[1][1] == self.ui.board[2][2]) or\
           (self.ui.board[0][2] == self.ui.board[1][1] == self.ui.board[2][0]):
            if (self.ui.board[1][1] != " ") and\
               ((self.ui.board[0][2] != " " and self.ui.board[2][0] != " ") or\
               (self.ui.board[0][0] != " " and self.ui.board[2][2] != " ")):
                return True
        return False

    def check_valid(self, pos):
        valid = False
        if pos in range(1, 10):
            if pos not in self.played_positions:
                valid = True
        return valid


def main():
    GameUI()

if __name__ == "__main__":
	main()
