__author__ = "Joseph Braden Julian"
__version__ = "1.0"

"""
JavaC is an small application that allows the user to select
Java (.java) file(s) and convert them into Class (.class) file(s).
"""

import sys

from PyQt5 import QtWidgets

from src import main

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main.MainWindow()
    window.show()
    sys.exit(app.exec_())
