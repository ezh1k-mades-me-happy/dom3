import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PyQt5.uic import loadUi
import sqlite3


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Coffee Information")
        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("coffee.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_num, col_num, item)


class AddEditCoffeeForm(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("addEditCoffeeForm.ui", self)
        self.saveButton.clicked.connect(self.save_data)
        self.cancelButton.clicked.connect(self.close)

    def save_data(self):
        id_ = self.idLineEdit.text()
        name = self.nameLineEdit.text()
        type_ = self.typeLineEdit.text()
        price = self.priceLineEdit.text()

        connection = sqlite3.connect("coffee.db")
        cursor = connection.cursor()

        if id_:  # Edit existing record
            cursor.execute("UPDATE coffee SET Name=?, Type=?, Price=? WHERE ID=?", (name, type_, price, id_))
        else:  # Add new record
            cursor.execute("INSERT INTO coffee (Name, Type, Price) VALUES (?, ?, ?)", (name, type_, price))

        connection.commit()
        connection.close()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CoffeeApp()
    main_window.show()

    add_edit_form = AddEditCoffeeForm()

    sys.exit(app.exec_())
