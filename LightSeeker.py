import sys

from PyQt5.QtWidgets import QApplication, QAction, QSplitter, QMainWindow, QSplashScreen, QDesktopWidget
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QPixmap
import NewTable
import Calculate
import Aberrations
import Graph


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1400, 800)
        self.setWindowTitle('Light Seeker')

        self.menuBar()
        self.menu_bar()

        self.output = NewTable.OutputTable()
        self.input = NewTable.InputTable()

        spliter = QSplitter(self)
        spliter.addWidget(self.output)
        spliter.addWidget(self.input)
        spliter.setOrientation(Qt.Horizontal)
        self.setCentralWidget(spliter)

        QThread.sleep(1)
        self.show()

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def menu_bar(self):
        main_menu = self.menuBar()
        calculate_menu = main_menu.addMenu('Calculate')
        graph_menu = main_menu.addMenu('Graph')
        # layout_btn = main_menu.addAction('Layout')
        # layout_btn.triggered.connect(Layout.layout)

        paraxial_menu = calculate_menu.addMenu('Basic parameter')
        aberrations_menu = calculate_menu.addMenu('Aberrations')

        first_para_btn = QAction('Ideal spot', self)
        first_para_btn.triggered.connect(Calculate.first_para)
        height_btn = QAction('Height', self)
        height_btn.triggered.connect(Calculate.height)
        focal_btn = QAction('Focal', self)
        focal_btn.triggered.connect(Calculate.focal)
        lp_btn = QAction("Lp'", self)
        lp_btn.triggered.connect(Calculate.second_para)
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
        aberrations_menu.addAction(curvature_btn)
        aberrations_menu.addAction(distortion_btn)
        aberrations_menu.addAction(mag_chromatism_btn)
        aberrations_menu.addAction(trans_chromatism_btn)
        aberrations_menu.addAction(all_btn)

        gspherical_btn = QAction('Spherical', self)
        gspherical_btn.triggered.connect(Graph.spherical)
        gcurvature_btn = QAction('Curvature', self)
        gcurvature_btn.triggered.connect(Graph.curvature)
        gdistortion_btn = QAction('Distortion', self)
        gdistortion_btn.triggered.connect(Graph.distortion)
        gmag_chromatism_btn = QAction('Mag chromatism', self)
        gmag_chromatism_btn.triggered.connect(Graph.mag_chromatism)
        gtrans_chromatism_btn = QAction('Trans chromatism', self)
        gtrans_chromatism_btn.triggered.connect(Graph.trans_chromatism)
        gall_btn = QAction('All aberrations', self)
        gall_btn.triggered.connect(Graph.all_aberrations)
        graph_menu.addAction(gspherical_btn)
        graph_menu.addAction(gcurvature_btn)
        graph_menu.addAction(gdistortion_btn)
        graph_menu.addAction(gmag_chromatism_btn)
        graph_menu.addAction(gtrans_chromatism_btn)
        graph_menu.addAction(gall_btn)

        calculate_menu.triggered.connect(self.result)

    def result(self):
        self.output.result()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap('LightSeeker.jpg'))
    splash.show()
    app.processEvents()
    ex = MainWindow()
    splash.finish(ex)
    sys.exit(app.exec_())

