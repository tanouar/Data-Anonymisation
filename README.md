# Script de Anonymisation de fichier au format XML

Ce script Python permet d'anonymiser les données contenues dans un fichier XML en utilisant un fichier YAML pour spécifier les balises à modifier et les valeurs à générer.

## Utilisation

- `<xml_file>` : Le chemin vers le fichier XML à pseudonymiser.
- `<yaml_file>` : Le chemin vers le fichier YAML contenant les balises à modifier et les valeurs à générer.

Le script pseudonymisera les données spécifiées dans le fichier XML en utilisant les règles définies dans le fichier YAML. Une copie du fichier XML modifié sera créée avec un nom de fichier contenant l'horodatage.

Consultez le fichier balises.yaml pour obtenir plus d'informations sur la façon de spécifier les balises et les valeurs dans le fichier YAML.

## Prérequis

- python (version 3.6 ou supérieure)
- xml.etree.ElementTree
- yaml
- faker

Assurez-vous d'avoir les packages requis installés. Vous pouvez les installer en exécutant la commande suivante : `pip install -r requirements.txt`

## Exemple

Voici un exemple d'utilisation du script : `python xmlAnonymisation.py data4test.xml balises.yaml`
