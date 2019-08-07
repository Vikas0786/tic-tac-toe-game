def tic_tac_toe():
    print("            TIC TAC TOE GAME")
    print("Player 1: X")
    print("Player 2: O")
    print()
    board=[1,2,3,4,5,6,7,8,9]
    end=False
    win_combinations=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    def draw():
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])
        print()

    def p1():
        n=choose_number()
        if(board[n]=="X" or board[n] == "O"):
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"

    def p2():
        n=choose_number()
        if(board[n]=="X" or board[n] == "O"):
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "O"

    def choose_number():
            while True:
                a=input()
                try:
                    a=int(a)
                    a-=1
                    if a in range(0,9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue

    def check_board():
        count=0
        for a in win_combinations :
            if (board[a[0]] == board[a[1]] == board[a[2]] == "X"):
                print("Player 1 Wins!\n")
                print("congratulations!\n")
                return True

            elif (board[a[0]] == board[a[1]] == board[a[2]] == "O"):
                print("Player 2 Wins!\n")
                print("congratulations!\n")
                return True

        for i in range(9):
            if board[i] == "X" or board[i] == "O":
                count+=1
            if (count==9):
                print("The game ends in a tie\n")
                return True

    while (not end):
        draw()
        end=check_board()
        if end == True:
            break
        print("Player 1 : ")
        p1()
        print()
        draw()
        end == check_board()
        if end == True:
            break
        print("Player 2 : ")
        p2()
        print()

    if input("play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()
                


