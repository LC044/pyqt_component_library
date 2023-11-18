# Pyqt实现微信气泡消息

特性：
1. 自适应大小、支持缩放
2. 支持图片显示
3. 支持更换头像

效果

![](./data/result.gif)

## 实现原理，重写QLabel，添加布局

聊天框由四部分组成，最左侧是图像，右边是聊天内容，中间绘制一个三角形指向头像，最右侧放置一个弹簧控件来调整消息的长度

![布局](./data/layout.png)

* 头像的实现

```python
class Avatar(QLabel):
    def __init__(self, avatar, parent=None):
        super().__init__(parent)
        if isinstance(avatar, str):
            self.setPixmap(QPixmap(avatar).scaled(45, 45))
            self.image_path = avatar
        elif isinstance(avatar, QPixmap):
            self.setPixmap(avatar.scaled(45, 45))
        self.setFixedSize(QSize(45, 45))
```
* 绘制三角形

发送消息绘制右三角，接收消息绘制左三角

```python
class Triangle(QLabel):
    def __init__(self, Type, is_send=False, parent=None):
        super().__init__(parent)
        self.Type = Type
        self.is_send = is_send
        self.setFixedSize(6, 45)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(Triangle, self).paintEvent(a0)
        if self.Type == MessageType.Text:
            painter = QPainter(self)
            triangle = QPolygon()
            if self.is_send:
                painter.setPen(QColor('#b2e281'))
                painter.setBrush(QColor('#b2e281'))
                triangle.setPoints(0, 20, 0, 35, 6, 25)
            else:
                painter.setPen(QColor('white'))
                painter.setBrush(QColor('white'))
                triangle.setPoints(0, 25, 6, 20, 6, 35)
            painter.drawPolygon(triangle)
```

* 文字消息控件

```python
class TextMessage(QLabel):
    heightSingal = pyqtSignal(int)

    def __init__(self, text, is_send=False, parent=None):
        super(TextMessage, self).__init__(text, parent)
        self.setFont(QFont('微软雅黑', 12))
        self.setWordWrap(True)
        self.setMaximumWidth(800)
        self.setMinimumWidth(100)
        self.setMinimumHeight(45)

        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        if is_send:
            self.setAlignment(Qt.AlignCenter | Qt.AlignRight)
            self.setStyleSheet(
                '''
                background-color:#b2e281;
                border-radius:10px;
                border-top: 10px solid #b2e281;
                border-bottom: 10px solid #b2e281;
                border-right: 10px solid #b2e281;
                border-left: 10px solid #b2e281;
                '''
            )
        else:
            self.setStyleSheet(
                '''
                background-color:white;
                border-radius:10px;
                border-top: 10px solid white;
                border-bottom: 10px solid white;
                border-right: 10px solid white;
                border-left: 10px solid white;
                '''
            )
        w = len(text) * 16 + 30
        if w < self.width():
            self.setMaximumWidth(w)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(TextMessage, self).paintEvent(a0)
```

核心是边框样式的设置，self.setWordWrap(True)设置文字自动换行，self.setTextInteractionFlags(Qt.TextSelectableByMouse)设置文字可选中，self.setAlignment(Qt.AlignCenter | Qt.AlignRight)设置文字对齐方式

```css
{
    background-color:#b2e281; // 边框颜色
    border-radius:10px;  // 边框圆角半径
    border-top: 10px solid #b2e281; // 各边框宽度颜色
    border-bottom: 10px solid #b2e281;
    border-right: 10px solid #b2e281;
    border-left: 10px solid #b2e281;
}
```

* 最后再设置一个布局，将三个元素添加进来

```python
class BubbleMessage(QWidget):
    def __init__(self, str_content, avatar, Type, is_send=False, parent=None):
        super().__init__(parent)
        self.isSend = is_send
        # self.set
        self.setStyleSheet(
            '''
            border:none;
            '''
        )
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 5, 5, 5)
        # self.resize(QSize(200, 50))
        self.avatar = Avatar(avatar)
        triangle = Triangle(Type, is_send)
        if Type == MessageType.Text:
            self.message = TextMessage(str_content, is_send)
            # self.message.setMaximumWidth(int(self.width() * 0.6))
        elif Type == MessageType.Image:
            self.message = ImageMessage(str_content)
        else:
            raise ValueError("未知的消息类型")

        self.spacerItem = QSpacerItem(45 + 6, 45, QSizePolicy.Expanding, QSizePolicy.Minimum)
        if is_send:
            layout.addItem(self.spacerItem)
            layout.addWidget(self.message, 1)
            layout.addWidget(triangle, 0, Qt.AlignTop | Qt.AlignLeft)
            layout.addWidget(self.avatar, 0, Qt.AlignTop | Qt.AlignLeft)
        else:
            layout.addWidget(self.avatar, 0, Qt.AlignTop | Qt.AlignRight)
            layout.addWidget(triangle, 0, Qt.AlignTop | Qt.AlignRight)
            layout.addWidget(self.message, 1)
            layout.addItem(self.spacerItem)
        self.setLayout(layout)
```

## 最终效果

![](./data/demo.png)

