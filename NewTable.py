from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QToolBar, QVBoxLayout, QAction,\
    QFileDialog

import datetime
import xlwt
import xlrd
import Materials
# n,v:面后面的折射率和阿贝,r是半径,d是跟前一个面的距离


class NewTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('New Table')

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['n', 'v', 'r', 'd', 'w'])
        self.tableWidget.setVerticalHeaderLabels(['OBJ', 'STO', 'IMA'])

        read_file = QAction('File', self)
        read_file.triggered.connect(self.read_file)
        submit = QAction('Submit', self)
        submit.triggered.connect(self.submit)
        save_file = QAction('Save', self)
        save_file.triggered.connect(self.save_file)
        add_line = QAction('Add Line', self)
        add_line.triggered.connect(self.add_line)

        tool = QToolBar(self)
        tool.addAction(read_file)
        tool.addAction(submit)
        tool.addAction(save_file)
        tool.addAction(add_line)

        self.layout = QVBoxLayout()
        self.layout.addWidget(tool)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    def read_file(self):
        # BUG!! click cancel will close all windows
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "File Input", "",
                                                   "All Files (*);;Excel Files (*.xls)",
                                                   options=options)

        data = xlrd.open_workbook(file_name)
        table = data.sheets()[0]
        count = table.nrows

        if count < 4:
            self.tableWidget.setRowCount(3)
        else:
            self.tableWidget.setRowCount(count-1)

        vertical_header = []
        for row in range(0, count-1):
            new_len = table.row_values(row+1)
            vertical_header.append(str(new_len[0]))
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(new_len[1])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(new_len[2])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(new_len[3])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(new_len[4])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(new_len[5])))

        self.tableWidget.setVerticalHeaderLabels(vertical_header)

    def submit(self):
        rows = self.tableWidget.rowCount()
        Materials.lens = []
        Materials.stops = []
        Materials.obj = {}
        my_table = []
        print('1')
        for row in range(0, rows):
            my_row = []
            for col in range(0, 4):
                if self.tableWidget.item(row, col) is not None:
                    my_row.append(float(self.tableWidget.item(row, col).text()))
                else:
                    if col == 0:
                        my_row.append(1)
                    elif col == 2:
                        my_row.append(FAR_L)
                    else:
                        my_row.append(0)

            my_table.append(my_row)

        for row in range(0, rows):

            if self.tableWidget.verticalHeaderItem(row) is not None:
                my_type = self.tableWidget.verticalHeaderItem(row).text()
            if my_type == 'OBJ':
                Materials.obj['n'] = my_table[row][0]
                Materials.obj['v'] = my_table[row][1]
                Materials.obj['r'] = my_table[row][2]
                Materials.obj['d'] = my_table[row][3]
                if self.tableWidget.item(row, 4) is not None:
                     Materials.obj['w'] = float(self.tableWidget.item(row, 4).text())
            elif my_type == 'STO':
                new_stop = Materials.Stop(my_table[row][2], my_table[row][3])
                Materials.stops.append(new_stop)
            elif my_type == 'IMA':
                print('ima')
            else:
                Materials.add_len(my_table[row])
        Materials.show()

    def save_file(self):
        data = xlwt.Workbook()
        sheet = data.add_sheet('sheet1')

        rows = self.tableWidget.rowCount()

        headers = ['', 'n', 'v', 'r', 'd', 'w']
        col_count = 0
        for header in headers:
            sheet.write(0, col_count, header)
            col_count += 1

        for row in range(0, rows):
            if self.tableWidget.verticalHeaderItem(row) is not None:
                sheet.write(row + 1, 0, self.tableWidget.verticalHeaderItem(row).text())
            for col in range(0, 4):
                if self.tableWidget.item(row, col) is not None:
                    sheet.write(row + 1, col + 1, self.tableWidget.item(row, col).text())

        data.save(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'.xls')

    def add_line(self):
        rows = self.tableWidget.rowCount()
        header = QTableWidgetItem(rows+1)
        self.tableWidget.setVerticalHeaderItem(rows, header)
        self.tableWidget.setRowCount(rows + 1)


