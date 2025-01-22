import sys
from PyQt5.QtWidgets import QApplication
from login import LoginPage


def create_app():
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show() 
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_app()