from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog

class SourceWidget(QWidget):

    def __init__(self):
        super(SourceWidget, self).__init__()

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        lblSource = QLabel("Source folder:")
        mainLayout.addWidget(lblSource)
        lblSource.setMinimumWidth(80)

        self.txtSource = QTextEdit()
        mainLayout.addWidget(self.txtSource)
        self.txtSource.setMaximumHeight(27)

        btnBrowse = QPushButton("Browse")
        mainLayout.addWidget(btnBrowse)
        btnBrowse.clicked.connect(self.browseSource)

        self.txtSource.textChanged.connect(self.autoChangeSize)

    def browseSource(self):

        filePath = QFileDialog.getExistingDirectory()
        self.txtSource.setText(filePath)

    def autoChangeSize(self):

        textHeight = self.txtSource.document().size().height()
        textLength = len(self.txtSource.toPlainText())

        if self.txtSource.height() < textHeight:
            self.setMinimumWidth(self.width() + textLength)


if __name__ == '__main__':

    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SourceWidget()
    window.show()
    app.exec_()