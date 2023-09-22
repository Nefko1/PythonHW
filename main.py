import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QLCDNumber, QMainWindow

class Calculator (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1024, 540, 600, 600)
        self.setWindowTitle('Kaplanlator')
        self.first = QLineEdit()
        self.second = QLineEdit()
        self.grid = QGridLayout()
        self.container = QWidget()
        self.container.setStyleSheet("background-image:url('1.jpg');")
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)
        self.setLayout(self.grid)
        self.buttonPlus = QPushButton('+', self)
        self.buttonPlus.clicked.connect(self.plusCliced)
        self.buttonMinus = QPushButton ('-',self)
        self.buttonMinus.clicked.connect(self.minusCliced)
        self.buttonMultiplication = QPushButton ('x',self)
        self.buttonMultiplication.clicked.connect(self.MultiplicationCliced)
        self.buttonDevide = QPushButton (':',self)
        self.buttonDevide.clicked.connect(self.DevideCliced)
        self.buttonDiv = QPushButton ('Div',self)
        self.buttonDiv.clicked.connect(self.DivCliced)
        self.buttonMod = QPushButton ('Mod',self)
        self.buttonMod.clicked.connect(self.ModCliced)
        self.buttonDegree = QPushButton ('X^x',self)
        self.buttonDegree.clicked.connect(self.DegreeCliced)
        self.result = QLCDNumber(8)
        self.result.display(0)
        self.result.setMaximumSize(100,50)

        self.grid.addWidget(self.result, 1,4)
        self.grid.addWidget(self.first, 2,1)
        self.grid.addWidget(self.second, 2, 7)
        self.grid.addWidget(self.buttonPlus, 3, 1)
        self.grid.addWidget(self.buttonMinus,3 ,2)
        self.grid.addWidget(self.buttonMultiplication,3 ,3)
        self.grid.addWidget(self.buttonDevide,3 ,4)
        self.grid.addWidget(self.buttonDiv,3,5)
        self.grid.addWidget(self.buttonMod, 3, 6)
        self.grid.addWidget(self.buttonDegree, 3, 7)


    def plusCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText + secondText)
    def minusCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText - secondText)

    def MultiplicationCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText * secondText)

    def DevideCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText / secondText)

    def DivCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText % secondText)

    def ModCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText // secondText)

    def DegreeCliced(self):
        firstText = int(self.first.text())
        secondText = int(self.second.text())
        self.result.display(firstText ** secondText)

    def MemorySave(self):
        firstText = int(self.first.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

