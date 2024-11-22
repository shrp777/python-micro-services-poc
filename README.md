# Architecture à base de micro services Python

🚨🚨🚨 Preuve de concept (work in progress) 🚨🚨🚨

TODO:

- les services Python ne sont pas connectés à leur base de données respective
- le service auth n'est pas implémenté (signin, signup, signout, verify token...)
- le service gateway n'est pas implémenté
- l'API REST du service tasks est fictive (données statiques / pas de connexion à la BDD)
- les services Python et BDD sont accessibles depuis l'extérieur du réseau : ils ne devraient pas l'être. Seul le service gateway devrait être accessible depuis l'extérieur
- le dossier flask-service contient un service modèle réalisé avec Flask qui peut être utilisé à la place de FastAPI

## Instructions pour l'installation (avant le lancement des services Docker)

- créer les fichiers .txt dans le dossier ./db en se basant sur les fichiers .example.txt
- chaque fichier doit être nommé sans la mention "example", auth-db-password.example.txt devient auth-db-password.txt

## Lancement des services Docker

### Sans reconstruction des images Docker

```sh
docker compose up
```

### Sans reconstruction des images Docker + activation du mode watch (permet de reconstruire en live les containers en cas de modification du code source)

```sh
docker compose up --watch
```

### Avec reconstruction des images Docker au lancement (si modification du code source associé)

```sh
docker compose up --build
```

### Avec reconstruction des images Docker au lancement (si modification du code source associé) + activation du mode watch (permet de reconstruire en live les containers en cas de modification du code source)

```sh
docker compose up --build --watch
```

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
