from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog

app = QApplication([])

# Simple rating dialog
rating, ok = QInputDialog.getInt(None, "Rate Us", "Please rate from 1 to 5:", 1, 1, 5)

if ok:
    QMessageBox.information(None, "Thank You", f"Your rating: {rating}")

app.exec_()
