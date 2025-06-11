# Gestion des Courriers – Gouvernorat du Sud-Kivu

Application web open source pour la gestion numérique des courriers entrants et sortants du Gouvernorat du Sud-Kivu.

## Structure

- **backend/** : API Django REST (gestion courriers, utilisateurs, pièces jointes)
- **frontend/** : Interface React (tableau de bord et gestion courriers)
- **README.md** : Ce fichier
- **.gitignore** : Fichiers/dossiers à ignorer par Git
- **LICENSE** : Licence MIT

## Démarrage rapide

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

Contributions bienvenues !
