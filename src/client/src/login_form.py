import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from ui.login_form_ui import Ui_MainWindow as Ui_LogginForm

class LogginForm(QMainWindow, Ui_LogginForm):

    login_correct = pyqtSignal(int, int)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_enter.clicked.connect(self.check_login)
        self.push_cancel.clicked.connect(self.exit)


    def check_login(self): #TODO реализовать проверку логина в базе
        user_id = 1
        user_post = 1
        if not user_id:
            print("Пользователя в базе нет")
            return
        self.login_correct.emit(user_id, user_post)
        self.close()

    def exit(self):
        self.close()