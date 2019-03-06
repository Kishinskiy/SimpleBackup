# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFileMask.ui'
#
# Created: Wed Feb 13 13:36:37 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FileTypeDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(248, 296)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.FileMaskList = QtGui.QListWidget(Dialog)
        self.FileMaskList.setGeometry(QtCore.QRect(20, 20, 101, 261))
        self.FileMaskList.setObjectName("FileMaskList")
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)
        QtGui.QListWidgetItem(self.FileMaskList)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.FileMaskList.isSortingEnabled()
        self.FileMaskList.setSortingEnabled(False)
        self.FileMaskList.item(0).setText(QtGui.QApplication.translate("Dialog", ".txt", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(1).setText(QtGui.QApplication.translate("Dialog", ".doc", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(2).setText(QtGui.QApplication.translate("Dialog", ".jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(3).setText(QtGui.QApplication.translate("Dialog", ".png", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(4).setText(QtGui.QApplication.translate("Dialog", ".wav", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(5).setText(QtGui.QApplication.translate("Dialog", ".mp3", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(6).setText(QtGui.QApplication.translate("Dialog", ".html", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(7).setText(QtGui.QApplication.translate("Dialog", ".js", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(8).setText(QtGui.QApplication.translate("Dialog", ".css", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.item(9).setText(QtGui.QApplication.translate("Dialog", ".bmp", None, QtGui.QApplication.UnicodeUTF8))
        self.FileMaskList.setSortingEnabled(__sortingEnabled)

