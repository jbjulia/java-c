#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    # initialize variables
    fileCount = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(401, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')

        """ lblTitle """

        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(100, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Condensed')
        font.setPointSize(28)
        font.setItalic(False)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName('lblTitle')

        """ lblDescription """

        self.lblDescription = QtWidgets.QLabel(self.centralwidget)
        self.lblDescription.setGeometry(QtCore.QRect(100, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Light')
        font.setPointSize(11)
        font.setItalic(True)
        self.lblDescription.setFont(font)
        self.lblDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDescription.setObjectName('lblDescription')

        """ listWidget """

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 220, 301, 192))
        self.listWidget.setObjectName('listWidget')

        """ btnSelect """

        self.btnSelect = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelect.setGeometry(QtCore.QRect(130, 150, 141, 51))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Condensed')
        font.setPointSize(16)
        self.btnSelect.setFont(font)
        self.btnSelect.setObjectName('btnSelect')
        self.btnSelect.clicked.connect(self.btnSelectFile_Click)

        """ btnConvert """

        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(210, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Condensed')
        font.setPointSize(16)
        self.btnConvert.setFont(font)
        self.btnConvert.setObjectName('btnConvert')
        self.btnConvert.clicked.connect(self.btnConvert_Click)

        """ btnCancel """

        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(50, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Condensed')
        font.setPointSize(16)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName('btnCancel')
        self.btnCancel.clicked.connect(self.btnCancel_Click)

        """ lblProgress """

        self.lblProgress = QtWidgets.QLabel(self.centralwidget)
        self.lblProgress.setGeometry(QtCore.QRect(50, 510, 301, 21))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Light')
        font.setPointSize(10)
        font.setItalic(False)
        self.lblProgress.setFont(font)
        self.lblProgress.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProgress.setObjectName('lblProgress')

        """ progressBar """

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 540, 301, 31))
        font = QtGui.QFont()
        font.setFamily('Ubuntu Condensed')
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setProperty('value', 0)
        self.progressBar.setObjectName('progressBar')

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnSelect, self.btnCancel)
        MainWindow.setTabOrder(self.btnCancel, self.btnConvert)

    """ retranslateUi """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'java c - v2'))
        self.lblTitle.setText(_translate('MainWindow', 'java c'))
        self.lblDescription.setText(_translate('MainWindow', 'automatic file conversion'))
        self.btnConvert.setText(_translate('MainWindow', 'convert [ ! ]'))
        self.btnSelect.setText(_translate('MainWindow', 'select a file [ + ]'))
        self.btnCancel.setText(_translate('MainWindow', 'cancel [ x ]'))
        self.lblProgress.setText(_translate('MainWindow', ''))

    """ btnSelectFile_Click """

    def btnSelectFile_Click(self):
        # self.lblProgress.setText('File selection in progress...')
        self.progressBar.setValue(0)

        # selectedFile = str(QFileDialog.getOpenFileName()).strip('(').split(',')

        selectedFile = QFileDialog.getOpenFileName()

        # print(selectedFile[0])

        if selectedFile[0].endswith('.java'):
            self.fileCount = self.fileCount + 1
            self.listWidget.addItem(selectedFile[0])
            if self.fileCount == 1:
                self.lblProgress.setText(str(self.fileCount) + ' file selected.')
            else:
                self.lblProgress.setText(str(self.fileCount) + ' files selected.')
        else:
            print('Error: Incorrect file type.')

        return None

    """ btnConvert_Click """

    def btnConvert_Click(self):
        progress = float(0)

        self.lblProgress.setText('Converting...')

        for i in range(self.listWidget.count()):
            command = 'javac ' + str(self.listWidget.item(i).text())

            # print(command)

            os.system(command)

        while progress < 100:
            progress += 0.0001
            self.progressBar.setValue(progress)

        if self.fileCount == 1:
            self.lblProgress.setText('Complete! ' + str(self.fileCount) + ' file converted.')
        else:
            self.lblProgress.setText('Complete! ' + str(self.fileCount) + ' files converted.')

        print('Conversion complete.')

        self.listWidget.clear()
        self.fileCount = 0

        return None

    """ btnCancel_Click """

    def btnCancel_Click(self):
        self.listWidget.clear()
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
