from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDateTime
from views.generated.ui_dialog_edition_tache import Ui_DialogEditionTache
from models.task import EtatTache

"Dialogue d'édition d'une tâche existante"
class DialogEditionTache(QDialog):
    
    def __init__(self, task, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogEditionTache()
        self.ui.setupUi(self)
        self.task = task
        self._populate_fields()
        
        # Connecter les boutons
        self.ui.btnValider.clicked.connect(self.accept)
        self.ui.btnAnnuler.clicked.connect(self.reject)

    "Remplit les champs avec les données de la tâche" 
    def _populate_fields(self):
        self.ui.input_titre.setText(self.task.titre)
        self.ui.input_description.setPlainText(self.task.description or "")
        
        # Dates
        if self.task.date_debut:
            qdt = QDateTime(self.task.date_debut)
            self.ui.input_date_debut.setDateTime(qdt)
        
        if self.task.date_fin:
            qdt = QDateTime(self.task.date_fin)
            self.ui.input_date_fin.setDateTime(qdt)
        
        # Sélectionner l'état correspondant
        etat_index = self._get_etat_index(self.task.etat)
        self.ui.input_etat.setCurrentIndex(etat_index)
    
    "Convertit un EtatTache en index de combo box"
    def _get_etat_index(self, etat):
        etats = [
            EtatTache.A_FAIRE,
            EtatTache.EN_COURS,
            EtatTache.REALISE,
            EtatTache.ABANDONNE,
            EtatTache.EN_ATTENTE
        ]
        try:
            return etats.index(etat)
        except ValueError:
            return 0
        
    "Récupère les données modifiées dans le dialogue"
    def get_data(self):
        # Convertir les QDateTime en datetime Python
        date_debut = self.ui.input_date_debut.dateTime().toPython() if self.ui.input_date_debut.dateTime().isValid() else None
        date_fin = self.ui.input_date_fin.dateTime().toPython() if self.ui.input_date_fin.dateTime().isValid() else None
        
        return {
            'titre': self.ui.input_titre.text().strip(),
            'description': self.ui.input_description.toPlainText().strip(),
            'date_debut': date_debut,
            'date_fin': date_fin,
            'etat': self._get_etat_from_combo()
        }
    
    def _get_etat_from_combo(self):
        index = self.ui.input_etat.currentIndex()
        etats = [
            EtatTache.A_FAIRE,
            EtatTache.EN_COURS,
            EtatTache.REALISE,
            EtatTache.ABANDONNE,
            EtatTache.EN_ATTENTE
        ]
        return etats[index] if index < len(etats) else EtatTache.A_FAIRE
