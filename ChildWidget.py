from PyQt5 import QtGui, QtCore, QtWidgets
import Materials


class Graph(QtWidgets.QWidget):
    def __init__(self):
        super(Graph, self).__init__()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.graph(qp)
        qp.end()

    def graph(self, qp):

        qp.setPen(QtGui.QColor(1, 10, 255))

        qp.drawText(50, 50, 'graph')


class Text(QtWidgets.QWidget):
    def __init__(self):
        super(Text, self).__init__()

        self.result = QtWidgets.QLabel('', self)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.result)
        self.setLayout(vbox)

    def result_text(self):

        msg = ''

        # for k in Materials.aber:
        #     msg = msg + str(k) + ':'
        #     if type(Materials.aber[k]) == dict:
        #         for i in Materials.aber[k]:
        #             msg = msg + str(i) + ':' + str(Materials.aber[k][i]) + ';'
        #     else:
        #         msg = msg + str(Materials.aber[k])
        #

        if Materials.aber:
            msg = msg + 'Aberration:' + str(Materials.aber)

        if Materials.basic:
            msg = msg + '\n' + 'Basic parameters:' + str(Materials.basic)

        self.result.setText(msg)
        self.result.adjustSize()
        self.result.setFont(QtGui.QFont('Calibri', 10))
        self.result.setWordWrap(True)
        self.result.setAlignment(QtCore.Qt.AlignBottom)