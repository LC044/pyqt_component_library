import random

from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication

from bubble_message import BubbleMessage, ChatWidget,MessageType,Notice



class Test(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.resize(500, 600)
        self.w1 = ChatWidget()
        send_avatar = './data/head1.svg'
        receive_avatar = './data/head1.jpg'
        TEXT = MessageType.Text
        IMAGE = MessageType.Image
        time_message = Notice('2023-11-18 17:43')
        self.w1.add_message_item(time_message)
        bubble_message = BubbleMessage('你好', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('你好啊💖', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        # bubble_message = BubbleMessage('./data/fg1.png', send_avatar, Type=IMAGE, is_send=True)
        # self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('咱们来对个诗吧！', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('落霞与孤鹜齐飞', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('秋水共成天一色', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('风急天高猿啸哀', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('渚清沙白鸟飞回', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('无边落木萧萧下', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('不尽长江滚滚来', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('万里悲秋常作客', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('百年多病独登台', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('艰难苦恨繁霜鬓', send_avatar, Type=TEXT, is_send=True)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('潦倒新停浊酒杯', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)

        bubble_message = BubbleMessage('这是一串很长的文字\n好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长', receive_avatar, Type=TEXT, is_send=False)
        self.w1.add_message_item(bubble_message)
        w2 = QLabel("nihao")
        layout.addWidget(self.w1)
        layout.addWidget(w2)
        self.setLayout(layout)

    def value(self, val):
        print('pos:', val)
        print('滚动条最大值', self.w1.verticalScrollBar().maximum())


if __name__ == '__main__':
    app = QApplication([])
    widget = Test()
    widget.w1.update()
    # widget = MyWidget()
    widget.w1.verticalScrollBar().setValue(200)
    print('滚动条最大值002', widget.w1.verticalScrollBar().maximum())
    widget.show()
    # QThread.sleep(2)
    widget.w1.verticalScrollBar().setValue(200)
    # widget.w1.verticalScrollBar().setValue(200)
    # widget.w1.verticalScrollBar().setValue(200)

    app.exec_()
