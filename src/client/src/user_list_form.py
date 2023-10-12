from typing import List

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui.ui_user_list import Ui_MainWindow as Ui_UserList
from .base_worker import BaseWorker, Login, User

ADMIN_ID = 1

class UserList(QMainWindow, Ui_UserList):
    def __init__(self, base_worker: BaseWorker, login: Login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.base_worker = base_worker
        self.load_posts()
        self.load_users()
        self.btn_reset.clicked.connect(self.reset_user)
        self.btn_add.clicked.connect(self.add_new_user)
        self.btn_delete.clicked.connect(self.delete_user)
        self.show()

    def load_posts(self) -> None:
        posts = self.base_worker.get_posts_list()
        self.cb_post.addItem('-')
        for post in posts:
            self.cb_post.addItem(post.name, post.post_id)

    def load_users(self) -> None:
        row = 0
        self.tw_user_list.setRowCount(0)
        users = self.base_worker.get_users_list()
        for user in users:
            self.tw_user_list.insertRow(row)
            self.tw_user_list.setItem(row, 0, QTableWidgetItem(str(user.user_id)))
            self.tw_user_list.setItem(row, 1, QTableWidgetItem(user.reg_date.strftime('%d.%m.%Y %H:%M:%S')))
            self.tw_user_list.setItem(row, 2, QTableWidgetItem(user.login))
            self.tw_user_list.setItem(row, 3, QTableWidgetItem(user.post))
            self.tw_user_list.resizeColumnsToContents()
            self.tw_user_list.horizontalHeader().setStretchLastSection(True)
            row += 1

    def reset_user(self) -> None    :
        self.line_login.setText('')
        self.line_password.setText('')
        self.cb_post.setCurrentIndex(0)

    def add_new_user(self) -> None:
        if not self.check_user_fields():
            return

        user = User(login=self.line_login.text(), password=self.line_password.text(),
                    post_id=self.cb_post.currentData())
        res = self.base_worker.add_new_user(user)
        self.load_users()
        print(res)

    def check_user_fields(self) -> bool:
        if self.line_login.text() != '' and self.line_password.text() != '' and self.cb_post.currentIndex() != 0:
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return False

    def check_admin(self, user_id):
        if user_id == ADMIN_ID:
            QMessageBox.information(self, "Ошибка удаления", "Этого пользователя удалить нельзя")
            return True
        return False

    def delete_user(self):
        if not self.tw_user_list.selectionModel().hasSelection():
            return

        user_id = self.tw_user_list.item(self.tw_user_list.currentRow(), 0).text()
        if self.check_admin(user_id):
            return

        answer = QMessageBox.question(self, "Удаление пользователя", "Вы действительно хотите удалить выбранного "
                                                                     "пользователя?")
        if answer == QMessageBox.StandardButton.No:
            return
        resp = self.base_worker.delete_user(user_id)
        print(resp)
        self.load_users()
