import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class Page1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel('Hello, this is a test label!', self)
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Page1()
    sys.exit(app.exec_())