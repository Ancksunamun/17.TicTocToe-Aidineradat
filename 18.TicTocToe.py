from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import  partial
import random

class TicTocToe(QMainWindow):
    def __init__(self):
        super().__init__()

        loader=QUiLoader()
        self.ui=loader.load('form.ui',None)
        self.ui.show()

        self.game = [[self.ui.btn_1 , self.ui.btn_2 , self.ui.btn_3],
                     [self.ui.btn_4 , self.ui.btn_5 , self.ui.btn_6],
                     [self.ui.btn_7 , self.ui.btn_8 , self.ui.btn_9]]
        self.ui.ngame.clicked.connect(self.newgame)
        self.ui.about.clicked.connect(self.about)
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color:black; background-color:orange')
                self.game[i][j].clicked.connect(partial(self.play,i,j))

        self.counter=0
        self.ply1wins = 0
        self.ply2wins = 0
        self.drawss = 0
    def play(self, i, j):
        if self.ui.multi.isChecked():

            if self.game[i][j].text()=="":
                if self.counter % 2 == 0:
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color:white; background-color:green')

                if self.counter % 2== 1:
                    self.game[i][j].setText('O')
                    self.game[i][j].setStyleSheet('color:black; background-color:yellow')
                self.counter += 1
            self.checkplwin()
            self.draw()
        elif self.ui.solo.isChecked():
            if self.game[i][j].text()=="":
                if self.counter % 2 == 0:
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color:white; background-color:green')
                    self.counter += 1
                while True:
                    if self.counter % 2 == 1 :
                        row = random.randint( 0 , 2 )
                        col = random.randint( 0 , 2 )
                        if self.game[row][col].text() == "" :
                            self.game[row][col].setText('O')
                            self.game[row][col].setStyleSheet('color:black; background-color:yellow')
                            self.counter += 1
                            break
            self.checkplwin()
            self.draw()

    def ply1win(self):
        self.ply1wins += 1
        msgBox = QMessageBox()
        msgBox.setText("Player one (X) wins")
        msgBox.exec()
        self.ui.ply1.setText('Player one:   ' + str(self.ply1wins))
        self.restart()

    def ply2win(self):
        self.ply2wins += 1
        if  self.ui.multi.isChecked():
            msgBox = QMessageBox()
            msgBox.setText("Player two (O) wins")
            msgBox.exec()
            self.ui.ply2.setText('Player two:   ' + str(self.ply2wins))
            self.restart()
        else:
            msgBox = QMessageBox()
            msgBox.setText("computer wins")
            msgBox.exec()
            self.ui.ply2.setText('Computer:   ' + str(self.ply2wins))
            self.restart()

    def draw(self):
        if self.counter == 9:
            self.drawss =+ 1
            msgBox = QMessageBox()
            msgBox.setText("Draw!!")
            msgBox.exec()
            self.ui.draws.setText('Draws:   ' + str(self.drawss))
            self.restart()

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color:black; background-color:orange')

        self.counter = 0
    def about(self):
        msgBox = QMessageBox()
        msgBox.setText("It is just designed by me!!")
        msgBox.exec()


    def newgame (self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color:black; background-color:orange')
        self.counter = 0
        self.ply1wins = 0
        self.ply2wins = 0
        self.drawss = 0
        self.ui.draws.setText('Draws:   ' + str(self.drawss))
        self.ui.ply1.setText('Player one:   ' + str(self.ply1wins))
        if self.ui.multi.isChecked():
            self.ui.ply2.setText('Player two:   ' + str(self.ply2wins))
        else:
            self.ui.ply2.setText('Computer:   ' + str(self.ply2wins))





    def checkplwin(self):
        l = 0
        p = 0
        for i in range(3):
            m = 0
            n = 0
            for j in range(3):
                if self.game[i][j].text() == "X":
                    m += 1
                    if m == 3:
                        self.ply1win()
                if self.game[i][j].text() == "O":
                    n += 1
                    if n == 3:
                        self.ply2win()

        for j in range(3):
            m = 0
            n = 0
            for i in range(3):
                if self.game[i][j].text()  == "X":
                    m += 1
                    if m == 3:
                        self.ply1win()
                if self.game[i][j].text() == "O":
                    n += 1
                    if n == 3:
                        self.ply2win()
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text()  == "X" and i == j:
                    l += 1
                    if l == 3:
                        self.ply1win()
                if self.game[i][j].text()  == "O" and i == j:
                    p += 1
                    if p == 3:
                        self.ply2win()
        if self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X':
            self.ply1win()
        if self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O':
            self.ply2win()




app = QApplication([])
windows = TicTocToe()
app.exec()