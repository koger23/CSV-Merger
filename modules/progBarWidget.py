from PySide2.QtWidgets import QProgressBar, QMessageBox

class ProgBar(QProgressBar):

    def __init__(self, maxValue=None):
        super(ProgBar, self).__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.setMaximumHeight(10)

        if maxValue:
            self.setMaximum(maxValue)
        else:
            self.setMaximum(100)

    def increaseValue(self, val):

        self.setValue(val)

        if self.value() == self.maximum():

            msgBox = QMessageBox()
            msgBox.setText("Progress is finished.")
            msgBox.exec_()

            self.hide()


if __name__ == '__main__':

    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ProgBar(100)

    for i in range(0, 101):
        window.increaseValue(i)

    window.show()
    app.exec_()