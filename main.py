import sys
from random import randint
from scnd import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.share = 0
        self.do_paint = False

    def PaintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        x = randint(10, 400)
        y = randint(10, 400)
        r = randint(1, 254)
        g = randint(1, 254)
        b = randint(1, 254)

        colors = (r, g, b)
        qp.setBrush(QColor(*colors))
        if self.share == 1:
            w = randint(10, 100)
            qp.drawEllipse(x - w // 2, y - w // 2, w, w)
            qp.end()

    def run(self):
        self.share = 1
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())