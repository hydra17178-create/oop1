import sys
from PyQt6.QtWidgets import QApplication
from calendar_app import CalendarApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec())