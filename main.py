import os

#LUYI LAI

def cut(nom_photo, increment):
    string = nom_photo
    couper = string[increment:]
    return couper


def split_ext(image):
    nom, ext = os.path.splitext(image)
    return nom, ext


def incrementation_photo():
    saisie = int(input("veuillez entrer l'incrementation\n"))
    format = "{:03d}".format(saisie)
    return format

def saisie():
    texte = input("veuillez entrer un texte suivant l'incrémentation\n")
    incrementation_decoupage = int(input("à partir de combien de caractère voulez vous conservez le texte original, 0 pour ne rien changer\n"))
    return texte, incrementation_decoupage


def renommage(incrementation, texte, decoup, file_ext):
    new= '{}-{}-{}{}'.format(incrementation, texte, decoup, file_ext)
    os.rename("rename/"+photo, "rename/"+new)


for photo in os.listdir("rename"):
    print("nom original de la photo:")
    print(photo)
    filename, file_ext = split_ext(photo)
    incrementation = incrementation_photo()
    texte, decoupage = saisie()
    decoup = cut(filename, decoupage)
    renommage(incrementation, texte, decoup, file_ext)





