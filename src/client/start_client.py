import sys

from PyQt6 import QtWidgets

from src.login_form import LogginForm
from src.main_form import MainForm


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LogginForm()
    main_form = MainForm()
    login_window.login_correct.connect(main_form.set_user_data)
    login_window.show()
    app.exec()


