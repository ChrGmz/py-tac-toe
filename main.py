from game import Game
from art import logo
from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def play_again():
    reset_response = input("Would you like to play again? Type 'y' or 'n': ").strip().lower()
    while reset_response not in ["y", "n"]:
        print("Invalid response entered. Please only enter 'y' or 'n': ")
        reset_response = input("Would you like to play again? Type 'y' or 'n': ").strip().lower()
    if reset_response == "y":
        return True
    return False


clear()
print("Welcome to Py Tac Toe: a Two-Player Python Version of Tic Tac Toe")
print(logo)

game = Game()

is_on = True
game.display_board()

while is_on:
    game.player_turn()
    game.display_board()

    if game.turn_num >= 5:
        winner = game.check_winner()
        if winner is not None:
            print(f"{winner} has won the game!")
            if play_again():
                clear()
                game = Game()
                game.display_board()
            else:
                is_on = False
                print("Thank you for playing Py Tac Toe!")
    if game.turn_num > 9:
        print("The game is a draw!")
        if play_again():
            clear()
            game = Game()
            game.display_board()
        else:
            is_on = False
            print("Thank you for playing Py Tac Toe!")

