# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Bt_factorial = QPushButton(self.centralwidget)
        self.Bt_factorial.setObjectName(u"Bt_factorial")
        self.Bt_factorial.setGeometry(QRect(60, 190, 51, 61))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Bt_factorial.setFont(font)
        self.Bt_factorial.setMouseTracking(False)
        self.Bt_factorial.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_cleanAll = QPushButton(self.centralwidget)
        self.Bt_cleanAll.setObjectName(u"Bt_cleanAll")
        self.Bt_cleanAll.setGeometry(QRect(120, 190, 51, 61))
        self.Bt_cleanAll.setFont(font)
        self.Bt_cleanAll.setMouseTracking(False)
        self.Bt_cleanAll.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_tau = QPushButton(self.centralwidget)
        self.Bt_tau.setObjectName(u"Bt_tau")
        self.Bt_tau.setGeometry(QRect(180, 190, 51, 61))
        self.Bt_tau.setFont(font)
        self.Bt_tau.setMouseTracking(False)
        self.Bt_tau.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_clean = QPushButton(self.centralwidget)
        self.Bt_clean.setObjectName(u"Bt_clean")
        self.Bt_clean.setGeometry(QRect(240, 190, 51, 61))
        self.Bt_clean.setFont(font)
        self.Bt_clean.setMouseTracking(False)
        self.Bt_clean.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_dividir = QPushButton(self.centralwidget)
        self.Bt_dividir.setObjectName(u"Bt_dividir")
        self.Bt_dividir.setGeometry(QRect(300, 190, 51, 61))
        self.Bt_dividir.setFont(font)
        self.Bt_dividir.setMouseTracking(False)
        self.Bt_dividir.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_8 = QPushButton(self.centralwidget)
        self.Bt_8.setObjectName(u"Bt_8")
        self.Bt_8.setGeometry(QRect(180, 260, 51, 61))
        self.Bt_8.setFont(font)
        self.Bt_8.setMouseTracking(False)
        self.Bt_8.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_expo = QPushButton(self.centralwidget)
        self.Bt_expo.setObjectName(u"Bt_expo")
        self.Bt_expo.setGeometry(QRect(60, 260, 51, 61))
        self.Bt_expo.setFont(font)
        self.Bt_expo.setMouseTracking(False)
        self.Bt_expo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_multi = QPushButton(self.centralwidget)
        self.Bt_multi.setObjectName(u"Bt_multi")
        self.Bt_multi.setGeometry(QRect(300, 260, 51, 61))
        self.Bt_multi.setFont(font)
        self.Bt_multi.setMouseTracking(False)
        self.Bt_multi.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_7 = QPushButton(self.centralwidget)
        self.Bt_7.setObjectName(u"Bt_7")
        self.Bt_7.setGeometry(QRect(120, 260, 51, 61))
        self.Bt_7.setFont(font)
        self.Bt_7.setMouseTracking(False)
        self.Bt_7.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_9 = QPushButton(self.centralwidget)
        self.Bt_9.setObjectName(u"Bt_9")
        self.Bt_9.setGeometry(QRect(240, 260, 51, 61))
        self.Bt_9.setFont(font)
        self.Bt_9.setMouseTracking(False)
        self.Bt_9.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_5 = QPushButton(self.centralwidget)
        self.Bt_5.setObjectName(u"Bt_5")
        self.Bt_5.setGeometry(QRect(180, 330, 51, 61))
        self.Bt_5.setFont(font)
        self.Bt_5.setMouseTracking(False)
        self.Bt_5.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_raiz = QPushButton(self.centralwidget)
        self.Bt_raiz.setObjectName(u"Bt_raiz")
        self.Bt_raiz.setGeometry(QRect(60, 330, 51, 61))
        self.Bt_raiz.setFont(font)
        self.Bt_raiz.setMouseTracking(False)
        self.Bt_raiz.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_menos = QPushButton(self.centralwidget)
        self.Bt_menos.setObjectName(u"Bt_menos")
        self.Bt_menos.setGeometry(QRect(300, 330, 51, 61))
        self.Bt_menos.setFont(font)
        self.Bt_menos.setMouseTracking(False)
        self.Bt_menos.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_4 = QPushButton(self.centralwidget)
        self.Bt_4.setObjectName(u"Bt_4")
        self.Bt_4.setGeometry(QRect(120, 330, 51, 61))
        self.Bt_4.setFont(font)
        self.Bt_4.setMouseTracking(False)
        self.Bt_4.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_6 = QPushButton(self.centralwidget)
        self.Bt_6.setObjectName(u"Bt_6")
        self.Bt_6.setGeometry(QRect(240, 330, 51, 61))
        self.Bt_6.setFont(font)
        self.Bt_6.setMouseTracking(False)
        self.Bt_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_2 = QPushButton(self.centralwidget)
        self.Bt_2.setObjectName(u"Bt_2")
        self.Bt_2.setGeometry(QRect(180, 400, 51, 61))
        self.Bt_2.setFont(font)
        self.Bt_2.setMouseTracking(False)
        self.Bt_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_pi = QPushButton(self.centralwidget)
        self.Bt_pi.setObjectName(u"Bt_pi")
        self.Bt_pi.setGeometry(QRect(60, 400, 51, 61))
        self.Bt_pi.setFont(font)
        self.Bt_pi.setMouseTracking(False)
        self.Bt_pi.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_sumar = QPushButton(self.centralwidget)
        self.Bt_sumar.setObjectName(u"Bt_sumar")
        self.Bt_sumar.setGeometry(QRect(300, 400, 51, 61))
        self.Bt_sumar.setFont(font)
        self.Bt_sumar.setMouseTracking(False)
        self.Bt_sumar.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_1 = QPushButton(self.centralwidget)
        self.Bt_1.setObjectName(u"Bt_1")
        self.Bt_1.setGeometry(QRect(120, 400, 51, 61))
        self.Bt_1.setFont(font)
        self.Bt_1.setMouseTracking(False)
        self.Bt_1.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_3 = QPushButton(self.centralwidget)
        self.Bt_3.setObjectName(u"Bt_3")
        self.Bt_3.setGeometry(QRect(240, 400, 51, 61))
        self.Bt_3.setFont(font)
        self.Bt_3.setMouseTracking(False)
        self.Bt_3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_0 = QPushButton(self.centralwidget)
        self.Bt_0.setObjectName(u"Bt_0")
        self.Bt_0.setGeometry(QRect(180, 480, 51, 61))
        self.Bt_0.setFont(font)
        self.Bt_0.setMouseTracking(False)
        self.Bt_0.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_parenIzq = QPushButton(self.centralwidget)
        self.Bt_parenIzq.setObjectName(u"Bt_parenIzq")
        self.Bt_parenIzq.setGeometry(QRect(60, 480, 51, 61))
        self.Bt_parenIzq.setFont(font)
        self.Bt_parenIzq.setMouseTracking(False)
        self.Bt_parenIzq.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_igual = QPushButton(self.centralwidget)
        self.Bt_igual.setObjectName(u"Bt_igual")
        self.Bt_igual.setGeometry(QRect(300, 480, 51, 61))
        self.Bt_igual.setFont(font)
        self.Bt_igual.setMouseTracking(False)
        self.Bt_igual.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_parenDer = QPushButton(self.centralwidget)
        self.Bt_parenDer.setObjectName(u"Bt_parenDer")
        self.Bt_parenDer.setGeometry(QRect(120, 480, 51, 61))
        self.Bt_parenDer.setFont(font)
        self.Bt_parenDer.setMouseTracking(False)
        self.Bt_parenDer.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_coma = QPushButton(self.centralwidget)
        self.Bt_coma.setObjectName(u"Bt_coma")
        self.Bt_coma.setGeometry(QRect(240, 480, 51, 61))
        self.Bt_coma.setFont(font)
        self.Bt_coma.setMouseTracking(False)
        self.Bt_coma.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_seno = QPushButton(self.centralwidget)
        self.Bt_seno.setObjectName(u"Bt_seno")
        self.Bt_seno.setGeometry(QRect(180, 120, 51, 61))
        self.Bt_seno.setFont(font)
        self.Bt_seno.setMouseTracking(False)
        self.Bt_seno.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_logaritmo = QPushButton(self.centralwidget)
        self.Bt_logaritmo.setObjectName(u"Bt_logaritmo")
        self.Bt_logaritmo.setGeometry(QRect(60, 120, 51, 61))
        self.Bt_logaritmo.setFont(font)
        self.Bt_logaritmo.setMouseTracking(False)
        self.Bt_logaritmo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_tangente = QPushButton(self.centralwidget)
        self.Bt_tangente.setObjectName(u"Bt_tangente")
        self.Bt_tangente.setGeometry(QRect(300, 120, 51, 61))
        self.Bt_tangente.setFont(font)
        self.Bt_tangente.setMouseTracking(False)
        self.Bt_tangente.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_e = QPushButton(self.centralwidget)
        self.Bt_e.setObjectName(u"Bt_e")
        self.Bt_e.setGeometry(QRect(120, 120, 51, 61))
        self.Bt_e.setFont(font)
        self.Bt_e.setMouseTracking(False)
        self.Bt_e.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Bt_coseno = QPushButton(self.centralwidget)
        self.Bt_coseno.setObjectName(u"Bt_coseno")
        self.Bt_coseno.setGeometry(QRect(240, 120, 51, 61))
        self.Bt_coseno.setFont(font)
        self.Bt_coseno.setMouseTracking(False)
        self.Bt_coseno.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.TW_table = QTableWidget(self.centralwidget)
        self.TW_table.setObjectName(u"TW_table")
        self.TW_table.setGeometry(QRect(420, 20, 256, 521))
        self.TE_resultado = QLineEdit(self.centralwidget)
        self.TE_resultado.setObjectName(u"TE_resultado")
        self.TE_resultado.setGeometry(QRect(62, 50, 291, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Bt_factorial.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.Bt_cleanAll.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.Bt_tau.setText(QCoreApplication.translate("MainWindow", u"\u03c4", None))
        self.Bt_clean.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Bt_dividir.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.Bt_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Bt_expo.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.Bt_multi.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.Bt_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Bt_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Bt_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Bt_raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.Bt_menos.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Bt_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Bt_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Bt_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Bt_pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.Bt_sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Bt_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Bt_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Bt_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Bt_parenIzq.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.Bt_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Bt_parenDer.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.Bt_coma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.Bt_seno.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.Bt_logaritmo.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.Bt_tangente.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.Bt_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.Bt_coseno.setText(QCoreApplication.translate("MainWindow", u"cos", None))
    # retranslateUi

