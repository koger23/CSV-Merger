from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog


class TargetWidget(QWidget):

    def __init__(self):
        super(TargetWidget, self).__init__()

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        lblTarget = QLabel("Target filepath:")
        mainLayout.addWidget(lblTarget)
        lblTarget.setMinimumWidth(80)

        self.txtTarget = QTextEdit()
        mainLayout.addWidget(self.txtTarget)
        self.txtTarget.setMaximumHeight(27)

        btnBrowse = QPushButton("Browse")
        mainLayout.addWidget(btnBrowse)
        btnBrowse.clicked.connect(self.browseTarget)

    def browseTarget(self):

        filePath = QFileDialog.getSaveFileName(filter=("Comma separated text files (*.csv)"))

        self.txtTarget.setText(filePath[0])


if __name__ == '__main__':

    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = TargetWidget()
    window.show()
    app.exec_()