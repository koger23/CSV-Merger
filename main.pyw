#!/usr/bin/python3

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox
import threading, sys, os
from modules import sourceWidget, targetWidget, progBarWidget, startWidget
from utils import getCsvFileList as getCsv, unifyCsvFiles as uni


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("CSV File Unifyer")

        self.centralWidget = QWidget()
        mainLayout = QVBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        # Source widget
        self.wSource = sourceWidget.SourceWidget()
        mainLayout.addWidget(self.wSource)

        # Target widget
        self.wTarget = targetWidget.TargetWidget()
        mainLayout.addWidget(self.wTarget)

        # Start button with checkbox
        self.wStart = startWidget.StartWidget()
        mainLayout.addWidget(self.wStart)
        self.wStart.btnStart.clicked.connect(self.start)

        # Progressbar
        self.wProgBar = progBarWidget.ProgBar()
        mainLayout.addWidget(self.wProgBar)
        self.wProgBar.hide()

    def start(self):

        sourcePath = self.wSource.txtSource.toPlainText()
        targetFullPath = self.wTarget.txtTarget.toPlainText()
        targetFileName = targetFullPath.split("/")[-1:][0]
        targetPath = '/'.join(targetFullPath.split("/")[:-1])
        keepHeader = self.wStart.chkbxHeader.isChecked()
        encoding = self.wStart.encodeList.currentText()

        # Checking paths
        if not os.path.isdir(sourcePath):
            msgBox = QMessageBox()
            msgBox.setText("Source folder is invalid or not given.")
            msgBox.exec_()
            return

        elif not os.path.isdir(targetPath):
            msgBox = QMessageBox()
            msgBox.setText("Target folder is invalid or not given.")
            msgBox.exec_()
            return

        # Get csv list
        csvList = getCsv.getCsvFiles(sourcePath, "*.csv")

        self.wProgBar.show()

        # unify files
        unifying = uni.unifyCsvFiles(csvList, targetFileName, targetPath, keepHeader, encoding, self.wProgBar)

        # if error
        if unifying:
            msgBox = QMessageBox()
            msgBox.setText("Decoding error:\n\n" +
                           str(unifying) +
                           "\nProbably the selected encoding is not proper.")
            msgBox.exec_()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()