# 1. Initialiser Git dans le projet
git init

# 2. Ajouter tous les fichiers dans le dépôt local
git add .

# 3. Créer un commit initial
git commit -m "Initial commit"

# 4. Ajouter le dépôt distant avec votre token GitHub (token masqué dans l'URL HTTPS)
git remote add origin https://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@github.com/USERNAME/REPO_NAME.git

# 5. Pousser le projet vers le dépôt distant sur la branche principale
git branch -M main
git push -u origin main
