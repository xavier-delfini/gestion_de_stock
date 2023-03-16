# Importation de librairies
from tkinter import *
from tkinter import ttk

#Garder
def convert(amount, devise_1, devise_2):
    amount = verif_entry(amount)
    if amount != "ERROR":
        devise_1 = get_change_rate(devise_1)
        devise_2 = get_change_rate(devise_2)
        if devise_1[0] == "Euro" or devise_2[0] == "Euro":
            if devise_1[0] == "Euro":
                result = amount * devise_2[1]

            else:
                result = amount / devise_1[1]

        else:
            result = (amount * devise_2[1]) / devise_1[1]
        history(amount, result, devise_1, devise_2)
        # On supprime les decimal a partir des millièmes car non utile dans notre cas
        # Utilisation de format qui permet de ne pas arrondir et donc permet d'avoir la valeur arrondi inférieur et non supérieur
        print_result.set(format(result, '.2f'))
    else:
        return ("Une erreur est survenue")


def show_window():
    def insert(name, value):
        import json

        value=verif_entry(value)
        if value== "ERROR":
            message.set("La devise n'a pas pu être ajouter, veuillez vérifier votre entrée et recommencer")
            return 0
        current_list = fetch_array()
        for x in current_list:
            if x[0] == name:
                message.set("Cette devise existe déjà")
                return 0
        insert_array = [[name, value]]
        current_list.extend(insert_array)
        f = open("devises.json", "w")
        json_value = json.dumps(current_list)
        f.write(json_value)
        f.close()
        init_combo['values'] = get_combo_array()
        final_combo['values'] = get_combo_array()
        message.set("La devise a bien été ajouter")

    #Définiton de la seconde fenêtre n'apparaissant qu'avec le bouton Ajout devise
    sub = Toplevel()
    sub.title("Ajouter une devise")
    sub.resizable(False, False)

    devise_name = StringVar()
    euro_equal_to_devise = StringVar()
    message=StringVar()

    add = ttk.Frame(sub, borderwidth=2, relief="ridge", padding="10 10 5 5")
    add.grid(column=0, row=0)
    add.columnconfigure(0, weight=1)
    add.rowconfigure(0, weight=1)

    ttk.Label(add, text="Nom de la devise:").grid(column=0, row=0,sticky=("E"))
    ttk.Entry(add, textvariable=devise_name, width=20).grid(column=1, row=0)
    ttk.Label(add, text="Valeur de cette devise pour un euro:").grid(column=0, row=1,sticky=("E"))
    ttk.Entry(add, textvariable=euro_equal_to_devise, width=20).grid(column=1, row=1)
    ttk.Button(add, text='Ajouter devise', command=lambda: insert(devise_name.get(),euro_equal_to_devise.get())).grid(column=1, row=2)
    ttk.Label(add, textvariable=message).grid(column=0,row=3)

# Début de l'affichage
main = Tk()
main.title("Convertisseur de devises")
main.resizable(False, False)
conv = ttk.Frame(main, borderwidth=2, relief="ridge", padding="10 10 5 5")
conv.grid(column=0, row=0)
conv.columnconfigure(0, weight=1)
conv.rowconfigure(0, weight=1)

initial_devise = StringVar()
init_combo = ttk.Combobox(conv, textvariable=initial_devise, width=17)
init_combo.state(["readonly"])
init_combo['values'] = get_combo_array()
init_combo.grid(column=1, row=1)
init_combo.set(get_combo_array()[0])

final_devise = StringVar()
final_combo = ttk.Combobox(conv, textvariable=final_devise, width=17)
final_combo.state(["readonly"])
final_combo['values'] = get_combo_array()
final_combo.grid(column=1, row=2)
final_combo.set(get_combo_array()[1])

print_result = StringVar()
amount_enter = StringVar()

ttk.Label(conv, text="Quantité:", padding="10").grid(column=0, row=0)
ttk.Label(conv, text="De:", padding="10").grid(column=0, row=1)
ttk.Label(conv, text="à:", padding="10").grid(column=0, row=2)
ttk.Entry(conv, textvariable=amount_enter, width=20).grid(column=1, row=0)
ttk.Button(conv, text='Convertir',command=lambda: convert(amount_enter.get(), initial_devise.get(), final_devise.get())).grid(column=1, row=3)
ttk.Button(conv, text='Ajouter devise', command=lambda: show_window()).grid(column=1, row=5)
ttk.Label(conv, textvariable=print_result, padding="10").grid(column=1, row=4)
main.mainloop()