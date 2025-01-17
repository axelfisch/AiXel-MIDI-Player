# AiXel
A Python MIDI library that uses my custom jazz chord dictionary to generate .mid files.  Built for the Aixel-Jazzorchestrator to produce sophisticated chord progressions in the  unique Axel Fisch style (e.g., Bbmaj7 - A-11 - D13b9 - Ebmaj7(#11)).
# AiXel

**AiXel** est une librairie Python qui utilise un dictionnaire d'accords jazz personnalisé pour générer des fichiers `.mid`.  
Elle est conçue pour **Aixel-Jazzorchestrator**, le chatbot qui compose déjà des grilles d’accords sophistiquées dans le style unique **Axel Fisch** (ex. **Bbmaj7 - A-11 - D13b9 - Ebmaj7(#11)**).  

## Fonctionnalités
- Conversion de noms d’accords (ex. `"Cmaj7"`) en numéros MIDI via un dictionnaire jazz complet.  
- Génération de `.mid` à partir de progressions d’accords personnalisées.  
- Support de nombreuses tonalités et enrichissement d’accords (9, 11, 13, etc.).  

## Installation
Pour utiliser AiXel en local :
```bash
# Clone le dépôt
git clone https://github.com/axelfisch/AiXel.git
cd AiXel

# Installe les dépendances (si fichier requirements.txt)
pip install -r requirements.txt

# Ou bien, si tu préfères un setup.py, exécute
pip install .
