from PySide2.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QPushButton, QComboBox, QLabel


class StartWidget(QWidget):

    def __init__(self):
        super(StartWidget, self).__init__()

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.chkbxHeader = QCheckBox("Keep header")
        mainLayout.addWidget(self.chkbxHeader)

        lblEncoding = QLabel("Encoding:")
        mainLayout.addWidget(lblEncoding)

        self.encodeList = QComboBox()
        mainLayout.addWidget(self.encodeList)
        self.encodeList.addItem("iso-8859-1")
        self.encodeList.addItem("iso-8859-2")
        self.encodeList.addItem("iso-8859-3")
        self.encodeList.addItem("utf-8")

        self.btnStart = QPushButton("START")
        mainLayout.addWidget(self.btnStart)
        self.btnStart.setMinimumWidth(230)



if __name__ == '__main__':

    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = StartWidget()
    window.show()
    app.exec_()