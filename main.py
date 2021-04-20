from __initUI__ import *
import sys
from PyQt5.QtWidgets import QApplication

"""
This is the main.py script that runs the software. This script has two dependent .py
files, __initUI__.py and fn_cat.py

Austin Fraley
"""


def run_app():
    app = QApplication(sys.argv)

    window = App()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
