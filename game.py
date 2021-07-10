valid_choices = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]


class Game:
    def __init__(self):
        self.player_1 = input("The first player is x. What is the first player's name?\n")
        self.player_2 = input("The second player is o. What is the second player's name?\n")
        self.turn = "x"
        self.turn_num = 1
        self.board = {
            "a": ["-", "-", "-"],
            "b": ["-", "-", "-"],
            "c": ["-", "-", "-"]
        }

    def display_board(self):
        print(f"   a     b     c\n"
              f"      |     |     \n"
              f"1  {self.board['a'][0]}  |  {self.board['b'][0]}  |  {self.board['c'][0]}\n"
              f" _____|_____|_____\n"
              f"      |     |     \n"
              f"2  {self.board['a'][1]}  |  {self.board['b'][1]}  |  {self.board['c'][1]}\n"
              f" _____|_____|_____\n"
              f"      |     |     \n"
              f"3  {self.board['a'][2]}  |  {self.board['b'][2]}  |  {self.board['c'][2]}\n"
              f"      |     |     \n")

    def player_turn(self):
        """Asks the player to enter a valid choice"""
        if self.turn == "x":
            player_name = self.player_1
        else:
            player_name = self.player_2

        player_choice = input(f"{player_name}, pick an open box to put an {self.turn} by entering the column, 'a', 'b',"
                              f" or 'c' and the cell number, 1, 2, 3. (e.g. 'a1', 'b2' or 'c3'):\n").strip().lower()

        while player_choice not in valid_choices:
            print(f"Invalid choice entered! Please submit an open box as listed below")
            player_choice = input(
                f"{player_name}, pick an open box to put an {self.turn} by entering the column, 'a', 'b', or "
                f"'c' and the cell number, 1, 2, 3. (e.g. 'a1', 'b2' or 'c3'):\n").strip().lower()

        self.update_board(player_choice)

    def update_board(self, choice: str):
        col, row = [char for char in choice]
        valid_choices.remove(choice)
        self.board[col][int(row) - 1] = self.turn

        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"
        self.turn_num += 1

    def check_winner(self):
        """Checks rows, columns and diagonals for a winner and returns player name if winner found"""
        for row in self.board.values():
            if all([mark == "x" for mark in row]):
                return self.player_1
            elif all([mark == "o" for mark in row]):
                return self.player_2

        # checks every column
        for i in range(3):
            first_row, second_row, third_row = self.board.values()
            if first_row[i] == "x" and second_row[i] == "x" and third_row[i] == "x":
                return self.player_1
            elif first_row[i] == "o" and second_row[i] == "o" and third_row[i] == "o":
                return self.player_2

        # checks the diagonals
        if self.board["a"][0] == "x" and self.board["b"][1] == "x" and self.board["c"][2] == "x":
            return self.player_1
        if self.board["a"][2] == "o" and self.board["b"][1] == "o" and self.board["c"][0] == "o":
            return self.player_2

        return None
