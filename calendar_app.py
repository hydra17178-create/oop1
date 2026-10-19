
import os
from abc import ABC, abstractmethod, ABCMeta
from datetime import datetime

from PyQt6.QtWidgets import QMainWindow, QWidget, QListWidgetItem, QMessageBox

# Импортируем наши собственные модули
from models import CalendarEvent
from ui_widgets import (MyLabel, MyLineEdit, MyTextEdit, MyPushButton, MyListWidget,
                        MyVBoxLayout, MyHBoxLayout, MyGroupBox, MySplitter, MyStatusBar)


class AbstractAppView(ABC):
    @abstractmethod
    def build_ui(self):
        pass



class PyQtABCMeta(ABCMeta, type(QMainWindow)):
    pass


class CalendarApp(QMainWindow, AbstractAppView, metaclass=PyQtABCMeta):
    def __init__(self):
        super().__init__()
        self.login = "UserName"
        self.time_in = datetime.now()

        self.events = []
        self.selected_index = -1
        self.load_data()
        self.events.sort()

        self.build_ui()

    def build_ui(self):
        self.setWindowTitle("Календарь - ООП")
        self.resize(850, 500)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = MyHBoxLayout(main_widget)

        left_group = MyGroupBox("Список событий")
        left_layout = MyVBoxLayout()
        self.list_ui = MyListWidget()
        self.list_ui.currentRowChanged.connect(self.on_event_click)
        left_layout.addWidget(self.list_ui)
        left_group.setLayout(left_layout)

        right_group = MyGroupBox("Детали")
        right_layout = MyVBoxLayout()

        right_layout.addWidget(MyLabel("Название:"))
        self.input_title = MyLineEdit()
        right_layout.addWidget(self.input_title)

        right_layout.addWidget(MyLabel("Дата (ДД.ММ.ГГГГ):"))
        self.input_date = MyLineEdit()
        right_layout.addWidget(self.input_date)

        right_layout.addWidget(MyLabel("Описание:"))
        self.input_desc = MyTextEdit()
        right_layout.addWidget(self.input_desc)

        self.btn_save = MyPushButton("Сохранить изменения")
        self.btn_save.clicked.connect(self.save_changes)
        right_layout.addWidget(self.btn_save)

        right_group.setLayout(right_layout)

        splitter = MySplitter()
        splitter.addWidget(left_group)
        splitter.addWidget(right_group)
        splitter.setSizes([300, 500])

        main_layout.addWidget(splitter)

        self.status = MyStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Программа запущена")

        self.refresh_list_ui()

    def refresh_list_ui(self):
        self.list_ui.clear()
        for ev in self.events:
            item = QListWidgetItem(str(ev))
            item.setToolTip(ev.description)
            self.list_ui.addItem(item)

    def on_event_click(self, index):
        if index < 0 or index >= len(self.events):
            return
        self.selected_index = index
        ev = self.events[index]

        self.input_title.setText(ev.title)
        self.input_date.setText(ev.date)
        self.input_desc.setText(ev.description)

    def save_changes(self):
        if self.selected_index == -1:
            QMessageBox.warning(self, "Внимание", "Сначала выберите событие в списке!")
            return

        ev = self.events[self.selected_index]
        ev.title = self.input_title.text()
        ev.date = self.input_date.text()
        ev.description = self.input_desc.toPlainText()

        self.save_data()
        self.refresh_list_ui()
        self.list_ui.setCurrentRow(self.selected_index)
        self.status.showMessage("Сохранено!", 3000)

    def save_data(self):
        try:
            f = open("events_data.txt", "w", encoding="utf-8")
            for ev in self.events:
                f.write(f"{ev.event_id}|||{ev.title}|||{ev.date}|||{ev.description}\n")
            f.close()
        except Exception as e:
            print("Не удалось сохранить:", e)

    def load_data(self):
        if not os.path.exists("events_data.txt"):
            self.events.append(CalendarEvent(1, "Анапа", "29.10.2026", "поехать в анапу за справкой"))
            self.events.append(CalendarEvent(2, "Зачет", "19.10.2026", "ООП"))
            self.events.append(CalendarEvent(3, "Барбер", "20.10.2026", "15:40"))
            self.events.append(CalendarEvent(4, "Тренировка", "21.10.2026", "Спортзал"))
            self.events.append(CalendarEvent(5, "День рождения", "05.02.2027", "Купить торт"))
            self.events.append(CalendarEvent(6, "Машина", "20.11.2026", "забрать машину с сто"))
            self.events.append(CalendarEvent(7, "Оплата связи", "09.11.2026", "МТС"))
            self.events.append(CalendarEvent(8, "Павел", "25.11.2026", "туса в Новоросе"))
            self.events.append(CalendarEvent(9, "День рождения", "05.12.2026", "папа"))
            self.events.append(CalendarEvent(10, "Новый год", "31.12.2026", "Подготовка"))
            return

        try:
            f = open("events_data.txt", "r", encoding="utf-8")
            for line in f:
                parts = line.strip().split("|||")
                if len(parts) == 4:
                    ev = CalendarEvent(int(parts[0]), parts[1], parts[2], parts[3])
                    self.events.append(ev)
            f.close()
        except Exception:
            pass

    @staticmethod
    def make_report(login, t_in, t_out):
        fmt = "%d.%m.%Y %H:%M:%S"
        try:
            f = open("report.txt", "w", encoding="utf-8")
            f.write("| login | time_in | time_out |\n")
            f.write("|---|---|---|\n")
            f.write(f"| {login} | {t_in.strftime(fmt)} | {t_out.strftime(fmt)} |\n")
            f.close()
            print("Отчет сохранен")
        except Exception as e:
            print("Ошибка отчета:", e)

    def closeEvent(self, event):
        self.save_data()
        now_time = datetime.now()
        CalendarApp.make_report(self.login, self.time_in, now_time)
        super().closeEvent(event)