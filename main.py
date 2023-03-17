import produits as Prod
from tkinter import *
from tkinter import ttk

Produit = Prod.Produits()


def add_item():
    def item_creator(nom, desc, prix, quantite, id_cat):
        Produit.create_item(nom, desc, prix, quantite, id_cat)

    add_window = Toplevel()
    add_window.title("Ajouter un article")
    add_window.resizable(False, False)

    nom_add = StringVar()
    desc_add = StringVar()
    prix_add = StringVar()
    quantite_add = StringVar()
    categorie_id = StringVar()

    add = ttk.Frame(add_window, borderwidth=2, relief="ridge", padding="10 10 5 5")
    add.grid(column=0, row=0)
    add.columnconfigure(0, weight=1)
    add.rowconfigure(0, weight=1)

    ttk.Label(add, text="Nom").grid(column=0, row=0)
    ttk.Entry(add, textvariable=nom_add, width=20).grid(column=0, row=1)
    ttk.Label(add, text="Description").grid(column=1, row=0)
    ttk.Entry(add, textvariable=desc_add, width=20).grid(column=1, row=1)
    ttk.Label(add, text="Prix").grid(column=2, row=0)
    ttk.Entry(add, textvariable=prix_add, width=20).grid(column=2, row=1)
    ttk.Label(add, text="Quantité").grid(column=3, row=0)
    ttk.Entry(add, textvariable=quantite_add, width=20).grid(column=3, row=1)
    ttk.Label(add, text="Catégorie").grid(column=4, row=0)
    ttk.Entry(add, textvariable=categorie_id, width=20).grid(column=4, row=1)

    ttk.Button(add, text='Ajouter article',
               command=lambda: item_creator(nom_add.get(), desc_add.get(), prix_add.get(), quantite_add.get(),
                                            categorie_id.get())).grid(
        column=3, row=2)

def modify_item():

    def second_window(name):
        def item_modifier(nom, desc, prix, quantite, id_cat):
            Produit.create_item(nom, desc, prix, quantite, id_cat)
        modify_item = Toplevel()
        modify_item.title("Modifier un article")
        modify_item.resizable(False, False)
        nom_modif = StringVar()
        desc_modif = StringVar()
        prix_modif = StringVar()
        quantite_modif = StringVar()
        categorie_id_modif = StringVar()
        add = ttk.Frame(modify_item, borderwidth=2, relief="ridge", padding="10 10 5 5")
        add.grid(column=0, row=0)
        add.columnconfigure(0, weight=1)
        add.rowconfigure(0, weight=1)

        ttk.Label(add, text="Nom").grid(column=0, row=0)
        ttk.Entry(add, textvariable=nom_modif, width=20).grid(column=0, row=1)
        ttk.Label(add, text="Description").grid(column=1, row=0)
        ttk.Entry(add, textvariable=desc_modif, width=20).grid(column=1, row=1)
        ttk.Label(add, text="Prix").grid(column=2, row=0)
        ttk.Entry(add, textvariable=prix_modif, width=20).grid(column=2, row=1)
        ttk.Label(add, text="Quantité").grid(column=3, row=0)
        ttk.Entry(add, textvariable=quantite_modif, width=20).grid(column=3, row=1)
        ttk.Label(add, text="Catégorie").grid(column=4, row=0)
        ttk.Entry(add, textvariable=categorie_id_modif, width=20).grid(column=4, row=1)

        ttk.Button(add, text='Ajouter article',
                   command=lambda: item_modifier(nom_modif.get(), desc_add.get(), prix_add.get(), quantite_add.get(),
                                                categorie_id.get())).grid(
            column=3, row=2)

    get_name = Toplevel()
    get_name.title("Ajouter un article")
    get_name.resizable(False, False)
    ttk.Label(get_name, text="Veuillez entrer le nom de l'article").grid(column=0, row=0)

    listarticles = Produit.get_names()
    listarticlesredux = []
    for item in listarticles:
        listarticlesredux.append(item[0])


    nameVariableCombobox = StringVar()
    ComboBoxNames = ttk.Combobox(get_name, textvariable=nameVariableCombobox, width=17)
    ComboBoxNames.state(["readonly"])
    ComboBoxNames['values'] = listarticlesredux
    ComboBoxNames.grid(column=1, row=1)
    ComboBoxNames.set(listarticlesredux[0])

    namebutton=ttk.Button(get_name, text="Ajouter Article", command=lambda:second_window(nameVariableCombobox.get())).grid(column=2, row=1)




#def get_item_to_modify():

def get_stock():
    produits = Produit.get_Infos()
    id_string = ""
    nom_string = ""
    description_string = ""
    prix_string = ""
    quantite_string = ""
    categorie_id_string = ""
    for produit in produits:
        id_string += (str(produit[0]) + "\n")
        nom_string += produit[1] + "\n"
        description_string += produit[2] + "\n"
        prix_string += (str(produit[3]) + "\n")
        quantite_string += (str(produit[4]) + "\n")
        categorie_id_string += (str(produit[7]) + "\n")
    idDisplay.set(id_string)
    nom.set(nom_string)
    description.set(description_string)
    prix.set(prix_string)
    quantite.set(quantite_string)
    categorie.set(categorie_id_string)


main = Tk()

main.title("Stock")
main.resizable(False, False)
mainwindows = ttk.Frame(main, borderwidth=2, relief="ridge", padding="10 10 5 5")
mainwindows.grid(column=0, row=0)
mainwindows.columnconfigure(0, weight=1)
mainwindows.rowconfigure(0, weight=1)

list = ttk.Frame(mainwindows, borderwidth=2)
list.grid(column=0, row=0)
list.columnconfigure(0, weight=1)
list.rowconfigure(0, weight=1)

buttons = ttk.Frame(mainwindows, borderwidth=2, padding="10 10 5 5")
buttons.grid(column=0, row=1)
buttons.columnconfigure(0, weight=1)
buttons.rowconfigure(0, weight=1)
idDisplay = StringVar()
nom = StringVar()
description = StringVar()
prix = StringVar()
quantite = StringVar()
categorie = StringVar()
get_stock()
ttk.Label(list, text="ID", padding="10").grid(column=0, row=0)
ttk.Label(list, text="Nom", padding="10").grid(column=1, row=0)
ttk.Label(list, text="Description", padding="10").grid(column=2, row=0)
ttk.Label(list, text="Prix", padding="10").grid(column=3, row=0)
ttk.Label(list, text="Quantité", padding="10").grid(column=4, row=0)
ttk.Label(list, text="Catégorie", padding="10").grid(column=5, row=0)
ttk.Button(buttons, text="Ajouter Article", command=lambda: add_item()).grid(column=0, row=0)
ttk.Button(buttons, text='Modifier article', command=lambda: modify_item()).grid(column=1, row=0)
ttk.Button(buttons, text='Supprimer article').grid(column=2, row=0)
ttk.Button(buttons, text='Actualiser la liste', command=lambda: get_stock()).grid(column=3, row=0)
ttk.Label(list, textvariable=idDisplay, padding="10").grid(column=0, row=1)
ttk.Label(list, textvariable=nom, padding="10").grid(column=1, row=1)
ttk.Label(list, textvariable=description, padding="10").grid(column=2, row=1)
ttk.Label(list, textvariable=prix, padding="10").grid(column=3, row=1)
ttk.Label(list, textvariable=quantite, padding="10").grid(column=4, row=1)
ttk.Label(list, textvariable=categorie, padding="10").grid(column=5, row=1)


main.mainloop()
