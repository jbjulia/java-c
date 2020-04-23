import subprocess
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

from resources import constants as c


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(c.JAVAC, self)

        self.file_count = 0

        self.btnSelect.clicked.connect(self.select_files)
        self.btnConvert.clicked.connect(self.convert_files)
        self.btnCancel.clicked.connect(self.quit_app)

        if c.ERRORS:
            self.lblProgress.setText(c.ERRORS)  # Display permission error if one exists

    def select_files(self):
        """
        Prompts user to select a valid Java file (.java) from QFileDialog
        and add item to listWidget. Multiple items may be selected.
        :return:
        """
        self.progressBar.setValue(0)

        selected_file = QFileDialog.getOpenFileName()  # Prompt user to select files(s)

        if selected_file[0].endswith(".java"):
            self.file_count = self.file_count + 1
            self.listWidget.addItem(selected_file[0])
            self.lblProgress.setText(
                str(self.file_count)
                + " file selected." if self.file_count == 1 else " files selected."
            )
        else:
            print("Error: Incorrect file type.")

    def convert_files(self):
        """
        Checks that listWidget is not empty. Coverts each item from
        listWidget and displays progressBar updates.
        :return:
        """
        if self.listWidget.count() < 1:
            return

        progress = float(0)

        try:
            for i in range(self.listWidget.count()):
                command = "javac '" + str(self.listWidget.item(i).text()) + "'"
                returned = subprocess.call(command, shell=True)

                while progress < 100:
                    progress += 0.0001
                    self.progressBar.setValue(progress)

                self.lblProgress.setText(
                    "Complete! "
                    + str(self.file_count)
                    + " file converted." if self.file_count == 1 else " files converted."
                )

                print("Conversion complete.")

                if returned != 0:
                    raise Exception
        except Exception as e:
            print("Error, cannot convert file(s).", str(e))
            self.lblProgress.setText("Error converting file(s). Please check your syntax.")
            return

        self.listWidget.clear()

    def quit_app(self):
        """
        Clears listWidget items and quit application.
        :return:
        """
        self.listWidget.clear()
        sys.exit()
