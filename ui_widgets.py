from PyQt6.QtWidgets import (QLabel, QLineEdit, QTextEdit, QPushButton, QListWidget,
                             QVBoxLayout, QHBoxLayout, QGroupBox, QSplitter, QStatusBar)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MyLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Arial", 11))
        self.setStyleSheet("color: #212121;")


class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Arial", 11))
        self.setStyleSheet("border: 1px solid #1976D2; padding: 5px;")


class MyTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Arial", 11))
        self.setStyleSheet("border: 1px solid #1976D2; padding: 5px;")


class MyPushButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.setStyleSheet("background-color: #1976D2; color: white; padding: 8px; border-radius: 4px;")


class MyListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Arial", 11))


class MyVBoxLayout(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSpacing(10)


class MyHBoxLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSpacing(10)


class MyGroupBox(QGroupBox):
    def __init__(self, title="", parent=None):
        super().__init__(title, parent)
        self.setStyleSheet(
            "QGroupBox { font-weight: bold; border: 1px solid gray; border-radius: 5px; margin-top: 10px; }")


class MySplitter(QSplitter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOrientation(Qt.Orientation.Horizontal)


class MyStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #E0E0E0;")