from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt

from views.generated.ui_main_window import Ui_MainWindow
from views.dialogs import DialogCreationTache, DialogEditionTache, DialogDetailTache


class MainWindow(QMainWindow):
    """Wrapper MainWindow that uses the generated Ui_MainWindow."""
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.btnNouveau.clicked.connect(self.ouvrir_creation_tache)
        self.ui.btnVoir.clicked.connect(self.ouvrir_detail_tache)
        self.ui.btnModifier.clicked.connect(self.ouvrir_edition_tache)
        self.ui.btnCloturer.clicked.connect(self.ouvrir_cloturer_tache)
        self.ui.btnSupprimer.clicked.connect(self.ouvrir_supprimer_tache)
        self.ui.listeTaches.itemDoubleClicked.connect(self.ouvrir_detail_tache)
        
        # Connect filter and sort signals
        self.ui.comboFiltre.currentIndexChanged.connect(self.actualiser_liste)
        self.ui.comboTri.currentIndexChanged.connect(self.actualiser_liste)

        # Initial population
        self.actualiser_liste()

    def actualiser_liste(self):
        """Charge et affiche les tâches dans la liste avec filtrage et tri."""
        self.ui.listeTaches.clear()
        tasks = self.controller.lister_taches()
        
        # Appliquer le filtre
        filtre_index = self.ui.comboFiltre.currentIndex()
        if filtre_index == 1:
            tasks = [t for t in tasks if t.etat.name == 'A_FAIRE']
        elif filtre_index == 2:
            tasks = [t for t in tasks if t.etat.name == 'EN_COURS']
        elif filtre_index == 3:
            tasks = [t for t in tasks if t.etat.name == 'REALISE']
        elif filtre_index == 4:
            tasks = [t for t in tasks if t.etat.name == 'ABANDONNE']
        elif filtre_index == 5:
            tasks = [t for t in tasks if t.etat.name == 'EN_ATTENTE']
        # Si index == 0 -> on garde toutes les tâches
        
        # Appliquer le tri
        from datetime import datetime
        tri_index = self.ui.comboTri.currentIndex()
        if tri_index == 0:
            tasks.sort(key=lambda t: t.titre.lower())
        elif tri_index == 1:
            tasks.sort(key=lambda t: (t.date_debut is None, t.date_debut if t.date_debut else datetime.max))
        elif tri_index == 2:
            tasks.sort(key=lambda t: (t.date_fin is None, t.date_fin if t.date_fin else datetime.max))
        elif tri_index == 3:
            tasks.sort(key=lambda t: t.etat.value)
        
        # Mapping emojis par état
        emojis_etat = {
            'A_FAIRE': '📝',
            'EN_COURS': '⏳',
            'REALISE': '✅',
            'ABANDONNE': '❌',
            'EN_ATTENTE': '⏸️'
        }
        
        for t in tasks:
            # On récupère l'emoji correspondant à l'état
            emoji = emojis_etat.get(t.etat.name, '📋')
            
            dates_info = []
            if t.date_debut:
                dates_info.append(f"Début: {t.date_debut.strftime('%d/%m/%Y')}")
            if t.date_fin:
                dates_info.append(f"Échéance: {t.date_fin.strftime('%d/%m/%Y')}")
            
            if dates_info:
                dates_str = "  •  ".join(dates_info)
                item_text = f"{emoji} {t.titre}  •  {t.etat.value}  •  {dates_str}"
            else:
                item_text = f"{emoji} {t.titre}  •  {t.etat.value}"
            
            self.ui.listeTaches.addItem(item_text)

    def get_selected_task(self):
        current = self.ui.listeTaches.currentItem()
        if not current:
            return None
        # Extraire le titre (sans l'emoji)
        text = current.text()
        # Supprimer l'emoji (premier caractère + espace)
        if text and len(text) > 2:
            text = text[2:].strip()
            if '•' in text:
                title = text.split('•')[0].strip()
            else:
                title = text.strip()
            
            # Chercher la tâche correspondante
            for t in self.controller.tasks:
                if t.titre == title:
                    return t
        return None

    def ouvrir_creation_tache(self):
        dialog = DialogCreationTache(self)
        if dialog.exec():
            data = dialog.get_data()
            try:
                self.controller.creer_tache(
                    titre=data.get('titre'),
                    description=data.get('description',''),
                    date_debut=data.get('date_debut'),
                    date_fin=data.get('date_fin'),
                    etat=data.get('etat')
                )
                self.actualiser_liste()
            except Exception as e:
                QMessageBox.critical(self, "Erreur", str(e))

    def ouvrir_edition_tache(self):
        task = self.get_selected_task()
        if not task:
            return
        dialog = DialogEditionTache(task, self)
        if dialog.exec():
            data = dialog.get_data()
            try:
                self.controller.modifier_tache(
                    task_id=task.id,
                    titre=data.get('titre'),
                    description=data.get('description'),
                    date_debut=data.get('date_debut'),
                    date_fin=data.get('date_fin'),
                    etat=data.get('etat')
                )
                self.actualiser_liste()
            except Exception as e:
                QMessageBox.critical(self, "Erreur", str(e))

    def ouvrir_detail_tache(self):
        task = self.get_selected_task()
        if not task:
            return
        dialog = DialogDetailTache(task, self.controller, self)
        dialog.exec()
        self.actualiser_liste()

    def ouvrir_cloturer_tache(self):
        task = self.get_selected_task()
        if not task:
            return
        self.controller.cloturer_tache(task.id)
        self.actualiser_liste()

    def ouvrir_supprimer_tache(self):
        task = self.get_selected_task()
        if not task:
            return
        confirm = QMessageBox.question(self, "Confirmer", f"Supprimer la tâche '{task.titre}' ?")
        if confirm == QMessageBox.StandardButton.Yes:
            self.controller.supprimer_tache(task.id)
            self.actualiser_liste()


