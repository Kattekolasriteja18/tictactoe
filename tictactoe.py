s =[0,1,2,3,4,5,6,7,8,9]
def board():
    print("\n")
    print("\tTIC TAC TOE")
    print("\n")
    print("  PLAYER(X) -- PLAYER(O) ")
    print("\n")
    print("___________________")
    print("|     |     |     |")
    print("| ",s[1]," | ",s[2]," | ",s[3]," |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("| ",s[4]," | ",s[5]," | ",s[6]," |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("| ",s[7]," | ",s[8]," | ",s[9]," |")
    print("|_____|_____|_____|")


def checkwin():
    if s[1] == s[2] and s[2] == s[3]:
        return 1
    elif s[5] == s[4] and s[6] == s[5]:
        return 1
    elif s[7] == s[8] and s[8] == s[9]:
        return 1
    elif s[1] == s[4] and s[4] == s[7]:
        return 1
    elif s[2] == s[5] and s[5] == s[8]:
        return 1
    elif s[3] == s[6] and s[6] == s[9]:
        return 1
    elif s[1] == s[5] and s[5] == s[9]:
        return 1
    elif s[3] == s[5] and s[5] == s[7]:
        return 1
    if s[1] != 1 and s[2] != 2 and s[3] != 3 and s[4] != 4 and s[5] != 5 and s[6] != 6 and s[7] != 7 and s[8] != 8 and \
            s[9] != 9:
        return 0
    return -1


def play():
    player = 1
    i = -1
    while i == -1:
        board()
        if player%2==1:
            player=1
        else:
            player=2
        choice = int(input("player %d ,enter a choice :" % player))
        if player == 1:
            mark = "X"
        else:
            mark = "O"
        if choice == 1 and s[1] == 1:
            s[1] = mark
        elif choice == 2 and s[2] == 2:
            s[2] = mark
        elif choice == 3 and s[3] == 3:
            s[3] = mark
        elif choice == 4 and s[4] == 4:
            s[4] = mark
        elif choice == 5 and s[5] == 5:
            s[5] = mark
        elif choice == 6 and s[6] == 6:
            s[6] = mark
        elif choice == 7 and s[7] == 7:
            s[7] = mark
        elif choice == 8 and s[8] == 8:
            s[8] = mark
        elif choice == 9 and s[9] == 9:
            s[9] = mark
        else:
            player = player - 1
        i = checkwin()
        player += 1
    if i == 1:
        board()
        print("\t PLAYER %d WON THE MATCH " % (player - 1))
    else:
        print("DRAW")


play()


