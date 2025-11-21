from PySide6.QtWidgets import QApplication
import sys

from controllers.task_controller import TaskController
from utils.database import JSONDatabase
from views.main_window import MainWindow
from pathlib import Path


"Lancement de l'application de gestion des tâches"
def main():
    database = JSONDatabase("data/tasks.json")
    controller = TaskController(database)

    app = QApplication(sys.argv)

    # Appliquer le style QSS (méthode simple)
    qss_path = Path("styles/style.qss")
    if qss_path.exists():
        app.setStyleSheet(qss_path.read_text(encoding="utf-8"))
    else:
        print(f"⚠️ Fichier de style introuvable : {qss_path}")

    window = MainWindow(controller)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
