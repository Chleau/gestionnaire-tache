# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_creation_tache.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogCreationTache(object):
    def setupUi(self, DialogCreationTache):
        if not DialogCreationTache.objectName():
            DialogCreationTache.setObjectName(u"DialogCreationTache")
        DialogCreationTache.resize(565, 525)
        self.verticalLayout = QVBoxLayout(DialogCreationTache)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxInfos = QGroupBox(DialogCreationTache)
        self.groupBoxInfos.setObjectName(u"groupBoxInfos")
        self.formLayout = QFormLayout(self.groupBoxInfos)
        self.formLayout.setObjectName(u"formLayout")
        self.titleLabel = QLabel(self.groupBoxInfos)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.titleLabel)

        self.labelTitre = QLabel(self.groupBoxInfos)
        self.labelTitre.setObjectName(u"labelTitre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelTitre)

        self.lineEditTitre = QLineEdit(self.groupBoxInfos)
        self.lineEditTitre.setObjectName(u"lineEditTitre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEditTitre)

        self.labelDescription = QLabel(self.groupBoxInfos)
        self.labelDescription.setObjectName(u"labelDescription")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelDescription)

        self.plainTextEditDescription = QPlainTextEdit(self.groupBoxInfos)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.plainTextEditDescription)

        self.label_date_debut = QLabel(self.groupBoxInfos)
        self.label_date_debut.setObjectName(u"label_date_debut")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_date_debut)

        self.dateTimeEditDebut = QDateTimeEdit(self.groupBoxInfos)
        self.dateTimeEditDebut.setObjectName(u"dateTimeEditDebut")
        self.dateTimeEditDebut.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateTimeEditDebut)

        self.label_date_fin = QLabel(self.groupBoxInfos)
        self.label_date_fin.setObjectName(u"label_date_fin")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_date_fin)

        self.dateTimeEditFin = QDateTimeEdit(self.groupBoxInfos)
        self.dateTimeEditFin.setObjectName(u"dateTimeEditFin")
        self.dateTimeEditFin.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dateTimeEditFin)


        self.verticalLayout.addWidget(self.groupBoxInfos)

        self.groupBoxEtat = QGroupBox(DialogCreationTache)
        self.groupBoxEtat.setObjectName(u"groupBoxEtat")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxEtat)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBoxEtat = QComboBox(self.groupBoxEtat)
        self.comboBoxEtat.addItem("")
        self.comboBoxEtat.addItem("")
        self.comboBoxEtat.addItem("")
        self.comboBoxEtat.addItem("")
        self.comboBoxEtat.addItem("")
        self.comboBoxEtat.setObjectName(u"comboBoxEtat")

        self.verticalLayout_2.addWidget(self.comboBoxEtat)


        self.verticalLayout.addWidget(self.groupBoxEtat)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAnnuler = QPushButton(DialogCreationTache)
        self.btnAnnuler.setObjectName(u"btnAnnuler")

        self.horizontalLayout.addWidget(self.btnAnnuler)

        self.btnCreer = QPushButton(DialogCreationTache)
        self.btnCreer.setObjectName(u"btnCreer")

        self.horizontalLayout.addWidget(self.btnCreer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DialogCreationTache)
        self.btnAnnuler.clicked.connect(DialogCreationTache.reject)
        self.btnCreer.clicked.connect(DialogCreationTache.accept)

        QMetaObject.connectSlotsByName(DialogCreationTache)
    # setupUi

    def retranslateUi(self, DialogCreationTache):
        DialogCreationTache.setWindowTitle(QCoreApplication.translate("DialogCreationTache", u"Nouvelle t\u00e2che", None))
        self.groupBoxInfos.setTitle(QCoreApplication.translate("DialogCreationTache", u"Informations g\u00e9n\u00e9rales", None))
        self.titleLabel.setText(QCoreApplication.translate("DialogCreationTache", u"Cr\u00e9er une nouvelle t\u00e2che !", None))
        self.labelTitre.setText(QCoreApplication.translate("DialogCreationTache", u"Titre *", None))
        self.lineEditTitre.setPlaceholderText(QCoreApplication.translate("DialogCreationTache", u"Entrez le titre de la t\u00e2che", None))
        self.labelDescription.setText(QCoreApplication.translate("DialogCreationTache", u"Description", None))
        self.plainTextEditDescription.setPlaceholderText(QCoreApplication.translate("DialogCreationTache", u"Description d\u00e9taill\u00e9e (optionnel)", None))
        self.label_date_debut.setText(QCoreApplication.translate("DialogCreationTache", u"Commencer \u00e0 partir de :", None))
        self.dateTimeEditDebut.setDisplayFormat(QCoreApplication.translate("DialogCreationTache", u"dd/MM/yyyy HH:mm", None))
        self.label_date_fin.setText(QCoreApplication.translate("DialogCreationTache", u"Date de fin pr\u00e9vu :", None))
        self.dateTimeEditFin.setDisplayFormat(QCoreApplication.translate("DialogCreationTache", u"dd/MM/yyyy HH:mm", None))
        self.groupBoxEtat.setTitle(QCoreApplication.translate("DialogCreationTache", u"\u00c9tat *", None))
        self.comboBoxEtat.setItemText(0, QCoreApplication.translate("DialogCreationTache", u"\u00c0 faire", None))
        self.comboBoxEtat.setItemText(1, QCoreApplication.translate("DialogCreationTache", u"En cours", None))
        self.comboBoxEtat.setItemText(2, QCoreApplication.translate("DialogCreationTache", u"R\u00e9alis\u00e9", None))
        self.comboBoxEtat.setItemText(3, QCoreApplication.translate("DialogCreationTache", u"Abandonn\u00e9", None))
        self.comboBoxEtat.setItemText(4, QCoreApplication.translate("DialogCreationTache", u"En attente", None))

        self.btnAnnuler.setText(QCoreApplication.translate("DialogCreationTache", u"Annuler", None))
        self.btnCreer.setText(QCoreApplication.translate("DialogCreationTache", u"Cr\u00e9er la t\u00e2che :)", None))
    # retranslateUi

