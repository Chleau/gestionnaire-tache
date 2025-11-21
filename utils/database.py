#Gestion de la persistance des données.

from abc import ABC, abstractmethod
from typing import List
import json
import os
from pathlib import Path

#Classe abstraite pour la persistance des données
class Database(ABC):
    
    @abstractmethod
    #Charge toutes les tâches

    def load_tasks(self) -> List['Task']:
        pass
    
    @abstractmethod
    #Sauvegarde toutes les tâches
    def save_tasks(self, tasks: List['Task']) -> bool:
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
    
    #Initialise la base de données JSON
    def __init__(self, filepath: str = "data/tasks.json"):
        self.filepath = filepath
        self._ensure_file_exists()

    #Crée le fichier et les dossiers s'ils n'existent pas
    def _ensure_file_exists(self):
        path = Path(self.filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        if not path.exists():
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump({"tasks": []}, f, ensure_ascii=False, indent=2)
    
    #Charge les tâches depuis le fichier JSON
    def load_tasks(self) -> List['Task']:
        
        from models.task import Task
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Erreur lors du chargement : {e}")
            return []
    
    #Sauvegarde les tâches dans le fichier JSON
    def save_tasks(self, tasks: List['Task']) -> bool:
  
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


