from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QToolBar, QVBoxLayout, QAction,\
    QFileDialog, QTabWidget, QHeaderView

import xlwt
import xlrd
import Materials
from Prepare import FAR_L
# n,v:面后面的折射率和阿贝,r是半径,d是跟前一个面的距离


class InputTable(QWidget):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.lens = QWidget()
        self.k = QWidget()
        self.tabs.addTab(self.lens, 'Lens')
        self.tabs.addTab(self.k, 'Aberration sorts')

        self.lens.tableWidget = QTableWidget()
        self.lens.tableWidget.setRowCount(3)
        self.lens.tableWidget.setColumnCount(5)
        self.lens.tableWidget.setHorizontalHeaderLabels(['n', 'v', 'r', 'd', 'w'])
        self.lens.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lens.tableWidget.setVerticalHeaderLabels(['OBJ', 'STO', 'IMA'])

        self.k.tableWidget = QTableWidget()
        self.k.tableWidget.setRowCount(3)
        self.k.tableWidget.setColumnCount(3)
        self.k.tableWidget.setHorizontalHeaderLabels(['Aberration', 'K1', 'K2'])
        self.k.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        new_table = QAction('New Table', self)
        new_table.triggered.connect(self.new_table)
        read_file = QAction('File', self)
        read_file.triggered.connect(self.read_file)
        submit = QAction('Submit', self)
        submit.triggered.connect(self.submit)
        save_file = QAction('Save', self)
        save_file.triggered.connect(self.save_file)
        add_line = QAction('Add Line', self)
        add_line.triggered.connect(self.add_line)

        tool = QToolBar(self)
        tool.addAction(new_table)
        tool.addAction(read_file)
        tool.addAction(submit)
        tool.addAction(save_file)
        tool.addAction(add_line)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(tool)
        self.layout.addWidget(self.tabs)
        self.lens.layout = QVBoxLayout(self)
        self.lens.layout.addWidget(self.lens.tableWidget)
        self.lens.setLayout(self.lens.layout)
        self.k.layout = QVBoxLayout(self)
        self.k.layout.addWidget(self.k.tableWidget)
        self.k.setLayout(self.k.layout)
        self.setLayout(self.layout)

    def new_table(self):

        self.lens.tableWidget.clearContents()
        self.lens.tableWidget.setRowCount(3)
        self.lens.tableWidget.setVerticalHeaderLabels(['OBJ', 'STO', 'IMA'])

        self.k.tableWidget.clearContents()
        self.k.tableWidget.setRowCount(3)

    def read_file(self):
        # BUG!! click cancel will close all windows
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "File Input", "",
                                                   "All Files (*);;Excel Files (*.xls , *xlsx)",
                                                   options=options)

        data = xlrd.open_workbook(file_name)
        lens = data.sheets()[0]
        lens_count = lens.nrows

        self.lens.tableWidget.setRowCount(lens_count-1)
        vertical_header = []
        for row in range(0, lens_count-1):
            new_len = lens.row_values(row+1)
            vertical_header.append(str(new_len[0]))
            self.lens.tableWidget.setItem(row, 0, QTableWidgetItem(str(new_len[1])))
            self.lens.tableWidget.setItem(row, 1, QTableWidgetItem(str(new_len[2])))
            self.lens.tableWidget.setItem(row, 2, QTableWidgetItem(str(new_len[3])))
            self.lens.tableWidget.setItem(row, 3, QTableWidgetItem(str(new_len[4])))
            self.lens.tableWidget.setItem(row, 4, QTableWidgetItem(str(new_len[5])))

        self.lens.tableWidget.setVerticalHeaderLabels(vertical_header)

        if len(data.sheets()) > 1:
            k = data.sheets()[1]
            k_count = k.nrows
            if k_count > 1:
                self.k.tableWidget.setRowCount(k_count - 1)
                for row in range(0, k_count - 1):
                    new_aber = k.row_values(row + 1)
                    self.k.tableWidget.setItem(row, 0, QTableWidgetItem(str(new_aber[0])))
                    self.k.tableWidget.setItem(row, 1, QTableWidgetItem(str(new_aber[1])))
                    self.k.tableWidget.setItem(row, 2, QTableWidgetItem(str(new_aber[2])))

    def submit(self):
        Materials.lens = []
        Materials.stops = []
        Materials.obj = {}
        Materials.lights = {}
        Materials.aber = {}
        Materials.basic = {}

        lens_rows = self.lens.tableWidget.rowCount()
        k_rows = self.k.tableWidget.rowCount()

        my_table = []
        for row in range(0, lens_rows):
            my_row = []
            for col in range(0, 4):
                if self.lens.tableWidget.item(row, col) is not None:
                    my_row.append(float(self.lens.tableWidget.item(row, col).text()))
                else:
                    if col == 0:
                        my_row.append(1)
                    elif col == 2:
                        my_row.append(FAR_L)
                    else:
                        my_row.append(0)

            my_table.append(my_row)

        for row in range(0, lens_rows):

            if self.lens.tableWidget.verticalHeaderItem(row) is not None:
                my_type = self.lens.tableWidget.verticalHeaderItem(row).text()
            if my_type == 'OBJ':
                Materials.obj['n'] = my_table[row][0]
                Materials.obj['v'] = my_table[row][1]
                Materials.obj['r'] = my_table[row][2]
                Materials.obj['d'] = my_table[row][3]
                if self.lens.tableWidget.item(row, 4) is not None:
                     Materials.obj['w'] = float(self.lens.tableWidget.item(row, 4).text())
            elif my_type == 'STO':
                new_stop = {'r': my_table[row][2], 'd': my_table[row][3]}
                Materials.stops.append(new_stop)
            elif my_type == 'IMA':
                print('ima')
            else:
                Materials.add_len(my_table[row])
                Materials.nd.append(my_table[row][0])

        my_table = []
        for row in range(0, k_rows):
            my_row = []
            for col in range(0, 3):
                if self.k.tableWidget.item(row, col) is not None:
                    my_row.append(self.k.tableWidget.item(row, col).text())
                else:
                    my_row.append('')

            my_table.append(my_row)

        aber = ''
        for row in range(0, k_rows):
            if my_table[row][0] != '':
                aber = my_table[row][0]
                Materials.K[aber] = []

            if aber != '':
                Materials.K[aber].append([float(my_table[row][1]), float(my_table[row][2])])

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File',
                                                "newData", "Excel files (*.xls);;all files(*.*)")

        data = xlwt.Workbook()
        lens = data.add_sheet('Lens')
        k = data.add_sheet('Aberrations')

        rows = self.lens.tableWidget.rowCount()

        headers = ['', 'n', 'v', 'r', 'd', 'w']
        col_count = 0
        for header in headers:
            lens.write(0, col_count, header)
            col_count += 1

        for row in range(0, rows):
            if self.lens.tableWidget.verticalHeaderItem(row) is not None:
                lens.write(row + 1, 0, self.lens.tableWidget.verticalHeaderItem(row).text())
            for col in range(0, 4):
                if self.lens.tableWidget.item(row, col) is not None:
                    lens.write(row + 1, col + 1, self.lens.tableWidget.item(row, col).text())

        rows = self.k.tableWidget.rowCount()

        headers = ['Aberration', 'K1', 'K2']
        col_count = 0
        for header in headers:
            k.write(0, col_count, header)
            col_count += 1

        for row in range(0, rows):
            for col in range(0, 3):
                if self.k.tableWidget.item(row, col) is not None:
                    k.write(row + 1, col, self.k.tableWidget.item(row, col).text())

        data.save(file_path)

    def add_line(self):
        table = self.tabs.currentWidget().tableWidget
        rows = table.rowCount()

        row = table.currentRow() + 1
        table.insertRow(row)

        for i in range(0, rows + 1):
            if table.verticalHeaderItem(i) is not None:
                header = table.verticalHeaderItem(i).text()
            else:
                header = ''
            if header not in ['OBJ', 'STO', 'IMA']:
                new_header = QTableWidgetItem(str(i))
                table.setVerticalHeaderItem(i, new_header)


