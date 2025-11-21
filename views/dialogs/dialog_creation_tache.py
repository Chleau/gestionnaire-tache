from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDateTime
from views.generated.ui_dialog_creation_tache import Ui_DialogCreationTache
from models.task import EtatTache

"Dialogue de création d'une nouvelle tâche"
class DialogCreationTache(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogCreationTache()
        self.ui.setupUi(self)
        
        # Initialiser les dates avec la date actuelle
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEditDebut.setDateTime(now)
        self.ui.dateTimeEditFin.setDateTime(now.addDays(7))  # Par défaut : dans 7 jours
        
    "Dialogue de création d'une nouvelle tâche"
    def get_data(self):
       # Convertir les QDateTime en datetime Python
        date_debut = self.ui.dateTimeEditDebut.dateTime().toPython()
        date_fin = self.ui.dateTimeEditFin.dateTime().toPython()
        
        return {
            'titre': self.ui.lineEditTitre.text().strip(),
            'description': self.ui.plainTextEditDescription.toPlainText().strip(),
            'date_debut': date_debut if date_debut else None,
            'date_fin': date_fin if date_fin else None,
            'etat': self._get_etat_from_combo()
        }

    "Convertit l'index du combo box en EtatTache."
    def _get_etat_from_combo(self):
        index = self.ui.comboBoxEtat.currentIndex()
        etats = [
            EtatTache.A_FAIRE,
            EtatTache.EN_COURS,
            EtatTache.REALISE,
            EtatTache.ABANDONNE,
            EtatTache.EN_ATTENTE
        ]
        return etats[index] if index < len(etats) else EtatTache.A_FAIRE
