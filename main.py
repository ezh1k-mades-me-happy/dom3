import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sqlite3


class CoffeeApp(QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle("Coffee Information")

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()
        connection.close()

        for row in data:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for col, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, col, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
