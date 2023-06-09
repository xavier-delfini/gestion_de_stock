import connexion as dbconnect


class Produits:
    def __init__(self, nom="", description="", prix="", quantite=-1, id_categorie=-1, id=-1):
        self.__id = id
        self.__nom = nom
        self.__description = description
        self.__prix = prix
        self.__quantite = quantite
        self.__id_categorie = id_categorie
        self.__cursor = dbconnect.db.cursor()

    def get_names(self):
        self.__cursor.execute("SELECT nom from boutique.produit;")
        return self.__cursor.fetchall()
    def selectQuery(self, query, values=""):
        if values == "":
            # Cas 1 :toute la table
            self.__cursor.execute(query)
            return self.__cursor.fetchall()
        elif type(values) is list:
            # Cas 2 :plusieurs items(Non utiliser)
            result = []
            for value in values:
                self.__cursor.execute(query, value)
                result.append(self.__cursor.fetchall())
            return result
        else:
            # Cas 3 :Un seul item
            self.__cursor.execute(query, values)
            return self.__cursor.fetchall()

    def update_attribute_value(self, nom):
        result = self.get_Infos([nom], True)
        self.__id = result[0]
        self.__nom = result[1]
        self.__description = result[2]
        self.__prix = result[3]
        self.__quantite = result[4]
        self.__id_categorie = result[7]

    def get_Infos(self, nom="", where=False):
        SQL = "SELECT * FROM produit left join categorie c on produit.id_categorie = c.id" #Liaison du nom de la catégorie et de son ID
        if where != False and nom != "":
            if type(nom) is list:
                value = []
                for item in nom:
                    value.append([item])

            SQL += " WHERE nom = %s"
            value = [nom]
            result = self.selectQuery(SQL, value)
            for a in result:
                for result in a:
                    return result
        else:
            return self.selectQuery(SQL)

    def create_item(self, nom, description, prix, quantite, id_categorie):
        # Peut aussi être utiliser pour mettre a jour l'item
        self.__nom = nom
        self.__description = description
        self.__prix = prix
        self.__quantite = quantite
        self.__id_categorie = id_categorie
        self.__create_item_in_database()

    def __create_item_in_database(self):
        if self.__nom != "":
            command = "INSERT INTO boutique.produit(nom,description,prix,quantite,id_categorie) VALUES(%s,%s,%s,%s,%s)"
            values = (self.__nom, self.__description, self.__prix, self.__quantite, self.__id_categorie)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()
        else:
            return "No Values"

    def update_item_in_database(self,nom, description, prix, quantite, id_categorie):
        if id == -1:
            return "No id"
        else:
            command = "UPDATE boutique.produit SET nom = %s, description = %s,prix = %s,quantite=%s, id_categorie=%s WHERE nom =%s"
            values = (nom, description, prix, quantite, id_categorie, nom)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()

    def __delete_entry_in_database(self, nom):
        if self.get_Infos(nom) != [[]]:
            command = "DELETE FROM boutique.produit WHERE nom=%s"
            values = (nom)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()
            self.delete_attributes()
        else:
            return "Item Not Found"

    def delete_attributes(self):
        self.__id = -1
        self.__nom = ""
        self.__description = ""
        self.__prix = ""
        self.__quantite = -1
        self.__id_categorie = -1
