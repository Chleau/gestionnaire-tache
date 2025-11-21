# Modèle pour les tâches
from enum import Enum
from datetime import datetime
import uuid


# États possibles pour une tâche
class EtatTache(Enum):
    A_FAIRE = "À faire"
    EN_COURS = "En cours"
    REALISE = "Réalisé"
    ABANDONNE = "Abandonné"
    EN_ATTENTE = "En attente"


class Task:
    def __init__(self, titre, description="", date_debut=None, date_fin=None, 
                 etat=EtatTache.A_FAIRE, task_id=None):
        self.id = task_id if task_id else str(uuid.uuid4())
        self.titre = titre
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.etat = etat
        self.commentaires = []
    
    # Convertir en dictionnaire pour sauvegarder en JSON
    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "description": self.description,
            "date_debut": self.date_debut.isoformat() if self.date_debut else None,
            "date_fin": self.date_fin.isoformat() if self.date_fin else None,
            "etat": self.etat.value,
            "commentaires": [c.to_dict() for c in self.commentaires]
        }
    
    # Créer une tâche depuis un dictionnaire
    @classmethod
    def from_dict(cls, data):
        from models.comment import Comment
        
        task = cls(
            titre=data["titre"],
            description=data.get("description", ""),
            date_debut=datetime.fromisoformat(data["date_debut"]) if data.get("date_debut") else None,
            date_fin=datetime.fromisoformat(data["date_fin"]) if data.get("date_fin") else None,
            etat=EtatTache(data["etat"]),
            task_id=data["id"]
        )
        
        # Charger les commentaires
        for c in data.get("commentaires", []):
            task.commentaires.append(Comment.from_dict(c))
        
        return task
    
    # Marquer la tâche comme terminée
    def cloturer(self):
        self.etat = EtatTache.REALISE
        if not self.date_fin:
            self.date_fin = datetime.now()
    
    # Ajouter un commentaire
    def ajouter_commentaire(self, commentaire):
        self.commentaires.append(commentaire)
    
    # Supprimer un commentaire
    def supprimer_commentaire(self, commentaire_id):
        for i, comment in enumerate(self.commentaires):
            if comment.id == commentaire_id:
                del self.commentaires[i]
                return True
        return False
