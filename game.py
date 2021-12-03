
import math
import time



class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None






if __name__ == '__main__':
    gata = False
    contorx = 0
    contory = 0
    while gata != True:
        dificultate = input('Ce dificultate vrei? [1/2/3]  ')
        dif=dificultate
        x_player = HumanPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = TicTacToe()
        final = play(dif,t, x_player, o_player, print_game=True)
        if final == 'X':
            contorx = contorx + 1
        else:
            contory = contory + 1
        raspuns = input('Mai joci inca o data? [y/n]  ')
        if raspuns.lower() == 'y':
            gata = False
        else:
            print("Papa")
            gata = True
    s = 'Ai castigat de '
    s1 = ' ori, iar el de '
    s2 = ' ori!'
    print(s + str(contorx) + s1 + str(contory) + s2)

