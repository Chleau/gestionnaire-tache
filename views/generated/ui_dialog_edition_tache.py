# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_edition_tache.ui'
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

class Ui_DialogEditionTache(object):
    def setupUi(self, DialogEditionTache):
        if not DialogEditionTache.objectName():
            DialogEditionTache.setObjectName(u"DialogEditionTache")
        DialogEditionTache.resize(500, 600)
        self.verticalLayout = QVBoxLayout(DialogEditionTache)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(DialogEditionTache)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.groupBoxFormulaire = QGroupBox(DialogEditionTache)
        self.groupBoxFormulaire.setObjectName(u"groupBoxFormulaire")
        self.formLayout = QFormLayout(self.groupBoxFormulaire)
        self.formLayout.setObjectName(u"formLayout")
        self.label_titre = QLabel(self.groupBoxFormulaire)
        self.label_titre.setObjectName(u"label_titre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_titre)

        self.input_titre = QLineEdit(self.groupBoxFormulaire)
        self.input_titre.setObjectName(u"input_titre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_titre)

        self.label_description = QLabel(self.groupBoxFormulaire)
        self.label_description.setObjectName(u"label_description")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_description)

        self.input_description = QPlainTextEdit(self.groupBoxFormulaire)
        self.input_description.setObjectName(u"input_description")
        self.input_description.setMinimumSize(QSize(0, 100))
        self.input_description.setMaximumSize(QSize(16777215, 150))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_description)

        self.label_date_debut = QLabel(self.groupBoxFormulaire)
        self.label_date_debut.setObjectName(u"label_date_debut")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_date_debut)

        self.input_date_debut = QDateTimeEdit(self.groupBoxFormulaire)
        self.input_date_debut.setObjectName(u"input_date_debut")
        self.input_date_debut.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_date_debut)

        self.label_date_fin = QLabel(self.groupBoxFormulaire)
        self.label_date_fin.setObjectName(u"label_date_fin")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_date_fin)

        self.input_date_fin = QDateTimeEdit(self.groupBoxFormulaire)
        self.input_date_fin.setObjectName(u"input_date_fin")
        self.input_date_fin.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_date_fin)

        self.label_etat = QLabel(self.groupBoxFormulaire)
        self.label_etat.setObjectName(u"label_etat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_etat)

        self.input_etat = QComboBox(self.groupBoxFormulaire)
        self.input_etat.addItem("")
        self.input_etat.addItem("")
        self.input_etat.addItem("")
        self.input_etat.addItem("")
        self.input_etat.addItem("")
        self.input_etat.setObjectName(u"input_etat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.input_etat)


        self.verticalLayout.addWidget(self.groupBoxFormulaire)

        self.label_info = QLabel(DialogEditionTache)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"font-style: italic; color: #888;")

        self.verticalLayout.addWidget(self.label_info)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnValider = QPushButton(DialogEditionTache)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btnValider)

        self.btnAnnuler = QPushButton(DialogEditionTache)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btnAnnuler)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogEditionTache)

        QMetaObject.connectSlotsByName(DialogEditionTache)
    # setupUi

    def retranslateUi(self, DialogEditionTache):
        DialogEditionTache.setWindowTitle(QCoreApplication.translate("DialogEditionTache", u"Modifier la t\u00e2che", None))
        self.titleLabel.setText(QCoreApplication.translate("DialogEditionTache", u"Modifier la t\u00e2che", None))
        self.groupBoxFormulaire.setTitle(QCoreApplication.translate("DialogEditionTache", u"Informations de la t\u00e2che", None))
        self.label_titre.setText(QCoreApplication.translate("DialogEditionTache", u"Titre * :", None))
        self.input_titre.setPlaceholderText(QCoreApplication.translate("DialogEditionTache", u"Titre de la t\u00e2che", None))
        self.label_description.setText(QCoreApplication.translate("DialogEditionTache", u"Description :", None))
        self.input_description.setPlaceholderText(QCoreApplication.translate("DialogEditionTache", u"Description de la t\u00e2che (optionnelle)", None))
        self.label_date_debut.setText(QCoreApplication.translate("DialogEditionTache", u"Date de d\u00e9but :", None))
        self.input_date_debut.setDisplayFormat(QCoreApplication.translate("DialogEditionTache", u"dd/MM/yyyy HH:mm", None))
        self.label_date_fin.setText(QCoreApplication.translate("DialogEditionTache", u"Date de fin pr\u00e9vu:", None))
        self.input_date_fin.setDisplayFormat(QCoreApplication.translate("DialogEditionTache", u"dd/MM/yyyy HH:mm", None))
        self.label_etat.setText(QCoreApplication.translate("DialogEditionTache", u"\u00c9tat *:", None))
        self.input_etat.setItemText(0, QCoreApplication.translate("DialogEditionTache", u"\u00c0 faire", None))
        self.input_etat.setItemText(1, QCoreApplication.translate("DialogEditionTache", u"En cours", None))
        self.input_etat.setItemText(2, QCoreApplication.translate("DialogEditionTache", u"R\u00e9alis\u00e9", None))
        self.input_etat.setItemText(3, QCoreApplication.translate("DialogEditionTache", u"Abandonn\u00e9", None))
        self.input_etat.setItemText(4, QCoreApplication.translate("DialogEditionTache", u"En attente", None))

        self.label_info.setText(QCoreApplication.translate("DialogEditionTache", u"* Champs obligatoires", None))
        self.btnValider.setText(QCoreApplication.translate("DialogEditionTache", u"Valider les modifications", None))
        self.btnAnnuler.setText(QCoreApplication.translate("DialogEditionTache", u"Annuler", None))
    # retranslateUi

