# Contrôleur pour gérer les tâches
from datetime import datetime
from models.task import Task, EtatTache
from models.comment import Comment
from utils.database import Database


class TaskController:
    def __init__(self, database):
        self.database = database
        self.tasks = []
        self.charger_taches()
    
    # Charger les tâches depuis le fichier
    def charger_taches(self):
        self.tasks = self.database.load_tasks()

    # Sauvegarder les tâches dans le fichier
    def sauvegarder_taches(self):
        self.database.save_tasks(self.tasks)

    # Créer une nouvelle tâche
    def creer_tache(self, titre, description="", date_debut=None, date_fin=None, etat=EtatTache.A_FAIRE):
        # Vérifier que le titre n'est pas vide
        if not titre or not titre.strip():
            raise ValueError("Le titre est obligatoire")
        
        task = Task(
            titre=titre.strip(),
            description=description,
            date_debut=date_debut,
            date_fin=date_fin,
            etat=etat
        )
        
        self.tasks.append(task)
        self.sauvegarder_taches()
        return task
    
    # Trouver une tâche par son ID
    def lire_tache(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    # Modifier une tâche existante
    def modifier_tache(self, task_id, titre=None, description=None, date_debut=None, date_fin=None, etat=None):
        task = self.lire_tache(task_id)
        if not task:
            return False
        
        # Modifier seulement ce qui est fourni
        if titre:
            task.titre = titre.strip()
        if description is not None:
            task.description = description
        if date_debut is not None:
            task.date_debut = date_debut
        if date_fin is not None:
            task.date_fin = date_fin
        if etat is not None:
            task.etat = etat
        
        self.sauvegarder_taches()
        return True

    # Supprimer une tâche
    def supprimer_tache(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.sauvegarder_taches()
                return True
        return False

    # Clôturer une tâche (marquer comme terminée)
    def cloturer_tache(self, task_id):
        task = self.lire_tache(task_id)
        if not task:
            return False
        
        task.cloturer()
        self.sauvegarder_taches()
        return True
    
    # Récupérer toutes les tâches (avec filtre et tri optionnels)
    def lister_taches(self, filtre_etat=None, tri_par=None):
        tasks = self.tasks
        
        # Filtrer par état si demandé
        if filtre_etat:
            tasks = [t for t in tasks if t.etat == filtre_etat]
        
        # Trier si demandé
        if tri_par == "titre":
            tasks = sorted(tasks, key=lambda t: t.titre.lower())
        elif tri_par == "date_debut":
            tasks = sorted(tasks, key=lambda t: t.date_debut or datetime.min)
        elif tri_par == "date_fin":
            tasks = sorted(tasks, key=lambda t: t.date_fin or datetime.max)
        elif tri_par == "etat":
            tasks = sorted(tasks, key=lambda t: t.etat.value)
        
        return tasks
    
    # Ajouter un commentaire à une tâche
    def ajouter_commentaire(self, task_id, contenu):
        if not contenu or not contenu.strip():
            raise ValueError("Le commentaire est vide")
        
        task = self.lire_tache(task_id)
        if not task:
            return None
        
        comment = Comment(contenu=contenu.strip())
        task.ajouter_commentaire(comment)
        self.sauvegarder_taches()
        return comment
    
    # Supprimer un commentaire
    def supprimer_commentaire(self, task_id, comment_id):
        task = self.lire_tache(task_id)
        if not task:
            return False
        
        success = task.supprimer_commentaire(comment_id)
        if success:
            self.sauvegarder_taches()
        return success
