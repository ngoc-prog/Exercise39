import sys
from PyQt6.QtWidgets import QApplication
from MainWindowExt import MainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowExt()
    window.show()
    sys.exit(app.exec())
