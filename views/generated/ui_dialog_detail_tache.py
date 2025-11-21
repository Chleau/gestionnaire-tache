# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_detail_tache.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DialogDetailTache(object):
    def setupUi(self, DialogDetailTache):
        if not DialogDetailTache.objectName():
            DialogDetailTache.setObjectName(u"DialogDetailTache")
        DialogDetailTache.resize(600, 713)
        self.verticalLayout = QVBoxLayout(DialogDetailTache)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(DialogDetailTache)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.titleLabel)

        self.groupBoxInfos = QGroupBox(DialogDetailTache)
        self.groupBoxInfos.setObjectName(u"groupBoxInfos")
        self.formLayout = QFormLayout(self.groupBoxInfos)
        self.formLayout.setObjectName(u"formLayout")
        self.label_etat_text = QLabel(self.groupBoxInfos)
        self.label_etat_text.setObjectName(u"label_etat_text")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_etat_text)

        self.label_etat = QLabel(self.groupBoxInfos)
        self.label_etat.setObjectName(u"label_etat")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_etat)

        self.label_date_debut_text = QLabel(self.groupBoxInfos)
        self.label_date_debut_text.setObjectName(u"label_date_debut_text")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_date_debut_text)

        self.label_date_debut = QLabel(self.groupBoxInfos)
        self.label_date_debut.setObjectName(u"label_date_debut")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_date_debut)

        self.label_date_fin_text = QLabel(self.groupBoxInfos)
        self.label_date_fin_text.setObjectName(u"label_date_fin_text")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_date_fin_text)

        self.label_date_fin = QLabel(self.groupBoxInfos)
        self.label_date_fin.setObjectName(u"label_date_fin")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_date_fin)


        self.verticalLayout.addWidget(self.groupBoxInfos)

        self.groupBoxComments = QGroupBox(DialogDetailTache)
        self.groupBoxComments.setObjectName(u"groupBoxComments")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxComments)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 20, 15, 15)
        self.label_nouveau_commentaire = QLabel(self.groupBoxComments)
        self.label_nouveau_commentaire.setObjectName(u"label_nouveau_commentaire")

        self.verticalLayout_2.addWidget(self.label_nouveau_commentaire)

        self.text_nouveau_commentaire = QPlainTextEdit(self.groupBoxComments)
        self.text_nouveau_commentaire.setObjectName(u"text_nouveau_commentaire")
        self.text_nouveau_commentaire.setMinimumSize(QSize(0, 100))
        self.text_nouveau_commentaire.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.text_nouveau_commentaire)

        self.btnAjouterCommentaire = QPushButton(self.groupBoxComments)
        self.btnAjouterCommentaire.setObjectName(u"btnAjouterCommentaire")
        self.btnAjouterCommentaire.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.btnAjouterCommentaire)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_liste_commentaires = QLabel(self.groupBoxComments)
        self.label_liste_commentaires.setObjectName(u"label_liste_commentaires")

        self.verticalLayout_2.addWidget(self.label_liste_commentaires)

        self.liste_commentaires = QListWidget(self.groupBoxComments)
        self.liste_commentaires.setObjectName(u"liste_commentaires")
        self.liste_commentaires.setMinimumSize(QSize(0, 120))
        self.liste_commentaires.setMaximumSize(QSize(16777215, 200))
        self.liste_commentaires.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.liste_commentaires)

        self.btnSupprimerCommentaire = QPushButton(self.groupBoxComments)
        self.btnSupprimerCommentaire.setObjectName(u"btnSupprimerCommentaire")
        self.btnSupprimerCommentaire.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.btnSupprimerCommentaire)


        self.verticalLayout.addWidget(self.groupBoxComments)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCloturer = QPushButton(DialogDetailTache)
        self.btnCloturer.setObjectName(u"btnCloturer")

        self.horizontalLayout.addWidget(self.btnCloturer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnFermer = QPushButton(DialogDetailTache)
        self.btnFermer.setObjectName(u"btnFermer")

        self.horizontalLayout.addWidget(self.btnFermer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogDetailTache)

        QMetaObject.connectSlotsByName(DialogDetailTache)
    # setupUi

    def retranslateUi(self, DialogDetailTache):
        DialogDetailTache.setWindowTitle(QCoreApplication.translate("DialogDetailTache", u"D\u00e9tails de la t\u00e2che", None))
        self.titleLabel.setText(QCoreApplication.translate("DialogDetailTache", u"Titre de la t\u00e2che", None))
        self.groupBoxInfos.setTitle(QCoreApplication.translate("DialogDetailTache", u"Informations", None))
        self.label_etat_text.setText(QCoreApplication.translate("DialogDetailTache", u"\u00c9tat :", None))
        self.label_etat.setText(QCoreApplication.translate("DialogDetailTache", u"\u00c0 faire", None))
        self.label_date_debut_text.setText(QCoreApplication.translate("DialogDetailTache", u"Depuis le", None))
        self.label_date_debut.setText(QCoreApplication.translate("DialogDetailTache", u"Non d\u00e9finie", None))
        self.label_date_fin_text.setText(QCoreApplication.translate("DialogDetailTache", u"Avant le ", None))
        self.label_date_fin.setText(QCoreApplication.translate("DialogDetailTache", u"Non d\u00e9finie", None))
        self.groupBoxComments.setTitle(QCoreApplication.translate("DialogDetailTache", u"Commentaires", None))
        self.label_nouveau_commentaire.setText(QCoreApplication.translate("DialogDetailTache", u"Une pens\u00e9e en plus pour cette t\u00e2che :", None))
        self.text_nouveau_commentaire.setPlaceholderText(QCoreApplication.translate("DialogDetailTache", u"\u00c9crivez votre commentaire ici...", None))
        self.btnAjouterCommentaire.setText(QCoreApplication.translate("DialogDetailTache", u"+ Ajouter le commentaire", None))
        self.label_liste_commentaires.setText(QCoreApplication.translate("DialogDetailTache", u"Commentaires existants :", None))
        self.btnSupprimerCommentaire.setText(QCoreApplication.translate("DialogDetailTache", u"Supprimer le commentaire s\u00e9lectionn\u00e9", None))
        self.btnCloturer.setText(QCoreApplication.translate("DialogDetailTache", u"Cl\u00f4turer la t\u00e2che", None))
        self.btnFermer.setText(QCoreApplication.translate("DialogDetailTache", u"Fermer", None))
    # retranslateUi

