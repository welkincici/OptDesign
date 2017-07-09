import sys

from PyQt5.QtWidgets import QApplication, QAction, QVBoxLayout, QWidget, QMenuBar

import NewTable
import Calculate
import Aberrations
import ChildWidget


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.main_menu = QMenuBar(self)
        self.menu_bar()
        self.main_menu.setGeometry(0, 0, 100000000, 30)

        self.setGeometry(200, 100, 800, 800)
        self.setWindowTitle('Light Seeker')

        self.gra = ChildWidget.Graph()
        self.tex = ChildWidget.Text()

        vbox = QVBoxLayout()
        vbox.addWidget(self.gra)
        vbox.addWidget(self.tex)
        self.setLayout(vbox)

        self.show()

    def menu_bar(self):
        main_menu = self.main_menu
        data_menu = main_menu.addMenu('Data')
        calculate_menu = main_menu.addMenu('Calculate')
        graph_menu = main_menu.addMenu('Graph')
        help_menu = main_menu.addMenu('Help')

        create_table_btn = QAction('New Table', self)
        create_table_btn.triggered.connect(self.create_table)
        save_btn = QAction('Save result', self)
        save_btn.triggered.connect(self.create_table)
        data_menu.addAction(create_table_btn)
        data_menu.addAction(save_btn)

        paraxial_menu = calculate_menu.addMenu('Basic parameter')
        aberrations_menu = calculate_menu.addMenu('Aberrations')

        first_para_btn = QAction('Ideal spot', self)
        first_para_btn.triggered.connect(Calculate.first_para)
        height_btn = QAction('Height', self)
        height_btn.triggered.connect(Calculate.height)
        focal_btn = QAction('Focal', self)
        focal_btn.triggered.connect(Calculate.focal)
        lp_btn = QAction("Lp'", self)
        lp_btn.triggered.connect(Calculate.lp)
        all1_btn = QAction('Calculate all basic parameters', self)
        all1_btn.triggered.connect(Calculate.all_parameters)
        paraxial_menu.addAction(first_para_btn)
        paraxial_menu.addAction(focal_btn)
        paraxial_menu.addAction(height_btn)
        paraxial_menu.addAction(lp_btn)
        paraxial_menu.addAction(all1_btn)

        spherical_btn = QAction('Spherical', self)
        spherical_btn.triggered.connect(Aberrations.spherical)
        coma_btn = QAction('Coma', self)
        coma_btn.triggered.connect(Aberrations.coma)
        astigmatism_btn = QAction('Astigmatism', self)
        astigmatism_btn.triggered.connect(Aberrations.astigmatism)
        curvature_btn = QAction('Curvature', self)
        curvature_btn.triggered.connect(Aberrations.curvature)
        distortion_btn = QAction('Distortion', self)
        distortion_btn.triggered.connect(Aberrations.distortion)
        mag_chromatism_btn = QAction('Mag chromatism', self)
        mag_chromatism_btn.triggered.connect(Aberrations.mag_chromatism)
        trans_chromatism_btn = QAction('Trans chromatism', self)
        trans_chromatism_btn.triggered.connect(Aberrations.trans_chromatism)
        all_btn = QAction('Calculate all aberrations', self)
        all_btn.triggered.connect(Aberrations.all_aberrations)
        aberrations_menu.addAction(spherical_btn)
        aberrations_menu.addAction(coma_btn)
        aberrations_menu.addAction(astigmatism_btn)
        aberrations_menu.addAction(curvature_btn)
        aberrations_menu.addAction(distortion_btn)
        aberrations_menu.addAction(mag_chromatism_btn)
        aberrations_menu.addAction(trans_chromatism_btn)
        aberrations_menu.addAction(all_btn)

        gspherical_btn = QAction('Spherical', self)
        gspherical_btn.triggered.connect(Aberrations.spherical)
        gcoma_btn = QAction('Coma', self)
        gcoma_btn.triggered.connect(Aberrations.coma)
        gastigmatism_btn = QAction('Astigmatism', self)
        gastigmatism_btn.triggered.connect(Aberrations.astigmatism)
        gcurvature_btn = QAction('Curvature', self)
        gcurvature_btn.triggered.connect(Aberrations.curvature)
        gdistortion_btn = QAction('Distortion', self)
        gdistortion_btn.triggered.connect(Aberrations.distortion)
        gmag_chromatism_btn = QAction('Mag chromatism', self)
        gmag_chromatism_btn.triggered.connect(Aberrations.mag_chromatism)
        gtrans_chromatism_btn = QAction('Trans chromatism', self)
        gtrans_chromatism_btn.triggered.connect(Aberrations.trans_chromatism)
        gall_btn = QAction('Calculate all aberrations', self)
        gall_btn.triggered.connect(Aberrations.all_aberrations)
        graph_menu.addAction(gspherical_btn)
        graph_menu.addAction(gcoma_btn)
        graph_menu.addAction(gastigmatism_btn)
        graph_menu.addAction(gcurvature_btn)
        graph_menu.addAction(gdistortion_btn)
        graph_menu.addAction(gmag_chromatism_btn)
        graph_menu.addAction(gtrans_chromatism_btn)
        graph_menu.addAction(gall_btn)

        help_btn = QAction('Help', self)
        help_btn.triggered.connect(self.help)
        help_menu.addAction(help_btn)

        calculate_menu.triggered.connect(self.result)

    def create_table(self):
        self.new_table = NewTable.NewTable()

    def help(self):
        print('help')

    def result(self):
        self.tex.result_text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

