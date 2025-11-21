"""
Gestion de la persistance des données.

Cette classe abstraite permet de changer facilement le mode de stockage
(JSON, SQLite, etc.) sans modifier le reste du code.
"""

from abc import ABC, abstractmethod
from typing import List
import json
import os
from pathlib import Path


class Database(ABC):
    """Classe abstraite pour la persistance des données."""
    
    @abstractmethod
    def load_tasks(self) -> List['Task']:
        """Charge toutes les tâches."""
        pass
    
    @abstractmethod
    def save_tasks(self, tasks: List['Task']) -> bool:
        """Sauvegarde toutes les tâches."""
        pass


class JSONDatabase(Database):
    """
    Implémentation JSON de la persistance.
    
    Structure du fichier JSON :
    {
        "tasks": [
            {
                "id": "...",
                "titre": "...",
                ...
            }
        ]
    }
    """
    
    def __init__(self, filepath: str = "data/tasks.json"):
        """
        Initialise la base de données JSON.
        
        Args:
            filepath: Chemin vers le fichier JSON
        """
        self.filepath = filepath
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Crée le fichier et les dossiers s'ils n'existent pas."""
        path = Path(self.filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        if not path.exists():
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump({"tasks": []}, f, ensure_ascii=False, indent=2)
    
    def load_tasks(self) -> List['Task']:
        """
        Charge les tâches depuis le fichier JSON.
        
        Returns:
            Liste des tâches
        """
        from models.task import Task
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Erreur lors du chargement : {e}")
            return []
    
    def save_tasks(self, tasks: List['Task']) -> bool:
        """
        Sauvegarde les tâches dans le fichier JSON.
        
        Args:
            tasks: Liste des tâches à sauvegarder
            
        Returns:
            True si la sauvegarde a réussi, False sinon
        """
        try:
            data = {
                "tasks": [task.to_dict() for task in tasks]
            }
            
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")
            return False


# TODO: Implémentation SQLite (pour comparaison dans les explications)
class SQLiteDatabase(Database):
    """
    Implémentation SQLite de la persistance (à implémenter si souhaité).
    
    Avantages vs JSON :
    - Meilleure performance pour grandes quantités de données
    - Requêtes SQL plus puissantes (filtres, joins, etc.)
    - Gestion native des transactions
    
    Inconvénients vs JSON :
    - Plus complexe à mettre en place
    - Moins lisible pour un humain
    - Nécessite une bibliothèque (sqlite3)
    """
    
    def __init__(self, filepath: str = "data/tasks.db"):
        self.filepath = filepath
        # TODO: Implémenter la connexion et la création des tables
        raise NotImplementedError("SQLite non encore implémenté")
    
    def load_tasks(self) -> List['Task']:
        raise NotImplementedError("SQLite non encore implémenté")
    
    def save_tasks(self, tasks: List['Task']) -> bool:
        raise NotImplementedError("SQLite non encore implémenté")
