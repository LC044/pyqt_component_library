from PyQt5.QtCore import Qt, pyqtSignal, QRectF
from PyQt5.QtGui import QPainter, QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from navigationUi import Ui_Form


class NavigationWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        self.buttons = []
        self.history = []
        self.addButton(btn1)
        self.addButton(btn2)
        self.addButton(self.pushButton)
        self.addButton(self.pushButton_2)
        self.addButton(self.pushButton_3)

    def addButton(self, item: QPushButton):
        item.clicked.connect(self._show_view)
        self.buttons.append(item)

    def _show_view(self):
        clicked_btn: QPushButton = self.sender()
        if self.history:
            last_btn = self.history[-1]
            last_btn.setText("world")
        self.history.append(clicked_btn)
        clicked_btn.setText("hello")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    view = NavigationWidget()
    view.show()
    # view.loadMainWinView('102')
    sys.exit(app.exec_())
