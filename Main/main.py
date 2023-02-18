import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from Main.Login import Login
if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Inizio")
    gui_main = Login()

    gui_main.show()
    sys.exit(app.exec())
