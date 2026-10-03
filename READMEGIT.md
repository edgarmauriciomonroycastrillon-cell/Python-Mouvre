Comando de git 

git config --global user.name "..."            # Colocar mi nombre en los commits

git config --global user.email "..."           # Colocar mi nombre en los commits

git config --list                              # Ver configuracion 



git init                                        # Crea un repo local

git remote add origin <url>                     # Crea un repo en github

git clone <url>                                 # Decarga un repo de github a local

git status                                      # Muestra que cambio

git add archivo.py                              # Prepara UN archivo para el commit 

git add .                                      # Prepara todos los archivos cambiados 

git commit -m "mensaje"                        # Hace una foto de los cambios con un mensaje

git log --oneline                              # Muestra el historial de commits Y EL ID

git diff                                       # Muestra que lineas cambiaron

git branch                                     # Lista las ramas , la actual tiene *

git switch -c nombre                           # Crea un rama y se cambia a ella

git switch nombre                              # Se cambia a una rama que ya existe

git merge nombre                               # Trae los cambios de esa rama a la rama donde esta

git branch -d nombre                           # Elimina esa rama

git push                                       # Envia los cambios a github

git revert <id>                                # Revierte el commit


git config --global push.autoSetupRemote true  # Crear un rama en github NO SOLO EN LOCAL



git ignores , para que no se suban archivos al repo de github



1. Se crea archivo junto al README.md llamado gitignore 

2. y se escriben los archivos a ignorar 


# Archivos que genera Python
__pycache__/
*.pyc

# Configuración del editor
.vscode/

# Entorno virtual
venv/

# Contraseñas y claves
.env