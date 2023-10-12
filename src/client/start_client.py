import sys

from PyQt6 import QtWidgets

import settings

from src.login_form import LoginForm
from src.base_worker import BaseWorker

base_worker = BaseWorker(settings.SERVER_URL)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginForm(base_worker)
    login_window.show()
    app.exec()


