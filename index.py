import os
import pathlib as pt
import yaml as yml
#import PySimpleGUI as sg
from hashlib import sha256

Menu = input("voulez vous entrez un nouveau mot de passe [N] ou en chercher un déjà existant [L] ?: ")

PATH = pt.Path("C:/Users/Documents/Project/Password_manager/Manager/src/manager/key/key.yml")

def New_password():
    appName = input("entrez le nom de l'application à sauvegarder le mot de passe: ")
    password = input("entrez le mot de passe à sauvegarder: ")

    parser = [{appName: password}]

    with open(PATH, 'a') as file:
        yml.dump_all(parser, file)


def Retrieve_password():
    pass


if Menu == "N" | "L":
    if Menu == "N":
        New_password()
    elif Menu == "L":
        Retrieve_password()
else:
    print("vous n'avez le choix qu'entre N ou L")
    quit
