# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/FileTypeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(248, 296)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.FileMaskList = QtWidgets.QListWidget(Dialog)
        self.FileMaskList.setGeometry(QtCore.QRect(20, 20, 101, 261))
        self.FileMaskList.setObjectName("FileMaskList")
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileMaskList.addItem(item)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.FileMaskList.isSortingEnabled()
        self.FileMaskList.setSortingEnabled(False)
        item = self.FileMaskList.item(0)
        item.setText(_translate("Dialog", ".txt"))
        item = self.FileMaskList.item(1)
        item.setText(_translate("Dialog", ".doc"))
        item = self.FileMaskList.item(2)
        item.setText(_translate("Dialog", ".jpg"))
        item = self.FileMaskList.item(3)
        item.setText(_translate("Dialog", ".png"))
        item = self.FileMaskList.item(4)
        item.setText(_translate("Dialog", ".wav"))
        item = self.FileMaskList.item(5)
        item.setText(_translate("Dialog", ".mp3"))
        item = self.FileMaskList.item(6)
        item.setText(_translate("Dialog", ".html"))
        item = self.FileMaskList.item(7)
        item.setText(_translate("Dialog", ".js"))
        item = self.FileMaskList.item(8)
        item.setText(_translate("Dialog", ".css"))
        item = self.FileMaskList.item(9)
        item.setText(_translate("Dialog", ".bmp"))
        self.FileMaskList.setSortingEnabled(__sortingEnabled)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
