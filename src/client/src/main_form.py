from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from ui.main_form_ui import Ui_MainWindow as Ui_MainForm


class MainForm(QMainWindow, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_user_data(self, user_id: int, user_post: int):
        self.user_id = user_id
        self.user_post = user_post
        self.show()