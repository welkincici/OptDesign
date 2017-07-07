import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

import NewTable
import Calculate
import Aberrations


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.menu_bar()

        self.setGeometry(300, 100, 800, 800)
        self.setWindowTitle('Light Seeker')
        self.show()

    def menu_bar(self):
        main_menu = self.menuBar()
        data_menu = main_menu.addMenu('Data')
        calculate_menu = main_menu.addMenu('Calculate')
        aberrations_menu = main_menu.addMenu('Aberrations')
        help_menu = main_menu.addMenu('Help')

        create_table_btn = QAction('New Table', self)
        create_table_btn.triggered.connect(self.create_table)
        data_menu.addAction(create_table_btn)

        paraxial_menu = calculate_menu.addMenu('Paraxial light')
        meridional_menu = calculate_menu.addMenu('Meridional light trace')
        # off_axis_menu = calculate_menu.addMenu('Off axis light')

        first_para_btn = QAction('First paraxial light', self)
        first_para_btn.triggered.connect(Calculate.first_para)
        second_para_btn = QAction('Second paraxial light', self)
        second_para_btn.triggered.connect(Calculate.second_para)
        height_btn = QAction('Height', self)
        height_btn.triggered.connect(Calculate.height)
        focal_btn = QAction('Focal', self)
        focal_btn.triggered.connect(Calculate.focal)
        lp_btn = QAction("Lp'", self)
        lp_btn.triggered.connect(Calculate.lp)
        paraxial_menu.addAction(first_para_btn)
        paraxial_menu.addAction(second_para_btn)
        paraxial_menu.addAction(focal_btn)
        paraxial_menu.addAction(height_btn)
        paraxial_menu.addAction(lp_btn)

        infi_on_btn = QAction('Infinity on-axis light', self)
        infi_on_btn.triggered.connect(Calculate.meri_infi_on)
        infi_off_btn = QAction('Infinity off-axis light', self)
        infi_off_btn.triggered.connect(Calculate.meri_infi_off)
        limi_on_btn = QAction('Limited distance on-axis light', self)
        limi_on_btn.triggered.connect(Calculate.meri_limi_on)
        limi_off_btn = QAction('Limited distance off-axis light', self)
        limi_off_btn.triggered.connect(Calculate.meri_limi_off)
        meridional_menu.addAction(infi_on_btn)
        meridional_menu.addAction(infi_off_btn)
        meridional_menu.addAction(limi_on_btn)
        meridional_menu.addAction(limi_off_btn)

        off_axis_btn = QAction('OffAxis', self)
        off_axis_btn.triggered.connect(Calculate.off_axis)
        calculate_menu.addAction(off_axis_btn)

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
        aberrations_menu.addAction(spherical_btn)
        aberrations_menu.addAction(coma_btn)
        aberrations_menu.addAction(astigmatism_btn)
        aberrations_menu.addAction(curvature_btn)
        aberrations_menu.addAction(distortion_btn)
        aberrations_menu.addAction(mag_chromatism_btn)
        aberrations_menu.addAction(trans_chromatism_btn)

        help_btn = QAction('Help', self)
        help_btn.triggered.connect(self.help)
        help_menu.addAction(help_btn)

    def create_table(self):
        self.new_table = NewTable.NewTable()

    def help(self):
        print('help')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())