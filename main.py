import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('UI.ui', self)

        self.button = self.findChild(QPushButton, 'button')
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 0))
        diameter = random.randint(10, 100)
        painter.drawEllipse(random.randint(0, self.width() - diameter), random.randint(0, self.height() - diameter),
                            diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
