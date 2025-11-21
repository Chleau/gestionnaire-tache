# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.headerLayout.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.btnNouveau = QPushButton(self.centralwidget)
        self.btnNouveau.setObjectName(u"btnNouveau")

        self.headerLayout.addWidget(self.btnNouveau)


        self.verticalLayout.addLayout(self.headerLayout)

        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.labelFiltre = QLabel(self.centralwidget)
        self.labelFiltre.setObjectName(u"labelFiltre")

        self.filterLayout.addWidget(self.labelFiltre)

        self.comboFiltre = QComboBox(self.centralwidget)
        self.comboFiltre.addItem("")
        self.comboFiltre.addItem("")
        self.comboFiltre.addItem("")
        self.comboFiltre.addItem("")
        self.comboFiltre.addItem("")
        self.comboFiltre.addItem("")
        self.comboFiltre.setObjectName(u"comboFiltre")

        self.filterLayout.addWidget(self.comboFiltre)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.horizontalSpacer_2)

        self.labelTri = QLabel(self.centralwidget)
        self.labelTri.setObjectName(u"labelTri")

        self.filterLayout.addWidget(self.labelTri)

        self.comboTri = QComboBox(self.centralwidget)
        self.comboTri.addItem("")
        self.comboTri.addItem("")
        self.comboTri.addItem("")
        self.comboTri.addItem("")
        self.comboTri.setObjectName(u"comboTri")

        self.filterLayout.addWidget(self.comboTri)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.filterLayout)

        self.listeTaches = QListWidget(self.centralwidget)
        self.listeTaches.setObjectName(u"listeTaches")
        self.listeTaches.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.listeTaches)

        self.actionsLayout = QHBoxLayout()
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.btnVoir = QPushButton(self.centralwidget)
        self.btnVoir.setObjectName(u"btnVoir")

        self.actionsLayout.addWidget(self.btnVoir)

        self.btnModifier = QPushButton(self.centralwidget)
        self.btnModifier.setObjectName(u"btnModifier")

        self.actionsLayout.addWidget(self.btnModifier)

        self.btnCloturer = QPushButton(self.centralwidget)
        self.btnCloturer.setObjectName(u"btnCloturer")

        self.actionsLayout.addWidget(self.btnCloturer)

        self.btnSupprimer = QPushButton(self.centralwidget)
        self.btnSupprimer.setObjectName(u"btnSupprimer")

        self.actionsLayout.addWidget(self.btnSupprimer)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionsLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.actionsLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestionnaire de t\u00e2ches", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Gestionnaire de t\u00e2ches", None))
        self.btnNouveau.setText(QCoreApplication.translate("MainWindow", u"+ Nouvelle t\u00e2che", None))
        self.labelFiltre.setText(QCoreApplication.translate("MainWindow", u"Filtrer par \u00e9tat :", None))
        self.comboFiltre.setItemText(0, QCoreApplication.translate("MainWindow", u"Tous", None))
        self.comboFiltre.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c0 faire", None))
        self.comboFiltre.setItemText(2, QCoreApplication.translate("MainWindow", u"En cours", None))
        self.comboFiltre.setItemText(3, QCoreApplication.translate("MainWindow", u"R\u00e9alis\u00e9", None))
        self.comboFiltre.setItemText(4, QCoreApplication.translate("MainWindow", u"Abandonn\u00e9", None))
        self.comboFiltre.setItemText(5, QCoreApplication.translate("MainWindow", u"En attente", None))

        self.labelTri.setText(QCoreApplication.translate("MainWindow", u"Trier par :", None))
        self.comboTri.setItemText(0, QCoreApplication.translate("MainWindow", u"Titre", None))
        self.comboTri.setItemText(1, QCoreApplication.translate("MainWindow", u"Date d\u00e9but", None))
        self.comboTri.setItemText(2, QCoreApplication.translate("MainWindow", u"Date fin", None))
        self.comboTri.setItemText(3, QCoreApplication.translate("MainWindow", u"\u00c9tat", None))

        self.btnVoir.setText(QCoreApplication.translate("MainWindow", u"Voir d\u00e9tails :D", None))
        self.btnModifier.setText(QCoreApplication.translate("MainWindow", u"Modifier ;)", None))
        self.btnCloturer.setText(QCoreApplication.translate("MainWindow", u"Cl\u00f4turer :O", None))
        self.btnSupprimer.setText(QCoreApplication.translate("MainWindow", u"Supprimer :'(", None))
    # retranslateUi

