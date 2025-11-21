from PySide6.QtWidgets import (
    QDialog,
    QListWidgetItem,
    QMessageBox,
    QWidget,
    QFrame,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
)
from PySide6.QtCore import Qt
from views.generated.ui_dialog_detail_tache import Ui_DialogDetailTache

"Dialogue d'affichage des détails d'une tâche"
class DialogDetailTache(QDialog):
    
    def __init__(self, task, controller=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogDetailTache()
        self.ui.setupUi(self)
        self.task = task
        self.controller = controller
        self._populate_fields()
        # Connecter les actions des boutons
        if hasattr(self.ui, 'btnAjouterCommentaire'):
            self.ui.btnAjouterCommentaire.clicked.connect(self._on_ajouter_commentaire)
        if hasattr(self.ui, 'btnSupprimerCommentaire'):
            self.ui.btnSupprimerCommentaire.clicked.connect(self._on_supprimer_commentaire)
        if hasattr(self.ui, 'btnCloturer'):
            self.ui.btnCloturer.clicked.connect(self._on_cloturer_tache)
        if hasattr(self.ui, 'btnFermer'):
            self.ui.btnFermer.clicked.connect(self.close)
        
    "Remplit les champs avec les données de la tâche"
    def _populate_fields(self):
        # Titre
        self.ui.titleLabel.setText(self.task.titre)
        
        # État
        self.ui.label_etat.setText(str(self.task.etat.value))
        
        # Date de début
        if self.task.date_debut:
            date_debut = self.task.date_debut.strftime("%d/%m/%Y %H:%M")
            self.ui.label_date_debut.setText(date_debut)
        else:
            self.ui.label_date_debut.setText("Non définie")
        
        # Date de fin
        if self.task.date_fin:
            date_fin = self.task.date_fin.strftime("%d/%m/%Y %H:%M")
            self.ui.label_date_fin.setText(date_fin)
        else:
            self.ui.label_date_fin.setText("Non définie")
        
        # Afficher les commentaires dans la liste (avec stockage de l'ID dans l'item)
        if hasattr(self.ui, 'liste_commentaires'):
            self.ui.liste_commentaires.clear()
            for comment in self.task.commentaires:
                date_str = comment.date_creation.strftime("%d/%m/%Y %H:%M")
                text = f"[{date_str}] {comment.contenu}"
                comment_id = getattr(comment, 'id', None)
                # créer un widget personnalisé pour chaque commentaire
                item = QListWidgetItem()
                widget = self._create_comment_widget(text, comment_id)
                # Définir une taille minimale pour l'item avec plus de hauteur
                from PySide6.QtCore import QSize
                item.setSizeHint(QSize(500, 80))
                # stocker l'id aussi dans l'item pour compatibilité
                item.setData(Qt.UserRole, comment_id)
                self.ui.liste_commentaires.addItem(item)
                self.ui.liste_commentaires.setItemWidget(item, widget)

    "Crée un QWidget contenant le texte du commentaire et des boutons d'action qui apparaissent au survol"
    def _create_comment_widget(self, text: str, comment_id: str) -> QWidget:
        container = QFrame()
        container.setObjectName("commentSection")
        container.setMinimumHeight(60)
        layout = QHBoxLayout(container)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(10)

        label = QLabel(text)
        label.setWordWrap(True)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        # Forcer la couleur du texte à noir
        label.setStyleSheet("QLabel { color: #12313a; background-color: transparent; }")

        btn_delete = QPushButton("🗑️")
        btn_delete.setToolTip("Supprimer ce commentaire")
        btn_delete.setCursor(Qt.PointingHandCursor)
        btn_delete.setFixedSize(30, 30)
        btn_delete.setVisible(False)  # caché par défaut

        # Connecter le clic du bouton au handler de suppression (capturer l'id)
        btn_delete.clicked.connect(lambda _, cid=comment_id: self._delete_comment_by_id(cid))

        layout.addWidget(label)
        layout.addWidget(btn_delete)

        # montrer/cacher le bouton au survol du container via événements
        def enter_event(e):
            btn_delete.setVisible(True)
            return QWidget.enterEvent(container, e)

        def leave_event(e):
            btn_delete.setVisible(False)
            return QWidget.leaveEvent(container, e)

        # Patcher les méthodes d'événement du widget container
        container.enterEvent = enter_event
        container.leaveEvent = leave_event

        return container

    "Rafraîchit l'affichage de la liste des commentaires depuis la tâche"
    def _refresh_comments(self):
        if hasattr(self.ui, 'liste_commentaires'):
            self.ui.liste_commentaires.clear()
            for comment in self.task.commentaires:
                date_str = comment.date_creation.strftime("%d/%m/%Y %H:%M")
                text = f"[{date_str}] {comment.contenu}"
                comment_id = getattr(comment, 'id', None)
                item = QListWidgetItem()
                widget = self._create_comment_widget(text, comment_id)
                # Définir une taille minimale pour l'item avec plus de hauteur
                from PySide6.QtCore import QSize
                item.setSizeHint(QSize(500, 80))
                item.setData(Qt.UserRole, comment_id)
                self.ui.liste_commentaires.addItem(item)
                self.ui.liste_commentaires.setItemWidget(item, widget)

    "Supprime le commentaire identifié par `comment_id` puis rafraîchit la vue"
    def _delete_comment_by_id(self, comment_id: str):
        if not comment_id:
            return
        try:
            if self.controller:
                self.controller.supprimer_commentaire(self.task.id, comment_id)
                updated = self.controller.lire_tache(self.task.id)
                if updated:
                    self.task = updated
            else:
                self.task.supprimer_commentaire(comment_id)
            self._refresh_comments()
        except Exception as e:
            print(f"Erreur lors de la suppression du commentaire: {e}")

    "Handler pour ajouter un commentaire via le controller si présent"
    def _on_ajouter_commentaire(self):
        if not hasattr(self.ui, 'text_nouveau_commentaire'):
            return
        contenu = self.ui.text_nouveau_commentaire.toPlainText().strip()
        if not contenu:
            return
        try:
            if self.controller:
                # utilise le controller pour sauvegarder
                self.controller.ajouter_commentaire(self.task.id, contenu)
                # recharger la tâche depuis le controller si disponible
                updated = self.controller.lire_tache(self.task.id)
                if updated:
                    self.task = updated
            else:
                # fallback local si pas de controller
                from models.comment import Comment
                comment = Comment(contenu=contenu)
                self.task.ajouter_commentaire(comment)
            # vider le champ et rafraîchir
            self.ui.text_nouveau_commentaire.clear()
            self._refresh_comments()
        except Exception as e:
            print(f"Erreur lors de l'ajout du commentaire: {e}")

    "Handler pour supprimer le commentaire sélectionné"
    def _on_supprimer_commentaire(self):
        if not hasattr(self.ui, 'liste_commentaires'):
            return
        current_item = self.ui.liste_commentaires.currentItem()
        if not current_item:
            return
        comment_id = current_item.data(Qt.UserRole)
        if not comment_id:
            return
        try:
            if self.controller:
                self.controller.supprimer_commentaire(self.task.id, comment_id)
                updated = self.controller.lire_tache(self.task.id)
                if updated:
                    self.task = updated
            else:
                self.task.supprimer_commentaire(comment_id)
            self._refresh_comments()
        except Exception as e:
            print(f"Erreur lors de la suppression du commentaire: {e}")

    "Clôturer la tâche via le controller et mettre à jour l'affichage"
    def _on_cloturer_tache(self):
        try:
            if self.controller:
                self.controller.cloturer_tache(self.task.id)
                updated = self.controller.lire_tache(self.task.id)
                if updated:
                    self.task = updated
            else:
                self.task.cloturer()
            # mettre à jour l'étiquette d'état
            if hasattr(self.ui, 'label_etat'):
                self.ui.label_etat.setText(str(self.task.etat.value))
            # feedback visuel et désactiver le bouton pour éviter double clic
            try:
                QMessageBox.information(self, "Tâche clôturée", "La tâche a été clôturée avec succès.")
            except Exception:
                # en environnements headless, QMessageBox peut échouer ; ignorez
                print("Tâche clôturée avec succès.")
            if hasattr(self.ui, 'btnCloturer'):
                try:
                    self.ui.btnCloturer.setEnabled(False)
                except Exception:
                    pass
        except Exception as e:
            print(f"Erreur lors de la clôture de la tâche: {e}")
