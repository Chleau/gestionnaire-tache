# Modèle pour les commentaires
from datetime import datetime
import uuid


class Comment:
    def __init__(self, contenu, id=None, date_creation=None):
        self.id = id if id else str(uuid.uuid4())
        self.contenu = contenu
        # Si pas de date, on prend maintenant
        self.date_creation = date_creation if date_creation else datetime.now()
    
    # Convertir en dictionnaire
    def to_dict(self):
        return {
            "id": self.id,
            "contenu": self.contenu,
            "date_creation": self.date_creation.isoformat()
        }
    
    # Créer depuis un dictionnaire
    @classmethod
    def from_dict(cls, data):
        return cls(
            contenu=data["contenu"],
            id=data["id"],
            date_creation=datetime.fromisoformat(data["date_creation"])
        )
