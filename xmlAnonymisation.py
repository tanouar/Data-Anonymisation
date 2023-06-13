#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:09:42 2023

@author: kawne
"""

import sys
import xml.etree.ElementTree as ET
import yaml
from datetime import datetime
from faker import Faker

def randomize_text(text, faker):
    if text.startswith('faker.'):
        faker_method = getattr(faker, text.split('faker.')[1])
        return faker_method()
    else:
        return text

def anonymize_xml(xml_file, yaml_file):
    # Charger le fichier YAML contenant les balises à anonymiser et les textes à générer
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)

    # Charger le fichier XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialiser Faker
    faker = Faker()

    # Parcourir les éléments du fichier XML
    for element in root.iter():
        # Vérifier si l'élément doit être anonymisé
        if element.tag in yaml_data:
            text = yaml_data[element.tag]  # Récupérer le texte à générer depuis le fichier YAML
            element.text = randomize_text(text, faker)  # Générer la valeur aléatoire avec Faker

    # Créer un nom de fichier avec l'horodatage
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"anonymized_{timestamp}.xml"

    # Enregistrer les modifications dans le fichier XML
    tree.write(output_file, encoding="utf-8", xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <xml_file> <yaml_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    yaml_file = sys.argv[2]

    anonymize_xml(xml_file, yaml_file)