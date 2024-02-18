import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.on_button_click)

        layout.addWidget(self.button)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def on_button_click(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        painter.setBrush(color)

        diameter = random.randint(10, 100)
        painter.drawEllipse(random.randint(0, self.width() - diameter), random.randint(0, self.height() - diameter),
                            diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