class OutputTable(QWidget):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.aber = QWidget()
        self.basic = QWidget()
        self.tabs.addTab(self.aber, 'Aberrations')
        self.tabs.addTab(self.basic, 'Basic parameters')

        self.aber.tableWidget = QTableWidget()
        self.aber.tableWidget.setRowCount(0)
        self.aber.tableWidget.setColumnCount(4)
        self.aber.tableWidget.setHorizontalHeaderLabels(['Aberration', 'K1', 'K2', 'Result'])
        self.aber.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.basic.tableWidget = QTableWidget()
        self.basic.tableWidget.setRowCount(0)
        self.basic.tableWidget.setColumnCount(2)
        self.basic.tableWidget.setHorizontalHeaderLabels(['Basic parameter', 'Result'])
        self.basic.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        save_file = QAction('Save', self)
        save_file.triggered.connect(self.save_file)
        tool = QToolBar(self)
        tool.addAction(save_file)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(tool)
        self.layout.addWidget(self.tabs)
        self.aber.layout = QVBoxLayout(self)
        self.aber.layout.addWidget(self.aber.tableWidget)
        self.aber.setLayout(self.aber.layout)
        self.basic.layout = QVBoxLayout(self)
        self.basic.layout.addWidget(self.basic.tableWidget)
        self.basic.setLayout(self.basic.layout)
        self.setLayout(self.layout)

    def result(self):
        row = 0
        for aber in Materials.aber:
            flag = 1
            for item in Materials.aber[aber]:
                self.aber.tableWidget.setRowCount(row + 1)
                if flag:
                    self.aber.tableWidget.setItem(row, 0, QTableWidgetItem(str(aber)))
                K = item.split('_')
                self.aber.tableWidget.setItem(row, 1, QTableWidgetItem(str(K[0])))
                self.aber.tableWidget.setItem(row, 2, QTableWidgetItem(str(K[1])))
                self.aber.tableWidget.setItem(row, 3, QTableWidgetItem(str(Materials.aber[aber][item])))
                row = row + 1
                flag = 0

        row = 0
        for basic in Materials.basic:
            self.basic.tableWidget.setRowCount(row + 1)
            self.basic.tableWidget.setItem(row, 0, QTableWidgetItem(str(basic)))
            self.basic.tableWidget.setItem(row, 1, QTableWidgetItem(str(Materials.basic[basic])))
            row = row + 1

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File',
                                                   "newData", "Excel files (*.xls);;all files(*.*)")

        data = xlwt.Workbook()
        aber = data.add_sheet('Aberrations')
        basic = data.add_sheet('Basic parameter')

        rows = self.aber.tableWidget.rowCount()
        headers = ['Aberration', 'K1', 'K2', 'Result']
        col_count = 0
        for header in headers:
            aber.write(0, col_count, header)
            col_count += 1

        for row in range(0, rows):
            for col in range(0, 4):
                if self.aber.tableWidget.item(row, col) is not None:
                    aber.write(row + 1, col, self.aber.tableWidget.item(row, col).text())

        rows = self.basic.tableWidget.rowCount()
        headers = ['Basic parameter', 'Result']
        col_count = 0
        for header in headers:
            basic.write(0, col_count, header)
            col_count += 1

        for row in range(0, rows):
            for col in range(0, 3):
                if self.basic.tableWidget.item(row, col) is not None:
                    basic.write(row + 1, col, self.basic.tableWidget.item(row, col).text())

        data.save(file_path)



