import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen

class Cvad(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('newl.ui', self)
        self.initUI()

    def initUI(self):
        self.label.setPixmap(QPixmap(501, 500))
        self.pushButton.clicked.connect(self.elip)

    def elip(self):
        x, y = [randint(10, 360) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]

        pain = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        pain.setPen(pen)
        pain.drawEllipse(x, y, w, h)
        pain.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cvad()
    ex.show()
    sys.exit(app.exec())
