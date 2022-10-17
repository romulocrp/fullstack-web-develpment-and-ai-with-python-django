from random import choice

# This code can surely be refactored and turned into a more reusable one.

game_mode = input("Select the mode you want to play, vs Computer or vs Player, type \"exit\" to exit:\n")

while game_mode.lower() != "exit":

    board = "1    2    3\n   |   |   \n4    5    6\n   |   |   \n7    8    9\n   |   |  "

    coord_dict = {"1":13, "2":17, "3":21, "4":37, "5":41, "6":45, "7":61, "8":65, "9":69}

    if game_mode.lower() == "player":

        print(board)

        tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space (player): ").split()]

        board_lst = list(board)
        board_lst[coord_dict[coord]] = tic.lower()
        board = "".join(board_lst)

        vic_con = False

        while vic_con == False:
            print(board)
            board_lst = list(board)
            tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space: ").split()]
            if board_lst[coord_dict[coord]] == tic.lower():
                print("Space already taken, please try again.")
                tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space: ").split()]
            else:
                board_lst[coord_dict[coord]] = tic.lower()
                board = "".join(board_lst)
                vc1 = (board[13] == board[41] == board[69] == tic)
                vc2 = (board[21] == board[41] == board[61] == tic)
                vc3 = (board[13] == board[17] == board[21] == tic)
                vc4 = (board[37] == board[41] == board[45] == tic)
                vc5 = (board[61] == board[65] == board[69] == tic)
                vc6 = (board[13] == board[37] == board[61] == tic)
                vc7 = (board[17] == board[41] == board[65] == tic)
                vc8 = (board[21] == board[45] == board[69] == tic)
                vic_con = vc1 or vc2 or vc3 or vc4 or vc5 or vc6 or vc7 or vc8


        print(board)
        print(f"Game is finished {tic} won")
        break
    elif game_mode.lower() == "computer":

        print(board)

        tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space (computer): ").split()]
        
        if (tic.lower() != "x") and (tic.lower() != "o"):
            print("Please enter either \"x\" or \"o\".")
            tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space (computer): ").split()]

        elif tic.lower() == "x":
            board_lst = list(board)
            board_lst[coord_dict[coord]] = tic.lower()
            board = "".join(board_lst)

            vic_con = False

            computer_move = "o"
        
            while vic_con == False:
                board_lst = list(board)
                computer_coord = choice(list(coord_dict.values()))
                while (board_lst[computer_coord] == "o") or (board_lst[computer_coord] == tic.lower()):
                    computer_coord = choice(list(coord_dict.values()))
                board_lst[computer_coord] = computer_move
                vc1 = (board[13] == board[41] == board[69] == computer_move)
                vc2 = (board[21] == board[41] == board[61] == computer_move)
                vc3 = (board[13] == board[17] == board[21] == computer_move)
                vc4 = (board[37] == board[41] == board[45] == computer_move)
                vc5 = (board[61] == board[65] == board[69] == computer_move)
                vc6 = (board[13] == board[37] == board[61] == computer_move)
                vc7 = (board[17] == board[41] == board[65] == computer_move)
                vc8 = (board[21] == board[45] == board[69] == computer_move)
                vic_con = vc1 or vc2 or vc3 or vc4 or vc5 or vc6 or vc7 or vc8
                if vic_con == True:
                    print("Computer won!")
                    board = "".join(board_lst)
                    print(board)
                    break
                
                board = "".join(board_lst)
                print(board)
                tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space: ").split()]
                board_lst = list(board)
                if board_lst[coord_dict[coord]] == tic.lower():
                    print("Space already taken, please try again.")
                    tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space: ").split()]
                else:
                    board_lst[coord_dict[coord]] = tic.lower()
                    board = "".join(board_lst)
                    vc1 = (board[13] == board[41] == board[69] == tic)
                    vc2 = (board[21] == board[41] == board[61] == tic)
                    vc3 = (board[13] == board[17] == board[21] == tic)
                    vc4 = (board[37] == board[41] == board[45] == tic)
                    vc5 = (board[61] == board[65] == board[69] == tic)
                    vc6 = (board[13] == board[37] == board[61] == tic)
                    vc7 = (board[17] == board[41] == board[65] == tic)
                    vc8 = (board[21] == board[45] == board[69] == tic)
                    vic_con = vc1 or vc2 or vc3 or vc4 or vc5 or vc6 or vc7 or vc8
                    if vic_con == True:
                        print("Congratulations! You beat the computer!")
                        print(board)
                        break
            break
        elif tic.lower() == "o":
            board_lst = list(board)
            board_lst[coord_dict[coord]] = tic.lower()
            board = "".join(board_lst)

            vic_con = False

            computer_move = "x"
        
            while vic_con == False:
                board_lst = list(board)
                computer_coord = choice(list(coord_dict.values()))
                while (board_lst[computer_coord] == "o") or (board_lst[computer_coord] == tic.lower()):
                    computer_coord = choice(list(coord_dict.values()))
                board_lst[computer_coord] = computer_move
                vc1 = (board[13] == board[41] == board[69] == computer_move)
                vc2 = (board[21] == board[41] == board[61] == computer_move)
                vc3 = (board[13] == board[17] == board[21] == computer_move)
                vc4 = (board[37] == board[41] == board[45] == computer_move)
                vc5 = (board[61] == board[65] == board[69] == computer_move)
                vc6 = (board[13] == board[37] == board[61] == computer_move)
                vc7 = (board[17] == board[41] == board[65] == computer_move)
                vc8 = (board[21] == board[45] == board[69] == computer_move)
                vic_con = vc1 or vc2 or vc3 or vc4 or vc5 or vc6 or vc7 or vc8
                if vic_con == True:
                    print("Computer won!")
                    board = "".join(board_lst)
                    print(board)
                    break
                
                board = "".join(board_lst)
                print(board)
                tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space: ").split()]
                board_lst = list(board)
                if board_lst[coord_dict[coord]] == tic.lower():
                    print("Space already taken, please try again.")
                    tic, coord = [x for x in input("Insert \"x\" or \"o\" and coordinate (1-9) separate by space: ").split()]
                else:
                    board_lst[coord_dict[coord]] = tic.lower()
                    board = "".join(board_lst)
                    vc1 = (board[13] == board[41] == board[69] == tic)
                    vc2 = (board[21] == board[41] == board[61] == tic)
                    vc3 = (board[13] == board[17] == board[21] == tic)
                    vc4 = (board[37] == board[41] == board[45] == tic)
                    vc5 = (board[61] == board[65] == board[69] == tic)
                    vc6 = (board[13] == board[37] == board[61] == tic)
                    vc7 = (board[17] == board[41] == board[65] == tic)
                    vc8 = (board[21] == board[45] == board[69] == tic)
                    vic_con = vc1 or vc2 or vc3 or vc4 or vc5 or vc6 or vc7 or vc8
                    if vic_con == True:
                        print("Congratulations! You beat the computer!")
                        print(board)
                        break
            break
    else:
        print("Please select a valid game mode.")
        game_mode = input("Select the mode you want to play, vs Computer or vs Player, type \"exit\" to exit:\n")

print("Game exited soundly.")