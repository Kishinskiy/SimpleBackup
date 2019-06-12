# -*- coding: utf-8 -*-
import json
import os
import subprocess
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QFileDialog, QAbstractItemView, QMainWindow, QDialog

from ui.uiMainWindow import Ui_MainWindow
from ui.uiFileTypeDialog import Ui_Dialog


class WorkerThread(QThread):
    #back_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__()
        self.presenter = parent
        self.selected_items = None

    def start_schedule(self):
        for item in self.selected_items:
            process = subprocess.Popen(['python', 'backup.py', '-p', './data/' + item.text() + '.json'], shell=True,
                                       stdout=subprocess.PIPE)
            try:
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        # print output.strip()
                        self.back_signal.emit(output)
            except Exception as e:
                print(e)
            return 'Success!!!'

    def set_argument(self, sel_i):
        self.selected_items = sel_i

    def run(self):
        print("thread started!")
        print(self.start_schedule())


class AddFileMaskDialog(QDialog, Ui_FileTypeDialog):
    def __init__(self):
        super(AddFileMaskDialog, self).__init__()
        self.setupUi(self)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Simple BackUP")
        self.setWindowIcon(QtGui.QIcon('ui/icon.png'))
        data_path = "./data/"
        if not os.path.exists(data_path):
            os.makedirs(data_path)


class Presenter:
    def __init__(self):
        self.w = Window()
        self.FileMaskDialogWindow = AddFileMaskDialog()
        self.workerThread = WorkerThread(parent=self)
        self.workerThread.finished.connect(self.thread_finished)
        self.workerThread.back_signal.connect(self.back_from_thread)
        self.threads = []

    def starting_thread(self):
        item = self.selected_item()
        self.threads.append(item.text())

    def start_backup_thread(self):
        self.workerThread.set_argument(self.w.projetcList.selectedItems())
        self.workerThread.start()

    def thread_finished(self):
        self.workerThread.exit()

        print('Thread finished!')
        # self.w.close()

    @staticmethod
    def back_from_thread(text):
        print(text)

    # Controllers
    # main window
    def window_processor(self):
        self.w.projetcList.addItem(self.get_project_list())
        self.w.addButton.clicked.connect(self.add_new_items)
        self.w.removeButton.clicked.connect(self.remove_items)
        self.w.projetcList.clicked.connect(self.show_options)
        self.w.setFilesMaskButton.clicked.connect(self.file_mask_dialog_processor)
        self.w.buttonBox.accepted.connect(self.send_data_to_file)
        self.w.buttonBox.rejected.connect(self.thread_finished)
        self.w.backupButton.clicked.connect(self.start_backup_thread)
        self.w.add_src_path_button.clicked.connect(self.set_src_path)
        self.w.add_dest_path_button.clicked.connect(self.set_dst_path)
        self.w.projetcList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.w.show()

    # file Type  Dialog
    def file_mask_dialog_processor(self):
        self.FileMaskDialogWindow.buttonBox.accepted.connect(self.add_filemask)
        self.FileMaskDialogWindow.FileMaskList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.FileMaskDialogWindow.buttonBox.rejected.connect(self.FileMaskDialogWindow.close)
        self.FileMaskDialogWindow.exec_()

    # Logics

    @staticmethod
    def path(selected_item):
        path = './data/' + selected_item + '.json'
        return path

    def selected_item(self):
        for item in self.w.projetcList.selectedItems():
            return item

    @staticmethod
    def open_folder_dialog():
        folder_name_path = QFileDialog().getExistingDirectory(None, 'Output directory', QtCore.QDir.homePath(),
                                                              QFileDialog.ShowDirsOnly)
        if folder_name_path:
            return folder_name_path

    def set_src_path(self):
        self.w.SrcPath.setText(self.open_folder_dialog())

    def set_dst_path(self):
        self.w.DestPath.setText(self.open_folder_dialog())

    def add_filemask(self):
        list_items = []
        selected_item = self.FileMaskDialogWindow.FileMaskList.selectedItems()
        for item in selected_item:
            list_items.append(item.text())
        string_items = ' '.join(list_items)
        self.w.FileMaskLine.setText(string_items)
        self.FileMaskDialogWindow.close()

    def add_new_items(self):
        self.w.projetcList.addItem("NewProject")

    def remove_items(self):
        item = self.selected_item()
        print("Item for delete: " + item.text())
        removed_item = self.w.projetcList.takeItem(self.w.projetcList.row(item))
        try:
            os.remove('./data/' + removed_item.text() + '.json')
        except IOError as e:
            print("Project Removing Error: " + e.message)
        else:
            print("Project " + removed_item.text() + " successfully removed")

    def send_data_to_file(self):
        data_dict = {'ProjectName': self.w.ProjectNameLine.text(),
                     'src': self.w.SrcPath.text(),
                     'dest': self.w.DestPath.text(),
                     'filemask': self.w.FileMaskLine.text(),
                     'TimePereod': self.w.TimePereodSpinBox.value(),
                     'TimeToLive': self.w.TimeToLiveSpinBox.value(),
                     'DirectoryMask': self.w.DirectoryMask.text()}
        item = self.selected_item()
        item.setText(data_dict['ProjectName'])

        try:
            with open(self.path(item.text()), 'w') as fp:
                json.dump(data_dict, fp)
        except Exception as e:
            print(e)
        return data_dict

    def get_project_list(self):
        for path, _, files in os.walk('./data'):
            for projects in files:
                string = projects.split('.')
                projects = string[0]
                self.w.projetcList.addItem(projects)

    def clear_form(self):
        # clear
        self.w.ProjectNameLine.clear()
        self.w.SrcPath.clear()
        self.w.DestPath.clear()
        self.w.FileMaskLine.clear()
        self.w.TimePereodSpinBox.clear()
        self.w.TimeToLiveSpinBox.clear()
        self.w.DirectoryMask.clear()

    @staticmethod
    def read_options(project):
        try:
            with open(project, 'r') as fp:
                data = json.load(fp)
        except IOError as e:
            print("Read options Error:", e)
        return data

    def show_options(self):
        self.clear_form()
        selected_item = self.selected_item()
        data = self.read_options(self.path(selected_item.text()))
        self.w.ProjectNameLine.setText(data['ProjectName'])
        self.w.SrcPath.setText(data['src'])
        self.w.DestPath.setText(data['dest'])
        self.w.FileMaskLine.setText(data['filemask'])
        self.w.TimePereodSpinBox.setValue(data['TimePereod'])
        self.w.TimeToLiveSpinBox.setValue(data['TimeToLive'])
        self.w.DirectoryMask.setText(data['DirectoryMask'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pres = Presenter()
    pres.window_processor()
    sys.exit(app.exec_())
